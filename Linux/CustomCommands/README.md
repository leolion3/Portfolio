# Custom Linux/MacOS Commands

Here is a list of custom commands crafted as extensions for your OS's commands. They include git shortcuts, common task shortcuts and some shortened commands.

## Installation

To install and use the commands, simply download the `install.sh` file and execute it:

### Quick Install

```bash
curl https://raw.githubusercontent.com/leolion3/Portfolio/master/Linux/CustomCommands/install.sh | /bin/bash
```

### Manual Install

```bash
curl -O https://raw.githubusercontent.com/leolion3/Portfolio/master/Linux/CustomCommands/install.sh
chmod +x install.sh
./install.sh
```

The command executables will be placed under `~/.commands`, which you then need to add to your shell's `rc` file.

## Commands

The following commands are included:

| Command          | Type    | Description                                                                           |
| ---------------- | ------- | ------------------------------------------------------------------------------------- |
| a                | alias   | `git add [args]`                                                                      |
| b                | alias   | `git branch [args]`                                                                   |
| c                | alias   | `git add --ignore-errors . && git commit -a`                                          |
| checkout         | alias   | `git checkout [args]`                                                                 |
| f                | alias   | `git fetch [args]`                                                                    |
| gdiff            | alias   | `git alias [args]`                                                                    |
| merge            | alias   | `git merge [args]`                                                                    |
| p                | alias   | `git pull`                                                                            |
| s                | alias   | `git status`                                                                          |
| sts              | alias   | `git stash [args]`                                                                    |
| lg               | alias   | `git lg` from [johanmeiring](https://gist.github.com/johanmeiring/3002458)            |
| pull             | script  | `git add . && git commit -a && git pull`                                              |
| push             | script  | `git add . && git commit -a && git pull && git push`                                  |
| delall           | script  | Deletes all git branches except `main` and `master`                                   |
| git-obliterate   | script  | Extended version of [git-obliterate](https://gist.github.com/brianloveswords/7545299) |
| genpass          | script  | Python [password generator](https://github.com/leolion3/Portfolio/blob/master/CustomCommands/Scripts%20-%20DONT%20ADD%20TO%20PATH/passwordGen.py) |
| keepbusy         | script  | [Keepbusy mouse mover](https://github.com/leolion3/Portfolio/blob/master/Python/KeepBusy/keepbusy) |
| keepbusy_cross   | script  | [Keepbusy-cross mouse mover](https://github.com/leolion3/Portfolio/blob/master/Python/KeepBusy/keepbusy_cross) |
| killdock (MacOs) | script  | Kills and restarts MacOs Touch-Dock (Old MBP <2022)                                   |
| passtransfer     | script  | [TCP password transfer tool](https://github.com/leolion3/Portfolio/blob/master/Python/PasswordUtils/passtransfer) |
| ptransfer        | script  | [ptransfer file transfer tool](https://github.com/leolion3/Portfolio/blob/master/Python/FileSender/ptransfer) |
| pv               | script  | [Python password vault](https://github.com/leolion3/Portfolio/blob/master/Python/PasswordVault/passwordVault.py) |
| serve            | alias   | `python3 -m http.server`                                                              |
| wd               | alias   | `open .` - opens current working directory in default window manager                  |
