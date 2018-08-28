from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import pyodbc
import pandas as pd
import datetime
import pytz
import dateutil.parser
from dateutil.relativedelta import relativedelta
 


class ActionSales(Action):
    def name(self):
        return 'action_sales'

    
    def run(self, dispatcher, tracker, domain):
        store_id = tracker.get_slot('store_id')
        date = tracker.get_slot('time')
        #d1 = date[:10]
        
        time_entity = next((e for e in tracker.latest_message.entities if
                                 e['entity'] == 'time'), None)

        
        ####### Extracting date extracted from the duckling for SQL query
        
        
        
        #Check for **duckling_time_dictionary['additional_info']['type']**
        #It would be either 
        #interval
        #value
        
        if time_entity['additional_info']['type'] == 'value':
            
            # Checking grain value for day, week, month, quarter, year
            
            # Day
            
            if time_entity['additional_info']['grain'] == 'day':
                format = '%Y-%m-%dT%H:%M:%S%z'
                datestring = time_entity['additional_info']['value'] 
                d = dateutil.parser.parse(datestring) 
                d1 = d.date() 
                d2 = d.date() + relativedelta(days = +1) # need to change the days=+1
            
            # Week
            elif time_entity['additional_info']['grain'] == 'week':
                format = '%Y-%m-%dT%H:%M:%S%z'
                datestring = time_entity['additional_info']['value']
                d = dateutil.parser.parse(datestring) 
                d1 = d.date() 
                d2 = d.date() + relativedelta(weeks = +1)
                
            # Month
            elif time_entity['additional_info']['grain'] == 'month':
                format = '%Y-%m-%dT%H:%M:%S%z'
                datestring = time_entity['additional_info']['value']
                d = dateutil.parser.parse(datestring) 
                d1 = d.date() 
                d2 = d.date() + relativedelta(months = +1)
                
            # Quarter
            elif time_entity['additional_info']['grain'] == 'quarter':
                format = '%Y-%m-%dT%H:%M:%S%z'
                datestring = time_entity['additional_info']['value']
                d = dateutil.parser.parse(datestring) 
                d1 = d.date() 
                d2 = d.date() + relativedelta(months = +3)
                
            # Year
            elif time_entity['additional_info']['grain'] == 'year':
                format = '%Y-%m-%dT%H:%M:%S%z'
                datestring = time_entity['additional_info']['value']
                d = dateutil.parser.parse(datestring) 
                d1 = d.date() 
                d2 = d.date() + relativedelta(years = +1)
                
            else:
                d1 = None
                d2 = None
                
        elif time_entity['additional_info']['type'] == 'interval':
            format = '%Y-%m-%dT%H:%M:%S%z'
            datestring_from = time_entity['value']['from'] 
            d_from = dateutil.parser.parse(datestring_from) 
            d1 = d_from.date()
            
            datestring_to = time_entity['value']['to']
            d_to = dateutil.parser.parse(datestring_to)
            d2 = d_to.date()
            
        else:
            d1 = None
            d2 = None
            
        ### Creating coonection to database on the basis of date       
            
        if d1 is not None:
            
        
        # Credentilas for connecting to the database
        
            cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=pdssoldb.database.windows.net;"
                            "Database=PDS_Sol_1;"
                            "uid=Sandeep;pwd=Abcd@1111")
            
            
            d1 = d1.strftime('%Y-%m-%d')
            d2 = d2.strftime('%Y-%m-%d')

            query = "select sum(sales) from DH_ALL_STORES_ALL_DAYS_SALES_PRED_A where store_id = 369 and date >= {} and date < {} ".format("'"+ d1 +"'","'"+ d2 +"'")
            
            #query = "select sum(sales) from DH_ALL_STORES_ALL_DAYS_SALES_PRED_A where store_id = 369 and date >= {} ".format("'"+ d1 +"'")
            
            df = pd.read_sql_query(query,cnxn)
            sale_extracted = str(df[''].values[0])



            #query = "select sum(sales) from DH_ALL_STORES_ALL_DAYS_SALES_PRED_A where store_id = 369 and date = {}".format("'"+ d1 +"'")
            
            response = "The total sale is : {}".format(sale_extracted)
        
        else:
            response = "Kindly provide a valid date for the query"
        
        dispatcher.utter_message(response)
        return [SlotSet('store_id',store_id)]
				
	