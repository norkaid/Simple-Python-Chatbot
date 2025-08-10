import streamlit as st
import os

# Chatbot logic function
def get_bot_response(user_input):
    user_input = user_input.lower()
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    gratitude = ["thank you", "thanks", "thx", "appreciate"]
    mood = ["how are you", "how do you feel", "how's it going"]
    weather = ["weather", "rain", "sunny", "cloudy", "forecast"]
    jokes = ["joke", "funny", "laugh"]
    name = ["name", "who are you", "your name"]
    help_words = ["help", "can you do", "what can you do", "options"]

    # Contextual memory (simple)
    if "context" not in st.session_state:
        st.session_state.context = {}

    # Greetings
    if any(word in user_input for word in greetings):
        return "Hi! 👋 How can I help you today?"
    # Farewells
    if any(word in user_input for word in farewells):
        return "Goodbye! If you need anything else, just say hi again."
    # Gratitude
    if any(word in user_input for word in gratitude):
        return "You're welcome! 😊"
    # Mood
    if any(word in user_input for word in mood):
        return "I'm just a bot, but I'm always here to help! How are you?"
    # Weather
    if any(word in user_input for word in weather):
        return "I can't check the weather, but I hope it's nice where you are!"
    # Jokes
    if any(word in user_input for word in jokes):
        return "Why did the computer show up at work late? It had a hard drive! 😄"
    # Name
    if any(word in user_input for word in name):
        return "I'm called ChatBot, your friendly virtual assistant."
    # Help
    if any(word in user_input for word in help_words):
        return "I can chat, tell a joke, answer simple questions, and keep you company! Try saying 'hello', 'tell me a joke', or 'bye'."
    # Remember user's name
    if "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().split()[0].capitalize()
        st.session_state.context["user_name"] = name
        return f"Nice to meet you, {name}! How can I assist you today?"
    if "user_name" in st.session_state.context:
        if "how are you" in user_input:
            return f"I'm great, {st.session_state.context['user_name']}! How can I help you?"
        if "joke" in user_input:
            return f"Here's a joke for you, {st.session_state.context['user_name']}: Why did the math book look sad? Because it had too many problems!"
    # Fallback
    return "I'm not sure how to respond to that. You can ask for help to see what I can do!"

# Set page title
st.set_page_config(page_title="Simple ChatBot")

# Inject custom CSS for improved appearance
css_path = os.path.join(os.path.dirname(__file__), "chatbot_style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("💬 Simple Python ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "user":
            st.markdown(f"<strong>user</strong>: {msg['content']}", unsafe_allow_html=True)
        else:
            st.markdown(f"<strong>assistant</strong>: {msg['content']}", unsafe_allow_html=True)

# Get user input
user_input = st.chat_input("Say something...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(f"<strong>user</strong>: {user_input}", unsafe_allow_html=True)

    # Get and display bot response
    response = get_bot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(f"<strong>assistant</strong>: {response}", unsafe_allow_html=True)
