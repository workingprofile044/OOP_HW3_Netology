import requests

url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    hero_intelligence = {}
    for hero in data:
        if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
            hero_intelligence[hero['name']] = int(hero['powerstats']['intelligence'])

    sorted_heroes = sorted(hero_intelligence.items(), key=lambda x: x[1], reverse=True)

    for hero in sorted_heroes:
        print(f"{hero[0]}: {hero[1]}")
else:
    print(f"Ошибка реквеста {response.status_code}")

if sorted_heroes:
    smartest_hero = sorted_heroes[0]
    print(f"Самый умный герой {smartest_hero[0]} с показателем интеллекта {smartest_hero[1]}")
else:
    print("Не найдено")


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        headers = {'Authorization': 'OAuth ' + self.token}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers=headers, params={'path': 'file.txt', 'overwrite': 'true'})
        href = response.json().get('href')
        with open(file_path, 'rb') as f:
            requests.put(href, data=f)


if __name__ == '__main__':
    path_to_file = r'C:\Users\NAME\Desktop\OOP_HW3\file.txt'
    token = 'y0_token'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
