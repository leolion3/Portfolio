# Trash Calendar

This script can be used to generate a trash calendar similar to the one offered by the [Bremer Stadtreinigung](https://www.die-bremer-stadtreinigung.de/api/c-trace/app/garbage-calendar-web).

## Requirements

The script runs as a blocking scheduler using APScheduler, it requires the following modules:

```
html2image
APScheduler
requests
```

**Additionally, all files within this and the "media" directory are required for the script to run (except for the demo images, obviously).**

## Demo

The script executes a test run, then runs once per month on the first day of the month at 12 PM (Noon).

![Telegram demo message](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/TrashCalendar/media/telegram_demo.jpg)

![Calendar demo](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/TrashCalendar/media/calendar_demo.jpg)

## Disclaimer

All resources have been downloaded from public domain sources and are owned by their respective parties.
As far as it concerns me, usage is allowed solely for private use. Redistribution and commercial usage are prohibited unless explicitly allowed by the copyright owners.