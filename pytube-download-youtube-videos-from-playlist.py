from pytube import YouTube
from pytube import Playlist

#where to save
SAVE_PATH = "Dowloads/WhaamBhaam videos" #to_do

playlist = Playlist('https://www.youtube.com/watch?v=0XJLsFTyeJk&list=PLuzoIVkUK-eWWioDxXTNDTkN8EoeFtrg0')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for url in playlist.video_urls:
    try:
		
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(url)
    except:
    
        #to handle exception
        print("Connection Error")

    #filters out all the files with "mp4" extension
    mp4files = yt.streams.filter(res='720p', file_extension='mp4')

    # get the video with the extension and
    # resolution passed in the get() function
    #d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
    try:
        # downloading the video
        mp4files.first().download(SAVE_PATH)
    except:
        print("Some Error!")
print("Task Completed!")