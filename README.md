# Serial Soundboard

![Python application](https://github.com/krmax44/serial-soundboard/workflows/Python%20application/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simple soundboard designed to be controlled by a serial interface. It also offers a minimal UI.

## Usage

Clone the repo or download the [archive](https://github.com/krmax44/serial-soundboard/archive/main.zip). Then, install using:

```bash
python3 -m venv .venv
pip install -r requirements.txt
```

Create a folder `sounds` and put your sound files into it. Start the program:

```bash
python3 soundboard.py [--port <PORT> --rate <RATE>]
```

Here, `<PORT>` is your serial port (like `/dev/ttyS0` or `COM1`). If you don't specify a port, the UI will open. Optionally, you can specify a baud rate using the `--rate` flag. All options can be listed via the `--help` flag.

To trigger a sound, send its filename (with or without the extension) via serial, with a newline afterwards.

