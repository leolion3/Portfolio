# Canary Tracking Token

This script allows generating canary tracking tokens for emails.

Canary tokens are generated based on the recipient and the email subject.
The generation is done in a simple bootstrap interface.

Server logs are stored in a `app.log` file.

The app can be extended to send messages through Telegram or Discord,
instead of writing logs. Use it as you desire.

## Requirements

To run the app, Flask is required. It can be installed using

```bash
pip3 install Flask -y
```

## GUI

The GUI is shown below

![Canary Tracker GUI](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/CanaryTrackingPixel/media/demo.png)