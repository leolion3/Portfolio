# Custom Windows Commands

This package adds multiple shotcuts/combined git commands, and some other useful commands.

To use the tools from the command line, add the current folder to your System PATH. After doing so you may use them from the command line. 
For example: "c" would execute the c.cmd script. 

## Setup

Most commands work out-of-the-box. The following commands require a file path to the scripts to be added to function:
- genpass
- hashcmp
- numconv
- oneline
- pingme
- ptransfer
- pv
- unzipall

## Features

### Git Shortcuts

Note: the use of the world "params" is used to showcase that the given command can receive parameters.


In order to automate the workflow when using git, the following commands were added:
- "git add params" shortcut
```bash
a [params]
```
- "git branch params" shortcut
```bash
b [params]
```
- "git add --ignore-errors params all && git commit -a" shortcut
```bash
c [params]
```
- "git checkout params" shortcut
```bash
checkout [params]
```
- "git fetch params" shortcut
```bash
f [params]
```
- "git diff params" shortcut
```bash
gdiff [params]
```
- "git lgs" fancy log shortcut (see disclaimer below)
```bash
l
```
- "git logs" shortcut
```bash
lgs
```
- "git merge params" shortcut
```bash
m [params]
```
- "git pull params" shortcut
```bash
git pull [params]
```
- "git add * && git commit -a && git pull params" shortcut
```bash
pull [params]
```
- "git add --ignore-errors * && git commit -a && git pull && git push params" shortcut
```bash
push [params]
```
- "git remote params" shortcut
```bash
remote [params]
```
- "git status" shortcut
```bash
s
```
- "git stash params" shortcut
```bash
stash [params]
```

### Etc automations

- "certutil -decode source [target]" shortcut
```bash
b64d source [target]
```
- "certutil -encode source [target]" shortcut
```bash
b64e source [target]
```
- LaTeX delete build files (keeps only .pdf and .tex and deletes generated build files)
```bash
clean
```
- Python password generation on-the-fly
```bash
genpass
```
- "netsh wlan show profile [params] key=clear" - if "params" (name of wifi network, in quotation marks if it contains spaces) is supplied, shows the wifi network's password.
```bash
getpass [params]
```
- Check file hash using powershell. The "algorithm" needs to be one of powershell's supported hashes and written as follows (SHA1, SHA256, MD5, etc.) 
```bash
hashcmp (provided_hash) (path/to/source_file) (algorithm) 
```
- Get public ip address
```bash
ip
```
- Convert number from any base to any other base
```bash
numconv
```
- Performs a "shutdown params /t 0". "params" is the shutdown type (for instance /r for restart, /s for shutdown)
```bash
off params
```
- Reads a file out in one line
```bash
oneline /path/to/file
```
- Attempts to connect to an ip address on a given port
```bash
pingme
```
- Radio player, currently supports (Requires VLC to be installed!):
    - NDR 2 Radio [ndr2]
    - FFN Radio [ffn]
    - Rotana Radio Jordan [rotana]
```bash
play [station_name]
play stop
```
- Kills radio player/vlc
```bash
stop
```
- File transfer using python
```bash
ptransfer ip_address_of_file_sender
```
- Starts python password vault
```bash
pv
```
- Starts serving an http server using python
```bash
serve
```
- Unzips all zip files in the current directory
```bash
unzipall
```
- Opens the current directory
```bash
wd
```
- Lists network profiles
```bash
wifi
```

## Please note:
- To use the "l.cmd" file properly, please execute (in an administrative command shell) the command included at the end of the l.cmd file. This only needs to be done once.

## DISCLAIMER:
The customized git log command included in the "l.cmd" file is not made by me. All credits go to the creator: https://coderwall.com/p/euwpig/a-better-git-log 
