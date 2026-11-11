responses = {
    # Greetings
    "hello": "Hi! How can I help you?",
    "hi": "Hey there! How are you?",
    "hey": "Hello! Nice to meet you.",
    "good morning": "Good morning! Have a wonderful day.",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! Hope you're doing well.",

    # General conversation
    "how are you": "I'm fine, thanks! How about you?",
    "i am fine": "That's great to hear!",
    "what are you doing": "I'm chatting with you. What about you?",
    "who are you": "I'm a simple Python rule-based chatbot.",
    "what is your name": "You can call me PyBot!",
    "how old are you": "I'm just a program, so I don't have an age.",

    # Help and information
    "help": "Sure! What do you need help with?",
    "what can you do": "I can answer simple predefined questions and chat with you.",
    "what is python": "Python is a popular, high-level programming language.",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",

    # Social responses
    "thank you": "You're welcome!",
    "thanks": "My pleasure!",
    "sorry": "No worries! It's all good.",
    "nice to meet you": "Nice to meet you too!",

    # Ending conversation
    "bye": "Goodbye! Have a nice day.",
    "goodbye": "See you again soon!",
    "see you": "Take care! See you later."
}

while(True):
    user = input("You :").strip().lower()
    if not user:
        continue
    if user in responses:
        print("PyBot :",responses[user])
        if user in {'bye','goodbye','see you'}:
            exit()
    else:
        print("PyBot :Didn't understand !!\n")