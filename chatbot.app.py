import streamlit as st

# Chatbot logic function
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

# Set page title
st.set_page_config(page_title="Simple ChatBot")

st.title("💬 Simple Python ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get user input
user_input = st.chat_input("Say something...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get and display bot response
    response = get_bot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
