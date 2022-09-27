import math

import createPhone

def text_create(name, msg):
    desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    # file.close()

msg = createPhone.createPhone()
text_create('mytxtfile', 'msg')
# 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!

