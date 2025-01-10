import epd4in26
from PIL import Image, ImageDraw, ImageFont
import time

epd = epd4in26.EPD()

epd.init()
epd.Clear()
print('init and clear')

font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 24)
image = Image.new('1', (epd.width, epd.height), 255)
draw = ImageDraw.Draw(image)
draw.text((10, 10), 'Hello, world!', font=font, fill=0)
epd.display(epd.getbuffer(image))
print('displayed')
time.sleep(5)

epd.init()
epd.Clear()
print('cleared')

epd.sleep()
print('bedtime')
