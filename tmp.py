#from pytubefix import YouTube

#url = "https://www.youtube.com/watch?v=maXsM_NFTFo"
#yt = YouTube(url, client="WEB")#, use_po_token=False, use_oauth=True, allow_oauth_cache=True
#print("title:", yt.title)
#print("author:", yt.author)
#print("desc:", yt.description)
#print("views:", yt.views)
#print("likes:", yt.likes)
#print("length:", yt.length)
#print("date:", yt.publish_date)

import pytubefix as pt

#print(pt.Channel('www.youtube.com/@justanoval').videos[0].likes)
#print(pt.Channel('www.youtube.com/@justanoval').videos)
channel = pt.Channel('www.youtube.com/@justanoval')
#print(channel.videos[1])
print(channel.videos[0].likes)
