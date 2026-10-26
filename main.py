import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("HF_TOKEN")
if not api_key:
    raise RuntimeError("API Key not set")
total_token_usage=0
messages=[
    {"role":"system",
     "content":"You are a concise and precise assistant.Answer directly and briefly."
               "Use only the information relevant to the user's question."
               "Avoid unnecessary explanations, repetition, introductions, and conclusions."
               "Use bullet points when appropriate.Unless explicitly requested, limit your answer to 3-5 sentences."
               "If you don't know the answer, say so briefly."
}
]
while True:
    user_input=input("you:\n").strip()
    if user_input.lower() in ("exit","end","خروج","quit"):
        print("bye")
        break
    messages.append({
        "role":"user",
        "content":user_input
    })

    client = OpenAI(base_url='https://api.gapgpt.app/v1', api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        assistant_text=response.choices[0].message.content
        token_usage=response.usage.total_tokens
        total_token_usage +=int(token_usage)
    except Exception as e:
        print("404 no response from llm ")
        print("Error:",e)
        messages.pop()
        continue
    print("Assistant:\n",assistant_text)
    print("==========================================")
    print("current token use",token_usage)
    print("total token usage:",total_token_usage)
    print("===========================================")
    messages.append({
        "role":"assistant",
        "content":assistant_text
    })
    messages = messages[-6:]


