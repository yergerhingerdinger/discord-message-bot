**Discord Message Bot**

A Python bot that sends an automated message to a Discord channel via webhook.

**Features**
- This is mostly for personal use - just to send an automated message about the price of a card into one of the discord channels that I'm in.
- Sends a scheduled message every day at 9AM and 9PM PT.
- Deployed and running 24/7 on Oracle Cloud Free Tier VPS (Ubuntu 22.04)

**Tech Stack**
- Python 3.10
- Discord Webhooks API
- Scryfall API (for the MTG foil information)
- `requests` — HTTP calls
- `schedule` — cron-style task scheduling
- `python-dotenv` — secure environment variable management
- systemd — 24/7 background service on Linux
- Oracle Cloud Free Tier VPS
