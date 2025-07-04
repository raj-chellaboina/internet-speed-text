# Internet Speed Text

A simple Python GUI application to check your internet speed (ping, download, upload) using Tkinter and Speedtest.

## Features

- Check your current internet download and upload speeds
- View your ping (latency)
- Simple and attractive Tkinter interface
- Visual display with custom images/icons

## Requirements

- Python 3.x
- [speedtest-cli](https://pypi.org/project/speedtest-cli/)
- [textblob](https://pypi.org/project/textblob/)
- Tkinter (usually included with Python)
- Image files: `logo.png`, `top (1).png`, `main.png`, `button.png`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/raj-chellaboina/internet-speed-text.git
   cd internet-speed-text
   ```

2. **Install dependencies:**
   ```bash
   pip install speedtest-cli textblob
   ```

3. **Make sure all required image files are in the project directory.**

## Usage

Run the application with:
```bash
python main.py
```

Click the button in the GUI to check your internet speed.

## Notes

- If you get errors about missing images, ensure the image file paths in `main.py` are correct and use relative paths if possible.
- The GUI will display your ping, download, and upload speeds in Mbps.

## Screenshots

*(Add screenshots here if available)*

## License

This project is licensed under the MIT License.
