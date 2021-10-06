# Setup oh my zsh

## Install zsh and powerline fonts

```bash
sudo apt install zsh -y && sudo apt-get install powerline fonts-powerline -y
```

## Clone oh my zsh

```bash
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
```

## Create new zsh config file

```bash
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

## Install powerlevel9k

```bash
git clone https://github.com/Powerlevel9k/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

## Setup theme

```bash
nano .zshrc
ZSH_THEME="powerlevel9k/powerlevel9k"
POWERLEVEL9K_DISABLE_RPROMPT=true
POWERLEVEL9K_PROMPT_ON_NEWLINE=true
POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX=""
```

## Change default shell

```bash
chsh -s /bin/zsh
```

## Syntax highlighting

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$HOME/.zsh-syntax-highlighting" --depth 1 && echo "source $HOME/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> "$HOME/.zshrc"
```

## One-Liner

```bash
sudo apt install zsh -y && sudo apt-get install powerline fonts-powerline -y && git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc && git clone https://github.com/Powerlevel9k/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k && chsh -s /bin/zsh && git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$HOME/.zsh-syntax-highlighting" --depth 1 && echo "source $HOME/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> "$HOME/.zshrc" && nano .zshrc
```

## Revert on error

```bash
chsh -s /bin/bash
```

### Source

```
https://caffeinedev.medium.com/customize-your-terminal-oh-my-zsh-on-ubuntu-18-04-lts-a9b11b63f2
```

## Change Colors

In .zshrc:

```bash
ZSH_THEME="powerlevel9k/powerlevel9k"
```

Clone tmux-powerline:

```bash
git clone https://github.com/erikw/tmux-powerline .tmux-powerline
```

Paste files .tmux.conf and .tmux.conf.local in ```~/```

## One-Liner

```bash
sudo apt install tmux -y && git clone https://github.com/erikw/tmux-powerline .tmux-powerline
```

## Optional Tools

In the folder "tools/" there are a couple tools included:

- A file transfer tool written in python 3,
- A script to print the content of a file in one line, useful when working with encoding/decoding
- A script that converts Windows file endings to unix ones, useful when transferring a file using the above tool from Windows to Linux

To add them, execute the following:

```bash
cd ~ && mkdir etc && echo "export PATH=$PATH:~/etc" >> .zshrc
``` 

then copy the files into the "etc/" folder.