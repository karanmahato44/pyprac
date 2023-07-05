# a basic one
# import qrcode as qr

# img = qr.make('https://karanmahato44.github.io/web/')
# img.save('file.png')
# print(img)

import qrcode
from PIL import Image


# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # Set the QR code version (adjust as needed)
    # Set the error correction level
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # Set the size of each box in pixels
    border=3  # Set the border size in boxes
)

# Add data to the QRCode
data = "nice"  # Specify the data you want to encode in the QR code
qr.add_data(data)

# Make the QRCode fit within a certain number of pixels
qr.make(fit=True)

# Create an image from the QRCode object
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image file
image_file_path = "qr_code.png"
qr_image.save(image_file_path)
