from pynput.mouse import Listener as MouseListener
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
import pyautogui, os

def main():
    mouse = MouseController()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    start = ()
    count = 0

    # --------------KEYBOARD-------------
    def on_press(key):
        nonlocal start, count
        print(f'{key} pressed')
        if key == Key.shift:
            print(f"Mouse position at {mouse.position} is recorded")
            start = mouse.position
        if key == Key.ctrl_l and start:
            print(f"""Image captured from {start} to {mouse.position} is save as screen_shot_{count}.png""")
            end = [mouse.position[i] - start[i] for i in range(2)]
            pyautogui.screenshot(region=(*start, *end)).save(f"{dir_path}/screen_shot_{count}.png")
            start = ()
            count += 1

        if key == Key.esc: # Stop listener
            return False

    def on_release(key):
        # print(f'{key} release')
        pass

    # --------------MOUSE-------------
    def on_move(x, y):
        # print(f"Mouse moved to ({x}, x{y})")
        pass

    def on_click(x, y, button, pressed):
        if pressed:
            print(f"Mouse clicked at ({x}, {y} with {button})")

    def on_scroll(x, y, dx, dy):
        print(f"Mouse scrolled at ({x}, {y}, {dx}, {dy})")

    with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        with KeyboardListener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

if __name__ == "__main__":
    main()