from MyQR import myqr
import os
urls = "https://wx.qq.com/"

#生成动图二维码
version,level,qr_name = myqr.run(
    words=urls,
    version=1,
    level='H',
    picture='皮卡丘.gif',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='myqr.gif',
    save_dir=os.getcwd()
)