import tkinter as tk #import tkinter library
import image_to_text


root = tk.Tk() #create a root window
root.title("Image_Describer_V1") #set the title of the window
root.geometry("800x600") #set the size of the window
root.configure(bg="lightblue") #set the background color of the window

# Add a label to the window
label = tk.Label(root, text="Describe this image", bg="lightblue", font=("Arial", 24))
label.pack(pady=20)  #pack is geometry manager 
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)
button = tk.Button(root, text="Click Me!")
button.pack(pady=10)

root.mainloop() #initite tkinter event loop

