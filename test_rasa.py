from rasa_nlu.model import Interpreter
from rasa_nlu.config import RasaNLUConfig
import json
import glob

model_dirs = sorted(glob.glob('./rasa_model/default/model_*/'))
model_path = model_dirs[-1]

#spacy_sklearn
args = {'pipeline': 'spacy_sklearn'}

config = RasaNLUConfig(cmdline_args = args)

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(model_path, config)

test_phrases = [
u'what is the top grossing app',
u'is Facebook the number 1 free app',
u'what place is FACEBOOK',
u'how is snapchat doing',
u'what is the 50th most popular free app',
u"hi bot, what's up",
u'good day sir'
]

for phrase in test_phrases:
	parsed = interpreter.parse(phrase)

	print('INPUT')
	print(parsed['text'])
	print('INTENT')
	print(json.dumps(parsed['intent'], indent=2))
	print('ENTITIES')
	print(json.dumps(parsed['entities'], indent=2))
	print('\n')