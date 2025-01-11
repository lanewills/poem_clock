from PIL import Image, ImageDraw, ImageFont
import textwrap
import logging


def draw_text(text, epd):
    logging.info('drawing text')
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 65)
    image = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(image)

    wrapped_text = textwrap.fill(text, width=20)
    draw.multiline_text((10, 10), wrapped_text, font=font, fill=0)

    epd.Clear()
    logging.info('cleared')
    epd.display(epd.getbuffer(image))
    logging.info('displayed')
    epd.sleep()
    logging.info('sleeping')
