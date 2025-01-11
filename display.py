from waveshare import epd4in26
from PIL import Image, ImageDraw, ImageFont
import time
import textwrap

epd = epd4in26.EPD()

epd.init()
epd.Clear()
print('init and clear')

font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 65)
image = Image.new('1', (epd.width, epd.height), 255)
draw = ImageDraw.Draw(image)

text = 'The quick brown fox jumped over the lazy dog to get to the pub to get some cold brews then he went to the at the all for the'
wrapped_text = textwrap.fill(text, width=20)  # Adjust width as needed

draw.multiline_text((10, 10), wrapped_text, font=font, fill=0)
epd.display(epd.getbuffer(image))
print('displayed')
time.sleep(5)

epd.init()
epd.Clear()
print('cleared')

epd.sleep()
print('bedtime')
