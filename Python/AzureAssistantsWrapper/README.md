# Azure OpenAI Assistants (Preview) Wrapper

This Assistants module allows seemless integration of the Azure OpenAI Assistants (Preview) chatbots.

The provided logging operations require my [Logging module](https://github.com/leolion3/Portfolio/tree/master/Python/Logger) but can also be replaced by any generic logging framework. To use the logger, simply add the `ASSIST` enum declaration to the `Logger.Module` dictionary.

## Requirements

The module requires the `openai` python library.

```bash
pip install openai
```

## Setup

On `line 177` the Azure OpenAI API key needs to be loaded in whichever form you prefer.

In the demo's case, the API key is loaded from a `setup.py` file which loads it from the user's environment
variables and validates its functionality before passing it to the module.

By default, the Azure OpenAI configs are loaded from a `assistant.json` file:

```json
{
  "api_version": "2024-05-01-preview", # Latest at the moment
  "azure_endpoint": "https://link_to_your_azure_openai_deployment.com/",
  "model": "Your GPT model, for instance, gpt4o",
  "instructions": "Instructions for the assistant",
  "tools": [ # Optional, can be empty [].
    {
      "type": "file_search",
      "file_search": {
        "ranking_options": {
          "ranker": "default_2024_08_21", # Latest at the moment
          "score_threshold": 0
        }
      }
    }
  ],
  "tool_resources": { # Optional, can be empty {}.
    "file_search": {
      "vector_store_ids": [
      	"Your vector store ids"
      ]
    }
  },
  "temperature": 0.9, # Adjust as necessary, 90% works well
  "top_p": 0.92 # Adjust as necessary, 92% works well
}
```

## Usage

To use the module, simply import the `assistant` singleton instance and call the `make_request` method:

```python
import assistants_wrapper
from assistant_wrappers import assistant


wrapper: AzureOpenAIAssistantsWrapper = assistants_wrapper.assistant
user_message: Dict[str, str] = {
    'role': 'user',
    'content': 'How are you today?'
}
response = wrapper.make_request([user_message])
print(response)  # "Im good, how are you doing?"
```

The input to the `make_request` method is always a list of dictionaries in the format, where the newest message is always **the first element** of the list:

```json
[
	{
		"role": "user",
		"content": "Newest question to ask"
	},
	{
		"role": "assistant",
		"content": "some answer"
	},
	{
		"role": "user",
		"content": "some question"
	}
]
```

The module currently returns only the latest message from the assistant (as a string). This can be changed through the `carve_response` method.

The assistant also cites sources and provides attachments in its response, these are omitted here for simplicity. To see the whole response, read the logs provided
by the code snippet on `line 68`.
