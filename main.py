from cyphra import Chatbot
bot = Chatbot("cyphra")

def main():
    while True:
        user_input = input("user: ")
        reply = bot.response(user_input)
        print (reply)
        if user_input.lower() == "bye":
            break
       

if __name__ == "__main__":
    main()