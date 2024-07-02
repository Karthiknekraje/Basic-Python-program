class BankAccountOpeningChatbot:
    def __init__(self):
        # Initialize the chatbot
        self.current_step = 0  # Track the current step in the conversation
        self.questions = [
            "Welcome to our bank! To open a new account, I need to ask you a few questions.",
            "Could you please provide your full name?",
            "What is your date of birth? (Format: DD/MM/YYYY)",
            "Could you please provide your address?",
            "Which type of account are you interested in? (e.g., Savings, Checking)",
            "How much initial deposit would you like to make?",
            "Thank you for the information. We will process your application and get back to you shortly.",
        ]
        self.responses = []  # List to store user responses
    
    def get_response(self, input_text):
        # Method to retrieve the chatbot's response based on user input
        if self.current_step < len(self.questions):
            # If there are more questions to ask
            self.responses.append(input_text)  # Store user input
            response = self.questions[self.current_step]  # Get the next question
            self.current_step += 1  # Move to the next question
        else:
            # If all questions have been asked
            response = "We have completed the account opening process. Is there anything else I can assist you with?"
        return response  # Return the response to be printed
    
    def start_chat(self):
        # Method to start the chatbot session
        print("Hello! I am your bank's virtual assistant.")
        print("How can I help you today?")
        while True:
            user_input = input("You: ").lower()  # Get user input and convert to lowercase
            if user_input in ['quit', 'exit', 'thank you']:  # Check if user wants to end the chat
                print("Chat ended.")
                break
            response = self.get_response(user_input)  # Get response from the chatbot
            print("Bank Bot:", response)  # Print the response from the bot

# Example usage:
bank_bot = BankAccountOpeningChatbot()
bank_bot.start_chat()