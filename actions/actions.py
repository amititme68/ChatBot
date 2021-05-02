# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import time
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
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
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         times=list(map(int, time.strftime('%H:%M').split(':')))
         if int(times[1])>30:
             timestr = '%02d:00'% (times[0]+1)
         else:
             timestr = '%02d:30' % (times[0])
         if(times[0]+(times[1]/60)>=19 and times[0]+(times[1]/60)<=22):
             dispatcher.utter_message(text="You have reserved 2 seats in our AC section for %s pm. Thanks!" % timestr)
         else:
            dispatcher.utter_message(text="We are not open at that time. We are only open from 7pm to 10pm")

         return []
