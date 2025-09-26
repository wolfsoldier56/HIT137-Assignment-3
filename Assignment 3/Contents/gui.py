import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import threading
import os
from image_to_text import generate_caption
from text_to_speech import text_to_voice
from text_to_image import generate_image

# ===============================
# Decorator to run functions in threads
# ===============================
def run_in_thread(func):
    """Decorator: runs the wrapped function in a background thread."""
    def wrapper(*args, **kwargs):
        threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True).start()
    return wrapper

# ===============================
# Main GUI Class
# ===============================
class AIImageTextApp:

    def __init__(self, root):
        """Initialize the GUI, variables, and layout."""
        self.root = root
        self.root.title("AI Image/Text Tool")
        self.root.geometry("1200x900")  # Set window size

        # ===============================
        # Internal variables
        # ===============================
        self.last_image = None           # PIL Image reference for current image
        self.image_on_canvas = None      # Tkinter PhotoImage reference for canvas
        self.loaded_image_path = None    # Path to uploaded image

        # ===============================
        # Build GUI components
        # ===============================
        self._build_canvas()             # Canvas + scrollbars
        self._build_controls()           # Buttons, entry, dropdown
        self._build_description()        # Mode description label

        # ===============================
        # Load logo on startup
        # ===============================
        self._load_logo()                # Display initial logo

    # ===============================
    # Canvas setup
    # ===============================
    def _build_canvas(self):
        """Create canvas frame, canvas, and scrollbars."""
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white")  # Canvas for images
        self.canvas.pack(side="left", fill="both", expand=True)

        # Vertical scrollbar
        self.v_scroll = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.v_scroll.pack(side="right", fill="y")

        # Horizontal scrollbar
        self.h_scroll = tk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        self.h_scroll.pack(side="bottom", fill="x")

        # Configure canvas scroll commands
        self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        # Bind redraw image when canvas is resized
        self.canvas.bind("<Configure>", lambda e: self.redraw_image())

    # ===============================
    # Control frame (buttons + entry)
    # ===============================
    def _build_controls(self):
        """Create buttons, dropdown, text entry for prompt/caption."""
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=5)

        # Upload image button
        self.upload_btn = tk.Button(self.control_frame, text="Upload Image", command=self.choose_image)
        self.upload_btn.grid(row=0, column=0, padx=5)

        # Mode selection dropdown
        self.mode_var = tk.StringVar(value="Image to Text")
        self.mode_dropdown = ttk.Combobox(self.control_frame, textvariable=self.mode_var,
                                          values=["Image to Text", "Text to Image"],
                                          state="readonly", width=20)
        self.mode_dropdown.grid(row=0, column=1, padx=5)

        # Execute button (runs selected mode)
        self.execute_btn = tk.Button(self.control_frame, text="Execute", command=self.handle_execute)
        self.execute_btn.grid(row=0, column=2, padx=5)

        # Caption or text prompt entry
        self.caption_var = tk.StringVar()
        self.caption_entry = tk.Entry(self.control_frame, textvariable=self.caption_var, width=50)
        self.caption_entry.grid(row=1, column=0, columnspan=2, pady=5)

        # Text-to-speech button
        self.audio_btn = tk.Button(self.control_frame, text="Play Voice", command=self.handle_voice, state="disabled")
        self.audio_btn.grid(row=1, column=2, pady=5)

        # Trace mode dropdown to update description dynamically
        self.mode_var.trace_add("write", self.update_description)

    # ===============================
    # Description label setup
    # ===============================
    def _build_description(self):
        """Label to show description of selected mode."""
        self.description_var = tk.StringVar()
        self.description_label = tk.Label(self.root, textvariable=self.description_var, wraplength=1150,
                                          justify="left", bg="#f0f0f0", anchor="w", relief="sunken",
                                          bd=1, padx=5, pady=5)
        self.description_label.pack(fill="x", padx=10, pady=10)
        self.update_description()  # initial description

    # ===============================
    # Update description label
    # ===============================
    def update_description(self, *args):
        """Update description text based on selected mode."""
        mode = self.mode_var.get()
        if mode == "Image to Text":
            self.description_var.set(
                "Image to Text: Upload an image and generate a brief textual description of it. "
                "Useful for understanding the content of images or for accessibility purposes."
            )
        elif mode == "Text to Image":
            self.description_var.set(
                "Text to Image: Enter descriptive text to generate an image based on it. "
                "Useful for visualizing ideas or concepts from text."
            )

    # ===============================
    # Load and display logo
    # ===============================
    def _load_logo(self):
        """Load logo image at startup if it exists."""
        base_dir = os.path.dirname(__file__)
        logo_path = os.path.join(base_dir, "logo.jpg")
        if os.path.exists(logo_path):
            logo_img = Image.open(logo_path).resize((400, 300))  # Resize logo to fit canvas
            self.display_image(logo_img)  # Center it
        else:
            self.canvas.create_text(10, 10, anchor="nw", text="No logo found")

    # ===============================
    # Display and redraw image
    # ===============================
    def display_image(self, pil_img):
        """Store references to PIL and Tkinter images, draw centered."""
        self.last_image = pil_img
        self.image_on_canvas = ImageTk.PhotoImage(pil_img)
        self.redraw_image()  # Draw immediately

    def redraw_image(self, event=None):
        """Redraw the last image centered on canvas."""
        if self.last_image is None:
            return

        self.canvas.delete("all")  # Clear previous image

        # Get canvas size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        img_width, img_height = self.last_image.size

        # Calculate top-left coordinates for centering
        x = max((canvas_width - img_width) // 2, 0)
        y = max((canvas_height - img_height) // 2, 0)

        # Draw image
        self.canvas.create_image(x, y, anchor="nw", image=self.image_on_canvas)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # ===============================
    # Upload Image
    # ===============================
    def choose_image(self):
        """Open file dialog to select an image and display it."""
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp *.gif")])
        if not filepath:
            return
        self.loaded_image_path = filepath
        img = Image.open(filepath)
        self.display_image(img)  # Center uploaded image
        self.caption_var.set("")
        self.audio_btn.config(state="disabled")

    # ===============================
    # Execute button handler
    # ===============================
    def handle_execute(self):
        """Run the selected mode (Image→Text or Text→Image)."""
        mode = self.mode_var.get()
        if mode == "Image to Text":
            self.handle_caption_threaded()
        elif mode == "Text to Image":
            self.handle_text_to_image_threaded()

    # ===============================
    # Image → Text (Caption)
    # ===============================
    @run_in_thread
    def handle_caption_threaded(self):
        """Generate caption in background to avoid freezing GUI."""
        if not self.loaded_image_path:
            messagebox.showwarning("No image", "Please upload an image first.")
            return
        self.execute_btn.config(state="disabled")
        self.upload_btn.config(state="disabled")

        caption = generate_caption(self.loaded_image_path)
        self.caption_var.set(caption)
        if not caption.startswith("Error"):
            self.audio_btn.config(state="normal")

        self.execute_btn.config(state="normal")
        self.upload_btn.config(state="normal")

    # ===============================
    # Text → Image
    # ===============================
    @run_in_thread
    def handle_text_to_image_threaded(self):
        """Generate image from text in background."""
        text = self.caption_var.get().strip()
        if not text:
            messagebox.showwarning("No text", "Please enter text to generate an image.")
            return

        self.execute_btn.config(state="disabled")
        self.upload_btn.config(state="disabled")

        try:
            img_large = generate_image(text, width=1024, height=1024, steps=25)
            self.display_image(img_large)
        except Exception as e:
            messagebox.showerror("Error", f"Image generation failed:\n{e}")
        finally:
            self.execute_btn.config(state="normal")
            self.upload_btn.config(state="normal")

    # ===============================
    # Text-to-Speech
    # ===============================
    @run_in_thread
    def handle_voice(self):
        """Convert caption text to audio using text_to_voice."""
        text = self.caption_var.get()
        if not text:
            messagebox.showwarning("No caption", "Generate or enter text first.")
            return
        result = text_to_voice(text)
        if result.startswith("Error"):
            messagebox.showerror("Error", result)

# ===============================
# Run the application
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = AIImageTextApp(root)
    root.mainloop()
