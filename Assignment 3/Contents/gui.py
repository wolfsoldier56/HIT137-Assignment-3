
###------------------------------------------------------------------------------------------------------------------------------------------------------### V3 
###running in VENV with py 3.12### 


##Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

##.\venv312\Scripts\Activate.ps1

### RUN AS python "C:\Users\Gabriel\Desktop\Assignment 3\Contents\gui.py"    

# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk
# from PIL import Image, ImageTk
# import threading
# import os

# from image_to_text import generate_caption
# from text_to_speech import text_to_voice
# from text_to_image import generate_image

# # -------------------------------
# # Global variable
# # -------------------------------
# image_path = None

# # Target sizes
# DISPLAY_WIDTH, DISPLAY_HEIGHT = 1000, 700    # Size shown in GUI
# INTERNAL_WIDTH, INTERNAL_HEIGHT = 1024, 1024 # CPU-friendly internal resolution

# # -------------------------------
# # Functions
# # -------------------------------
# # def choose_image():
# #     global image_path
# #     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
# #     if not filepath:
# #         return
# #     image_path = filepath
# #     img = Image.open(filepath)

# #     # Internal processing copy
# #     img_large = img.resize((INTERNAL_WIDTH, INTERNAL_HEIGHT))

# #     # Use the original size for display
# #     tk_img = ImageTk.PhotoImage(img)

# #     # Update label
# #     image_label.config(image=tk_img, text="")
# #     image_label.image = tk_img
# #     image_label.large_image = img_large

# #     caption_var.set("")
# #     audio_btn.config(state="disabled")

# def choose_image():
#     global image_path
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
#     if not filepath:
#         return
#     image_path = filepath
#     img = Image.open(filepath)

#     # Internal processing copy (always 1024x1024 for AI)
#     img_large = img.resize((INTERNAL_WIDTH, INTERNAL_HEIGHT))

#     # Display at natural/original size (no stretching)
#     tk_img = ImageTk.PhotoImage(img)

#     # Update label with real size
#     image_label.config(image=tk_img, text="")
#     image_label.image = tk_img
#     image_label.large_image = img_large

#     caption_var.set("")
#     audio_btn.config(state="disabled")

# # --- Threaded handlers ---
# def handle_caption_threaded():
#     if not image_path:
#         messagebox.showwarning("No image", "Please upload an image first.")
#         return

#     execute_btn.config(state="disabled")
#     upload_btn.config(state="disabled")
    
#     def task():
#         caption = generate_caption(image_path)
#         caption_var.set(caption)
#         if not caption.startswith("Error"):
#             audio_btn.config(state="normal")
#         execute_btn.config(state="normal")
#         upload_btn.config(state="normal")
    
#     threading.Thread(target=task).start()

# def handle_text_to_image_threaded():
#     text = caption_var.get().strip()
#     if not text:
#         messagebox.showwarning("No text", "Please enter text to generate an image.")
#         return

#     execute_btn.config(state="disabled")
#     upload_btn.config(state="disabled")

#     def task():
#         try:
#             img_large = generate_image(text, width=INTERNAL_WIDTH, height=INTERNAL_HEIGHT, steps=25)
#             tk_img = ImageTk.PhotoImage(img_large)

#             image_label.config(image=tk_img, text="")
#             image_label.image = tk_img
#             image_label.large_image = img_large
#         except Exception as e:
#             messagebox.showerror("Error", f"Image generation failed:\n{e}")
#         finally:
#             execute_btn.config(state="normal")
#             upload_btn.config(state="normal")

#     threading.Thread(target=task).start()
    
#     def task():
#         try:
#             img_large = generate_image(text, width=INTERNAL_WIDTH, height=INTERNAL_HEIGHT, steps=25)
#             display_img = img_large.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
#             tk_img = ImageTk.PhotoImage(display_img)
            
#             image_label.config(image=tk_img)
#             image_label.image = tk_img
#             image_label.large_image = img_large
#         except Exception as e:
#             messagebox.showerror("Error", f"Image generation failed:\n{e}")
#         finally:
#             execute_btn.config(state="normal")
#             upload_btn.config(state="normal")
    
#     threading.Thread(target=task).start()

# def handle_execute():
#     mode = mode_var.get()
#     if mode == "Image to Text":
#         handle_caption_threaded()
#     elif mode == "Text to Image":
#         handle_text_to_image_threaded()

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
# # root.geometry("1200x900")  # remove fixed window size so it can grow/shrink with image

# # Frame to display images (auto-sizes to content)
# image_frame = tk.Frame(root, relief="solid", bd=1)
# image_frame.pack(pady=10)

# # Label that takes the natural image size
# image_label = tk.Label(image_frame)
# image_label.pack()

