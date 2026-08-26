import logging
class Chatbot:
    def __init__(self, name):
        self.name = name

    def response(self, user_input):
        user_input = user_input.lower()
        if user_input == "hello":
            reply = "Hi, how can i help you today"
        elif user_input == "who are you":
            reply = f"i am {self.name} an automated chatbot..."
        elif user_input == "bye":
            reply = "good bye and have a nice day ahead.."
        else:
            logging.info(f"unrecognizedinput from user: {user_input!r}")
            reply = "Sorry but this is beyond my scope for now... "
        return reply

        

    