from pytube import YouTube

url = input('Youtube video URL here: ')
my_video = YouTube(url)

############################# Video Title #############################
# Get Video Title
print(my_video.title)

############################# Youtube video Tumbnail Image #############################
# Get Youtube video Thumbnail
print(my_video.thumbnail_url)

############################# Download Youtube video #############################
# Get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

# Set stream resolution
my_video = my_video.streams.get_highest_resolution()

# Or
# my_video = my_video.streams.first()

# Download video
my_video.download()