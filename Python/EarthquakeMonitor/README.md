# Simple Earthquake Monitor w/ Telegram Notifications

This module implements a simple application to monitor a country (or city) for earthquakes.

## Requirements

The module only requires two libraries

```bash
requests
APScheduler
```

## Demo

To run the app, simply start it using `python3 ./monitor.py` (preferably in a detachable `screen`), then enter the country, city and telegram credentials.

The app will execute a test-run using the latest earthquake to make sure the Telegram messages are sent correctly, afterwards it will start the listener for future data retrieval.
Quakes that have been notified about will get cached. The cache gets cleared every 7 days automatically.

The monitor automatically reaches out to the [API](https://earthquake.usgs.gov/earthquakes) every 30 seconds for an update on current quakes, hopefully giving you enough time to find shelter!

![Demo Thumbnail](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/EarthquakeMonitor/media/demo.png)

## Demo

![Telegram bot demo](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/EarthquakeMonitor/media/demo2.jpg)