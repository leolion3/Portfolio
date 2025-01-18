#!/usr/bin/env python3
"""
Open-Source Azure OpenAI Assistants (Preview) Wrapper by Leonard Haddad, 2025.
Provided in accords with the MIT License.
More on GitHub at https://leolion.tk/
"""
import json
import os
import time
from typing import Dict, List

from openai import AzureOpenAI
from openai.pagination import SyncCursorPage
from openai.types.beta import Assistant, Thread
from openai.types.beta.threads import Run, Message, TextContentBlock

import setup
from log_handling.log_handler import Logger, Module, get_instance

logger: Logger = get_instance()


class AzureOpenAIAssistantsWrapper:
    """
    Azure OpenAI Assistants wrapper.
    """

    def _create_chat_history(self, thread: Thread, current_messages: List[Dict[str, str]]) -> None:
        """
        Recreates the assistant's chat history when opening a new chat thread.
        :param thread: the openai assistant thread.
        :param current_messages: the current chat messages, including the new one from the user.
        :return:
        """
        for message in current_messages:
            if not message or not message["content"] or not message["role"]:
                continue
            if message["role"] not in ["user", "assistant"]:
                continue
            self.client.beta.threads.messages.create(
                thread_id=thread.id,
                role=message["role"],
                content=message["content"]
            )

    @staticmethod
    def _extract_text(message: Message) -> str:
        """
        Extracts the text from the api's response.
        :param message: the api's response message.
        :return: the text content, separated by newlines.
        """
        text_blocks: List[str] = []
        for block in message.content:
            if isinstance(block, TextContentBlock):
                text_blocks.append(str(block.text.value))
        return '\n'.join(text_blocks)

    def _carve_response(self, messages: SyncCursorPage[Message]) -> Dict[str, str]:
        """
        Extracts the actual answer from the assistant api.
        :param messages: the pagination of new messages returned by the assistants api.
        :return: a message formatted as a dictionary in the format {'role': 'assistant', 'content': 'message'}
        """
        if len(messages.data) < 2:
            raise Exception('Invalid message format returned.')
        # TODO expand or replace as necessary.
        logger.debug('Assistant response:', messages)
        message: Message = messages.data[0]
        return {
            'role': message.role,
            'content': self._extract_text(message)
        }

    @staticmethod
    def _handle_failed_run(run: Run) -> Dict[str, str]:
        """
        When a run does not complete with the state 'completed', handle the returned state.
        :param run: the unsuccessful run.
        :return: a data dictionary.
        """
        logger.debug('Run state:', run.status)
        if run.status == 'failed':
            error_message: str = run.last_error.message
            logger.error('Run failed with error:', error_message, module=Module.ASSIST)
        return {
            'role': 'assistant',
            'content': 'An error occurred. Please try again later.'
        }

    def _execute_completion(self, thread: Thread) -> Dict[str, str]:
        """
        Sends the messages to the assistant and awaits the completion.
        :param thread: the openai assistant thread.
        :return: the new generated message.
        """
        run: Run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant.id
        )
        while run.status in ['queued', 'in_progress', 'cancelling']:
            time.sleep(1)
            run: Run = self.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
        if run.status != 'completed':
            return self._handle_failed_run(run)

        messages: SyncCursorPage[Message] = self.client.beta.threads.messages.list(
            thread_id=thread.id
        )
        return self._carve_response(messages)

    def make_request(self, current_messages: List[Dict[str, str]]) -> Dict[str, str]:
        """
        Makes a new request to the assistant.
        :param current_messages: the current chat messages, including the new one from the user.
        :return: the new assistant response.
        Note: Messages have the format [{"role":"user","content":"hello?"},
                                        {"role":"assistant","content":"Hi, how may I help you?"}]
        """
        try:
            thread: Thread = self.client.beta.threads.create()
            self._create_chat_history(thread, current_messages)
            new_message: Dict[str, str] = self._execute_completion(thread)
            return new_message
        except Exception as e:
            logger.error('Error during assistant request. Trace:', e, module=Module.ASSIST)
            return {
                'role': 'assistant',
                'content': 'An error occurred. Please try again later.'
            }

    @staticmethod
    def _load_configs(file_path: str = 'assistant.json') -> Dict[str, str]:
        """
        Load the assistant's openai configs from disk.
        :return: the configs dictionary.
        """
        file_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Assistant config file couldn't be found at {file_path}")
        with open(file_path) as f:
            return json.loads(f.read())

    def _create_assistant(self) -> Assistant:
        """
        Creates the azure openai assistant.
        :return: the Azure OpenAI Assistant.
        """
        configs: Dict[str, any] = self.configs
        model: str = configs['model']
        instructions: str = configs['instructions']
        temperature: float = float(configs['temperature'])
        tools: List = configs['tools']
        tool_resources: Dict = configs['tool_resources']
        top_p: float = float(configs['top_p'])
        return self.client.beta.assistants.create(
            model=model,
            instructions=instructions,
            tools=tools,
            tool_resources=tool_resources,
            temperature=temperature,
            top_p=top_p
        )

    def _get_azure_client(self) -> AzureOpenAI:
        """
        Creates the azure openai client.
        :return: The Azure OpenAI client.
        """
        configs: Dict[str, any] = self.configs
        return AzureOpenAI(
            api_version=configs['api_version'],
            azure_endpoint=configs['azure_endpoint'],
            api_key=setup.AZURE_OPENAI_API_KEY,  # TODO load the API key from your desired location.
        )

    def __init__(self):
        """
        Default constructor.
        """
        try:
            logger.info('Initialising Azure OpenAI Assistants client...', module=Module.ASSIST)
            self.configs: Dict[str, any] = self._load_configs()
            self.client: AzureOpenAI = self._get_azure_client()
            self.assistant: Assistant = self._create_assistant()
            logger.info('Assistants client initialized.', module=Module.ASSIST)
        except Exception as e:
            logger.error('Failed to initialise Assistants client. Trace:', e, module=Module.ASSIST)
            exit(-1)


assistant: AzureOpenAIAssistantsWrapper = AzureOpenAIAssistantsWrapper()
