from PIL import Image

def xor_encrypt(message,key):
    return ''.join(chr(ord(c)^ord(key[i%len(key)])) for i,c in enumerate(message))

def xor_decrypt(encrypted_message,key):
    return ''.join(chr(ord(c)^ord(key[i%len(key)])) for i,c in enumerate(encrypted_message))

def text_to_binary(message):
    return ''.join(format(ord(char),'08b') for char in message)

def binary_to_text(binary_data):
    chars=[]
    for i in range(0,len(binary_data),8):
        byte=binary_data[i:i+8]
        chars.append(chr(int(byte,2)))
    return ''.join(chars)

def encode_image(image_path,secret_message,output_path,key=None):
    if key:
        secret_message=xor_encrypt(secret_message,key)
        
    img=Image.open(image_path)
    encoded=img.copy()
    width,height=img.size
    binary_message=text_to_binary(secret_message)+'1111111111111110'

    data_index=0
    message_len=len(binary_message)

    for y in range(height):
        for x in range(width):
            if data_index>=message_len:
                break

            r,g,b=img.getpixel((x,y))

            r_bin=format(r,'08b')
            g_bin=format(g,'08b')
            b_bin=format(b,'08b')

            if data_index<message_len:
                r_bin=r_bin[:-1]+binary_message[data_index]
                data_index+=1
            if data_index<message_len:
                g_bin=g_bin[:-1]+binary_message[data_index]
                data_index+=1
            if data_index<message_len:
                b_bin=b_bin[:-1]+binary_message[data_index]
                data_index+=1

            new_pixel=(int(r_bin,2),int(g_bin,2),int(b_bin,2))
            encoded.putpixel((x,y),new_pixel)

            if data_index>=message_len:
                break
    encoded.save(output_path)
    print(f"Message encoded and saved as '{output_path}'")

def decode_image(image_path,key=None):
    img=Image.open(image_path)
    width,height=img.size
    binary_data=''

    for y in range(height):
        for x in range(width):
            r,g,b=img.getpixel((x,y))
            r_bin=format(r,'08b')
            g_bin=format(g,'08b')
            b_bin=format(b,'08b')

            binary_data+=r_bin[-1]
            binary_data+=g_bin[-1]
            binary_data+=b_bin[-1]

            if '1111111111111110' in binary_data:
                binary_data=binary_data[:binary_data.find('1111111111111110')]
                message=binary_to_text(binary_data)
                if key:
                    message=xor_decrypt(message,key)
                    
                print("Decoded message:",message)
                return message
            
    print("No hidden message found.")

#if __name__=="__main__":
    #input_image="image.png"
    #output_image="output.png"
    #secret_message="Meet me at 9PM at the old bridge."
    #xor_key="key123"

#encode_image(input_image,secret_message,output_image,key=xor_key)
#decode_image(output_image,key=xor_key)
            
#image=Image.open("image.png")
#pixels=image.load()

#print("Image size:",image.size)
#print("First 10 pixels:")
#for x in range(10):
    #print(pixels[x,0])

#message="Hello"
#binary=text_to_binary(message)
#print("Binary:",binary)
