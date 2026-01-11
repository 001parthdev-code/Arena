Arena (MVP v1)

Arena is a minimal command-line tool that enforces daily execution accountability through a single binary check-in.

Purpose

Arena exists to answer one question per day:

**Did you ship today?**

It does not track habits, streaks, or productivity metrics.
It records execution.

Features (v1)

One-time user setup

Forced specificity for goals

Daily yes/no check-in

One check-in per day enforced

Local JSON persistence

Zero UI, zero notifications

Non-Features (by design)

No reminders

No gamification

No streaks

No rewards or penalties

No cloud sync

No analytics

Arena does not motivate.
It logs reality.

Project Structure
arena/
├── arena.py        # Entry point and routing
├── setup.py        # First-time user setup
├── checkin.py      # Daily execution check-in
├── data/
│   ├── user.json
│   └── checkins.json
└── README.md

How It Works

On startup, Arena checks for an existing user.

If no user exists, setup is triggered.

Setup captures name and a concrete goal.

On subsequent runs, Arena performs a daily check-in.

The result is persisted locally.

If Arena is not run, no check-in is recorded.

Usage
python arena.py

Data Storage

All data is stored locally as JSON:

data/user.json — user information and goal

data/checkins.json — daily check-in history

No external services are used.