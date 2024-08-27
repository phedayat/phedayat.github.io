---
title: {{ replace .File.ContentBaseName "-" " " | title }}
date: {{ .Date }}
draft: true
markup: markdown

params:
    math: false
    mermaid: false
    private: false
---
