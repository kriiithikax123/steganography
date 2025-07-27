Image Steganography Tool
This project is a simple Image Steganography tool built using Python and Tkinter GUI. It allows users to hide secret messages inside images using LSB (Least Significant Bit) encoding, and optionally encrypt the message with a key. Users can also extract and decode the hidden message.

Features
1. Hide secret text inside an image (PNG)
2. Extract the hidden message from an image
3. Optional encryption using XOR and a user-supplied key
4. User-friendly GUI interface
5. Basic error handling and message validation

Tools & Technologies
1. Python 3.x
2. Tkinter (GUI)
3. PIL (Pillow) for image handling

How to Run
1. Install dependencies
   (pip install pillow)
2. Run the GUI
   (python gui.py)
3. Use the interface to:
   - Browse and select a PNG image
   - Enter your secret message
   - Optionally enter an encryption key
   - Click Hide Message to encode
   - Click Extract Message to decode

How It Works
Encoding: The message is converted to binary, optionally XOR-encrypted, and embedded into the image’s least significant bits. A delimiter is added to mark the end of the message.
Decoding: The binary data is extracted from the image’s pixels and decoded back to text using the delimiter as a stopping point.
