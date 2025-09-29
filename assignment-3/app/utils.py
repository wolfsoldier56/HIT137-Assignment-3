import threading

# ===============================
# Decorator to run functions in threads
# ===============================
def run_in_thread(func):
    """Decorator: runs the wrapped function in a background thread."""
    def wrapper(*args, **kwargs):
        threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True).start()
    return wrapper
