# Trash Schedule Notifier

This script runs an active scheduler which queries the API of the [Bremer Stadtreinigung](https://www.die-bremer-stadtreinigung.de/) and looks up the trash schedule for the next day.
The script then proceeds to send a telegram message to the given chat-id if the garbage collection is happening on the next day.

The script can best be ran in a [screen](https://www.gnu.org/software/screen/) session on some hosted server. No need to worry about credentials - everything is passed in using the getpass module.

## Requirements

The script requires 2 modules:

```bash
apscheduler
requests
```

They can be installed using the provided `requirements.txt` file.

To allow Telegram notifications, a Bot needs to be created ([see how](https://core.telegram.org/bots/tutorial)) and the Chat-ID of the chat/group-chat needs to be provided to the script.

Since the contacted API service is quite "primitive", the street address and house number need to be provided in the correct abbreviations and capitalisations. To check how your address is spelled, check the network logs when accessing the service at https://www.die-bremer-stadtreinigung.de/abfallkalender.