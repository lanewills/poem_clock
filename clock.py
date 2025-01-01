from openai import OpenAI
from datetime import datetime
import time
from secrets import API_KEY

# OpenAI model to use
ai_model = "gpt-4o-mini"
# System message to the AI
system_message = "You are a creative poem-writing AI. When you are given a time in the format 'HH:MM AM/PM', you will write a very short poem about that time, including the time itself, in two lines maximum."

client = OpenAI(
    api_key=API_KEY
)

now = datetime.now()
seconds_to_next_hour = (60 - now.minute) * 60 - now.second

completion = client.chat.completions.create(
    model=ai_model,
    messages=[
        {"role": "developer", "content": system_message},
        {"role": "user", "content": now.strftime("%I:%M %p")}
    ]
)

print(completion.choices[0].message.content)

# Makes sure clock starts at the top of the next hour
time.sleep(seconds_to_next_hour)

while True:
    completion = client.chat.completions.create(
        model=ai_model,
        messages=[
            {"role": "developer", "content": system_message},
            {"role": "user", "content": datetime.now().strftime("%I:%M %p")}
        ]
    )
    print(completion.choices[0].message.content)
    time.sleep(3600)
