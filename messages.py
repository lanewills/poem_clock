from dateutil.easter import easter

# This file contains the functions used to determine the system message that is sent to the OpenAI model

# Change to False to disable holiday-themed messages (womp)
holiday_messages = True

# Customize the system message here
message_opening = ("You are a creative poem-writing AI. When you are given a time in the format 'HH:MM AM/PM', "
                   "you will write a very short ")
message_closing = "poem about that time, including the time itself, in two lines maximum."


# Check if the current date is Easter sunday using dateutil
def is_easter(now):
    easter_date = easter(now.year)
    if now == easter_date:
        return True
    return False


# Check if the current date is Thanksgiving
def is_thanksgiving(now):
    # Thanksgiving is the fourth Thursday in November
    if now.month == 11:
        # Find the day of the week of the first day of the month
        first_day_of_month = now.replace(day=1)
        first_day_of_month_weekday = first_day_of_month.weekday()
        # Find the day of the week of the fourth Thursday of the month
        fourth_thursday = 4 - first_day_of_month_weekday + 4 * 7
        fourth_thursday_date = now.replace(day=fourth_thursday)
        if now == fourth_thursday_date:
            return True
    return False


# Checks the datetime object against a list of holidays and returns the appropriate system message
def get_message(now):
    if holiday_messages:
        if now.month == 1 and now.day == 1:
            return message_opening + "New Year's Day themed " + message_closing
        elif now.month == 2 and now.day == 14:
            return message_opening + "Valentine's Day themed " + message_closing
        elif now.month == 3 and now.day == 17:
            return message_opening + "St. Patrick's Day themed " + message_closing
        elif is_easter(now):
            return message_opening + "Easter themed " + message_closing
        elif now.month == 5 and now.day == 5:
            return message_opening + "Cinco de Mayo themed " + message_closing
        elif now.month == 7 and now.day == 4:
            return message_opening + "Independence Day themed " + message_closing
        elif now.month == 10 and now.day == 31:
            return message_opening + "Halloween themed " + message_closing
        elif is_thanksgiving(now):
            return message_opening + "Thanksgiving themed " + message_closing
        elif now.month == 12 and now.day == 25:
            return message_opening + "Christmas themed " + message_closing

    return message_opening + message_closing
