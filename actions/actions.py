
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime

class ActionTellTime(Action):
    def name(self):
        return "action_tell_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        current_time = datetime.now()
        hour = current_time.hour

        if 5 <= hour < 12:
            greeting = "Bom dia"
        elif 12 <= hour < 18:
            greeting = "Boa tarde"
        else:
            greeting = "Boa noite"

        time_str = current_time.strftime("%H:%M")
        message = f"{greeting}! Agora são {time_str}."
        dispatcher.utter_message(text=message)

        return []
        