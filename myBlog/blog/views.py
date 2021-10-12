from django.shortcuts import render, HttpResponse
import random


# Create your views here.


def login(request):
    return render(request, 'blog/login.html')


def get_validCode_img(request):
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),)

    # 方式1
    # with open("lufei.jpg", "rb") as f:
    #     data = f.read()

    # 方式2：
    # from PIL import Image
    # img = Image.new("RGB", (250, 40), color=get_random_color())
    #
    # with open("validcode.png", 'wb') as f:
    #     img.save(f, "png")
    # with open("validcode.png", "rb") as f:
    #     data = f.read()

    # 方式三

    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO

    width = 250
    height = 40
    font_size = 30

    # img_color = get_random_color()
    img_color = (153, 101, 143)
    font_color = get_random_color()
    print("\nimg:", img_color, '\n', "font", font_color)
    img = Image.new("RGB", (width, height), color=img_color)

    draw = ImageDraw.Draw(img)
    # kumo_font = ImageFont.truetype("static/blog/bs/fonts/云峰林桥体.ttf", size=30)
    kumo_font = ImageFont.truetype("static/blog/bs/fonts/FZSJ-TUEDT.TTF", size=font_size)

    # 生成随机5位验证码
    char = ''
    for i in range(5):
        random_num = random.randint(0, 9)
        random_low_alpha = chr(random.randint(97, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        char += str(random_char)  # 验证码字符串
        draw.text((60 + i * 20, 5), text=str(random_char),font=kumo_font)
        # draw.text((100,20), text=str(random_char), color=font_color, font=kumo_font)

    # 给验证码生成噪点噪线
    for i in range(80):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    for i in range(4):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=get_random_color())

    print("char:", char)
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()

    return HttpResponse(data)
