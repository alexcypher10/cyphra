import logging
from src.cyphra import Chatbot
from src.database import *
bot = Chatbot("cyphra")

logging.basicConfig(
     filename="cyphra.log",
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    while True:
        try:
            user_input = input("user: ")
            save_message(conversation_id, "user", user_input)
            reply = bot.response(user_input)
            print (reply)
            if user_input.lower() == "bye":
                 break
        except KeyboardInterrupt:
             print("Goodbye!!")       
             break
        except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print(f"sorry, something went wrong: {e}")

existing_user = get_user_by_username("cypher")
if existing_user:
     user_id = existing_user[0]
else:
     user_id = create_user("cypher","cypher@gmail.com", hash_password ("placeholder123"))

conversation_id = start_conversation(user_id)
            

if __name__ == "__main__":
    main()