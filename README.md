# PortoFifi

# Portfolio Setup Task

## Overview

This repository was created as part of a portfolio setup task. The objective was to install the required tools, connect environments, create a GitHub repository, and document the overall process, including any issues encountered and how they were resolved.

---

# Tools Installed

- Cursor IDE
- Claude Code extension for Cursor
- Codex extension for Cursor

---

# Steps Completed

## 1. Installed Cursor IDE

- Downloaded Cursor for macOS
- Installed Cursor on my laptop
- Signed up to Cursor using my Google account
- Completed the initial Cursor setup process
- Connected Cursor to GitHub

## 2. Installed Claude Code Extension

- Opened Extensions in Cursor using:
  - 'Cmd + Shift + X'
- Searched for:
  - 'Claude Code'
- Installed:
  - 'Claude Code for VS Code'

## 3. Installed Codex Extension

- Opened Extensions in Cursor
- Searched for:
  - 'Codex'
- Installed:
  - 'Codex – OpenAI's Coding Agent'

## 4. Signed In to Codex

- Opened the Command Palette using:
  - 'Cmd + Shift + P'
- Typed:
  - 'Codex'
- Selected:
  - 'Codex: Open in Side Bar'
- Signed in using my ChatGPT/OpenAI account
- Successfully logged in to Codex on Cursor

## 5. Attempted to Sign In to Claude Code

- Opened the Command Palette
- Typed:
  - 'Claude'
- Selected:
  - 'Claude Code: Open in Side Bar'
- Attempted to sign in using ClaudeAI
- Learned that logging in to Claude Code requires a Claude Max or Claude Pro subscription

## 6. Created GitHub Repository

- Created a public GitHub repository named:
  - 'PortoFifi'
  - Check 'README.md'

## 7. Cloned Repository Using Cursor

- Cloned the repository locally using Cursor 
- Selected 'PortoFifi'
- Selected a local folder destination
- Opened the repository in Cursor

## 8. Edited README File

- Edited the 'README.md' file
- Documented:
  - installed tools
  - completed steps
  - encountered issues
  - troubleshooting process

## 9. Committed and Pushed Changes

- Committed the README and project files using Git
- Pushed the changes to the GitHub repository

---

# Issues Encountered and How I Solved Them

## Issue 1: Unable to Sign Up to Cursor with GitHub

Initially, I attempted to create a Cursor account using my GitHub account, but I encountered an error multiple times.

### Solution

I switched to signing up with my Google account instead, which worked successfully.

---

## Issue 2: Confusion Between Browser Cursor and Desktop Cursor

At first, I was using Cursor in the browser instead of the desktop application installed on my laptop. This caused confusion while trying to install extensions and complete the setup process.

### Solution

After encountering several errors, I realized I needed to use the desktop application. Once I switched to the installed version of Cursor, I was able to continue the setup correctly.

---

## Issue 3: Installing Claude Code and Codex

I was initially unsure how to install Claude Code and Codex inside Cursor.

### Solution

I searched Google for tutorials and step-by-step instructions on:

- 'how to install Claude Code on Cursor'
- 'how to install Codex on Cursor'
I then followed the instructions to successfully install both extensions.

---

## Issue 4: Logging In to Codex

I was initially confused about how to login to Codex inside Cursor.

### Solution

I searched:

- 'how to login to Codex on Cursor'
I also watched a tutorial video that helped me understand the authentication flow. It was not the video I was looking for, but it helped me figure things out until I successfully logged in using my ChatGPT/OpenAI account.

---

## Issue 5: Unable to Log In to Claude Code

I was unable to log in to Claude Code inside Cursor.

### Solution

After trying twice, I learned that logging in to Claude Code requires a Claude Max or Claude Pro subscription, which I currently do not have.

---

## Issue 6: Committing and Pushing Changes to GitHub

I was initially unsure how to commit and push changes to GitHub from Cursor.

### Solution

I searched Google for tutorials on:

- 'how to commit to GitHub from Cursor'
- 'how to push to GitHub from Cursor'

Although I found several step-by-step guides, I still found the process confusing. I then asked ChatGPT:

- 'What command should I give the AI agent to commit and push the changes to GitHub?'

I copied and pasted one of the suggested commands into the AI agent. The agent successfully committed my changes, but it was unable to push them to the GitHub remote repository.

To complete the process, I manually clicked the 'Sync Changes' button in the Source Control panel inside Cursor, and the push was completed successfully.

---

# What I Learned

Through this task, I learned:

- how to install and configure Cursor IDE
- how to install AI coding extensions
- how to authenticate development tools
- how to create and clone GitHub repositories
- how to commit and push to GitHub from Cursor IDE
- how to document technical workflows
- how to troubleshoot setup issues independently using online resources

# AI-Powered SEO Content Production — Research Project

## Topic

AI-Powered SEO Content Production

## Why This Topic

It sits at the intersection of two fast-moving trends, AI tooling and organic search strategy, making it one of the most actively debated topics among B2B SaaS marketers right now. Every serious SEO practitioner is navigating this shift, which means there's a rich pool of practitioners publishing real, experience-based content on it.

## Why These Experts

Rather than looking for people who explicitly label themselves "AI SEO experts," the research focused on active SEO practitioners whose recent content naturally covers AI; because that's where the most grounded, experience-based perspectives live. The list includes a mix of individual practitioners (Diggity, Gotch, Sturm, Hufford, Crestodina, Natividad) and company channels that function as content publishers in their own right (Semrush, Ahrefs, WPBeginner, HubSpot Marketing).

## What Was Collected

### YouTube Transcripts (via `youtube-transcript-api`)


| Channel           | Videos Collected |
| ----------------- | ---------------- |
| Matt Diggity      | 3                |
| Nathan Gotch      | 2                |
| Semrush           | 2                |
| Ahrefs            | 2                |
| WPBeginner        | 2                |
| Edward Sturm      | 3                |
| HubSpot Marketing | 3                |


### LinkedIn Posts (manually collected)


| Expert           | Posts Collected |
| ---------------- | --------------- |
| Brendan Hufford  | 3               |
| Andy Crestodina  | 2               |
| Amanda Natividad | 3               |


## Repository Structure

research/

├── sources.md — full list of experts with links and annotations

├── youtube-transcripts/ — transcripts organized by channel, one file per video

 │   ├── matt-diggity/

 │   ├── nathan-gotch/

 │   ├── semrush/

 │   ├── ahrefs/

 │   ├── wpbeginner/

 │   ├── edward-sturm/

 │   └── hubspot-marketing/

└── linkedin-posts/ — posts organized by expert

  |  ├── brendan-hufford.md

  |  ├── andy-crestodina.md

  |  └── amanda-natividad.md

scripts/

└── fetch_transcripts.py — script used to pull YouTube transcripts via API

## Total

10 experts · 17 YouTube transcripts · 8 LinkedIn posts