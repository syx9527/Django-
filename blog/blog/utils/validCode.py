# -*- coding: utf-8 -*-
# @Time : 2021/8/25 9:53
# @Author : 41999
# @Email : 419997284@qq.com
# @File : validCode.py
# @Project : whereabouts
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import random


def get_random_color():
    """生成三组随机RGB数字，以便构成颜色"""
    a = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return a


def get_valide_code_img(request):
    """
    功能设计：分别为绘图，随机噪点，随机噪线
    Image.new:生成图片对象，分别是显示模式，大小[长宽]，RGB数字
    ImageDraw.Draw: 导入并且绘制图像
    ImageFont:指定文字文件地址，TTF格式字体
    """
    img = Image.new("RGB", (240, 30), color=get_random_color())
    draw = ImageDraw.Draw(img)
    FiraCode = ImageFont.truetype("static/font/FiraCode-Regular.ttf", size=24)
    valid_code_str = ""
    for i in range(5):
        random_num = random.randint(0, 9)  # 随机数字
        random_low_alpha = chr(random.randint(95, 122))  # 随机小写字符，ASCⅡ大小写字母范围
        random_upper_alpha = chr(random.randint(65, 90)) # 随机大写字符
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((i * 50 + 20, 5), str(random_char), get_random_color(), font=FiraCode)  # 转换第二个参数的类型
        # 保存验证码字符串
        valid_code_str += str(random_char)

    width = 250
    height = 40
    for i in range(10):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, x2, y1, y2), fill=get_random_color())

    for i in range(200):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    # 打印保存的验证码
    # print("valid_code_str", valid_code_str)

    request.session["valid_code_str"] = valid_code_str

    """
    1. 生成随机字符串
    2. 设置一个cookie{sessionid:随机字符串}
    3. django——session存储session_key---随机字符串,session_data---验证码
    """
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()

    return data
