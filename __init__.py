# number adding
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

__author__ = 'pythona620/prasad'
LOGGER = getLogger(__name__)

class NumberAddingSkill(MycroftSkill):

	frist_no = 0
	second_no = 0
	
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

		# get frist_no
		frist_no = self.get_numerical_response("get.frist_no")
		# get second_no
		second_no = self.get_numerical_response("get.second_no")
		answer = (frist_no + second_no)
	def stop(self):
		print ("add two numbers is:",answer)
		pass
def create_skill():
	return NumberAddingSkill()
