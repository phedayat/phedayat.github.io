---
title: Build a Discord Bot For Adding Tracks To a Collaborative Spotify Playlist
date: 2025-06-12
math: true
---

## Context

Suppose you have a Discord server with a dedicated `#music` channel, where you and your friends share Spotify links. We can build a bot which reads that channel and automatically adds the songs to a collaborative playlist, with **duplicate detection**!

We’ll use Python to build the bot, and Docker and Fly.io to deploy.

### Disclaimer

I tend to use functions such as `map`, `filter`, and `reduce` in my Python scripts. If these are unfamiliar, refer to the Python docs to learn more about them: [builtins](https://docs.python.org/3/library/functions.html) and [functools](https://docs.python.org/3/library/functools.html).

## Links

- [Project Repo Link](https://github.com/marbifold/discord_playlist_bot)
- [Spotify API](https://developer.spotify.com/)
- [Discord Developer Portal and Docs](https://discord.com/developers/docs/intro)
- [Spotipy](https://spotipy.readthedocs.io/en/2.25.1/#)
- [Discord.py](https://discordpy.readthedocs.io/en/latest/)
- [Fly.io](https://fly.io/)

## Getting Started

Before we begin building the bot, we need to do some setup.

### Create a Spotify App

Through the Spotify API portal, create a new application with these particular values:

- Redirect URI: https://google.com (though this can be any URL)
- Which API/SDK: Web API

Once you’ve created the app, you’ll have a client ID and secret pair, which we’ll use later.

Finally, check the `User Management` tab in the app details to add yourself as a user if you're not already listed.

### Create a Discord App

Through the Discord App Dashboard, create a new app.

In the `Bot` menu, reset your token and copy the resulting value; we'll use that token to connect to Discord and perform actions in the server. There are lots of different options for configuring a Discord app, but we won't need any of them to setup a basic bot like this.

### Create a Spotify Collaborative Playlist

Spotify collaborative playlists allow multiple users to add songs to the same playlist, making it easy to share music with other people on the platform.

You can make a shared playlist through the web, desktop, or mobile Spotify interfaces.

## Design

When you share a song on Spotify through its share link, the track ID of the song is included in the link:

```plaintext
https://open.spotify.com/track/5ohfpKB5tt275f4Y4lQ9F7
```

and this applies generally to different collections of assets on Spotify:

```plaintext
https://open.spotify.com/album/7gy2aXBbOrpQFp5dDFKJ67
```

(there’s also going to be a user-specific token attached at the end, but we can ignore that)

Using regular expressions, we can extract precisely the asset type and ID. If the user shares an album, we can extract all of the tracks using its ID. In particular, we’ll use this regex pattern to identify Spotify share links, which accounts for messages around the link:

```python
[\s\S.]*https://\w+\.spotify\.com/(\w+)/(\w+)\??[\s\S.]*
```

(you’ll have to trust me on this one, but play around with it at https://regex101.com if you’re skeptical)

Implementing a system which simply adds whatever song is shared is easy enough: we already have the link, so use the Spotify API to add it to the playlist; however, we don’t want to add duplicates over and over again (I’m guilty of sending the same song multiple times). Spotify doesn’t check if a song already exists in a playlist, so we’ll need to implement this ourselves.

This implementation takes advantage of sets, with their quick lookup times, to check if a song exists in a playlist. Using sets, we automatically generalize to collections of songs.

If we have the set of all track IDs $A$ from the playlist and the set of shared track IDs $B$, we check existence using set intersection: $A \cap B$; this will tell us how many songs in $B$ are already in $A$.

If the result is the empty set, none of the shared tracks already exist in the playlist; otherwise, simply filter out the existing tracks using set difference. We’re left with a completely generalized expression, giving us all the track IDs that need to be added to the playlist:

$$
B - (A \cap B)
$$

One caveat is that Spotify paginates their responses, limiting the number of songs we can pull from a playlist at a time to 100 tracks. Knowing this, we can calculate the exact number of offsets, and all of their values, we need to get all of the songs.

If we get the total number of tracks `T` in the playlist, then the number of offsets to get the whole playlist is `T // 100 + 1`, and the values of those offsets will be `[100 * i for i in range(T // 100 + 1)]` (where `//` is integer division in Python).

## Build

First, create a new directory to store the project:

```shell
mkdir discord_playlist_bot
cd discord_playlist_bot
```

Prepare your Python environment:

```shell
python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip
pip install "discord.py" "spotipy" --upgrade
```

Create a .env file to store secrets:

```python
DISCORD_TOKEN = <value>

SPOTIFY_CLIENT_ID = <value>
SPOTIFY_CLIENT_SECRET = <value>
SPOTIFY_REDIRECT_URI = <value>

SPOTIFY_PLAYLIST_NAME = <value>
SPOTIFY_PLAYLIST_ID = <value>
```

### Spotify Helper

We’ll start by making a helper module, `spotify_helper.py`, to handle Spotify API interactions. The Spotify client library we’re using is Spotipy.

Setting up the client requires the environment variables we set earlier:

```python
from spotipy.oauth2 import SpotifyOAuth

# Permissions scopes we need access to
scopes = "playlist-read-collaborative,playlist-modify-public,playlist-modify-private"

# The Spotify client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope=scopes,
    )
)
```

To get items and length from the playlist:

```python
from typing import Set

def _get_playlist_length(playlist_id: str) -> int:
  res = sp.playlist(playlist_id=playlist_id, fields="tracks.total")
  if res:
      return res["tracks"]["total"]
  return 0

def _get_tracks_in_section(playlist_id: str, track_ids: Set[str], i: int) -> Set[str]:
    res = sp.playlist_items(
        playlist_id=playlist_id,
        fields="items.track.id",
        limit=100,
        offset=i*100,
    )
    if res:
        valid_items = filter(lambda x: x and x["track"], res)
        items_ids = frozenset(map(lambda x: x["track"]["id"], valid_items))
        return track_ids & items_ids
    return set()
```

If the user shares an album, we need to first get all the track IDs in it:

```python
def _get_album_track_ids(album_id: str) -> Set[str]:
	res = sp.album_tracks(album_id=album_id)
	if res:
		return set(map(lambda track: track["id"], res["items"]))
        return set()
```

Finally, we put it all together and filter out all the tracks which already exist:

```python
def get_tracks_to_add(share_type: str, playlist_id: str, asset_id: str) -> Set[str]:
    n_existing_tracks = _get_playlist_length(playlist_id)
    n_sections = n_existing_tracks // 100 + 1

    # If the user shared an album, we need to get
    # all of its tracks first
    if share_type == "album":
        track_ids = _get_album_track_ids(asset_id)
    else:
        track_ids = set([asset_id])

    args_list = [
        (playlist_id, track_ids, i)
        for i in range(n_sections)
    ]
    res = map(lambda x: _get_tracks_in_section(*x), args_list)
    
    existing_tracks = reduce(lambda x, y: x | y, res, set())
    return track_ids - existing_tracks
```

Once we have the final track IDs, we need to prepare Spotify URIs which identify those tracks, then add them to the playlist:

```python
def _build_uri(track_id: str) -> str:
    return f"spotify:track:{track_id}"

def add_tracks_to_playlist(playlist_id: str, track_ids: Set[str]):
    items = map(_build_uri, track_ids)
    return sp.playlist_add_items(
        playlist_id=playlist_id,
        items=items,
    )
```

Some nice additional helpers for when we want to display information about the asset we added:

```python
def _get_track_name(track_id: str) -> str:
    track = sp.track(track_id)
    return track["name"]

def _get_album_name(album_id: str) -> str:
    album = sp.album(album_id)
    return album["name"]

SHARE_TYPES = {
  "album": _get_album_name,
  "track": _get_track_name,
}

def get_shared_asset_name(share_type: str, asset_id: str) -> Optional[str]:
    if share_type in SHARE_TYPES:
        return SHARE_TYPES[share_type](asset_id)
```

### Main Loop

We can finally build the main loop of the bot, which will continuously read our server for messages.

Discord bots use asynchronous methods to perform different actions in response to events in the server, like when the bot is ready and when a message has been sent. We can read messages and only act on them if they’re from a particular channel, or even from specific users. Creating a bot is simple: subclass `discord.client.Client`.

For this project, we want to check the music channel for messages, and extract the asset type and ID from Spotify links that appear in those messages.

To receive the content from messages, we have to set intents, which subscribe the Discord bot to certain events in the server.

We create `main.py`:

```python
import re

from discord.client import Client
from discord import Message, Intents

from spotify_helper import (
    get_tracks_to_add,
    get_shared_asset_name,
    add_tracks_to_playlist,
)

message_regex = re.compile(r"[\s\S.]*https://\w+\.spotify.com/(\w+)/(\w+)\?[\s\S.]*")

class PlaylistBot(Client):
  def __init__(self, playlist_id: str, playlist_name: str, **kwargs):
      super().__init__(**kwargs)
      self.playlist_name = playlist_name
      self.playlist_id = playlist_id

  async def on_ready(self):
      print(f"Logged in as: {self.user}")
  
  async def on_message(self, message: Message):
      if message.channel.name == "music":
          res = re.match(message_regex, message.content)
          if res:
              share_type, asset_id = res.groups()
              share_type_str = share_type.capitalize()
              asset_name = get_shared_asset_name(share_type, asset_id)
              
              # Just to make sure the users only share assets we're prepared for
              if asset_name is None:
                  await message.reply(f"Unsupported share type: {share_type}")
                  return
              
              tracks_to_add = get_tracks_to_add(self.playlist_id, share_type, asset_id)
              if tracks_to_add:
                  add_tracks_to_playlist(self.playlist_id, tracks_to_add)                
                  await message.reply(f"{share_type_str} \"{asset_name}\" added to \"{self.playlist_name}\"")
              else:
                  await message.reply(f"{share_type_str} \"{asset_name}\" already exists in playlist \"{self.playlist_name}\"")

if __name__=="__main__":
    intents = Intents.default()
    intents.message_content = True

    playlist_name = os.getenv("SPOTIFY_PLAYLIST_NAME")
    playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")

    client = PlaylistBot(
        playlist_id,
        playlist_name,
        intents=intents,
    )

    token = os.getenv("DISCORD_TOKEN")
    if token:
        client.run(token)
    else:
        print("Cannot access token")
```

The bot can now be run with the following command:

```shell
python main.py
```

However, you might not get as far as you’d hope.

## Authentication

In order for the bot to interact with Spotify, we need to authenticate our user; I setup the bot to assume my profile for all of those interactions. Okay, I’m going to do this… wrong? Weird? I don’t know, it’s not the “right” way to do it, but it works. Here’s [a Github thread that talks about the right way to do it](https://github.com/spotipy-dev/spotipy/issues/632). We need to do this because when it runs on a virtual machine, we won’t be able to complete the typical authentication flow.

1. Run the `spotify_helper.py` module on its own: `python spotify_helper.py`
2. Follow the prompted URL
3. Paste the final redirected URL

You’ll end up with a token… and then it just works when you deploy it. I don’t supply the token anywhere; I hosted this for about a year before dealing with any kind of auth issues (which I fixed by running this process again).

## Deploying

Create `requirements.txt` to keep track of our dependencies:

```shell
pip freeze > requirements.txt
```

### Dockerizing

We can streamline deployment, and ensure things are running correctly, by Dockerizing the project. To do this, define this short Dockerfile:

```dockerfile
FROM python:3.12

COPY . /workspace
WORKDIR /workspace

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]
```

### Hosting

The hosting service we'll be using is Fly.io. Here's why:

1. Easy-to-use CLI tool
2. Simple configs
2. Docker support

Follow the docs to install `fly`.

Create a new app from the root of our repo, which will create a new app in your organization on Fly.io and generate a `fly.toml` config file: `fly launch`.

### Fly Secrets

Before we can run the bot, we need to set the necessary environment variables. In your app’s `Secrets` tab, set the environment variables we defined previously.

### Launching

If you’ve already made the Dockerfile, it should recognize it at the beginning of launching a new app. Otherwise, after the app is created, run `fly deploy`.

The deployment will build the Docker Image and upload it to their registry; your machines will start automatically. Check `Live Logs` to see if the bot is ready.

## Installing The Bot

Through the Discord App details for the project, under the `Installation` tab, we can find the installation link that we can use to install the bot in a server.

For this bot in particular, we only need a guild install.

Before we can install, we need to make sure the correct scopes and permissions are setup:

- Scopes: `application.commands` and `bot`
- Permissions: `Send Messages`

Once those options are set, copy-paste the Install Link either into your Discord server or into a browser, and it’ll prompt you to add the bot.

When you complete the authorization flow, the bot will join your server and start listening for messages on `#music`.

## Final Thoughts

The bot is done! You can now share links in your `#music` channel and the assets will get added to the collaborative playlist.

You’ll notice that there’s a distinct wait when running the bot, as it needs to get all the pages of your playlist and perform the intersection. To improve on this, I used a `ThreadPoolExecutor` to parallelize getting the pages, which gave a decent speedup.

You can enhance the bot with slash commands or a small UI in Discord, though those are more than I needed for the server I’m in.