# # Load logo at its natural size
# base_dir = os.path.dirname(__file__)
# logo_path = os.path.join(base_dir, "logo.jpg")
# if os.path.exists(logo_path):
#     logo_img = Image.open(logo_path)
#     tk_logo = ImageTk.PhotoImage(logo_img)
#     image_label.config(image=tk_logo)
#     image_label.image = tk_logo
# else:
#     image_label.config(text="No logo found")

# # Buttons, dropdowns, and entry
# upload_btn = tk.Button(root, text="Upload Image", command=choose_image)
# upload_btn.pack(pady=5)

# mode_var = tk.StringVar(value="Image to Text")
# mode_dropdown = ttk.Combobox(root, textvariable=mode_var,
#                              values=["Image to Text", "Text to Image"],
#                              state="readonly", width=20)
# mode_dropdown.pack(pady=5)

# execute_btn = tk.Button(root, text="Execute", command=handle_execute)
# execute_btn.pack(pady=10)

# caption_var = tk.StringVar()
# caption_entry = tk.Entry(root, textvariable=caption_var, width=70)
# caption_entry.pack(pady=10)

# audio_btn = tk.Button(root, text="Play Voice", command=handle_voice, state="disabled")
# audio_btn.pack(pady=5)

# root.mainloop()

# # logo_img = Image.open("logo.jpg")

# # # Optionally resize it to fit the frame
# # logo_img = logo_img.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# # # Convert to Tkinter image
# # tk_logo = ImageTk.PhotoImage(logo_img)

# # # image_label = tk.Label(image_frame, text="No image uploaded")
# # # image_label.pack(expand=True)

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import threading
import os
from image_to_text import generate_caption
from text_to_speech import text_to_voice
from text_to_image import generate_image

# Global variables
image_path = None
image_on_canvas = None

def display_image_on_canvas(pil_img):
    """Display PIL image on canvas, natural size with scrollbars"""
    global image_on_canvas
    tk_img = ImageTk.PhotoImage(pil_img)
    canvas.delete("all")
    image_on_canvas = tk_img
    canvas.create_image(0, 0, anchor="nw", image=tk_img)
    canvas.config(scrollregion=canvas.bbox("all"))

def choose_image():
    global image_path
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if not filepath:
        return
    image_path = filepath
    img = Image.open(filepath)
    img_large = img.resize((1024,1024))  # internal AI processing copy
    display_image_on_canvas(img)
    caption_var.set("")
    audio_btn.config(state="disabled")

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
            img_large = generate_image(text, width=1024, height=1024, steps=25)
            display_image_on_canvas(img_large)
        except Exception as e:
            messagebox.showerror("Error", f"Image generation failed:\n{e}")
        finally:
            execute_btn.config(state="normal")
            upload_btn.config(state="normal")
    threading.Thread(target=task).start()

def handle_execute():      # Execute button handler
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

# GUI Setup-----------------
root = tk.Tk()
root.title("AI Image/Text Tool")
root.geometry("1200x800")

# Canvas with scrollbars
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(canvas_frame, bg="white")
canvas.pack(side="left", fill="both", expand=True)

v_scroll = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
v_scroll.pack(side="right", fill="y")
h_scroll = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
h_scroll.pack(side="bottom", fill="x")

canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

# Buttons and controls (outside canvas)
control_frame = tk.Frame(root)
control_frame.pack(pady=5)

upload_btn = tk.Button(control_frame, text="Upload Image", command=choose_image)   # Upload button linked to handler
upload_btn.grid(row=0, column=0, padx=5)

mode_var = tk.StringVar(value="Image to Text")    # Dropdown for mode selection
mode_dropdown = ttk.Combobox(control_frame, textvariable=mode_var,
                             values=["Image to Text", "Text to Image"],
                             state="readonly", width=20)
mode_dropdown.grid(row=0, column=1, padx=5)

execute_btn = tk.Button(control_frame, text="Execute", command=handle_execute)  # Execute button- linked to handler
execute_btn.grid(row=0, column=2, padx=5)

caption_var = tk.StringVar()  # Entry for caption/text
caption_entry = tk.Entry(control_frame, textvariable=caption_var, width=50)
caption_entry.grid(row=1, column=0, columnspan=2, pady=5)

audio_btn = tk.Button(control_frame, text="Play Voice", command=handle_voice, state="disabled")
audio_btn.grid(row=1, column=2, pady=5)

# Load logo naturally
base_dir = os.path.dirname(__file__)
logo_path = os.path.join(base_dir, "logo.jpg")
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    display_image_on_canvas(logo_img)
else:
    canvas.create_text(10,10, anchor="nw", text="No logo found")

root.mainloop()
