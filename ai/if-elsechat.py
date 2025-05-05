def get_response(user_input):
    user_input = user_input.lower()

    if "my name is" in user_input:
        return f"Hello {user_input.split('is ')[1]}, how can I help you today?"
    
    elif "what is your name" in user_input:
        return "I am a simple chatbot created using Python."

    elif "how are you" in user_input:
        return "I'm doing well, thank you!"
    
    elif "sorry" in user_input:
        return "It's okay, no problem."
    
    elif "quit" in user_input:
        return "Goodbye! Have a great day!"
    
    elif "help" in user_input or "support" in user_input:
        return "Sure, I can help you. What do you need assistance with?"
    
    elif "hi" in user_input or "hey" in user_input or "hello" in user_input:
        return "Hello! How can I assist you?"
    
    elif "weather" in user_input or "temperature" in user_input:
        return "I'm sorry, I don't have access to real-time weather data."
    
    elif "age" in user_input or "old" in user_input:
        return "I'm just a program, so I don't have an age!"
    
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    
    elif "aws" in user_input or "azure" in user_input or "gcp" in user_input:
        return f"Sure, I can help with {user_input.split()[-1]}. Please specify your issue."
    
    elif "billing issue" in user_input:
        return "Billing issues are common. Could you provide your account ID?"
    
    elif "how to deploy" in user_input:
        return "To deploy, you can follow the official documentation or I can walk you through it."
    
    elif "create vm" in user_input:
        return "To create a VM, go to your cloud provider's console, select 'Compute', and follow the steps."
    
    # Additional simple cases
    elif "cloud computing" in user_input:
        return "Cloud computing is the delivery of computing services over the internet."
    
    elif "tell me a joke" in user_input:
        return "Why don’t skeletons fight each other? They don’t have the guts!"
    
    elif "who are you" in user_input:
        return "I am a chatbot here to assist you with anything you need!"

    else:
        return "Sorry, I didn't quite understand that. Can you ask something else?"

# Main program loop
def start_chat():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")  # Get the user's input
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the chat
        else:
            response = get_response(user_input)  # Get chatbot's response
            print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
