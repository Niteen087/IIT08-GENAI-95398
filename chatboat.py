from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# Set up logging (optional, helps with debugging)
logging.basicConfig(level=logging.INFO)

# Create a new chatbot instance
chatbot = ChatBot("MyChatBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus data
trainer.train("chatterbot.corpus.english")

print("ChatBot: Hello! Type 'bye' to exit.")

# Main conversation loop
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print(f"ChatBot: {response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
