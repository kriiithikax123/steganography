import tkinter as tk
from tkinter import filedialog, messagebox
import os
from stego_core import encode_image, decode_image   

root = tk.Tk()
root.title("Image Steganography Tool")
root.geometry("500x500")
root.resizable(False, False)

image_path = ""
output_path = "output.png"

def browse_image():
    global image_path
    file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp")])
    if file:
        image_path = file
        image_label.config(text=f"Selected: {os.path.basename(file)}")
    else:
        image_label.config(text="No image selected")

def hide_message():
    global image_path, output_path
    if not image_path:
        messagebox.showerror("Error", "Please select an image first.")
        return

    secret_msg = message_entry.get("1.0", tk.END).strip()
    if not secret_msg:
        messagebox.showwarning("Warning", "Secret message cannot be empty.")
        return

    key = key_entry.get().strip()
    try:
        encode_image(image_path, secret_msg, output_path, key if key else None)
        messagebox.showinfo("Success", f"Message encoded and saved to '{output_path}'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def extract_message():
    global output_path
    if not os.path.exists(output_path):
        messagebox.showerror("Error", "No encoded image found. Please hide a message first.")
        return

    key = key_entry.get().strip()
    try:
        decoded_msg = decode_image(output_path, key if key else None)
        
        result_box.delete("1.0", tk.END)

        if decoded_msg:
            decoded_msg=decoded_msg.strip()
            result_box.insert("1.0", decoded_msg)
        
            if not decoded_msg:
                messagebox.showwarning("Warning","No message was found")
            
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Label(root, text="Image Steganography", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Browse Image", command=browse_image).pack(pady=5)
image_label = tk.Label(root, text="No image selected", fg="gray")
image_label.pack()

tk.Label(root, text="Secret Message:").pack()
message_entry = tk.Text(root, height=5, width=50)
message_entry.pack()

tk.Label(root, text="Encryption Key (optional):").pack()
key_entry = tk.Entry(root, width=40, show="*")
key_entry.pack(pady=5)

tk.Button(root, text="Hide Message", command=hide_message, bg="#4CAF50", fg="white", width=20).pack(pady=10)
tk.Button(root, text="Extract Message", command=extract_message, bg="#2196F3", fg="white", width=20).pack(pady=5)

tk.Label(root, text="Decoded Message:").pack()
result_box = tk.Text(root, height=5, width=50)
result_box.pack(pady=5)

root.mainloop()


    
