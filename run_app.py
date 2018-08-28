from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/retailbot') ## model path
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-423894218069-423894219605-424790010167-542a4c4faab8353d53dfe2e1d3ae56af', #app verification token
							'xoxb-423894218069-423901535829-mCl8rB6reWAonQpHCMXhsbB9', # bot verification token
							'tmuWECAy59Qba6hbYzSJft11', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))