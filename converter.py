import moviepy.editor
from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox as mb



# function to get only filename without the directory
def fmp4(filename):
    x = filename.rfind("/")
    y = filename.rfind('.mp4')
    return filename[(x + 1):(y + 4)]


# function to convert the mp4 file into mp3
def convert():
    filenames = askopenfilenames(title='Select files', filetypes=(('MP4', '.mp4'), ('All files', '.*')))

    filename = ''.join(filenames)
    # x is the filename without the directory
    x = fmp4(filename)
    # y is the name without the extension
    y = x[:-4]

    video = moviepy.editor.VideoFileClip(filename)
    audio = video.audio

    audio.write_audiofile(y + '.mp3')

    mb.showinfo("Success", "File successfully converted to MP4")

# end function




root = Tk()
root.title('Converter')

label1 = Label(root, text='Select Video to be converted to MP3', padx=20, pady=5).pack()

button1 = Button(root, text='Select', command=convert)
button1.pack()

button2 = Button(root, text='Quit', command=sys.exit)
button2.pack()

mainloop()
