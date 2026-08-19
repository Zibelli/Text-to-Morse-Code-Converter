# Text‑to‑Morse‑Code Converter

Small Flask web application that converts plain text into Morse code.

## Overview

This small utility demonstrates how to map characters to their Morse code
representations and display the result in a web interface.

## Features

- Convert ASCII text to Morse code.
- Support for letters, digits, and a handful of punctuation marks.
- Simple web interface.
- Unit tests included.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --require-hashes -r requirements.txt
```

The current dependency set requires Python 3.10 or newer.

`requirements.in` contains the direct dependency. Regenerate the hashed lock
file after reviewing dependency updates:

```bash
python -m pip install pip-tools
pip-compile --generate-hashes --strip-extras requirements.in
```

## Run locally

Start the local development server without debug mode:

```bash
python -m flask --app main run
```

Debug mode must only be enabled explicitly on a trusted development machine:

```bash
python -m flask --app main run --debug
```

Do not use Flask's built-in development server or debugger in production.
Deploy the `main:app` WSGI application with an appropriate production server
and enforce request and rate limits at the hosting layer.

## Project Structure

```
main.py          # Flask application and WSGI entry point
README.md        # This file
requirements.in  # Direct dependency declaration
requirements.txt # Fully pinned dependency set with hashes
static/
	css/
		style.css
templates/
	index.html
tests/
	test_app.py
```

## Contributing

Feel free to open issues or pull requests. Please run the tests before
submitting:

```bash
python -m unittest discover -s tests
```

## License

MIT License – see the [LICENSE](LICENSE) file.
