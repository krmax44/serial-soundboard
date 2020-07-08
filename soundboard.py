from playsound import playsound
from os import path, getcwd, listdir
import serial, time, sys, argparse

BASEPATH = getcwd()
SOUNDSPATH = path.join(BASEPATH, "./sounds/")
SOUNDEXTS = (".mp3", ".flac", ".wav", ".aac", ".m4a", ".wma")
last_play = 0


def all_sounds():
    all_files = listdir(SOUNDSPATH)
    sounds = filter(
        lambda file: path.isfile(path.join(SOUNDSPATH, file))
        and file.endswith(SOUNDEXTS),
        all_files,
    )
    return list(sounds)


def play_sound(sound):
    for ext in ("", *SOUNDEXTS):
        location = path.join(SOUNDSPATH, sound + ext)

        if path.isfile(location):
            return playsound(location, False)

    print("The serial interface requested a sound that does not exist.", sound)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Serial-controlled soundboard.")
    parser.add_argument(
        "-p",
        "--port",
        type=str,
        required=False,
        help="Serial port. If unspecified, it opens the UI.",
    )
    parser.add_argument(
        "-r", "--rate", type=int, required=False, help="Baud rate. Defaults to 9600."
    )
    parser.add_argument(
        "-s",
        "--path",
        type=str,
        required=False,
        help="Path to sound folder. Defaults to ./sounds.",
    )
    args = parser.parse_args()

    if args.path:
        SOUNDSPATH = path.join(BASEPATH, args.path)

    if not args.port:
        from ui import start_ui

        start_ui()
    else:
        try:
            with serial.Serial(args.port, args.rate or 9600) as ser:
                while True:
                    data = ser.readline()

                    if time.time() - last_play < 0.1:
                        continue

                    sound = data.decode().strip()
                    play_sound(sound)

        except serial.serialutil.SerialException:
            print("Error: can't connect to serial port.")
            exit(1)
