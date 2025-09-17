from transformers import pipeline

###https://huggingface.co/nlpconnect/vit-gpt2-image-captioning###

# Load the Hugging Face image-to-text pipeline
pipe = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

def generate_caption(image_path: str) -> str:
    """
    Generate a caption from an image.
    """
    try:
        caption = pipe(image_path)[0]["generated_text"]
        return caption
    except Exception as e:
        return f"Error: {e}"


###Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

##.\venv312\Scripts\Activate.ps1

##python "C:\Users\Gabriel\Desktop\Assignment 3\Contents\image_to_text.py"  