#!/usr/bin/env python3
"""
Open-Source Dall-E Wrapper Module by Leonard Haddad, 2025.
Provided in accords with the MIT License.
More on GitHub at https://leolion.tk/
"""
import os
import json
from typing import List, Literal, Optional, Dict
from openai import AzureOpenAI

import setup
from log_handling.log_handler import Logger, Module, get_instance

logger: Logger = get_instance()


class DallE:
    """
    Handles Dall-E image generation.
    """

    @staticmethod
    def _get_image_quality(specified_quality: str) -> str:
        """
        Detect the generation quality specified by the user.
        :param specified_quality: the image quality specified by the user.
        :return: the actual quality for Dall-E.
        """
        if specified_quality.lower().strip() == 'hd':
            return 'hd'
        return 'standard'

    @staticmethod
    def _get_image_style(specified_style: str) -> str:
        """
        Detect the generation style specified by the user.
        :param specified_style: the image style specified by the user.
        :return: the actual style for Dall-E.
        """
        if specified_style.lower().strip() == 'vivid':
            return 'vivid'
        return 'natural'

    @staticmethod
    def _get_image_size(provided_size: str) -> str:
        """
        Detect the image size specified by the user.
        :param provided_size: the image size specified by the user.
        :return: the actual size for Dall-E.
        """
        sizes: List[str] = ["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"]
        if provided_size.lower().strip() in sizes:
            return provided_size.lower().strip()
        return sizes[2]

    def generate_image(
            self,
            prompt: str,
            image_size: Optional[Literal["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"]] = '"1024x1024"',
            image_style: Optional[Literal["vivid", "natural"]] = 'natural',
            image_quality: Optional[Literal['hd', 'standard']] = 'standard',
            response_format: Literal["url", "b64_json"] = 'url',
            retries: int = 0
    ) -> str:
        """
        Makes a request to Dall-E.
        :param prompt: the user's prompt.
        :param image_size: the chosen image size. Default: '1024x1024'.
        :param image_style: the chosen image style. Default: 'natural'.
        :param image_quality: the chosen image quality. Default: 'standard'.
        :param response_format: the response format, either of 'url' or 'b64_json'.
        :param retries: the number of times the request has been retried (up to 3 retries by default).
        :return: the url of the generated image.
        """
        try:
            logger.debug('Requesting image generation for prompt {} with size {}, style {} and quality {}'
                         .format(prompt, image_size, image_style, image_quality), module=Module.DALL_E)
            result = self.client.images.generate(
                model="Dalle3",
                size=self._get_image_size(image_size),
                style=self._get_image_style(image_style),
                quality=self._get_image_quality(image_quality),
                response_format=response_format,
                prompt=prompt,
                n=1
            )
            image_url: str = json.loads(result.model_dump_json())['data'][0]['url']
            logger.debug('Generated image URL:', image_url, module=Module.DALL_E)
            return image_url
        except Exception as e:
            logger.error('Failed to generate image. Trace:', e, module=Module.DALL_E)
            if retries < 3:
                logger.error(f'Retrying {retries + 1}/3...')
                return self.make_dall_e_request(
                    prompt,
                    image_size,
                    image_style,
                    image_quality,
                    response_format,
                    retries + 1
                )
            return 'An internal error occurred during image generation. Please try again later.'

    @staticmethod
    def _load_configs(file_path: str = 'dall_e.json') -> Dict[str, str]:
        """
        Load the openai configs from disk.
        :return: the configs dictionary.
        """
        file_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Dall-E config file couldn't be found at {file_path}")
        with open(file_path) as f:
            return json.loads(f.read())

    def _get_azure_client(self) -> AzureOpenAI:
        """
        Creates the AzureOpenAI Dall-E client.
        :return:
        """
        configs: Dict[str, str] = self._load_configs()
        return AzureOpenAI(
            api_version=configs['api_version'],
            azure_endpoint=configs['azure_endpoint'],
            api_key=setup.DALL_E_API_KEY,  # TODO load the API key from your desired location.
        )

    def __init__(self):
        """
        Default constructor.
        """
        try:
            logger.info('Initialising Dall-E client...', module=Module.DALL_E)
            self.client = self._get_azure_client()
            logger.info('Dall-E client initialized.', module=Module.DALL_E)
        except Exception as e:
            logger.error('Failed to initialise Dall-E client. Trace:', e, module=Module.DALL_E)
            exit(-1)


dall_e: DallE = DallE()
