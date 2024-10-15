# Git SSH Config Generator

Simple script for generating ssh-to-domain configurations for git (`~/.ssh/config`).

## Usage:

Before running the script, make sure to change the `username` constant to your own name.

```bash
./gconf.py -d domain.name -k /path/to/ssh/key
```

Generated file:

```bash
Host github.com
    HostName github.com
    User Leonard
    IdentityFile /path/to/id_rsa
    IdentitiesOnly yes
```