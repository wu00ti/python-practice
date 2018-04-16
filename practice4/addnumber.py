from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('Arial.ttf',size=20)
    fillcolor = "#ff0000"
    width,height = img.size
    draw.text((width-20,0),'4',font=myfont,fill=fillcolor)
    img.save('result.jpg','jpeg')
    return 0

if __name__ == '__main__':
    image = Image.open('test.jpg')
    print(image.format,image.size,image.mode)
    add_num(image)
