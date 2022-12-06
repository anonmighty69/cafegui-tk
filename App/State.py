

DATA_MEJA = [False, False, False, False, False, False, False, False, False, False]

def get_center(window, width, height) -> str:
    x = int(window.winfo_screenwidth() / 2 - width / 2)
    y = int(window.winfo_screenheight() / 2 - height / 2)
    return f"{width}x{height}+{x}+{y}"