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
		date = tracker.get_slot('time')
		d1 = date[:10]

		import pyodbc
		import pandas as pd
		
		cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                	"Server=pdssoldb.database.windows.net;"
                        "Database=PDS_Sol_1;"
                        "uid=Sandeep;pwd=Abcd@1111")

		query = "select sum(sales) from DH_ALL_STORES_ALL_DAYS_SALES_PRED_A where store_id = 369 and date = {}".format("'"+ d1 +"'")
		#df = pd.read_sql_query(query,cnxn)
		
		


		#response = """It is currently the default message, since the database connection is pending"""
		response = pd.read_sql_query(query,cnxn)
				
		dispatcher.utter_message(response)
		return [SlotSet('store_id',store_id)]