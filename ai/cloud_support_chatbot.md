
# Cloud Support Chatbot (Python + NLTK + Tkinter)

This chatbot is designed for elementary customer interaction and has been **specialized for cloud support queries**. It uses a rule-based approach with the `nltk.chat.util.Chat` module.

## 💻 Requirements

Install these on your system (Ubuntu or Arch Linux):
```bash
pip install nltk pillow
```

## 🚀 Run the Chatbot (Terminal Friendly Backup Version)

Save this code as `cloud_chatbot_terminal.py` and run:
```bash
python3 cloud_chatbot_terminal.py
```

```python
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Cloud support specialized pairs
pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?"]],
    [r"what is your name?", ["I am a cloud support assistant created using Python."]],
    [r"how are you ?", ["I'm doing well, thank you!"]],
    [r"sorry (.*)", ["It's okay, no problem."]],
    [r"quit", ["Goodbye! Have a great day!"]],
    [r"(.*) (help|support) (.*)", ["Sure, I can help. What do you need assistance with?"]],
    [r"hi|hey|hello", ["Hello!", "Hey there!", "Hi! How can I assist you?"]],
    [r"(.*) billing issue (.*)", ["Billing issues are common. Could you provide your account ID?"]],
    [r"i need help with (aws|azure|gcp)", ["Sure, I can help with %1. Please specify your issue."]],
    [r"(.*) can't access (.*)", ["Access issues are usually permission-related. Can you check IAM settings?"]],
    [r"(.*) create vm (.*)", ["To create a VM, go to your cloud provider console and navigate to 'Compute'."]],
    [r"(.*) deploy (.*)", ["To deploy %1, refer to the documentation or I can assist further."]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
```

## 🖥️ GUI Version (Optional)

The GUI version uses Tkinter and Pillow for an enhanced interface. Save this code as `cloud_chatbot_gui.py`:
```python
import nltk
from nltk.chat.util import Chat, reflections
from tkinter import Tk, Label, Entry, Button, Text, END
from PIL import Image, ImageTk

nltk.download('punkt')

pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?"]],
    [r"what is your name?", ["I am a cloud support assistant created using Python."]],
    [r"how are you ?", ["I'm doing well, thank you!"]],
    [r"sorry (.*)", ["It's okay, no problem."]],
    [r"quit", ["Goodbye! Have a great day!"]],
    [r"(.*) (help|support) (.*)", ["Sure, I can help. What do you need assistance with?"]],
    [r"hi|hey|hello", ["Hello!", "Hey there!", "Hi! How can I assist you?"]],
    [r"(.*) billing issue (.*)", ["Billing issues are common. Could you provide your account ID?"]],
    [r"i need help with (aws|azure|gcp)", ["Sure, I can help with %1. Please specify your issue."]],
    [r"(.*) can't access (.*)", ["Access issues are usually permission-related. Can you check IAM settings?"]],
    [r"(.*) create vm (.*)", ["To create a VM, go to your cloud provider console and navigate to 'Compute'."]],
    [r"(.*) deploy (.*)", ["To deploy %1, refer to the documentation or I can assist further."]]
]

chatbot = Chat(pairs, reflections)

def start_chat():
    def send_message():
        user_input = entry.get()
        if user_input.lower() == "quit":
            chat_window.insert(END, "You: " + user_input + "\n")
            chat_window.insert(END, "Chatbot: Goodbye!\n")
            root.quit()
        else:
            chat_window.insert(END, "You: " + user_input + "\n")
            response = chatbot.respond(user_input)
            chat_window.insert(END, "Chatbot: " + response + "\n")
            entry.delete(0, END)

    root = Tk()
    root.title("Cloud Support Chatbot")
    chat_window = Text(root, wrap="word")
    chat_window.pack(expand=True, fill="both")
    entry = Entry(root, width=50)
    entry.pack(side="left", expand=True, fill="x")
    send_button = Button(root, text="Send", command=send_message)
    send_button.pack(side="right")
    root.mainloop()

if __name__ == "__main__":
    start_chat()
```

## 🔐 Notes
- Internet required on first run to download `punkt`
- GUI assumes you have a default image file; you may remove image parts if not needed

---
