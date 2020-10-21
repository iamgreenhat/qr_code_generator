import pyqrcode
# make sure to install pypng also

data = input("Enter the data you want to encode in QR:")
# data can be anything in text also you can add redirections such as redirecting to email by adding to email like mailto:someone@example.com
img = pyqrcode.create(data)
# now its creating the qrcode
img.png('new.png', scale= 10)
# now your qr code will be saved in the directory where this python file is located 
