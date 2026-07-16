---
title: Response-formatting Skills in Claude
date: 2026-07-16
---

I use the Claude desktop app constantly for doing preliminary research and ideation about new projects. Every model I've ever used seems to have a problem with responding with a Kantian wall of text to questions that demand a much leaner response format. In general, the models need explicit guidance on how to respond in a much more palatable format; these are the skills I use to enforce that.

## Adding to Claude
This works in the desktop and web versions of Claude. 

1. Go to `Customize > Skills`
2. Select the `Add` button
   - You can certainly create skills with Claude, but I've opted to write my own
3. Select `Write skill instructions`.

## Skills
- `bullets-only`
    - Description: "Enforce output structure as bulleted or numbered lists only"
```plaintext
Respond using nested bulleted or numbered lists only. Use only - to make bullets in Markdown
```
- `dense`
    - Description: "Enforce response content to be as minimal as possible while maximizing information"
```plaintext
Completely maximize information per word. Avoid filler language at all costs. Minimize output tokens, maximize information. The goal is to minimize read time while maintaining maximum information.
```
- `ask-first`
    - Description: "Ask clarification questions before continuing or starting a task"
```plaintext
Always ask clarifying questions before starting or continuing a task. Always ask questions using the `ask_user_input`/`AskUserQuestion` tool. Ask questions based on my answers to earlier questions.
```
- `formal`
    - Description: "Keep responses formal and precise"
```plaintext
All responses must be precise and formal.
```
- `cite-everything`
    - Description: "All information should be cited from a source external to the model"
```plaintext
Always and only use, rely on, and cite external sources for information. All facts must be based on an external source. Rely on the web search tool to gather information.
```
- `adversarial`
    - Description: "Critique and question my ideas, thoughts, and questions."
```plaintext
Be hypercritical and adversarial. Question if I'm even asking the right question. Assume that I'm leaving out details that could help you respond better. Ask me lots of questions in order to completely flesh out my intentions and ideas.
```
