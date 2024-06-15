import instaloader
import pandas as pd
from datetime import datetime

L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, 'medecinsdumonde')
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)


posts_data = []
for post in profile.get_posts():
    post_date = post.date
    if start_date <= post_date <= end_date:
        post_info = {
            'date': post_date,
            'url': f"https://www.instagram.com/p/{post.shortcode}/",
            'media_url': post.url,
            'media_type': 'Video' if post.is_video else 'Image',
            'likes': post.likes,
            'comments': post.comments,
            'caption': post.caption
        }
        posts_data.append(post_info)


df = pd.DataFrame(posts_data)
df.to_csv('mdm_posts.csv', index=False)

print("Les données sont sauvegardées")
