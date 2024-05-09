# 7. Develop an elementary chatboat for any suitable customer interaction 
# application.


class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "help": "Sure, I can help you. What do you need assistance with?",
            "bye": "Goodbye! Have a great day!",
            "default": "I'm sorry, I didn't understand that. Can you please rephrase?",
        }

    def respond(self, message):
        message = message.lower()
        if message in self.responses:
            return self.responses[message]
        else:
            return self.responses["default"]


# Example usage:
if __name__ == "__main__":
    bot = SimpleChatbot()
    print("Bot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = bot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() == "bye":
            break