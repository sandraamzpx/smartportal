import os
import subprocess
import json
from pathlib import Path

class SmartPortal:
    def __init__(self):
        self.shortcuts_file = Path("shortcuts.json")
        self.shortcuts = self.load_shortcuts()

    def load_shortcuts(self):
        if self.shortcuts_file.exists():
            with open(self.shortcuts_file, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_shortcuts(self):
        with open(self.shortcuts_file, 'w') as f:
            json.dump(self.shortcuts, f, indent=4)

    def add_shortcut(self, name, path, launch_on_startup=False):
        self.shortcuts[name] = {'path': path, 'launch_on_startup': launch_on_startup}
        self.save_shortcuts()

    def remove_shortcut(self, name):
        if name in self.shortcuts:
            del self.shortcuts[name]
            self.save_shortcuts()

    def launch_application(self, name):
        if name in self.shortcuts:
            app_path = self.shortcuts[name]['path']
            if os.path.exists(app_path):
                subprocess.Popen(app_path)
                print(f"Launched {name}")
            else:
                print(f"Application path for {name} not found.")
        else:
            print(f"No shortcut found for {name}.")

    def configure_startup(self):
        startup_folder = Path(os.getenv('APPDATA')) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
        for name, details in self.shortcuts.items():
            shortcut_path = startup_folder / f"{name}.lnk"
            if details['launch_on_startup']:
                if not shortcut_path.exists():
                    # Create a shortcut if it doesn't exist
                    self.create_shortcut(details['path'], shortcut_path)
            else:
                if shortcut_path.exists():
                    # Remove the shortcut if it exists
                    os.remove(shortcut_path)

    def create_shortcut(self, target, shortcut_path):
        # Use Python's ctypes or other library to create a .lnk file
        # This is a placeholder for the actual shortcut creation logic
        print(f"Creating shortcut for {target} at {shortcut_path}")

    def list_shortcuts(self):
        return self.shortcuts.keys()

if __name__ == "__main__":
    portal = SmartPortal()
    portal.add_shortcut("Notepad", "C:\\Windows\\System32\\notepad.exe", launch_on_startup=True)
    portal.launch_application("Notepad")
    portal.configure_startup()
    print("Available shortcuts:", list(portal.list_shortcuts()))