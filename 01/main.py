# 01 연예인 사진 모으기 프로젝트
import requests
import json

# 이미지를 파일로 저장
def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)

# 이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization" : "KakaoAK 6eada6849b8e4f98296fdb6bbd408277"
}
data = {
    "query" : "김태리"
}

# 이미지 검색 요청
response = requests.post(url, data=data, headers=headers)

if response.status_code != 200:
    print("error! because ", response.json())
else:
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image_url =", image_info['image_url'])
        count = count+1
        file_name = "test_%d.jpg" % (count)
        save_image(image_info['image_url'], file_name)