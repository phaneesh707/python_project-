from tkinter import *
import pygame
from tkinter import filedialog

root=Tk()
root.title('music player')
root.geometry('500x340')

#initialize pygame mixer
pygame.mixer.init()

#add song function
def add_song():
    song =filedialog.askopenfilename(initialdir="C:/",filetypes=(("mp3 Files","*.mp3"),))
    song=song_box.insert(END,song)

# def add_song1():
#     l="your favourite songs"
#     l=song_box.insert(TOP)
#     song = filedialog.askopenfilename(initialdir="C:/", filetypes=(("mp3 Files", "*.mp3"),))
#     song = song_box.insert(END, song)

#fuctions of button
def play():
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# create global paused variable
global paused
paused= False
def pause(is_paused):
    global paused
    paused=is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused = True


# create a playlist box
l=Label(text="Play List",bg="red",font="verdana",width=80,fg="black",bd=3)
l.pack()
song_box=Listbox(root,width=60,bg="grey",fg="black",selectbackground="#009EFA",selectforeground="black")
song_box.pack(pady=20)

# define player control buttons
play_btn_img=PhotoImage(file='C:/gui/audio/pl.png')
pause_btn_img=PhotoImage(file='C:/gui/audio/pau.png')
stop_btn_img=PhotoImage(file='C:/gui/audio/stop.png')

# create player control frame
control_frame=Frame(root)
control_frame.pack()

# create player control buttons
pause_btn=Button(control_frame,borderwidth=5,bg="#FA8E73",fg="yellow",text="pause",command=lambda: pause(paused),image=pause_btn_img)
play_btn=Button(control_frame,borderwidth=5,bg="#FA8E73",fg="yellow",text="play",command=play,image=play_btn_img)
stop_btn=Button(control_frame,borderwidth=5,bg="#FA8E73",fg="yellow",text="stop",command=stop,image=stop_btn_img)

play_btn.grid(row=0,column=2,padx=10)
pause_btn.grid(row=0,column=1,padx=10)
stop_btn.grid(row=0,column=3,padx=10)

# create menu
my_menu=Menu(root)
root.config(menu=my_menu)

# add "add song" menu
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="add songs",menu=add_song_menu)
add_song_menu.add_command(label="add song to playlist",command=add_song)

add_song2_menu=Menu(my_menu)
my_menu.add_cascade(label="add favourite song",menu=add_song2_menu)
add_song2_menu.add_command(label="add your favourite song",command=add_song)


root.mainloop()



