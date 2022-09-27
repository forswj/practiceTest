import random
from random import randint
import pysnooper



@pysnooper.snoop()
def cr_mobile(no):
    number_list = []
    number = str(random.randint(135, 139) + str(random.randint(10000000, 99999999)))
    count = 0
    while count <= no:
        if number not in number_list:
            number_list.append(number)
            count += 1
        fp = open("d:\\a.txt", "w")
        for num in number_list:
            fp.write(num+"n")
            fp.close()

cr_mobile(1)