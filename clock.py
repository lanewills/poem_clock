from openai import OpenAI
from datetime import datetime
import time
from messages import get_message
from secrets import API_KEY

# OpenAI model to use
ai_model = "gpt-4o-mini"
client = OpenAI(
    api_key=API_KEY
)

now = datetime.now()
system_message = get_message(now)

# Clock generates poems every hour, because I'm not rich enough for every minute
seconds_to_next_hour = (60 - now.minute) * 60 - now.second

completion = client.chat.completions.create(
    model=ai_model,
    store=True,
    messages=[
        {"role": "developer", "content": system_message},
        {"role": "user", "content": now.strftime("%I:%M %p")}
    ]
)
print(completion.choices[0].message.content)

# Makes sure clock starts at the top of the next hour
time.sleep(seconds_to_next_hour)

# Main clock loop
while True:
    now = datetime.now()
    system_message = get_message(now)
    completion = client.chat.completions.create(
        model=ai_model,
        store=True,
        messages=[
            {"role": "developer", "content": system_message},
            {"role": "user", "content": datetime.now().strftime("%I:%M %p")}
        ]
    )
    print(completion.choices[0].message.content)
    time.sleep(3600)
