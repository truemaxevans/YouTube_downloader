from pytube import YouTube
from playsound import playsound
import tkinter as tk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 200
WINDOW_TITLE = 'YouTube downloader'
BUTTON_CLICK_SOUND = 'play'

class YouTubeDownloader:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.configure(bg='#a9dcd6')
        self.window.title(WINDOW_TITLE)

        # Create labels
        self.link_lable = tk.Label(self.window, text='Download link')
        self.link_lable.grid(column=0, row=0)
        self.link_lable = tk.Label(self.window, text='Save file as')
        self.link_lable.grid(column=0, row=1)
        self.link_lable = tk.Label(self.window, text='Save PATH')
        self.link_lable.grid(column=0, row=2)
        self.link_lable = tk.Label(self.window, text='File extension')
        self.link_lable.grid(column=0, row=3)

    def run_app(self):
        self.window.mainloop()
        return
if __name__ =='__main__':
    app = YouTubeDownloader()
    app.run_app()










