import yt_dlp
try:
    video_url = input("Enter YouTube Video URL: ")
    destination = input("Enter destination folder path: ")
    ydl_opts = {
        'outtmpl': destination + '/%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("✅ Video Downloaded Successfully!")
except Exception as e:
    print("❌ Error:", e)
    print("Please enter a valid YouTube link.")