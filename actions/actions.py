# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

from datetime import datetime
import pytz
def CheckAvailablityTime():
    UTC=pytz.utc
    IST=pytz.timezone('Asia/Kolkata')
    datetime_ist=datetime.now(IST)
    check_new = 0
    check = datetime_ist.strftime('%H')
    if (check[0] == '0'):
        check_new = check[1]
    else:
        check_new = int(check)
    if ((check_new >= 7 and check_new < 10) or (check_new >= 19 and check_new < 22)):
        return 1
    else:
        return 0
    print(check_new)

n=CheckAvailablityTime()
if(n==1):
    return(time())