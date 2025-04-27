import random

responses = {
    "hi": ["Hello!", "Hi there!", "Greetings!"],
    "order": ["Your order is being processed", "Order status: shipped"],
    "return": ["Please contact returns department", "Returns policy: 30 days"],
    "default": ["I didn't understand that", "Could you rephrase that?"]
}

def chatbot():
    print("Chatbot: Hi! How can I help you today? (type 'bye' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye!")
            break
        reply = None
        for key in responses:
            if key in user_input:
                reply = random.choice(responses[key])
                break
        if not reply:
            reply = random.choice(responses["default"])
        print("Chatbot:", reply)

# Example usage
chatbot()