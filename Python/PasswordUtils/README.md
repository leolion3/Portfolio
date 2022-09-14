# Password Transfer Tool (Insecure)

Use this tool to send passwords or sensitive text over LAN.

## Usage

The tool can be used with the sender's IP Address as a CMD argument, or it can be specified through the input field.
The password is read **from the sender's clipboard** using Pyperclip or using getpass if Pyperclip fails to do so.

```bash
./passtransfer [optional_sender's_ip_address]
```

## Requirements

The following modules are required:

```
getpass
pyperclip
```