# Serial Soundboard

Simple soundboard designed to be controlled by a serial interface.

## Usage

Clone the repo or download the [archive](https://github.com/krmax44/serial-soundboard/archive/main.zip). Then, install using:

```bash
python3 -m venv .venv
pip install -r requirements.txt
```

Create a folder `sounds` and put your sound files into it. At the moment, only `.mp3` files are supported. Start the program:

```bash
python3 soundboard.py <PORT> [--rate <RATE>]
```

Here, `<PORT>` is your serial port (like `/dev/ttyS0` or `COM1`). Optionally, you can specify a baud rate using the `--rate` flag. To trigger a sound, send its filename (without the extension) via serial, with a newline afterwards.

There is also a simple GUI available, that doesn't require a serial connection. To start it, open:

```bash
python3 ui.py
```