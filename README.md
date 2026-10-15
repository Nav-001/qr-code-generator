# QR Code Generator

A simple Python application that generates QR codes from text or URLs and saves them as image files.

## Features

- Generates QR codes from user-provided text or URLs.
- Creates high-error-correction QR codes.
- Saves the generated QR code as a PNG image.
- Includes basic input validation.

## Technologies Used

- Python
- `qrcode` — QR code generation
- Pillow — image processing

## Installation

1. Make sure Python is installed.
2. Clone this repository or download the project files.
3. Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python qr_generator.py
```

Enter your text or URL when prompted. The generated QR code will be saved as `QR_Code.png` in the current working directory.

## Project Structure

```text
QR-Code-Generator/
├── qr_generator.py
├── requirements.txt
└── README.md
```

## What I Learned

- Using a Python library to generate QR codes.
- Accepting and validating user input.
- Saving generated images to a file.

## Future Improvements

- Allow users to choose QR code colors.
- Let users specify the output filename.
- Add a graphical user interface.

---

Built as a hands-on Python project.