import os
import getpass
from colorama import Fore, Style, init

init(autoreset=True)

user = getpass.getuser()

print(Fore.CYAN + f"Welcome {user} to PyShell 3.0!")
print(Fore.YELLOW + "Type 'exit' to quit or 'help' for commands.\n")

while True:
    current_dir = os.getcwd()
    cmd = input(Fore.GREEN + f"{user}@PyShell {current_dir}> " + Style.RESET_ALL).strip().lower()

    if cmd == "exit":
        print(Fore.RED + "Exiting PyShell..." + Style.RESET_ALL)
        break

    elif cmd == "clear":
        os.system("cls" if os.name == "nt" else "clear")

    elif cmd.startswith("cd "):
        path = cmd[3:].strip()
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(Fore.RED + f"No such directory: {path}")
        continue

    elif cmd == "help":
        print(Fore.CYAN + """
Available commands:
  cd [path]        - change directory
  clear            - clear terminal
  color            - change terminal color
  youtube/google   - open websites
  notepad/calc     - open apps
  exit             - quit
""")

    elif cmd == "youtube":
        os.system("start https://www.youtube.com" if os.name == "nt" else "xdg-open https://www.youtube.com")

    elif cmd == "google":
        os.system("start https://www.google.com" if os.name == "nt" else "xdg-open https://www.google.com")

    elif cmd == "notepad":
        os.system("notepad" if os.name == "nt" else "gedit")

    elif cmd == "calc":
        os.system("calc" if os.name == "nt" else "gnome-calculator")

    elif cmd == "color":
        color_code = input("Enter color code (e.g., 0A): ").upper()
        os.system(f"color {color_code}")

    else:
        # run system command directly
        os.system(cmd)
