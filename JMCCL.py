import jmcomic
import os

os.system('pip install jmcomic -i https://pypi.org/project --upgrade')
def dld(number):
    global status
    try:
        print(number)
        jmcomic.download_album(number)
        status = "下載成功！"
    except:
        print('出現錯誤！\n1.本子id可能有誤\n2.此漫畫可能只有登入用戶可以查看')
        status = "error! 本子id可能有誤或此漫畫可能只有登入用戶可以查看"