# Microsoft Graph API Services

This module contains a list of generic Microsoft Graph API Service classes with plug-and-play capability for production code.

## Current List

- `mail_service.py`: Module for sending outgoing emails through microsoft graph.
	- Requires the `SEND_MAIL` permission along with a mailbox for sending outgoing emails.

## Config File

The modules utilize a `config.json` file that is used for storing authentication credentials with the Graph API.

The config must be structured as follows:

```json
{
	"TENANT_ID": "Tenant ID of the Graph API app registration",
	"CLIENT_ID": "Client ID of the Graph API app registration",
	"OUTGOING_MAILBOX_ADDRESS": "Email for sending outgoing emails, used by the `mail_service` module."
}
```

Additionally, a `MSAL_CLIENT_SECRET` must be specified in some config file. This can be done in a `config.py` file as follows:

```python3
import os
import dotenv

dotenv.load_dotenv()
MSAL_CLIENT_SECRET: str = os.getenv('MSAL_CLIENT_SECRET')
```

> These modules utilize my logging framework which can be found [here](https://github.com/leolion3/Portfolio/tree/master/Python/Logger). To use it, simply add the key-value pairs to the `log_handler.Module` enum, For example: `MAIL = "Graph API Email Service"`
