import qrcode

# This line sets the data the QR code should contain and encodes it:
qr = qrcode.make("https://coolplaydev.com")
# Save the QR code as a png file (can also be a jpg)
qr.save("qr.png")