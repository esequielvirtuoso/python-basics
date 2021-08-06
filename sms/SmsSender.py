import requests
import json


class SmsSender():
    """Class for SMS sending."""

    def __init__(self) -> None:

        self.url = "https://www.fast2sms.com/dev/bulk"

        self.default_data = {
            'sender_id': 'FSTSMS',
            'message': 'Hi, this is a test message.',
            'language': 'english',
            'route': 'p',
            'numbers': '+5548991857512'
        }

        self.headers = {
            'authorization': 'YOUR API KEY HERE',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache'
        }

    def send_sms(self, data: dict, headers: dict) -> None:
        """Send the SMS.

        Args:
            data (dict): Data to send.
            headers (dict): Headers
        """
        if data == None:
            data = self.default_data

        response = requests.request("POST",
                                    self.url,
                                    data=data,
                                    headers=headers)

        returned_message = json.loads(response.text)

        print(returned_message['message'])

    def generate_data(msg: str, numbers: str, language: str='english') -> dict:
        """Generate a dict for sending SMS.

        Args:
            msg (str): Message to send.
            numbers (str): Recipient
            language (str, optional): Language of message. Defaults to 'english'.

        Returns:
            dict: returns a dict with the messages metadata.
        """
        return {
            'sender_id': 'FSTSMS',
            'message': msg,
            'language': language,
            'route': 'p',
            'numbers': numbers
        }
