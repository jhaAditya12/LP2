# Define the ChatBot class
class ChatBot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello! Welcome to our service. How can I assist you today?"

    def farewell(self):
        return "Thank you for visiting us. Have a great day!"

    def handle_message(self, message):
        message = message.lower()
        if "help" in message or "support" in message:
            return "Sure, I can help you. What seems to be the problem?"
        elif "thank" in message:
            return "You're welcome! Is there anything else I can do for you?"
        elif "bye" in message:
            return self.farewell()
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Create an instance of the ChatBot
bot = ChatBot("CustomerSupportBot")

# Simulate a conversation
print(bot.greet())
user_message = ""
while user_message != "bye":
    user_message = input("You: ")
    response = bot.handle_message(user_message)
    print(f"{bot.name}: {response}")
