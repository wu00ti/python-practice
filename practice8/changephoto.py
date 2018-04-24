from PIL import Image
import os,sys

def resize_image(image):
    im = Image.open(image)
    weight,height = im.size
    if weight > 1136 or height >640:
        dw = weight / 1136
        dh = height / 640
        ds = max(dw,dh)
        new_weight = int(weight / ds)
        new_height = int(height / ds)
        im = im.resize((new_weight,new_height))
        print("Succeed to resize the image %s to %s*%s "%(image,new_weight,new_height))
        im.save(image)
    else:
        print("The image %s doesn't need to be resized." % image)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter.Try to execute 'python changephoto.py $dir_path'")
    else:
        for dir_path in sys.argv[1:]:
            for image_name in os.listdir(dir_path):
                image_path = os.path.join(dir_path,image_name)
                resize_image(image_path)
