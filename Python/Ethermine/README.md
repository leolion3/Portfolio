# Ethermine Ticker

## Usage

Set the ADDRESS constant to your ethereum address, the API_TOKEN to your Etherscan API Token and the POLY_API_TOKEN to your Polygonscan API Token. 

Get API Tokens:

Etherscan:
```
https://etherscan.io/apis
```

Polyscan:
```
https://polygonscan.com/apis
```

Output example (number of x's after the comma is predefined as seen below):

```bash
#> ./ethermine_fetch_outstanding_balance.py
===== Ethermine status =====

--- Account Statistics ---
Account Balance: x.xxxx ⧫
Polygon Balance: x.xxxx ⧫
---------------------------
Total Balance: x.xxxx ⧫
Total Balance USD: x.xx $

--- Miner Statistics ---
Current Hashrate: x MH/s
Reported Hashrate: x MH/s
Unpaid Balance: x.xxxxx ⧫
Active Workers: x
Valid Shares: x
Invalid Shares: x
Stale Shares: x

============================
```

## Requirements

The script requires the following modules:

```
# requests_html - not required unless you want to view the next payout date, currently not working
requests
```

Please note that getting the requests_html library to work on ARM Chips (for instance Raspberry Pi's) requires a bit of additional fiddling, check the guide below.

## Author

Leonard Haddad

## Requests_html on ARM

### One-Liners

Chromium installation:

```bash
sudo apt install python3-pip libxslt-dev chromium-codecs-ffmpeg-extra chromium-browser -y && pip3 install --upgrade requests && pip3 install --upgrade requests_html
```

Replacing x86/x64 version of chromium with ARM version:

```bash
rm -rf ~/.local/share/pyppeteer/local-chromium/588429/chrome-linux/* && cd ~/.local/share/pyppeteer/local-chromium/588429/chrome-linux/ && ln -s /usr/bin/chromium-browser chrome && cd ~
```

### Detailed Documentation

Install pip3 using

```bash
sudo apt install python3-pip -y
```

Install the required libraries

```bash
pip3 install requests && pip3 install requests_html
```

To get the ARM chromium browser running (used in background by requests_html) execute

```bash
sudo apt-get install libxslt-dev chromium-codecs-ffmpeg-extra chromium-browser -y
```

Now execute the python script, this will download a x86/x64 Version of Chromium, however just let it run. The script will then spit out an error as the browser can't be run on the ARM Chip, this however is completely fine.

Execute the following to remove the x86/x64 version of chromium and create a symbolic link in its place pointing to the ARM version of chromium

```bash
rm -rf ~/.local/share/pyppeteer/local-chromium/588429/chrome-linux/* && cd ~/.local/share/pyppeteer/local-chromium/588429/chrome-linux/ && ln -s /usr/bin/chromium-browser chrome && cd ~
```
