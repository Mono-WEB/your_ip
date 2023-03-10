import requests
from pyfiglet import Figlet
import folium


def get_ip_address(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            'IP ': response.get('query'),
            'Provider ': response.get('isp'),
            'Org ': response.get('org'),
            'Country ': response.get('country'),
            'Region ': response.get('regionName'),
            'City ': response.get('city'),
            'Zip ': response.get('zip'),
            'Lat ': response.get('lat'),
            'Lon ': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f"{response.get('query')}_{response.get('country')}.html")

    except requests.exceptions.ConnectionError:
        print('ConnectionError')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText(text='Your IP address'))
    ip = input('Enter your ip address: ')
    get_ip_address(ip=ip)


if __name__ == '__main__':
    main()