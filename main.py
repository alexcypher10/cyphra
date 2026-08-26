from cyphra import Chatbot
bot = Chatbot("cyphra")

def main():
    while True:
        try:
            user_input = input("user: ")
            reply = bot.response(user_input)
            print (reply)
            if user_input.lower() == "bye":
                 break
        except KeyboardInterrupt:
             print("Goodbye!!")       
             break
        except Exception as e:
                print(f"sorry, something went wrong: {e}")
            

if __name__ == "__main__":
    main()