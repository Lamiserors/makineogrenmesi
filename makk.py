from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime


API_KEY = "AIzaSyCNJz5DlaNqR1rWNhD6p8jVA5ld-Nsn76c"  
youtube = build("youtube", "v3", developerKey=API_KEY)


channel_id = "UCpko_-a4wgz2u_DgDgd9fqA"


def get_channel_info(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    response = request.execute()
    channel_info = []
    for item in response["items"]:
        data = {
            "Channel Name": item["snippet"]["title"],
            "Subscribers": int(item["statistics"].get("subscriberCount", 0)),
            "Views": int(item["statistics"].get("viewCount", 0)),
            "Total Videos": int(item["statistics"].get("videoCount", 0)),
            "Channel ID": channel_id,
        }
        channel_info.append(data)
    return channel_info


def get_all_videos(youtube, channel_id):
    all_videos = []
    next_page_token = None

    while True:
       
        request = youtube.search().list(
            part="id",
            channelId=channel_id,
            maxResults=50,
            type="video",
            pageToken=next_page_token
        )
        response = request.execute()

        
        video_ids = [item["id"]["videoId"] for item in response.get("items", [])]
        if video_ids:
            video_request = youtube.videos().list(
                part="snippet,statistics,contentDetails",
                id=",".join(video_ids)
            )
            video_response = video_request.execute()

            for video in video_response.get("items", []):
                published_at = video["snippet"]["publishedAt"]
                published_date = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")

                views = int(video["statistics"].get("viewCount", 0))
                likes = int(video["statistics"].get("likeCount", 0))
                comments = int(video["statistics"].get("commentCount", 0))

               
                video_age_days = max((datetime.utcnow() - published_date).days, 1)

                
                interaction_rate = (likes + comments) / views if views > 0 else 0
                daily_views = views / video_age_days
                daily_likes = likes / video_age_days

                video_data = {
                    "Video Title": video["snippet"]["title"],
                    "Video ID": video["id"],
                    "Published Date": published_at,
                    "Video Age (Days)": video_age_days,
                    "Views": views,
                    "Likes": likes,
                    "Comments": comments,
                    "(Likes + Comments) / Views": round(interaction_rate, 4),
                    "Daily Views": round(daily_views, 2),
                    "Daily Likes": round(daily_likes, 2),
                }
                all_videos.append(video_data)

       
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return all_videos

channel_info = get_channel_info(youtube, channel_id)
channel_df = pd.DataFrame(channel_info)


all_videos_data = get_all_videos(youtube, channel_id)
video_df = pd.DataFrame(all_videos_data)


channel_df.to_csv("youtube_channel_info.csv", index=False)
video_df.to_csv("youtube_video_info.csv", index=False)

print(f"Kanal bilgileri başarıyla 'youtube_channel_info.csv' dosyasına kaydedildi!")
print(f"{len(all_videos_data)} video bilgisi başarıyla 'youtube_video_info.csv' dosyasına kaydedildi!")
