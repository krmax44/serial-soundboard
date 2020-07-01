import tkinter as tk
import tkinter.font as font
import soundboard

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        large_font = font.Font(size=20)

        sounds = soundboard.all_sounds()
        soundnames = sorted(map(lambda s: s.split('.')[0], sounds))
        
        for sound in soundnames:
            command = lambda sound = sound: soundboard.play_sound(sound)
            button = tk.Button(self, text = sound, command = command)
            button['font'] = large_font
            button.pack(side='left')
            self.buttons.append(button)

        self.quit = tk.Button(self, text='QUIT', command=self.master.destroy)
        self.quit.pack(side='bottom')

root = tk.Tk()
app = Application(master=root)
app.mainloop()