import json
from facebook_scraper import get_posts, set_noscript
from facebook_scraper import get_group_info

ginfo = get_group_info("VenomousAndOtherSnakesOfSiam")
print(ginfo['id'])

listposts=[]

posts = get_posts(post_urls=["ใสโพสต์ที่ต้องการดึง"], credentials=('email_facebook','password_facebook'), options={"comments":True})

for post in posts:
    with open('fb.json', 'a', encoding='utf-8') as f:
        json.dump(post, f, ensure_ascii=False, default=str)
        f.write("\n")
    print(post['post_text'])
    for cmt in post['comments_full']:
        print(cmt['commenter_name']," : ", cmt['comment_text'].replace("\n",""))