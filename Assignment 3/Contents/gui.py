# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk

# from image_to_text import generate_caption
# from text_to_speech import text_to_voice

# ###------------  py -m pip install torch torchvision torchaudio transformers huggingface_hub[hf_xet] pillow pygame scipy soundfile diffusers accelerate safetensors  ---------------###

# ###-- find images https://www.pexels.com/ --###

# image_path = None

# def choose_image():
#     global image_path
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
#     if filepath:
#         image_path = filepath
#         img = Image.open(filepath)
#         img.thumbnail((300, 300))
#         tk_img = ImageTk.PhotoImage(img)
#         image_label.config(image=tk_img)
#         image_label.image = tk_img
#         caption_var.set("")
#         audio_btn.config(state="disabled")

# def handle_caption():
#     if not image_path:
#         messagebox.showwarning("No image", "Please upload an image first.")
#         return
#     caption = generate_caption(image_path)
#     caption_var.set(caption)
#     if not caption.startswith("Error"):
#         audio_btn.config(state="normal")

# def handle_voice():
#     text = caption_var.get()
#     if not text:
#         messagebox.showwarning("No caption", "Generate a caption first.")
#         return
#     result = text_to_voice(text)
#     if result.startswith("Error"):
#         messagebox.showerror("Error", result)

# # ----------------- GUI Setup -----------------
# root = tk.Tk()
# root.title("Image Caption + Text-to-Speech")
# root.geometry("1000x1000")

# image_label = tk.Label(root, text="No image uploaded", width=40, height=10)
# image_label.pack(pady=10)

# upload_btn = tk.Button(root, text="Upload Image", command=choose_image)
# upload_btn.pack(pady=5)

# caption_btn = tk.Button(root, text="Generate Caption", command=handle_caption)
# caption_btn.pack(pady=5)

# caption_var = tk.StringVar()
# caption_entry = tk.Entry(root, textvariable=caption_var, width=50)
# caption_entry.pack(pady=10)

# audio_btn = tk.Button(root, text="Play Voice", command=handle_voice, state="disabled")
# audio_btn.pack(pady=5)

# root.mainloop()

###------------------------------------------------------------------------------------------------------------------------------------------------------### V2

# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk
# from PIL import Image, ImageTk, ImageDraw

# from image_to_text import generate_caption
# from text_to_speech import text_to_voice

# # -------------------------------
# # Global variable
# # -------------------------------
# image_path = None

# # Target sizes
# DISPLAY_WIDTH, DISPLAY_HEIGHT = 1000, 700    # Size shown in GUI
# INTERNAL_WIDTH, INTERNAL_HEIGHT = 6000, 4200 # 10x bigger internal resolution

# # -------------------------------
# # Functions
# # -------------------------------
# def choose_image():
#     global image_path
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
#     if not filepath:
#         return
#     image_path = filepath
#     img = Image.open(filepath)
    
#     # Resize for internal processing (10x bigger)
#     img_large = img.resize((INTERNAL_WIDTH, INTERNAL_HEIGHT))
    
#     # Scale to display in GUI
#     display_img = img_large.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
#     tk_img = ImageTk.PhotoImage(display_img)
    
#     image_label.config(image=tk_img)
#     image_label.image = tk_img
#     image_label.large_image = img_large  # Keep high-res copy for processing
    
#     caption_var.set("")
#     audio_btn.config(state="disabled")

# def handle_execute():
#     mode = mode_var.get()
#     if mode == "Image to Text":
#         handle_caption()
#     elif mode == "Text to Image":
#         handle_text_to_image()

# def handle_caption():
#     if not image_path:
#         messagebox.showwarning("No image", "Please upload an image first.")
#         return
#     caption = generate_caption(image_path)
#     caption_var.set(caption)
#     if not caption.startswith("Error"):
#         audio_btn.config(state="normal")

# def handle_text_to_image():
#     text = caption_var.get().strip()
#     if not text:
#         messagebox.showwarning("No text", "Please enter text to generate an image.")
#         return
    
#     # -------------------------------
#     # Placeholder "generated" image
#     # -------------------------------
#     img_large = Image.new("RGB", (INTERNAL_WIDTH, INTERNAL_HEIGHT), color=(200, 200, 255))
#     draw = ImageDraw.Draw(img_large)
#     draw.text((50, 50), text[:500], fill=(0, 0, 0))  # First 500 chars
    
#     # Scale to display
#     display_img = img_large.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
#     tk_img = ImageTk.PhotoImage(display_img)
    
#     image_label.config(image=tk_img)
#     image_label.image = tk_img
#     image_label.large_image = img_large
    
#     messagebox.showinfo("Text-to-Image", "Image generated from text (placeholder).")

# def handle_voice():
#     text = caption_var.get()
#     if not text:
#         messagebox.showwarning("No caption", "Generate or enter text first.")
#         return
#     result = text_to_voice(text)
#     if result.startswith("Error"):
#         messagebox.showerror("Error", result)

# # -------------------------------
# # GUI Setup
# # -------------------------------
# root = tk.Tk()
# root.title("AI Image/Text Tool")
# root.geometry("1200x900")

# # Fixed-size frame to hold image
# image_frame = tk.Frame(root, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, relief="solid", bd=1)
# image_frame.pack(pady=10)
# image_frame.pack_propagate(False)  # Prevent frame from resizing to image

# # Image label inside frame
# image_label = tk.Label(image_frame, text="No image uploaded")
# image_label.pack(expand=True)

# # Upload button
# upload_btn = tk.Button(root, text="Upload Image", command=choose_image)
# upload_btn.pack(pady=5)

