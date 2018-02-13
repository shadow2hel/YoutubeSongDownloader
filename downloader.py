from pytube import YouTube
import os
import moviepy.editor as mp
import time

if not os.path.exists("downloads/"):
    os.makedirs("downloads/")

if not os.path.exists("mp3s/"):
    os.makedirs("mp3s/")

def convert_to_mp3(file):
    clip = mp.VideoFileClip(file)
    clip.audio.write_audiofile(file+ ".mp3")
    del clip.reader
    del clip

def get_urls() -> list:
    with open("urls.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content

links = get_urls()

if links == []:
    print("You need to put links in the urls.txt file!")
    exit()

for yts in links:
    new_yts = YouTube(yts)
    print("Downloading ", new_yts.title, "...")
    video = new_yts.streams.get_by_itag(18).download('downloads/')
    print("Completed")

for file in os.listdir("downloads/"):
    if file.endswith(".mp4"):
        print("Converting ", file, " to MP3..")
        mp3 = convert_to_mp3("downloads/" + file)

mp3s = os.listdir("downloads/")

for mp3 in mp3s:
    if mp3.endswith(".mp3"):
        new_mp3 = mp3.replace(".mp4", "")
        print("Moving " + new_mp3 + " to the mp3 folder..")
        if os.path.isfile("mp3s/" + new_mp3):
            print("File already there!")
            continue
        else:
            os.rename("downloads/" + mp3, "mp3s/" + new_mp3)

for rm in os.listdir("downloads/"):
    os.remove("downloads/" + rm)
