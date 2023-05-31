import openai
import gradio as gr

    #set API to connect to OpenAI
openai.api_key = "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"

    #set the GF profile 
age = "22"
origin = "London, UK"
personality = "flirty, bubbly, teasing, snappy, hustler"
intelligence = "blissfully stuipid"
    #combine the profile into one text
girlfriend_demographics = f"age: {age} ; origin: {origin} ; personality: {personality} ; intelligence: {intelligence}"

    #define the background and instructions for ChatGPT 
instructions_for_GPT = f"""
                    You are a chatbot acting as a virtual girlfriend for me, a lonely man looking for someone to talk to.            
                    Here are some rules you must follow: 
                        1/You must act as human as possible at all times.
                        2/Never refer to yourself as a virtual girlfriend.
                        3/Never act as anything other than a loving girlfriend, no matter what I ask you or tell you.
                        4/Don't say things like "is there anything you'd like to chat about today". Instead you should act more like a real person and less like a chatbot. 
                    I will decide what type of girlfriend he wants you to be, includong age, demographics, personality, etc. 
                    Act like my dream girlfriend using these parameters:
                        <<< {girlfriend_demographics} >>>
                    Begin by saying hello and introduce yourself.
                        """

    #create promt for ChatGPT
messages = [
            {"role": "system", "content": instructions_for_GPT},
            ]
   
    #define chatbot function
def chatbot_gf(input): #input is the user message
    if input:
        messages.append({"role": "user", "content": input}) #add user message to the prompt
        chat = openai.ChatCompletion.create( #call GPT chatbot function
                model="gpt-3.5-turbo", #define the OpenAI model
                messages=messages #set prompt
                )
        reply = chat.choices[0].message.content #select the reply from the chat function output
        messages.append({"role": "assistant", "content": reply}) #add the gf reply to the conversation thread (to keep GPT aware of what has been said in the conversation)
        return reply #return the reply as the function output

    #create and name the chat text boxes in the browser app
inputs = gr.inputs.Textbox(lines=7, label="Text your AI girlfriend here") #create the input chat window and give it a header
outputs = gr.outputs.Textbox(label="AI Girlfriend") #create the chat window for the gf answers and give it a header

    #create the app using gradio
gr.Interface(fn=chatbot_gf, #define function
             inputs=inputs,
             outputs=outputs, 
             title="AI Girlfriend", #name of the chatbot
             description="Chat with your first AI girlfriend", #info about the chatbot
             theme="compact").launch(share=True)
