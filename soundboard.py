from playsound import playsound
from os import path, getcwd, listdir
import serial, time, sys, argparse

BASEPATH = getcwd()
SOUNDSPATH = path.join(BASEPATH, './sounds/')
last_play = 0

def all_sounds():
    return [f for f in listdir(SOUNDSPATH) if path.isfile(path.join(SOUNDSPATH, f))]

def play_sound(sound):
    location = path.join(BASEPATH, './sounds/', sound + '.mp3')
            
    if path.isfile(location):
        playsound(location, False)
        last_play = time.time()
    else:
        print('The serial interface requested a sound that does not exist.', sound)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arduino-controlled soundboard.')
    parser.add_argument('port', type=str, help='Serial port')
    parser.add_argument('-r', '--rate', type=int, required=False, help='Baud rate')
    args = parser.parse_args()

    try:
        with serial.Serial(args.port, args.rate or 9600) as ser:
            while True:
                data = ser.readline()  
                
                if time.time() - last_play < 0.1:
                    continue

                sound  = data.decode().strip()
                play_sound(sound)

    except serial.serialutil.SerialException:
        print("Error: can't connect to serial port.")
        exit(1)
