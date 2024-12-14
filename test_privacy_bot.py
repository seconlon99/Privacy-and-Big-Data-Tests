from zulip_bots.request_test_lib import mock_request_exception
from zulip_bots.test_lib import BotTestCase, DefaultTests
from typing_extensions import override
from typing import Any, Dict, Optional

class TestPrivacyBot(BotTestCase, DefaultTests):
    bot_name = "privacy_bot"
    @override
    #to control, what information of message is created in test evnironment, in real settings is much more
    def make_request_message(self, content: str) -> Dict[str, Any]:
        message = super().make_request_message(content)
        message["sender_full_name"] = "Julius Caesar"
        message["id"] = "1234567"
        message["sender_email"] = "emperor@zulip.com"
        message["sender_id"] = "505"
        message["display_recipient"] = 'JulCaes'
        return message

    def test_sender_full_name(self) -> None:
        # This test tests, whether full name of recipient is present in message dic
        message_in_chat = 'Nice to meet you John, my name is Charles.'
        message = self.make_request_message(message_in_chat)
        #if sender's full name is not present in message then raise error
        assert 'sender_full_name' in message

    def test_bot(self) -> None:
        # This test tests, how much information and what of kind was passed to the bot
        message_in_chat = 'Nice to meet you John, my name is Charles.'
        self.verify_privacy(message_in_chat)
