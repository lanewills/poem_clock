from waveshare import epd4in26
from PIL import Image, ImageDraw, ImageFont
import time

epd = epd4in26.EPD()

epd.init()
epd.Clear()
print('init and clear')

font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 50)
image = Image.new('1', (epd.width, epd.height), 255)
draw = ImageDraw.Draw(image)
draw.text((10, 10), 'The quick brown fox jumped over the lazy dog to get to the pub to get some cold brews then he went to the at the all for the', font=font, fill=0)
epd.display(epd.getbuffer(image))
print('displayed')
time.sleep(5)

epd.init()
epd.Clear()
print('cleared')

epd.sleep()
print('bedtime')
