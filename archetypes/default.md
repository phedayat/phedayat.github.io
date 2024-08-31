---
title: {{ replace .File.ContentBaseName "-" " " | title }}
date: {{ .Date | time.Format "2006-01-_2" }}
draft: true
markup: markdown

params:
    math: false
    mermaid: false
    private: false
---
