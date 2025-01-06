import os
import time
from openai import OpenAI
from datetime import datetime, timedelta
from messages import get_message
from internetcheck import internet_check
from dotenv import load_dotenv

# Time between poem generations in minutes. Works best with intervals of 1, 5, 15, 30, or 60.
interval = 5
# OpenAI model to use
ai_model = "gpt-4o-mini"

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# Returns the number of seconds until the next interval
def get_seconds_to_next_interval(now_interval, time_interval):
    next_interval_minute = (now_interval.minute // time_interval + 1) * time_interval
    next_interval_time = now_interval.replace(minute=0, second=0, microsecond=0) + timedelta(minutes=next_interval_minute)
    return (next_interval_time - now_interval).total_seconds()


now = datetime.now()
system_message = get_message(now)

internet_check()
completion = client.chat.completions.create(
    model=ai_model,
    store=True,
    messages=[
        {"role": "developer", "content": system_message},
        {"role": "user", "content": now.strftime("%I:%M %p")}
    ]
)
print(completion.choices[0].message.content)

# Sleep until the next interval
seconds_to_next_interval = get_seconds_to_next_interval(now, interval)
time.sleep(seconds_to_next_interval)

# Main clock loop
while True:
    now = datetime.now()
    system_message = get_message(now)
    internet_check()
    completion = client.chat.completions.create(
        model=ai_model,
        store=True,
        messages=[
            {"role": "developer", "content": system_message},
            {"role": "user", "content": datetime.now().strftime("%I:%M %p")}
        ]
    )
    print(completion.choices[0].message.content)

    now = datetime.now()
    time.sleep(get_seconds_to_next_interval(now, interval))
