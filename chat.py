import random
import re

# List of possible responses for different scenarios
greetings = ["hello", "hi", "hey", "hola"]
thanks = ["thanks", "thank you"]
options = ["account opening", "open an account", "new account"]
goodbyes = ["bye", "goodbye", "see you later"]

# Variable to track the state of the conversation
waiting_for_confirmation = False

# Function to generate random responses
def get_random_response(responses):
    return random.choice(responses)

# Function to handle user input and generate responses
def respond(message):
    global waiting_for_confirmation
    
    if re.search(r"\bhello\b", message, re.IGNORECASE):
        return get_random_response(greetings)
    
    elif re.search(r"\bbye\b", message, re.IGNORECASE):
        return get_random_response(goodbyes)
    
    elif re.search(r"\b(?:open|opening|new)\b.*\baccount\b", message, re.IGNORECASE):
        waiting_for_confirmation = True
        return "Sure, let's continue."
    
    elif any(word in message.lower() for word in thanks):
        return "You're welcome!"
    
    elif waiting_for_confirmation and message.strip().lower() == "ok":
        waiting_for_confirmation = False
        return "Please provide your full name."
    
    else:
        return "I'm sorry, I didn't understand that."

# Sample conversation loop
def main():
    print("Welcome to the Bank Account Opening Chatbot!")
    print("How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        response = respond(user_input)
        print("Bot:", response)
        
        if any(word in user_input.lower() for word in goodbyes):
            break

if __name__ == "__main__":
    main()
