import logging
from typing import Dict, Final

import requests

from zulip_bots.lib import AbstractBotHandler
# See readme.md for instructions on running this code.


class PrivacyBotHandler:
    """
    This bot will return sender's full name from message dictionary.
    It is used to test, what bot can and what can't access.
    """

    META: Final = {
        "name": "Privacy bot",
        "description": "This bot will return sender's full name from message dictionary.",
    }

    def usage(self) -> str:
        return """
            This bot will return sender's full name from message dictionary.
            """

    def handle_message(self, message: Dict[str, str], bot_handler: AbstractBotHandler) -> None:
        bot_handler.send_reply(message, message)

handler_class = PrivacyBotHandler
