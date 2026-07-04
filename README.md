# Text‑to‑Morse‑Code Converter

Python project that converts plain text into Morse code and vice‑versa.

## Overview

This small utility demonstrates how to map characters to their Morse code
representations and back again. It is written in pure Python and can be
run from the command line or imported as a library.

## Features

- Convert any ASCII string to Morse code.
- Decode Morse code back to text.
- Support for letters, digits, and a handful of punctuation marks.
- Simple command‑line interface.
- Unit tests included.

## Installation

```bash
python -m pip install -r requirements.txt
```

If you prefer to run the script directly without installing, just
execute:

```bash
python main.py
```

## Usage

```bash
# Convert text to Morse
python main.py "HELLO WORLD"

# Decode Morse
python main.py ".- .-.. .-.. --- / .-- --- .-. .-.. -.."
```

The script prints the result to stdout.

## Project Structure

```
main.py          # CLI entry point
README.md        # This file
static/
	css/
		style.css
templates/
	index.html
```

## Contributing

Feel free to open issues or pull requests. Please run the tests before
submitting:

```bash
python -m unittest discover
```

## License

MIT License – see the [LICENSE](LICENSE) file.
