# from rasa_nlu.converters import load_data
# from rasa_nlu_config import RasaNLUConfig
# from rasa_nlu.model import Trainer

# def train_nlu(data, config, model_dir):
	# training_data = load_data(data)
	# trainer = Trainer(RasaNLUConfig(config))
	# trainer.train(training_data)
	# model_directory = training.persist(model_dir, fixed_model_name = 'retailbot')
	
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter


def train_nlu(data, confi, model_dir):
	training_data = load_data(data)
	#trainer = Trainer(RasaNLUConfig(config))
	trainer = Trainer(config.load(confi))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'retailbot')

	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/retailbot')
	print(interpreter.parse("what is the sales in store369 between 01-01-2018 and 02-01-2018 ?"))
	

	
if __name__ == '__main__':
	#train_nlu("./data/data.json","config.yml","./models/nlu")
	run_nlu()