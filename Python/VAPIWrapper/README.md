# VAPI API Wrapper

This module provides a simple VAPI API Wrapper that allows placing and scheduling outbout phone calls,
getting a list of currently scheduled calls and deleting both scheduled and past calls.

It also allows retrieving the coversation flow with OpenAI from messages sent from VAPI to your backend, along with fetching the conversation summary.

## Requirements

The module requires the `requests` library.

## Setup

To instantiate the wrapper, create a `config.py` file and add the following variables:

```python
VAPI_API_KEY: str = os.getenv('VAPI_API_KEY')
VAPI_PHONE_NUMBER_ID: str = os.getenv('VAPI_PHONE_NUMBER_ID')
VAPI_ASSISTANT_ID: str = os.getenv('VAPI_ASSISTANT_ID')
```

You can then import the wrapper using:

```python
from vapi_wrapper import vapi
```

## Placing Phone Calls

To place a phone call:

```python3
vapi_wrapper.place_call(
	customer_phone_numbers=['phone numbers (with (+) country code)']
)
```

## Scheduling Phone Calls

To schedule a call at a later date:

```python3
vapi_wrapper.place_call(
	customer_phone_numbers=['phone numbers (with (+) country code)'],
	scheduled=True,
	scheduled_at_iso='Datetime object in ISO 806 format (datetime.isoformat())'
)
```

## Delete (Scheduled-) Call

To delete a scheduled call or past call data:

```python
vapi_wrapper.delete_call(call_id)
```

The `call_id` can be retrieved from `list_scheduled_calls` and is present in the key `id` for each value of the returned dictionary.

## Get (Scheduled) Calls

To get a list of calls, use:

```python3
vapi_wrapper.list_calls()  # Defaults to scheduled calls.
```

To get a list of all calls:

```python3
vapi_wrapper.list_calls(status_filters=[])  # Defaults to scheduled calls.
```

> Available filters: `['scheduled', 'queued', 'ringing', 'in-progress', 'forwarding', 'ended']`

## Get Scheduled Call Ids

Returns a dictionary mapping of phone numbers to call-ids. This allows mapping call ids to summary messages.
To retrieve the dictionary, pass the result of `place_call` to `get_call_ids_for_call_schedule`:

```python
vapi_wrapper.get_call_ids_for_call_schedule(vapi_wrapper.place_call(...))

# Output:

{
	'phone_number': 'call_id',
	...
}
```

## Get OpenAI Messages

To retrieve the OpenAI messages used during the call, enable call messaging in your assistant `Assistant > Advanced > Messaging` and then pass the request body from vapi to `get_openai_messages_from_vapi_message`:

```python
vapi_wrapper.get_openai_messages_from_vapi_message(request.body.json())

# Output

[
	{
		'role': 'system',
		'prompt': '...'
	}
]
```

## Get Call Analysis

Similar to `Get OpenAI Messages`, retrieves the call summary when the call is over. Just pass the request body from the vapi message to `get_call_analysis`:

```python
vapi_wrapper.get_call_analysis(request.body.json())

# Output
The user said xyz... (Based on your evaluation prompt)
```
