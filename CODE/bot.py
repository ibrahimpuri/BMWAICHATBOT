import utils
import config
from dialogue_manager import DialogueManager

# Initialize dialogue manager
dialogue_manager = DialogueManager()

def chat():
    print("Welcome to the BMW AI Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = dialogue_manager.generate_response(user_input)
        print("BMW AI Chatbot:", response)

if __name__ == "__main__":
    chat()
