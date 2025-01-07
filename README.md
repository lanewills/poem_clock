# Poem Clock
Poem Clock is a clock that tells the time with AI generated poems, displayed on an e-ink display.
Driven by a Raspberry pi and Python script that fetches poems through the OpenAI API.
Gets festive during holidays and special occasions.

## Hardware
>These are the parts that I used, though I'm sure you can use other RPi models and e-ink display sizes with a little modification.
- Raspberry Pi Zero 2 WH
- Waveshare 4.26inch e-Paper Display HAT
- A microSD and power supply for the RPi

## Installation and Usage
- Clone the repository

    ```git clone https://github.com/lanewills/poem_clock.git```

- Install the required libraries
    
    ```pip install -r requirements.txt```

- Create a .env file in the root directory and add your OpenAI API key

    ```OPENAI_API_KEY="<YOUR_API_KEY>"```

- Run the script
    
    ```python3 clock.py```

- Enjoy the poems

## Customization
### Intervals
- You can change the interval at which the clock updates by changing the `interval` variable in `clock.py`.
- An interval of 5 will make poems generate every 5 minutes. The clock generates a poem for the current time at startup,
but will latch to the next interval after that. Works best with intervals that are multiples of 5.
- The default is 5, so the clock will update at 12:00, 12:05, 12:10, etc.

### System Message
- The AI's system message is located in `messages.py` in two parts: `message_opening` and `message_closing`.
- I separated the message into two parts to allow for holiday themed poems. More on that below.

### Holidays and Special Occasions
- The clock will display a special message on holidays and special occasions. This currently includes:
    - New Year's Day
    - Valentine's Day
    - St. Patrick's Day
    - Easter
    - Cinco de Mayo
    - Independence Day
    - Halloween
    - Thanksgiving
    - Christmas
- These can be disabled by setting `holiday_messages` to `False` in `messages.py`.
