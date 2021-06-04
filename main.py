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

        # Create entry fields
        self.link_entry = tk.Entry(master=self.window, width=60)
        self.link_entry.grid(column=1, row=0)
        self.link_entry = tk.Entry(master=self.window, width=60)
        self.link_entry.grid(column=1, row=1)
        self.link_entry = tk.Entry(master=self.window, width=60)
        self.link_entry.grid(column=1, row=2)
        self.link_entry = tk.Entry(master=self.window, width=60)
        self.link_entry.grid(column=1, row=3)

        # Download button
        self.download_button = tk.Button(self.window, text='Submit', command=self.__get_link)
        self.download_button.grid(column=1, row=4)

        return

    def downloader(self, link, save_path='', save_name='', extension='mp4'):
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first()
        yt.streams.download(output_path=save_path, filename=save_name)

        return

    def __get_link(self):
        playsound(BUTTON_CLICK_SOUND)
        link = self.link_entry.get()
        path = self.link_entry.get()
        name = self.link_entry.get()
        ext = self.link_entry.get()

        self.downloader(link, path, name, ext)

        return

    def run_app(self):
        self.window.mainloop()
        return


if __name__ == '__main__':
    app = YouTubeDownloader()
    app.run_app()
