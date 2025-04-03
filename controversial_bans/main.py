from chatbot import ChatBot

def main():
    bot = ChatBot()
    print("Starting secure chatbot...")
    print("*" *50)
    print("\nType 'exit', 'quit', or 'bye' to end the conversation.")
    bot.start_chat()

if __name__ == "__main__":
    main()