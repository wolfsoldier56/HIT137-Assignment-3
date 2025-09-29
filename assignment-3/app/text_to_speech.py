# from gtts import gTTS
# import tempfile
# import pygame

# pygame.mixer.init()

# def text_to_voice(text: str) -> str:
#     """
#     Convert text to speech and play it.
#     Returns the path to the temp audio file.
#     """
#     try:
#         tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
#         tts = gTTS(text)
#         tts.save(tmp_file.name)

#         pygame.mixer.music.load(tmp_file.name)
#         pygame.mixer.music.play()

#         return tmp_file.name
#     except Exception as e:
#         return f"Error: {e}"


##Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

##.\venv312\Scripts\Activate.ps1

##python "C:\Users\Gabriel\Desktop\Assignment 3\Contents\text_to_speech.py"###

from gtts import gTTS
import tempfile
import pygame
import os

pygame.mixer.init()

def text_to_voice(text: str) -> str:
    """
    Convert text to speech and play it.
    Returns the path to a temporary MP3 file.
    """
    try:
        # Create a temporary file path
        tmp_fd, tmp_path = tempfile.mkstemp(suffix=".mp3")
        os.close(tmp_fd)  # Close immediately, so TTS can write

        # Generate speech
        tts = gTTS(text)
        tts.save(tmp_path)

        # Play audio
        pygame.mixer.music.load(tmp_path)
        pygame.mixer.music.play()

        return tmp_path

    except Exception as e:
        return f"Error: {e}"
    
    ## not a hugging face model but works well for text to speech ## 