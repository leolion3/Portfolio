# Stream Together - A DYI Approach

So you've come across the scenario where you and your friends want to watch a movie together - each of you on their own machine in their own streaming platform. How do you start the movie synchronously? How do you pause it synchronously for bathroom breaks?

Thats where this module comes in! With StreamTogether you can pause your media - and that of everyone else as well!

## Requirements

This module requires two libraries:

```bash
pyautogui
keyboard
``` 

They can be installed from the `requirements.txt` file.

## Functionality

One of you is going to act as the server. Whoever this is needs to run the script as a server:

```bash
python3 ./stream_together.py server [IPv4-/Public IP-Address]
```

The others will connect as clients:

```bash
python3 ./stream_together.py client [IPv4-/Public IP-Address]
```

Then, just click all of your media players and hit the `spacebar` to start streaming synchronously! (More keys will be added soon)

## Demo

![Screenshot showcasing functionality](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/StreamTogether/media/demo.png)