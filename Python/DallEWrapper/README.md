# Azure OpenAI Dall-E Wrapper

This Dall-E module allows seemless integration of the Azure OpenAI Dall-E image generator.

The provided logging operations require my [Logging module](https://github.com/leolion3/Portfolio/tree/master/Python/Logger) but can also be replaced by any generic logging framework. To use the logger, simply add the `DALL_E` enum declaration to the `Logger.Module` dictionary.

## Requirements

The module requires the `openai` python library (version `1.0.0+`).

```bash
pip install openai
```

## Setup

On line `125` the Azure OpenAI API key needs to be loaded in whichever form you prefer.

In the demo's case, the API key is loaded from a `setup.py` file which loads it from the user's environment
variables and validates its functionality before passing it to the module.

By default, the Azure Dall-E configs are loaded from a `dall_e.json` file:

```json
{
	"api_version": "2024-02-01",
	"azure_endpoint": "https://link_to_your_azure_openai_deployment.com/",
}
```

## Usage

To use the module, simply import the `dall_e` singleton instance and call the `generate_image` method:

```python
import dall_e_wrapper
from dall_e_wrapper import DallE


dall_e: DallE = dall_e_wrapper.dall_e
image_url: str = dall_e.generate_image('Hello World!')  # Returns a URL to the generated image.
```

The module also allows customizing the generated image by providing the following variables:

```python
# The image size
image_size: Optional[Literal["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"]]

# The image style
image_style: Optional[Literal["vivid", "natural"]]

# The image quality
image_quality: Optional[Literal['hd', 'standard']]

# Whether to return a Azure URL to the image or return the image encoded in base64 in a json response.
# The default is 'url'.
response_format: Literal["url", "b64_json"]
```
