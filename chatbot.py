def get_response(user_input):
    """
    Takes the user's input, normalizes it, and returns a matching
    predefined reply using if-elif logic.
    """
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you doing", "how's it going"):
        return "I'm fine, thanks! How about you?"
    elif text in ("what is your name", "who are you"):
        return "I'm a simple rule-based chatbot!"
    elif text in ("bye", "goodbye", "see you"):
        return "Goodbye! Have a great day!"
    elif text in ("thanks", "thank you"):
        return "You're welcome!"
    elif text == "":
        return "Please type something so I can respond!"
    else:
        return "Sorry, I don't understand that. Can you try something else?"


def chat():
    """
    Runs the main chatbot loop, reading user input and printing responses
    until the user says 'bye'.
    """
    print("Chatbot: Hello! Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "see you"):
            break


if __name__ == "__main__":
    chat()
