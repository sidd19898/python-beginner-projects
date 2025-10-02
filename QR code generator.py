#ask user for url
#ask user for file name to save the file which contains qr code
#print qr code saved as file name

import qrcode
a = input("please enter url : ")
b = input("please enter file name to save:")
img = qrcode.make(a)
img.save(b)