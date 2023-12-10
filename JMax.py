import os
try:
    import jmcomic
except:
    os.system('python -m pip install jmcomic -i https://pypi.org/project --upgrade')

sauce = int(input())
try:
    jmcomic.download_album(sauce)
except:
    print('出現錯誤！\n1.本子id可能有誤\n2.此漫畫可能只有登入用戶可以查看')