# SmartPortal

SmartPortal is a Python-based program that streamlines the launching of applications on Windows with optimized shortcut management and startup configurations.

## Features

- **Add Shortcuts**: Easily add applications to your list of managed shortcuts.
- **Remove Shortcuts**: Remove applications from your shortcut list with ease.
- **Launch Applications**: Quickly launch any application from your managed list.
- **Configure Startup**: Automatically configure applications to launch on Windows startup.
- **List Shortcuts**: View all applications currently managed by SmartPortal.

## Installation

1. Ensure you have Python installed on your system.
2. Clone the repository or download the `smartportal.py` file.
3. Run `smartportal.py` using Python.

```bash
python smartportal.py
```

## Usage

- **Adding a Shortcut**: To add a new application shortcut, use the `add_shortcut` method with the application name, path, and whether it should launch on startup.
- **Removing a Shortcut**: Use the `remove_shortcut` method with the application name to remove it from the list.
- **Launching an Application**: Use the `launch_application` method with the application name to start it.
- **Configuring Startup**: Run `configure_startup` to set up or remove shortcuts from the Windows startup folder.
- **Listing Shortcuts**: Use the `list_shortcuts` method to view all managed shortcuts.

## Example

Here's a quick example to get you started:

```python
portal = SmartPortal()
portal.add_shortcut("Notepad", "C:\\Windows\\System32\\notepad.exe", launch_on_startup=True)
portal.launch_application("Notepad")
portal.configure_startup()
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.