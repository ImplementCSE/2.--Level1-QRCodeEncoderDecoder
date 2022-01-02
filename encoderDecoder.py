# In this video, we are going to use the pyqrcode library to encode texts and generate QR code

# Welcome to Implement CSE, thanks for watching the video.

# importing the libraries
# use pip install "library" to install the following libraries

import pyqrcode
from pyzbar.pyzbar import decode  # library for decoding the qr code generated
from PIL import Image

# generating the QR code of text
qr_code = pyqrcode.create(
    "This is the sample text for encoding, Level 1 project - Implement_CSE")
# this is the name of the image file containing QR code
qr_code.png("QR_Code_image.png", scale=10)

# now the code for generating the QR Code is complete, Lets run it!!
# As you can see, the image file is automatically generated.

# Next step is to decode the QR code, generated above.

# decoding the QR code
decode_QRcode = decode(Image.open("QR_Code_image.png"))
# printing the decoded QR code on the screen in ASCII format
print(decode_QRcode[0].data.decode("ascii"))

# As you can see the program has successfully decoded the previously generated QR code.

#created by Implement_CSE.
# Now lets encode a given file, and generate a QR code for the same


# encoding the text file

f = open("ThisIsASampleFile.txt", "r")
# alternatively, you can also define the path, if test file is in other directory
# example: f = open("D:\\myfile\file_name.txt", "r")

qr_code_testfile = pyqrcode.create(f.read())
qr_code_testfile.png("QR_Code_for_test_file.png", scale=40)
# As you can see the QR code is generated

# Now lets Decode the QR code for sample text file

decode_qrCode_for_TestFile = decode(Image.open("QR_Code_for_test_file.png"))

# printing the decoded QR code on the screen, in ASCII format
print(decode_qrCode_for_TestFile[0].data.decode("ascii"))

# Lets run the code and check, if it decodes the QR code and prints the contents of sample file correctly :)
# As you can see, only the first line is encoded-decoded, because of "readline()" used.
# Now, we use read function, and re-run the program
# Now, the entire file is encoded-decoded.

# That's how you code a QR Code encoder-decoder in Python
# Thanks for Watching :)
# Implement_CSE
