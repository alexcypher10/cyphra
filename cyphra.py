class Chatbot:
    def __init__(self, name):
        self.name = name

    def response(self, user_input):
        user_input = user_input.lower()
        if user_input == "hello":
            return "Hi, how can i help you today"
        elif user_input == "who are you":
            return f"i am {self.name} an automated chatbot..."
        elif user_input == "bye":
            return "good bye and have a nice day ahead.."
        else:
            return "Sorry but this is beyond my scope for now... "

        

    