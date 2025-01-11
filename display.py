from waveshare import epd4in26
from PIL import Image, ImageDraw, ImageFont
import time
import textwrap


def justify_text(text, width, font, draw):
    lines = textwrap.wrap(text, width=width)
    justified_lines = []
    for line in lines:
        words = line.split()
        if len(words) == 1:
            justified_lines.append(words[0])
            continue
        total_length = sum(draw.textsize(word, font=font)[0] for word in words)
        space_length = (width - total_length) // (len(words) - 1)
        extra_spaces = (width - total_length) % (len(words) - 1)
        justified_line = ""
        for i, word in enumerate(words[:-1]):
            justified_line += word + " " * (space_length + (1 if i < extra_spaces else 0))
        justified_line += words[-1]
        justified_lines.append(justified_line)
    return "\n".join(justified_lines)

epd = epd4in26.EPD()

epd.init()
epd.Clear()
print('init and clear')

font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 50)
image = Image.new('1', (epd.width, epd.height), 255)
draw = ImageDraw.Draw(image)

text = 'The quick brown fox jumped over the lazy dog to get to the pub to get some cold brews then he went to the at the all for the'
wrapped_text = justify_text(text, width=epd.width - 20, font=font, draw=draw)  # Adjust width as needed

draw.multiline_text((10, 10), wrapped_text, font=font, fill=0)
epd.display(epd.getbuffer(image))
print('displayed')
time.sleep(5)

epd.init()
epd.Clear()
print('cleared')

epd.sleep()
print('bedtime')