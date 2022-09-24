from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def authorization(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
            }

    def _get_upload_link(self, path):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.authorization()
        params = {"path": path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self._get_upload_link(path=file_path).get("href", "")
        response = requests.put(href, data=open('text.txt', 'rb'))
        return response.status_code


def smartest_superhero():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    iq = 0
    for i in response.json():
        if i['name'] in ['Hulk', 'Captain America', 'Thanos']:
            if iq < i['powerstats']['intelligence']:
                iq = i['powerstats']['intelligence']
                iq_belongs = i['name']
    print(f"Самый умный: {iq_belongs} со значением: {iq}")


#smartest_superhero()

with open('my_token.txt', 'rt') as f:
    f_token = f.readline()

path_to_file = "text.txt"
token = f_token
uploader = YaUploader(token)
result = uploader.upload(path_to_file)
print(result)