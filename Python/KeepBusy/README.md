# KeepBusy Mouse Mover

Need your PC to stay active? Just use this simple tool.

To stop, simply use your switch-window shortcut (`Alt-Tab` on Windows, `Ctrl-Tab` on MacOS/Linux) and hit Ctrl-C to stop.

## Requirements

This tool requires the Python module `pyautogui`.

## Adjusting Speed

To adjust to refresh rates beyond 60Hz, make sure to set the `refresh_rate = 144` to your monitor's refresh rate. This will
ensure the cursor does not move too quickly.

## Usage

Run the tool from a commandline window (easiest) or double click the file. 

```bash
chmod +x ./keepbusy
./keepbusy
```

The tool will start moving the mouse in a circle pattern.

To stop, hit `Ctrl+C`.

## Adjustments

To make the circle bigger, simply change the `r` (radius) variable to whatever size you want.

## Demo

![Demo of mouse moving in a circle pattern.](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/KeepBusy/media/demo.gif)
