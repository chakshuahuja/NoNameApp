import requests
import json
import yaml
crime_list = 'rape, murder, kidnapping, suicide'.split(',')
#crime_list = 'rape'.split(',')
#city_list = 'Mumbai, Delhi, Bangalore, Chennai'.split(',')
city_list = 'Delhi'.split(',')
#pollution_list = 'air, soil, water, thermal, light'.split(',')
pollution_list = 'air, water'.split(',')
start_time = 1356978600000
end_time = 1420050600000

def extract_news():
    d = {}
    for cityName in city_list:
        d['city'] = cityName
        d['results'] = {}
        for crime in crime_list:
            url = 'http://7ce4d095-9333-4c2c-89cd-7ded64335236:bWWAXCPsOX@cdeservice.au-syd.mybluemix.net/api/v1/messages/search?q={crimeType}%26{inputCity}%size=1'.format(inputCity=cityName, crimeType=crime)
            r = requests.get(url).json()
            d['results']['crime'] = r
        for pollution in pollution_list:
            url = 'http://7ce4d095-9333-4c2c-89cd-7ded64335236:bWWAXCPsOX@cdeservice.au-syd.mybluemix.net/api/v1/messages/search?q={pollutionType}%26{inputCity}&size=1'.format(pollutionType=pollution, inputCity=cityName)
            r = requests.get(url).json()
            d['results']['pollution'] = r
        url = 'http://7ce4d095-9333-4c2c-89cd-7ded64335236:bWWAXCPsOX@cdeservice.au-syd.mybluemix.net/api/v1/messages/search?q=accident%26{inputCity}&size=1'.format(inputCity=cityName)
        r = requests.get(url).json()
        d['results']['accident'] = r
    print json.dumps(d)

extract_news()
