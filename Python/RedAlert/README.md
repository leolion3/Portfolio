# Red Alert Telegram Notifier

<p align="center">
  <img src="https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/RedAlert/media/meme.jpg">
</p>

This python script allows setting up Telegram Notifications for the Israeli Red Alerts issued by Pikud Haeoref during emergencies.

The API is queried every 15 seconds for updates, which are reformatted and sent per Telegram.

(\*) The app runs in debug (PoC) mode by default. If you'd like to actually use it, set the `DEBUG` variable to false. This is done since the app only works from **within Israeli territory** due to firewall and national security restrictions.



## Requirements

This script only requires 2 libraries to run (flask is optional and only used for the test-server):

```bash
requests
flask
```

These can also be installed from the provided `requirements.txt` file.

## Functionality

The application utilizes 2 threads (3 in test-mode, the third one is used by flask):

1. UI/CMD Thread: Allows changing which regions are monitored.
2. API/Query Thread: Used for making requests to the API every 15 seconds.

The UI Thread allows you to change which regions are monitored through the various integrated commands:

![Screenshot showcasing functionality](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/RedAlert/media/demo1.png)

**Note:** when first running the app, it will attempt to download the JSON file [`targets.json`](https://github.com/leolion3/python-red-alert/blob/master/src/targets.json). Should you not be using Linux, ensure that either `curl` is available in your Windows Shell, or manually download the file and place it next to this script.

## How to run this app

Since the app has a main UI thread, running in in a simple terminal instance is quite annoying. I recommend starting a `screen` instance, running the app and adding the regions you'd like to monitor and then leaving the screen instance using `ctrl+A D`.

## Credit

Credit where credit is due: This project was inspired by the [red-alert-python](https://github.com/Zontex/python-red-alert) project. The `targets.json` file (containing the monitored regions and first downloaded when running the app), is also taken from there.

## Demo

![Screenshot showcasing Telegram bot](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/RedAlert/media/demo2.png)
