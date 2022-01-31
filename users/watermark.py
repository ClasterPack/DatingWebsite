from PIL import Image, ImageFont, ImageDraw


def add_watermark(image_file):
    avatar = Image.open(image_file)
    width, height = avatar.size

    draw = ImageDraw.Draw(avatar)
    text = 'Daiting Site'
    font = ImageFont.truetype('arial.ttf', 45)

    textwidth, textheight = draw.textsize(text, font)

    x = width - textwidth - 10
    y = height - textheight - 15

    draw.text((x, y), text, font=font)

    avatar.save(image_file)
    return image_file

