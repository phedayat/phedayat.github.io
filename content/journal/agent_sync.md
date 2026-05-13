---
title: Agent Synchronizer
date: 2026-05-13
---

I've spent the past few months working heavily with LLM coding agents. Regardless of the discourse you may see online about them, it's impossible to deny that they're incredible productivity tools for the working developer and researcher.

I found myself using several of them, some at the same time and others in phases. I use Cursor's agent through the IDE the most, with Codex and Claude Code following close behind; once in a while I'll use OpenCode, though for no particular reason at this point.

Over time, with frequent and heavy usage, I found myself writing similar structures in my prompts in order to guide the conversations (e.g. rules for the responses), which naturally end up in the agent harness' `AGENTS.md`. However, changes I made to one didn't always end up in the other harness' files, mostly due to laziness. What does laziness breed in a developer? New CLI tools.

I made `agent-synchronizer` ([link](https://pypi.org/project/agent-synchronizer/)) to consistently move all of the relevant global files for each harness into a dedicated central repo and symlink back to the original harness configuration directories. Files like `AGENTS.md` and the `skills` directory are universal; most, if not all, agents know what to do with these artifacts. Some harnesses use more targeted files, like Cursor's `.cursorrules` or Codex's `config.toml` for configuring the harness directly.

`agent-synchronizer` enables moving the universal and per-provider files to the dedicated repo, via a configuration file that you can either define yourself or let the tool do it for you. Here's an example:
```shell
# If the config file exists, it's read and used, 
# otherwise it's created with the defaults

uv run agent-synchronizer <central_repo_path> \
    --config my_config.yaml \
    --save-config
```

The example will produce `my_config.yaml` (your paths will actually have your `$HOME` path in them, I obfuscated them here):
```yaml
common:
- AGENTS.md
- skills
- agents
providers:
- name: codex
  path: $HOME/.codex
  files:
  - config.toml
- name: claude
  path: $HOME/.claude
  files:
  - settings.json
- name: cursor
  path: $HOME/.cursor
  files:
  - .cursorrules
- name: opencode
  path: $HOME/.config/opencode
  files:
  - opencode.jsonc
```

The above YAML defines the out-of-the-box defaults for the tool. `common` files/directories get symlinked to all included providers, and the provider-specific files get written to provider directories in the repo. We end up with this structure in the central repo:
```shell
.
├── agents
├── AGENTS.md
├── claude
├── codex
├── opencode
└── skills
```

Still working on the UX and hoping to add more features, like a TUI and searching all default locations for each supported harness, but this solves the problem for now.