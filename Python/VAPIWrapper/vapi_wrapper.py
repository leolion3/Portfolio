#!/usr/bin/env python3
"""
Open-Source VAPI API Wrapper by Leonard Haddad, 2025.
Provided in accords with the MIT License.
More on GitHub at https://leolion.tk/
"""
from datetime import datetime
from typing import Dict, Any, List
from logging_framework.log_handler import log, Module

import requests
import config


class VApiWrapper:
    """
    Allows scheduling phone calls with VAPI.
    """

    _base_url: str = 'https://api.vapi.ai'

    def _get_authentication_headers(self) -> Dict[str, str]:
        """
        Get the HTTP Authentication headers for all api requests.
        :return: the authentication headers.
        """
        return {
            'Authorization': f'Bearer {self._api_key}',
            'Content-Type': 'application/json'
        }

    @staticmethod
    def is_valid_iso8601(dt_str: str) -> bool:
        try:
            if dt_str.endswith("Z"):
                dt_str = dt_str.replace("Z", "+00:00")
            datetime.fromisoformat(dt_str)
            return True
        except ValueError:
            return False

    def _build_outbound_call_payload(
            self,
            customer_phone_numbers: List[str],
            scheduled: bool = False,
            scheduled_at_iso: str = ''
    ) -> Dict[str, str | Dict[str, str]]:
        """
        Builds the outbound call payload.
        :param customer_phone_numbers: phone numbers to call.
        :param scheduled: whether the call is scheduled or not. Defaults to False.
        :param scheduled_at_iso: when the call is scheduled for in ISO 806 format. Defaults to '' (Not scheduled).
        :return: the outbound call payload dictionary.
        """
        _json: Dict[str, str | Dict[str, str]] = {
            'assistantId': self._assistant_id,
            'phoneNumberId': self._outbound_phone_number_id,
            'customers': [
                {
                    'number': number
                } for number in customer_phone_numbers
            ]
        }
        if scheduled and self.is_valid_iso8601(scheduled_at_iso):
            log.info('Scheduling call for ', scheduled_at_iso, module=Module.VAPI)
            _json['schedulePlan'] = {
                'earliestAt': scheduled_at_iso
            }
        return _json

    @staticmethod
    def get_call_analysis(vapi_message: Dict[str, Any]) -> str:
        """
        Retrieves the call analysis from the VAPI message (Assistant > Advanced > Messaging).
        :param vapi_message: the payload from VAPI.
        :return: The call analysis after the call has been ended.
        """
        return (vapi_message.get('message', {})
                .get('analysis', {})
                .get('summary', ''))

    @staticmethod
    def get_openai_messages_from_vapi_message(vapi_message: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Retrieves the OpenAI messages from the VAPI message (Assistant > Advanced > Messaging).
        :param vapi_message: the payload from VAPI.
        :return: A list of OpenAI messages.
        """
        return (vapi_message.get('message', {})
                .get('artifact', {})
                .get('messagesOpenAIFormatted', []))

    def list_calls(self, status_filters: List[str] = ['scheduled']) -> List[Dict[str, Any]]:
        """
        Lists calls based on the selected filters. Defaults to scheduled calls only.
        Available filters: ['scheduled', 'queued', 'ringing', 'in-progress', 'forwarding', 'ended']
        :return: a list of scheduled calls.
        """
        url: str = f'{self._base_url}/call'
        headers: Dict[str, str] = self._get_authentication_headers()
        headers.pop('Content-Type')
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return list(filter(len, [call if call.get('status') in status_filters else '' for call in r.json()]))

    def delete_call(self, call_id: str) -> None:
        """
        Deletes a call.
        :param call_id: the call id.
        :return:
        """
        url: str = f'{self._base_url}/call/{call_id}'
        headers: Dict[str, str] = self._get_authentication_headers()
        headers.pop('Content-Type')
        r = requests.delete(url, headers=headers)
        r.raise_for_status()
        log.info('Deleted call with id:', call_id, module=Module.VAPI)

    @staticmethod
    def get_call_ids_for_call_schedule(call_schedule_response: Dict[str, Any]) -> Dict[str, str]:
        """
        Retrieves call ids for the called phone numbers.
        :param call_schedule_response: the json response from VAPI's /call endpoint.
        :return:a dictionary mapping phone numbers to call ids.
        """
        results = call_schedule_response.get('results', [])
        return {
            result.get('customer', {}).get('number'): result.get('id', '')
            for result in results
        }

    def place_call(
            self,
            customer_phone_numbers: List[str],
            scheduled: bool = False,
            scheduled_at_iso: str = ''
    ) -> Dict[str, Any]:
        """
        Place a call
        :param customer_phone_numbers: the phone numbers to call.
        :param scheduled: whether to schedule calls. Defaults to False.
        :param scheduled_at_iso: ISO 806 time at which to schedule the call. Defaults to '' (No scheduled call).
        :return: The json response from VAPI.
        """
        url: str = f'{self._base_url}/call'
        log.info('Dialing phone numbers:', customer_phone_numbers, module=Module.VAPI)
        r = requests.post(
            url,
            headers=self._get_authentication_headers(),
            json=self._build_outbound_call_payload(
                customer_phone_numbers=customer_phone_numbers,
                scheduled=scheduled,
                scheduled_at_iso=scheduled_at_iso
            )
        )
        try:
            r.raise_for_status()
            return r.json()
        except Exception as e:
            log.error('Error in request to VAPI. Trace:', e, module=Module.VAPI)
            raise

    def __init__(self):
        """
        Default constructor.
        """
        self._api_key: str = config.VAPI_API_KEY
        self._outbound_phone_number_id: str = config.VAPI_PHONE_NUMBER_ID
        self._assistant_id: str = config.VAPI_ASSISTANT_ID


vapi_wrapper = VApiWrapper()


# Test
if __name__ == '__main__':
    from datetime import timezone, timedelta

    scheduled_time = datetime.now(timezone.utc) + timedelta(minutes=1)
    response = vapi_wrapper.place_call(
        customer_phone_numbers=['+1...'],
        scheduled=True,
        scheduled_at_iso=scheduled_time.isoformat()
    )
    print(vapi_wrapper.get_call_ids_for_call_schedule(response))
    scheduled_calls = vapi_wrapper.list_calls()
    print(scheduled_calls)
    vapi_wrapper.delete_call(scheduled_calls[0].get('id', ''))
    print(vapi_wrapper.list_calls())
