"""
Naija News Bot
--------------
What this does, in plain words:
1. It checks a list of Nigerian news websites (their "RSS feed" - a page made
   for robots to read headlines easily).
2. It looks for ONE story it has never posted before.
3. It asks an AI to rewrite that story in a warm, Nigerian voice.
4. It sends that rewritten story to your Telegram channel.
5. It writes down "I already posted this one" so it never repeats itself.

We run this script every 15 minutes using GitHub Actions (free robot clock).
Every 15 minutes = 4 times an hour = at most 4 stories an hour. Simple.
"""

import os
import json
import time
import feedparser
import requests

FEEDS = [
    ("Punch", "https://punchng.com/feed/"),
    ("Vanguard", "https://www.vanguardngr.com/feed/"),
    ("The Nation", "https://thenationonlineng.net/feed/"),
    ("Premium Times", "https://www.premiumtimesng.com/feed"),
    ("Daily Trust", "https://dailytrust.com/feed/"),
    ("The Cable", "https://www.thecable.ng/feed"),
    ("Guardian Nigeria", "https://guardian.ng/feed/"),
]

STATE_FILE = "posted.json"
GROQ_API_KEY = os.environ["GROQ_API_KEY"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.3-70b-versatile"


def load_memory():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"posted_links": []}


def save_me
