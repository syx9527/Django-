def cat_img(path):
    from PIL import Image

    image = Image.open(path)
    image = image.convert('RGB')
    w, h = image.size

    length = int(abs(w - h) // 2)  # 一侧需要填充的长度

    if w > h:
        cropped = image.crop((length, 0, h + length, h))  # (left, upper, right, lower)
    else:
        cropped = image.crop((0, length, w, w + length))  # (left, upper, right, lower)

    cropped.save(path)
