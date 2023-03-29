import openai
import config

openai.api_key = config.api_key

messages=[{
        "role": "system", #it defines a context
        "content": "You are useful asistant."
    }]

while True:
    content = input("Question... ")

    if content == "exit":
        break

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    messages.append({"assistant": "user", "content": response})

    print(response.choices[0].message.content)
