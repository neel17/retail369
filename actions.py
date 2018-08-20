from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class ActionSales(Action):
	def name(self):
		return 'action_sales'
		
	def run(self, dispatcher, tracker, domain):
		store_id = tracker.get_slot('store_id')
		date = tracker.get_slot('date')

		response = """It is currently the default message, since the database connection is pending"""
		#response = []
		#response.append([store_id,date])

				
		dispatcher.utter_message(response)
		return [SlotSet('store_id',store_id)]