import requests

#crime_list = 'rape, murder, infanticide, kidnapping, abduction, foeticide, suicide, prostitution'.split(',')
crime_list = 'rape'
#city_list = 'Mumbai, Delhi, Bangalore, Hyderabad, Chennai, Kolkata, Jaipur, Lucknow, Bhopal, Patna, Kanpur, Agra, Varanasi, Amritsar, Ranchi, Chandigarh, Gurgaon, Ujjain, Udaipur'.split(',')
city_list = 'Delhi'
#pollution_list = 'air, soil, water, thermal, light'.split(',')
pollution_list = 'air'
start_time = 1356978600000
end_time = 1420050600000

def extract_news():
    d = {}
    for cityName in city_list:
        d['city'] = cityName
        d['results'] = {}
        for crime in crime_list:
            url = 'http://access.alchemyapi.com/calls/data/GetNews?apikey=5a529c8f8ac1cff1f341a7492f7ecf88dce19a59&return=enriched.url.title%2Cenriched.url.url&start=1356978600000&end=1420050600000&q.enriched.url.enrichedTitle.entities.entity=%7Ctext={inputCity},type=city%7C&q.enriched.url.concepts.concept.text={crimeType}&outputMode=json'.format(inputCity=cityName, crimeType=crime)
            r = requests.get(url).json()
            d['results']['crime'] = r
        for pollution in pollution_list:
            url = 'http://access.alchemyapi.com/calls/data/GetNews?apikey=5a529c8f8ac1cff1f341a7492f7ecf88dce19a59&return=enriched.url.title%2Cenriched.url.url&start=1356978600000&end=1420050600000&q.enriched.url.enrichedTitle.entities.entity=%7Ctext={inputCity},type=city%7C&q.enriched.url.concepts.concept.text={pollutionType}&outputMode=json'.format(inputCity=cityName, pollutionType=pollution)
            r = requests.get(url).json()
            d['results']['pollution'] = r
    print d

extract_news()
