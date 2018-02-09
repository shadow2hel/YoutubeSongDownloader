from pytube import YouTube
import moviepy.editor as mp
import os
import shutil

if not os.path.exists("downloads/"):
    os.makedirs("downloads/")


if not os.path.exists("mp3s/"):
    os.makedirs("mp3s/")

def convert_to_mp3(file):
    clip = mp.VideoFileClip(file)
    clip.audio.write_audiofile(file+ ".mp3")

print("Give some links yo:")
links = input()
ytvids = links.split(",")

for yt in ytvids:
    print("Downloading ", YouTube(yt).title, "...")
    YouTube(yt).streams.get_by_itag(18).download('downloads/')
    print("Completed")

for file in os.listdir("downloads/"):
    print("Converting ", file, " to MP3..")
    convert_to_mp3("downloads/" + file)
    os.remove("downloads/" + file)

mp3s = os.listdir("downloads/")
new_mp3s = [s.replace('.mp4', '') for s in mp3s]

for mp3 in mp3s:
    new_mp3 = mp3.replace(".mp4", "")
    print("Moving " + new_mp3 + " to the mp3 folder..")
    shutil.move("downloads/" + mp3, "mp3s/" + new_mp3)
