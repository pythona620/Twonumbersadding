# number adding

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger
from random import randint
__author__ = 'pythona620/prasad'
LOGGER = getLogger(__name__)
class NumberGuessSkill(MycroftSkill):
	lowerBound = 0
	upperBound = 100
	answer = 0
	userGuess = 0
	def get_numerical_response(self, dialog):
		while True:
			val = self.get_response(dialog)
			try:
				val = int(val)
				return val
			except ValueError:
				self.speak_dialog("invalid.input")
			except:
				self.speak_dialog("input.error")
	@intent_handler(IntentBuilder("").require("NumberGuess").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")
		# get lower bound
		lowerBound = self.get_numerical_response("get.lower")
		# get upper bound
		upperBound = self.get_numerical_response("get.upper")
		answer = randint((lowerBound +upperBound))
		self.speak_dialog("answer")
		
	def stop(self):
		lowerBound, upperBound = 0, 100
		answer = 0
		userGuess = answer
		return True
def create_skill():
	return NumberGuessSkill()