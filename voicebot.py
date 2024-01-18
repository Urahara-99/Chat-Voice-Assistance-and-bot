import gradio as gr
import openai

# Replace with your OpenAI API key
openai.api_key = 'API'

# Initial system message
messages = [{"role": "system", "content": "You are a multi speciality hospital guiding patients"
                                          "clearing their doubts and fixing appoinments"}]

def chatbot(audio_input):
    # Convert audio to text
    text_input = audio_to_text(audio_input)

    # Append the user's message to the conversation
    messages.append({"role": "user", "content": text_input})

    # Generate a response from the chatbot
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    # Extract and return the assistant's reply
    assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply

def audio_to_text(audio):
    # Convert audio to text (you'll need a proper speech-to-text library or service for this)
    # For demonstration, we'll assume a placeholder conversion function.
    # Replace this with a real speech-to-text solution like Google Cloud Speech-to-Text.
    return "This is a placeholder text from audio."

# Create a Gradio interface for the chatbot
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Audio(),
    outputs=gr.Textbox(),
    live=True,
    capture_session=True,  # Remember conversation history
    title="Intelligent chatbot for clearing queries in maintenance processes within substation",
    description="Maintenance virtual assistant",)

iface.launch()
