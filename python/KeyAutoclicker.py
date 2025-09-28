import pyautogui
import threading
import time
import keyboard
import tkinter as tk

#NOTICE: THIS SCRIPT IS NOT MINE, PROPS TO CHIQUI AND FORNAUT ON STEAM!

pyautogui.PAUSE = 0  # No Pause between keyDown/keyUp
# Safe Standartbuttons (without Windows-/System-Buttons)
keys = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9',]


# Settings
Interval = 0.01  # Seconds between button presses
key_to_press = 'space'  # Additional press
toggle_key = 'p'  # Start/Stop with button 'p'

# Control-Status
running = False
lock = threading.Lock()

def auto_press():
    while True:
        with lock:
            if running:
                for key in keys:
                    # press all buttons
                    try:
                        pyautogui.keyDown(key)
                    except Exception as e:
                        print(f"Error at {key} (keyDown): {e}")

                # let go of all buttons
                for key in keys:
                    try:
                        pyautogui.keyUp(key)
                    except Exception as e:
                        print(f"Error at {key} (keyUp): {e}")
                pyautogui.keyDown(key_to_press)
                pyautogui.keyUp(key_to_press)
        time.sleep(Interval)

def toggle_running():
    global running
    while True:
        keyboard.wait(toggle_key)
        with lock:
            running = not running
            print("Started" if running else "stopped")

def exit_on_esc():
    keyboard.wait('esc')
    print("\nClosing Program...")
    root.destroy()
    root.quit()

root = tk.Tk()
root.withdraw()

# Start threads
threading.Thread(target=auto_press, daemon=True).start()
threading.Thread(target=toggle_running, daemon=True).start()
threading.Thread(target=exit_on_esc, daemon=True).start()

print("Press 'p' to Start/Stop. Press 'ESC' to close.")

# Tkinter-Mainloop
root.mainloop()