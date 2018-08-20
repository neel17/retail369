## story 01
* greet
	- utter_greet

## story 02
* goodbye
	- utter_goodbye
	
## story 03
* sales
	- utter_information_type
	
## story 04
* sales
	- utter_ask_store_id
	
## story 05
* sales
	- action_sales

## Generated Story -5564729926074529026
* greet
    - utter_greet
* sales{"date": "yesterday", "time": "2018-08-19T00:00:00.000-07:00"}
    - slot{"date": "yesterday"}
    - utter_ask_store_id
* sales{"store_id": "store1234"}
    - slot{"store_id": "store1234"}
    - action_sales
    - slot{"store_id": "store1234"}
* sales{"date": "last year", "time": "2017-01-01T00:00:00.000-08:00"}
    - slot{"date": "last year"}
    - action_sales
    - slot{"store_id": "store1234"}
    - export


	