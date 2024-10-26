from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import locale

class ActionTellDay(Action):
    def name(self):
        return "action_tell_day"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Define o idioma para português
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

        # Obtém a data atual
        today = datetime.now()
        day_of_week = today.strftime("%A")  # Nome do dia da semana em português
        date_str = today.strftime("%d/%m/%Y")

        # Monta a mensagem
        message = f"Hoje é {day_of_week}, {date_str}."
        dispatcher.utter_message(text=message)

        return []
