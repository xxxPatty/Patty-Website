# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class relpy_sender_name(Action):
    def name(self) -> Text:
        return "relpy_sender_name"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("relpy_sender_name")
        sender_name = tracker.get_slot("sender_name").split(',',1)[1]
        dispatcher.utter_message(text="很高興認識你，"+sender_name+"。")
        return []
