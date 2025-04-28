import random

responses = {
    "hello": "Hi there!",
    "how are you": "I'm good, thanks!",
    "bye": "Goodbye! Have a great day!",
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I don't understand that.")

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        print(f"Chatbot: {chatbot_response(user_input)}")