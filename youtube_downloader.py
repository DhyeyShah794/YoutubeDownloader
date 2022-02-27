import pytube.exceptions
from pytube import YouTube
import os

url = str(input("URL: "))
location = str(input("Location: "))
file_name = str(input("Save as: "))
if "/" in file_name:
    print("The file name cannot contain '/'. Please enter a valid file name")
    file_name = str(input("Save as: "))
default_name = "Download"

yt = YouTube(url)
try:
    video = yt.streams.get_highest_resolution()
    print("Downloading...")
    video.download(output_path=location, filename=default_name)
    # Need to rename file separately because ↑ omits characters like "," and "."
    os.rename(location + "/Download.mp4", location + "/" + file_name + ".mp4")
    print("Download successful")
except pytube.exceptions.RegexMatchError:
    print("Invalid URL!")
