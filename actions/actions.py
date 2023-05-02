# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hola! Soy Polito, el bot del Polo. Cómo puedo ayudarte?")

        return []



# This is a simple example for a custom action which utters "Hello World!"

#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#class ActionSessionStart(Action):
#    def name(self) -> Text:
#        return "action_session_start"
#        
#         async def run(
#      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#    ) -> List[Dict[Text, Any]]:
#        dispatcher.utter_message(response="utter_iamabot")
#        return [SessionStarted(), ActionExecuted("action_listen")]
