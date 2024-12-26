---
title: "Building With The Replit Agent"
date: 2024-12-25
last_updated: 2024-12-25
draft: false
math: false
mermaid: false
private: false
---

## Prompting
---
Remember that these models only do as well as they're prompted
- Leaving *too* much up to the LLM may lead to unmaintainable code and a misconfigured project
- On the other hand, it's difficult without prior knowledge to know what you should be telling it what to do

Things to consider:
- Language (front-end, back-end)
  - You'll almost always want to use `Python`, as it's the quickest to prototype with and easiest to debug with little programming knowledge
- Cloud platforms
  - This one might be hard when you're building MVPs, but it matters if you need integrations, e.g. Google APIs
- User platforms
  - Web app
  - Just a running "job", which executes a task in regular intervals (e.g. sending periodic texts to friends)

## Building (After The Initial Prompt)
---
You'll be met with a chat box which allows you to interface with the agent. Here you can:
- Select `Fix Issues` to have it solve bugs
- Select new features that it suggests
- Tell it to start on a new feature you describe
- Tell it to fix specific issues that you encounter

Difficulties in building can stem from different problems: 
- The agent *doesn't* immediately have access to some platform that it needs
  - E.g. when your Google OAuth callbacks aren't working and you need to update the project in Google Cloud Platform
- There are problems that aren't directly related to the code (DBs, auth, etc.) and require deeper knowledge regarding the topics to properly troubleshoot and fix
  - The model may make multiple attempts to perform a fix, and none of them actually do anything

The general solution is to simply keep prompting for answers and describing issues in-detail
- Development is *iterative*, it will take several passes to make sure things are the way you expect them to be

## Tools
---
When you open a new *repl* (a project in Replit), you enter into your *workspace*
- This is where you can manage the code, deployments, databases, authentication, etc.

Some available services:
- **Replit Key-Value Store:** Database for storing mappings
    ```plaintext
    key1 --> value1
    key2 --> value2
    ```
- **PostgreSQL Database:** Common relational database management system (for managing data that can be arranged in tables)
- **Object Storage:** For storing objects like images, videos, and arbitrary files
- **Authentication:** For managing who can access your repl when it's deployed
- **Deployments:** For publishing your repl to the web

Replit also allows for native integrations with OpenAI, Anthropic, Mistral AI, Google Sheets, etc. 

Services and the agent and assistant can be accessed from the sidebar of your workspace.