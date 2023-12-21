import qrcode

input_url = input("Enter the URL to generate the QR Code: ")

img1 = qrcode.make('input_url')

img1.save('image.jpg')