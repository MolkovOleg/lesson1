city_info = {"city": "Москва", "temperature": "20"}
city_info['temperature'] = int(city_info['temperature']) - 5
city_info.setdefault('country', 'Россия')
city_info['date'] = '27.05.2019'
print(city_info)