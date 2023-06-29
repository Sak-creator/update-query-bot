


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class GenerateUpdateQueryAction(Action):
    def name(self) -> Text:
        return "generate_update_query_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity_value = tracker.get_slot("rowname")
        intent = tracker.latest_message.get("intent").get("name")
        rowname = tracker.get_slot("rowname")
        quantity = tracker.get_slot("quantity")
        update = tracker.get_slot("update")
        skill = tracker.get_slot("skill")
        new_name = tracker.get_slot("new_name")
        number = tracker.get_slot("number")
        customer_id = tracker.get_slot("customer_id")
        if intent == "provide_rowname":
            update_query = f"{update} {rowname} SET Name = '{new_name}', {skill} {quantity} {number} WHERE CustomerID = {customer_id};"
            dispatcher.utter_message(template="utter_display_update", querynew=update_query)
        else:
            sql_query = "default"

        return []
