def chatbot_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"
    
    elif any(bye in user_input for bye in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"

    elif "how are you" in user_input:
        return "I'm doing great, thank you! How about you?"
    
    elif "your name" in user_input:
        return "I am CodeAlphaBot, your friendly assistant."
    
    elif "thank" in user_input:
        return "You're welcome!"
    
    else:
        return "I am sorry, I don't understand. Can you rephrase?"

print("=== Welcome to CodeAlphaBot ===")
print("Type 'bye' to exit the chat.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    
    if any(bye in user_input.lower() for bye in ["bye", "goodbye", "see you"]):
        break
