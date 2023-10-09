import qrcode as qr
ans=input("Enter your online link which you want to make qr code.")
img=qr.make(ans)
img.save("qr.png")
print("done ")