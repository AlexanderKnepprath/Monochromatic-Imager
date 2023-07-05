from PIL import Image

def image_fix():

    img = Image.open("amplisamplerlogo.png")

    width, height = img.size

    img_rgb = img.convert('RGB')

    for w in range(width):
        for h in range(height):
            r, g, b = img_rgb.getpixel((w, h))
            if r < 130:
                r, g, b = 101, 49, 196
            else:
                r, g, b = 33, 33, 33
            img_rgb.putpixel((w, h), (r, g, b))

    img_rgb.save("amplisampler_ppt.png")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_fix()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
