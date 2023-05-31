import praw
import requests
import threading
import os

reddit = praw.Reddit(client_id='w7LPuTDQ5325fNf9HvrN4A',
                     client_secret='iOA7-J3ayNVADtrICqAGxang6Zrasw',
                     user_agent='Scrapper 1.0')

subreddits = ['PussyFlashing', 'pussy', 'Fingering','FingeringHerself','IndianBabes','Innie','simps','GodPussy','BreakingTheSeal']
num_posts = 1000

def download_media(subreddit_name):
    folder_name = subreddit_name
    os.makedirs(folder_name, exist_ok=True)

    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.top(limit=num_posts)

    for post in posts:
        media_url = post.url
        file_extension = os.path.splitext(media_url)[1].lower()
        if file_extension in ['.gif']:
            media_data = requests.get(media_url).content
            media_name = post.id + file_extension
            media_path = os.path.join(folder_name, media_name)
            with open(media_path, 'wb') as media_file:
                media_file.write(media_data)
            print(f"Downloaded media: {media_name} from {subreddit_name}")

threads = []
for subreddit_name in subreddits:
    thread = threading.Thread(target=download_media, args=(subreddit_name,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("All media downloaded.")