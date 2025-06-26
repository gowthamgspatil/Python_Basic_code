def chatbot():
    print("Hi, I'm ChatBot. Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user == 'bye':
            print("ChatBot: Goodbye Gowtham!")
            break
        elif "how are you" in user:
            print("ChatBot: I'm just code, but I'm fine!")
        elif "name" in user:
            print("ChatBot: I'm ChatBot, your assistant.")
        else:
            print("ChatBot: Sorry, I don't understand.")

chatbot()