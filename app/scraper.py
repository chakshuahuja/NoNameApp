#!/usr/bin/env python

import requests
import json

def twt():
    crime_list = 'rape,murder,infanticide,kidnapping,abduction,foeticide,suicide,prostitution'.split(',')
    states_list = 'Andhra Pradesh,Arunachal Pradesh,Assam,Bihar,Chhattisgarh,Goa,Gujarat,Haryana,Himachal Pradesh,Jammu and Kashmir,Jharkhand,Karnataka,Kerala,Madhya Pradesh,Maharashtra,Manipur,Meghalaya,Mizoram,Nagaland,Odisha,Punjab,Rajasthan,Sikkim,Tamil Nadu,Telangana,Tripura,Uttar Pradesh,Uttarakhand,West Bengal,Andaman and Nicobar,Chandigarh,Dadra and Nagar Haveli,Daman and Diu,Lakshadweep,Delhi,Puducherry'.split(',')
    state_dict = {}
    master_arr = []

    for state in states_list:
        state_dict = {}
        for crime in crime_list:
            query = "%s+%s"%(state,crime)
            url = 'https://cdeservice.au-syd.mybluemix.net/api/v1/messages/search?q=%s&apikey=30178e702595f2673235ba51c42fd336cb48536c&username=37bb268a-ba58-49a2-8a82-95a182ae6f30&password=8UX1vvVmo9'%(query)
            r = requests.get(url).json()
            state_dict['crime'] = r
        for pollution in pollution_list:
            query = "%+%s"%(state,crime)
            url = 'https://cdeservice.au-syd.mybluemix.net/api/v1/messages/search?q=%s&apikey=30178e702595f2673235ba51c42fd336cb48536c&username=37bb268a-ba58-49a2-8a82-95a182ae6f30&password=8UX1vvVmo9'%(query)
            r = requests.get(url).json()
            state_dict['air_pollution'] = r
        master_arr.append(state_dict)

    with open('data/data.json','w+') as f:
        f.write(json.dumps(master_arr))

def test():
	state = 'delhi'
	crime = 'kidnapping'
	query = "%s+%s"%(state,crime)
	url = 'http://cdeservice.au-syd.mybluemix.net/api/v1/messages/search?q=%s&apikey=30178e702595f2673235ba51c42fd336cb48536c&username=37bb268a-ba58-49a2-8a82-95a182ae6f30&password=8UX1vvVmo9'%(query)
	print url
	return
	r = requests.get(url).json()
	print r

def dataCrunch():
    with open ('../data/pollution.json') as f:
        data1 = json.loads(f.read())['data']
    
    with open ('../data/pollution_.json') as f:
        data2 = json.loads(f.read())

    arr =[]
    for counter,obj in enumerate(data2):
        d = obj
        d['data'] = data1[counter]
        arr.append(d)

    with open('../data/master_pollution.json','w+') as f:
        f.write(json.dumps(arr))


if __name__ == '__main__':
	dataCrunch()
    #test()

