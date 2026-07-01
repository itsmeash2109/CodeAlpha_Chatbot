# CodeAlpha_Chatbot
# 🤖 Rule-Based Chatbot in Python

## 📌 Project Description
This is a simple rule-based chatbot built using Python. It uses `if-elif` conditions to match predefined user inputs and return appropriate responses. The chatbot continues the conversation until the user types **"bye"**.

---

## ✨ Features
- Greets the user.
- Responds to common questions.
- Handles empty input.
- Ends the conversation when the user says "bye".
- Easy to understand and modify.

---

## 🛠️ Technologies Used
- Python 3

---

## 📂 Project Structure

```
Rule-Based-Chatbot/
│
├── chatbot.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rule-based-chatbot.git
```

### 2. Navigate to the project folder

```bash
cd rule-based-chatbot
```

### 3. Run the chatbot

```bash
python chatbot.py
```

---

## 💬 Sample Conversation

```
Chatbot: Hello! Type 'bye' to exit the chat.

You: Hi
Chatbot: Hi!

You: How are you
Chatbot: I'm fine, thanks! How about you?

You: What is your name
Chatbot: I'm a simple rule-based chatbot!

You: Thanks
Chatbot: You're welcome!

You: Bye
Chatbot: Goodbye! Have a great day!
```

---

## 📖 How It Works

1. The chatbot asks the user for input.
2. The input is converted to lowercase and extra spaces are removed.
3. It checks the input using `if-elif` statements.
4. If a match is found, the corresponding response is returned.
5. If no match exists, the chatbot displays a default message.
6. The program ends when the user enters **"bye"**, **"goodbye"**, or **"see you"**.

---

## 🚀 Future Improvements

- Add more conversation patterns.
- Use dictionaries instead of multiple `if-elif` statements.
- Integrate Natural Language Processing (NLP).
- Create a graphical user interface (GUI).
- Store conversation history.

---

## 👨‍💻 Author

**Alok Meshram**

Computer Engineering Student  
Government College of Engineering, Jalgaon

---

## 📜 License

This project is created for learning and educational purposes.
