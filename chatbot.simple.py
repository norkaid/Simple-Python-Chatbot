def get_bot_response(user_input):
    user_input = user_input.lower()
    if user_input == 'bye':
        return "Goodbye! Have a nice day."
    elif 'hello' in user_input or 'hi' in user_input:
        return "Hello there!"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing well. Thanks!"
    elif 'name' in user_input:
        return "I'm called ChatBot."
    elif 'help' in user_input:
        return "You can ask me things like 'hello', 'how are you', or 'bye'."
    else:
        return "I'm not sure how to respond to that."
