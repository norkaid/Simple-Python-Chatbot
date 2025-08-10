// JavaScript Chatbot Logic (for browser use)
function getBotResponse(userInput, context = {}) {
    const input = userInput.toLowerCase();
    const greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"];
    const farewells = ["bye", "goodbye", "see you", "farewell"];
    const gratitude = ["thank you", "thanks", "thx", "appreciate"];
    const mood = ["how are you", "how do you feel", "how's it going"];
    const weather = ["weather", "rain", "sunny", "cloudy", "forecast"];
    const jokes = ["joke", "funny", "laugh"];
    const nameWords = ["name", "who are you", "your name"];
    const helpWords = ["help", "can you do", "what can you do", "options"];

    // Greetings
    if (greetings.some(word => input.includes(word))) {
        return "Hi! 👋 How can I help you today?";
    }
    // Farewells
    if (farewells.some(word => input.includes(word))) {
        return "Goodbye! If you need anything else, just say hi again.";
    }
    // Gratitude
    if (gratitude.some(word => input.includes(word))) {
        return "You're welcome! 😊";
    }
    // Mood
    if (mood.some(word => input.includes(word))) {
        return "I'm just a bot, but I'm always here to help! How are you?";
    }
    // Weather
    if (weather.some(word => input.includes(word))) {
        return "I can't check the weather, but I hope it's nice where you are!";
    }
    // Jokes
    if (jokes.some(word => input.includes(word))) {
        if (context.user_name) {
            return `Here's a joke for you, ${context.user_name}: Why did the math book look sad? Because it had too many problems!`;
        }
        return "Why did the computer show up at work late? It had a hard drive! 😄";
    }
    // Name
    if (nameWords.some(word => input.includes(word))) {
        return "I'm called ChatBot, your friendly virtual assistant.";
    }
    // Help
    if (helpWords.some(word => input.includes(word))) {
        return "I can chat, tell a joke, answer simple questions, and keep you company! Try saying 'hello', 'tell me a joke', or 'bye'.";
    }
    // Remember user's name
    if (input.includes("my name is")) {
        const name = userInput.split("my name is").pop().trim().split(" ")[0];
        context.user_name = name.charAt(0).toUpperCase() + name.slice(1);
        return `Nice to meet you, ${context.user_name}! How can I assist you today?`;
    }
    if (context.user_name) {
        if (input.includes("how are you")) {
            return `I'm great, ${context.user_name}! How can I help you?`;
        }
    }
    // Fallback
    return "I'm not sure how to respond to that. You can ask for help to see what I can do!";
}
