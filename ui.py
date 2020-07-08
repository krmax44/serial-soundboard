import tkinter as tk
import tkinter.font as font
from soundboard import all_sounds, play_sound


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        large_font = font.Font(size=20)

        sounds = all_sounds()
        soundnames = sorted(map(lambda s: s.split(".")[0], sounds))

        for sound in soundnames:
            command = lambda sound=sound: play_sound(sound)
            button = tk.Button(self, text=sound, command=command)
            button["font"] = large_font
            button.pack(side="left")
            self.buttons.append(button)

        self.quit = tk.Button(self, text="QUIT", command=self.master.destroy)
        self.quit.pack(side="bottom")


def start_ui():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    start_ui()