# # Dropdown for mode selection
# mode_var = tk.StringVar(value="Image to Text")
# mode_dropdown = ttk.Combobox(
#     root, textvariable=mode_var, 
#     values=["Image to Text", "Text to Image"], 
#     state="readonly", width=20
# )
# mode_dropdown.pack(pady=5)

# # Execute button
# execute_btn = tk.Button(root, text="Execute", command=handle_execute)
# execute_btn.pack(pady=10)

# # Text entry box
# caption_var = tk.StringVar()
# caption_entry = tk.Entry(root, textvariable=caption_var, width=70)
# caption_entry.pack(pady=10)

# # Speech button
# audio_btn = tk.Button(root, text="Play Voice", command=handle_voice, state="disabled")
# audio_btn.pack(pady=5)

# root.mainloop()

###------------------------------------------------------------------------------------------------------------------------------------------------------### V3 
###running in VENV with py 3.12### 


##Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

##.\venv312\Scripts\Activate.ps1

### RUN AS python "C:\Users\Gabriel\Desktop\Assignment 3\Contents\gui.py"    

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import threading
import os

from image_to_text import generate_caption
from text_to_speech import text_to_voice
from text_to_image import generate_image

# -------------------------------
# Global variable
# -------------------------------
image_path = None

# Target sizes
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1000, 700    # Size shown in GUI
INTERNAL_WIDTH, INTERNAL_HEIGHT = 1024, 1024 # CPU-friendly internal resolution

# -------------------------------
# Functions
# -------------------------------
def choose_image():
    global image_path
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if not filepath:
        return
    image_path = filepath
    img = Image.open(filepath)
    
    # Resize for internal processing
    img_large = img.resize((INTERNAL_WIDTH, INTERNAL_HEIGHT))
    
    # Scale to display
    display_img = img_large.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    tk_img = ImageTk.PhotoImage(display_img)
    
    # Update the label
    image_label.config(image=tk_img)
    image_label.image = tk_img
    image_label.large_image = img_large
    
    caption_var.set("")
    audio_btn.config(state="disabled")

# --- Threaded handlers ---
def handle_caption_threaded():
    if not image_path:
        messagebox.showwarning("No image", "Please upload an image first.")
        return

    execute_btn.config(state="disabled")
    upload_btn.config(state="disabled")
    
    def task():
        caption = generate_caption(image_path)
        caption_var.set(caption)
        if not caption.startswith("Error"):
            audio_btn.config(state="normal")
        execute_btn.config(state="normal")
        upload_btn.config(state="normal")
    
    threading.Thread(target=task).start()

def handle_text_to_image_threaded():
    text = caption_var.get().strip()
    if not text:
        messagebox.showwarning("No text", "Please enter text to generate an image.")
        return

    execute_btn.config(state="disabled")
    upload_btn.config(state="disabled")
    
    def task():
        try:
            img_large = generate_image(text, width=INTERNAL_WIDTH, height=INTERNAL_HEIGHT, steps=25)
            display_img = img_large.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
            tk_img = ImageTk.PhotoImage(display_img)
            
            image_label.config(image=tk_img)
            image_label.image = tk_img
            image_label.large_image = img_large
        except Exception as e:
            messagebox.showerror("Error", f"Image generation failed:\n{e}")
        finally:
            execute_btn.config(state="normal")
            upload_btn.config(state="normal")
    
    threading.Thread(target=task).start()

def handle_execute():
    mode = mode_var.get()
    if mode == "Image to Text":
        handle_caption_threaded()
    elif mode == "Text to Image":
        handle_text_to_image_threaded()

def handle_voice():
    text = caption_var.get()
    if not text:
        messagebox.showwarning("No caption", "Generate or enter text first.")
        return
    result = text_to_voice(text)
    if result.startswith("Error"):
        messagebox.showerror("Error", result)

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("AI Image/Text Tool")
root.geometry("1200x900")

# Frame to display images
image_frame = tk.Frame(root, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, relief="solid", bd=1)
image_frame.pack(pady=10)
image_frame.pack_propagate(False)

# Create the label **first** and show logo
image_label = tk.Label(image_frame)
image_label.pack(expand=True)

# Load logo
base_dir = os.path.dirname(__file__)
logo_path = os.path.join(base_dir, "logo.jpg")
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    tk_logo = ImageTk.PhotoImage(logo_img)
    image_label.config(image=tk_logo)
    image_label.image = tk_logo
else:
    image_label.config(text="No logo found")

# Buttons, dropdowns, and entry
upload_btn = tk.Button(root, text="Upload Image", command=choose_image)
upload_btn.pack(pady=5)

mode_var = tk.StringVar(value="Image to Text")
mode_dropdown = ttk.Combobox(root, textvariable=mode_var,
                             values=["Image to Text", "Text to Image"],
                             state="readonly", width=20)
mode_dropdown.pack(pady=5)

execute_btn = tk.Button(root, text="Execute", command=handle_execute)
execute_btn.pack(pady=10)

caption_var = tk.StringVar()
caption_entry = tk.Entry(root, textvariable=caption_var, width=70)
caption_entry.pack(pady=10)

audio_btn = tk.Button(root, text="Play Voice", command=handle_voice, state="disabled")
audio_btn.pack(pady=5)

root.mainloop()

# logo_img = Image.open("logo.jpg")

# # Optionally resize it to fit the frame
# logo_img = logo_img.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# # Convert to Tkinter image
# tk_logo = ImageTk.PhotoImage(logo_img)

# # image_label = tk.Label(image_frame, text="No image uploaded")
# # image_label.pack(expand=True)
