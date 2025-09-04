#!/usr/bin/env python3
from typing import List, Dict, Any

import msal, requests, json
from msal import ConfidentialClientApplication

import os
import setup

from logging_framework.log_handler import log, Module


class GraphEmailService:
    """
    Handles outgoing mail using microsoft graph.
    """
    CONFIG: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    GRAPH_ROOT_URL: str = "https://graph.microsoft.com/v1.0"
    SCOPE: List[str] = ["https://graph.microsoft.com/.default"]

    @staticmethod
    def _build_html_payload(
            subject: str,
            body: str,
            recipients: List[str],
            is_html: bool = False,
            save_to_sent: bool = True
    ) -> Dict[str, Any]:
        """
        Build the payload for sending emails with graph api.
        :param subject: the email subject.
        :param body: the email body - either a string (default) or html text.
        :param recipients: list of email addresses.
        :param is_html: whether the mail body is already html text or plaintext. Defaults to False (Plaintext).
        :param save_to_sent: whether the email should be saved to the "sent" folder. Defaults to True.
        :return: the payload dictionary.
        """
        return {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "HTML",
                    "content": body if is_html else f"<p>{body}</p>"
                },
                "toRecipients": [{
                    "emailAddress": {
                        "address": email
                    }
                } for email in recipients],
            },
            "saveToSentItems": save_to_sent
        }

    def send_email(
            self,
            subject: str,
            body: str,
            recipients: List[str],
            is_html: bool = False,
            save_to_sent: bool = True
    ) -> None:
        """
        Send a new email using the graph api.
        :param subject: the email subject.
        :param body: the email body - either a string (default) or html text.
        :param recipients: list of email addresses.
        :param is_html: whether the mail body is already html text or plaintext. Defaults to False (Plaintext).
        :param save_to_sent: whether the email should be saved to the "sent" folder. Defaults to True.
        :return:
        """
        self._acquire_token()
        resp = requests.post(
            f"{self.GRAPH_ROOT_URL}/users/{self.outgoing_mailbox_address}/sendMail",
            headers=self._get_authentication_headers(),
            data=json.dumps(self._build_html_payload(
                subject=subject,
                body=body,
                recipients=recipients,
                is_html=is_html,
                save_to_sent=save_to_sent
            )),
            timeout=30
        )

        if resp.status_code not in (202, 200):
            raise SystemExit(f"Send failed: {resp.status_code} {resp.text}")
        log.info("Emails sent!", module=Module.MAIL)

    @staticmethod
    def _load_configs(config_file_path: str):
        """
        Load the azure chatbot configs from the provided file.
        :param config_file_path: path to the json configs file.
        :return: the configs as a json object.
        """
        with open(config_file_path) as config_file:
            return json.load(config_file)

    def _get_msal_application(self) -> ConfidentialClientApplication:
        """
        Load the azure chatbot configs and return the LLM objects.
        :return: the azure chatbot instance.
        """
        configs = self._load_configs(config_file_path=self.CONFIG)
        client_secret: str = setup.MSAL_CLIENT_SECRET
        client_id: str = configs['CLIENT_ID']
        tenant_id: str = configs['TENANT_ID']
        authority: str = f"https://login.microsoftonline.com/{tenant_id}"
        self.outgoing_mailbox_address: str = configs['OUTGOING_MAILBOX_ADDRESS']

        if not client_secret:
            log.error('MSAL Client secret not set!', module=Module.MAIL)
            raise Exception()

        return msal.ConfidentialClientApplication(
            client_id=client_id,
            authority=authority,
            client_credential=client_secret
        )

    def _get_authentication_headers(self) -> Dict[str, str]:
        """
        Get the authentication headers for authenticating with microsoft graph api.
        :return: the authentication headers.
        """
        self._acquire_token()
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def _acquire_token(self) -> None:
        """
        Acquire the msal access token.
        :return:
        """
        result = self.msal.acquire_token_for_client(scopes=self.SCOPE)
        if "access_token" not in result:
            raise SystemExit(f"Token error: {result.get('error')} - {result.get('error_description')}")
        self.access_token = result["access_token"]

    def __init__(self):
        """
        Default constructor.
        """
        log.info('Starting mail service...', module=Module.MAIL)
        self.msal: ConfidentialClientApplication = self._get_msal_application()
        self._acquire_token()
        log.info('Mail service started.', module=Module.MAIL)


mail_service: GraphEmailService = GraphEmailService()

if __name__ == '__main__':
    mail_service.send_email(
        subject='Hello from Graph API',
        body='Hello from microsoft graph',
        recipients=[''],
        is_html=False,
        save_to_sent=False
    )
