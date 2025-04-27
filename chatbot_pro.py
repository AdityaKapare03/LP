def simple_chatbot():
    # Responses organized by intent
    responses = {
        "greetings": ["Hi there!", "Hello!", "Hey! How can I help you today?"],
        "how_are_you": ["I'm just a bot, but I'm functioning well!", "All systems go!"],
        "name": ["I'm SimpleBot, your friendly chatbot.", "Call me SimpleBot!"],
        "goodbye": ["Goodbye! Have a great day!", "See you later!", "Bye! Come back soon!"],
        "help": [
            "I can help with: product info, contact details, or business hours.",
            "Ask me about: products, contact, or hours."
        ],
        "product": [
            "We offer AI solutions and tech products.",
            "Our flagship product is an AI assistant."
        ],
        "contact": [
            "Email us at support@example.com",
            "Call us at 123-456-7890."
        ],
        "hours": ["Open Mon-Fri, 9AM-5PM.", "Our hours are 9AM to 5PM weekdays."],
        "default": [
            "I’m not sure I understand. Can you rephrase?",
            "I don’t have that info. Try asking about products or hours."
        ]
    }

    # Keyword mapping to intents (more flexible matching)
    keyword_to_intent = {
        "hi": "greetings",
        "hello": "greetings",
        "hey": "greetings",
        "how are you": "how_are_you",
        "name": "name",
        "bye": "goodbye",
        "exit": "goodbye",
        "help": "help",
        "product": "product",
        "contact": "contact",
        "email": "contact",
        "call": "contact",
        "hours": "hours",
        "time": "hours",
        "open": "hours"
    }

    print("SimpleBot: Hi! I’m here to help. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ("bye", "exit", "quit"):
            print("SimpleBot:", random.choice(responses["goodbye"]))
            break

        # Match user input to intent
        intent = None
        for keyword, mapped_intent in keyword_to_intent.items():
            if keyword in user_input:
                intent = mapped_intent
                break

        # Default response if no intent matched
        if not intent:
            intent = "default"

        print("SimpleBot:", random.choice(responses[intent]))

if __name__ == "__main__":
    import random
    simple_chatbot()