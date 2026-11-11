# 🤖 PyBot – Rule-Based Chatbot using Python

PyBot is a simple console-based chatbot developed using Python. It responds to user messages using predefined conversations stored in a Python dictionary.

## 📌 Project Overview

The chatbot follows a rule-based approach.

It compares the user's input with predefined message keys and returns the corresponding response.

Unlike AI-powered chatbots, PyBot does not use machine learning or natural language processing. Its responses are based on predefined rules.

## ✨ Features

- Interactive command-line conversation.
- Predefined greetings and responses.
- General conversation support.
- Basic help and information responses.
- Predefined jokes and social responses.
- Case-insensitive input handling.
- Removes unnecessary spaces from user input.
- Handles empty input.
- Provides a fallback response for unknown messages.
- Supports predefined exit commands.

## 💬 Example Conversation

```text
PyBot: Hello! I am PyBot. How can I help you?

You: hello
PyBot: Hi! How can I help you?

You: how are you
PyBot: I'm fine, thanks! How about you?

You: what is python
PyBot: Python is a popular, high-level programming language.

You: tell me a joke
PyBot: Why do programmers prefer dark mode?
Because light attracts bugs!

You: bye
PyBot: Goodbye! Have a nice day.
```

## 🛠️ Technologies Used

- Python 3
- Dictionaries
- `input()` and `print()`
- `while` loops
- Conditional statements
- String methods (`strip()` and `lower()`)


## 🧠 How It Works

1. Predefined conversations are stored in a dictionary.
2. The chatbot accepts input from the user.
3. The input is normalized using `strip()` and `lower()`.
4. The program checks whether the message exists in the dictionary.
5. If a matching key is found, the corresponding response is displayed.
6. Otherwise, the chatbot displays a fallback message.
7. The conversation continues until an exit command is entered.


## ⚠️ Limitations

- Responses are predefined.
- Exact phrase matching is used.
- The chatbot does not understand context.
- It does not use AI, ML or NLP.
