from time import sleep
import requests

session = requests.Session()
username = input("Username: ")
password = input("Password: ")

url = "https://www.instagram.com/accounts/login/ajax/"
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
"x-csrftoken": "flABydJVnZRJYaGedv2ItjmC9UI77bqW",
"mid": "xgDrB4ZsEzKAr1Tqyb5QlmbS2oa6JqCt"
}
data = {
"enc_password": "#PWD_INSTAGRAM_BROWSER:0:1651709336:" + password,
"username": username,
"queryParams": "{}",
"optIntoOneTap": "false",
}
data = session.post(url, headers=headers, data=data)
print(data.text)
if "userId" in data.text:
    session_id = data.cookies.get("sessionid")
    headers["cookie"] = f"sessionid={session_id}"
    print("Successfully Logged In")
    print("Enter The Person's Username")
    target = input(": ")
    target_info = requests.get(f"https://instagram.com/{target}/?__a=1")
    target_post = []
    timeline_media = target_info.json()["graphql"] ["user"] ["edge_owner_to_timeline_media"] ["edges"]
    for media in timeline_media:
        media_id = media["node"] ["id"]
        target_post.append (media_id)
        
    for post in target_post:
        like_endpoint = (f"https://www.instagram.com/web/likes/{post}/like/")
        response = session.post(like_endpoint, headers=headers)
        print(f"media_id: {post}")
        sleep(2)
    
    print("Finished.")

else:
    print("Incorrect Username/Password")