import qrcode

Input = input("Enter matter for QR Code: ")

generate_image = qrcode.make(Input)

name = input("Enter name for file: ")
generate_image.save(name + ".png")

print("Successfull.")