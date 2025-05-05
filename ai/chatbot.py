import nltk
from nltk.chat.util import Chat, reflections
from tkinter import Tk, Label, Entry, Button, Text, END
from PIL import Image, ImageTk

# Download NLTK data (tokenizer)
nltk.download('punkt')

# Define patterns for chatbot responses
pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?",]],
    [r"what is your name?", ["I am a chatbot created using Python and NLTK.",]],
    [r"how are you ?", ["I'm doing well, thank you!", "I'm great, thanks for asking!",]],
    [r"sorry (.*)", ["It's okay, no problem.", "No worries!",]],
    [r"quit", ["Bye! Take care. See you soon.", "Goodbye! Have a great day!"]],
    [r"(.*) (help|support) (.*)", ["Sure, I can help you. What do you need assistance with?",]],
    [r"hi|hey|hello", ["Hello!", "Hey there!", "Hi! How can I assist you?",]],
    [r"(.*) (weather|temperature) (.*)", ["I'm sorry, I don't have access to real-time weather data.",]],
    [r"(.*) (age|old) (.*)", ["I'm just a program, so I don't have an age!",]],
    [r"(.*) (thank you|thanks) (.*)", ["You're welcome!", "No problem!", "Glad to help!",]],
    [r"i need help with (aws|azure|gcp)", ["Sure, I can help with %1. Please specify your issue."]],
    [r"(.*) billing issue (.*)", ["Billing issues are common. Could you provide your account ID?"]],
    [r"how to deploy (.*)", ["To deploy %1, you can follow the official documentation or I can walk you through it."]],
    [r"(.*) can't access (.*)", ["Access issues are usually permission related. Can you check your IAM settings?"]],
    [r"(.*) create vm (.*)", ["To create a VM, go to your cloud provider's console, select 'Compute', and follow the steps."]],
]

# Create a chatbot instance with predefined patterns and reflections
chatbot = Chat(pairs, reflections)

# Function to start the chat interface
def start_chat():
    def send_message():
        user_input = entry.get()  # Get the user's input
        if user_input.lower() == "quit":
            chat_window.insert(END, "You: " + user_input + "\n")
            chat_window.insert(END, "Chatbot: Goodbye!\n")
            root.quit()  # Close the application
        else:
            chat_window.insert(END, "You: " + user_input + "\n")
            response = chatbot.respond(user_input)  # Get chatbot's response
            chat_window.insert(END, "Chatbot: " + response + "\n")
            entry.delete(0, END)  # Clear the entry box

    # Set up the GUI window
    root = Tk()
    root.title("Customer Support Chatbot")

    # Load an image to display in the chat window (optional)
    try:
        image = Image.open("chatbot_image.png")  # Make sure this image exists in your directory
        photo = ImageTk.PhotoImage(image)
        image_label = Label(root, image=photo)
        image_label.pack()
    except Exception as e:
        print("Error loading image:", e)

    # Create a Text widget to display the chat history
    chat_window = Text(root, wrap="word", state='normal')
    chat_window.pack(expand=True, fill="both")

    # Create an Entry widget for user input
    entry = Entry(root, width=50)
    entry.pack(side="left", expand=True, fill="x")

    # Create a Button widget to send the message
    send_button = Button(root, text="Send", command=send_message)
    send_button.pack(side="right")

    # Start the Tkinter event loop
    root.mainloop()

# Run the chatbot when the script is executed
if __name__ == "__main__":
    start_chat()
