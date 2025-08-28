# chatbot.py

def chatbot_response(user_input):
    # super basic keyword-based logic
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hey there! 👋 How’s it going?"
    elif "how are you" in user_input:
        return "I’m just a bot, but I’m doing great 😄 What about you?"
    elif "bye" in user_input:
        return "Goodbye! 👋 Have a nice day!"
    else:
        return "Hmm... I’m not sure I understand 🤔"


# running the chatbot loop
if __name__ == "__main__":
    print("Chatbot is ready! Type 'bye' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye! 👋")
            break
        response = chatbot_response(user_input)
        print("Bot:", response)
