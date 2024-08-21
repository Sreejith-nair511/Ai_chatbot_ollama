#this is an langchain  based chatbot
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template= """" 
Answer the question below.

Here is the converstaion history:{context}

Question:{question}

Answer:
"""

model =OllamaLLM(model="neural-chat")
prompt = ChatPromptTemplate.from_template(template)
chain=prompt | model

def handle_conversation():
    context=""
    print("welcome to the AI chatbot ! Type 'exit' to quit.")
    while True:
        user_input=input("You: ")
        if user_input.lower() == "exit":
            break 
        result=chain.invoke({"context":"","question":user_input})
        print("Bot:",result)
        context+= f"\nUser:{user_input}\nAI:{result}"


if __name__ == "__main__":
    handle_conversation()