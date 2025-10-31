import os
import sys
import tkinter as tk
from PIL import Image, ImageDraw

def get_int(prompt, min_value=None, max_value=None):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if (min_value is not None and v < min_value) or (max_value is not None and v > max_value):
                print("Value out of range. Try again.")
                continue
            return v
        except ValueError:
            print("Please enter a valid integer.")

def capture_signature(save_path="signature.png", canvas_size=(600,200), pen_width=3):
    """
    Opens a Tk window where the user can draw with the mouse.
    Saves the drawing to save_path and returns True if saved.
    """
    
    img = Image.new("RGB", canvas_size, "white")
    draw = ImageDraw.Draw(img)

    root = tk.Tk()
    root.title("Draw your signature - Close window when done")

    canvas = tk.Canvas(root, width=canvas_size[0], height=canvas_size[1], bg="white", cursor="cross")
    canvas.pack()

    last_x, last_y = None, None

    def on_button_press(event):
        nonlocal last_x, last_y
        last_x, last_y = event.x, event.y

    def on_move(event):
        nonlocal last_x, last_y
        x, y = event.x, event.y
        if last_x is not None and last_y is not None:
            # draw on tkinter canvas
            canvas.create_line(last_x, last_y, x, y, width=pen_width, capstyle=tk.ROUND, smooth=True)
            # also draw on PIL image
            draw.line((last_x, last_y, x, y), fill="black", width=pen_width)
        last_x, last_y = x, y

    def on_button_release(event):
        nonlocal last_x, last_y
        last_x, last_y = None, None

    # optional: a "Clear" button to redraw
    def clear_canvas():
        canvas.delete("all")
        draw.rectangle([(0,0), canvas_size], fill="white")

    def save_and_close():
        try:
            img.save(save_path)
            print(f"Signature saved to: {os.path.abspath(save_path)}")
        except Exception as e:
            print("Error saving signature:", e)
        root.destroy()

    canvas.bind("<ButtonPress-1>", on_button_press)
    canvas.bind("<B1-Motion>", on_move)
    canvas.bind("<ButtonRelease-1>", on_button_release)

    btn_frame = tk.Frame(root)
    btn_frame.pack(fill="x", pady=4)
    tk.Button(btn_frame, text="Clear", command=clear_canvas).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Save & Close", command=save_and_close).pack(side="right", padx=5)
    root.mainloop()
    return os.path.exists(save_path)

def bank_menu():
    while True:
        print("\nWelcome to the bank! 🏦")
        print("1. Bank Account opening")
        print("2. Money deposit")
        print("3. Credit Card appeal")
        print("4. Exit")

        choice = get_int("Select from above (1-4): ", 1, 4)

        if choice == 1:
            print("\nWelcome to the bank account opening!")
            form = input("Would you like to fill the form? (yes/no): ").strip().lower()
            if form == "yes":
                name = input("Enter your name: ").strip()
                age = get_int("Enter your age: ", 0, 120)
                print("Now you'll draw your signature in a new window.")
                saved = capture_signature(save_path=f"{name.replace(' ', '_')}_signature.png")
                if saved:
                    print(f"Okay everything done!\nYour name: {name}\nYour age: {age}\nSignature file saved as: {name.replace(' ', '_')}_signature.png")
                else:
                    print("Signature was not saved.")
            else:
                print("Form skipped.")
        elif choice == 2:
            print("Money deposit feature not implemented yet.")
        elif choice == 3:
            print("Credit Card appeal feature not implemented yet.")
            print("bad!")
        elif choice == 4:
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    try:
        from PIL import Image, ImageDraw  
    except Exception:
        print("This program needs Pillow. Install it with: pip install pillow")
        sys.exit(1)

    bank_menu()


