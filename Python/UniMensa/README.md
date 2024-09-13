# Uni Bremen Mensa Food Telegram Notifier

This module scans the Uni Bremen Mensa food every day at 11 AM and sends you a message containing today's food offering.

## Requirements

The module relies on `requests` for making web requests and `APScheduler` for scheduling the daily task. They can be installed from the supplied `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

or manually:

```
APScheduler
requests
```

## Demo

![Screenshot showcasing Telegram bot](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/UniMensa/media/demo.png)