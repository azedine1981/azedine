import pytube
yt=pytube.YouTube('https://www.youtube.com/watch?v=JkIZlGeRoR0&t')
video=yt.streams.get_lowest_resolution()
video.download()
print("téléchargement terminé")
