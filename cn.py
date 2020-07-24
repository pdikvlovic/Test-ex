import requests

def convertW(data):

    output_dict = {}

    for k in range(len(data)):
        pressure = float(data[k]['pres'])
        pres = round(pressure * 0.75006376, 1)
        output_el = {'ts': data[k]['ts'],'temp': data[k]['temp'], 'rh': data[k]['rh'],
                     'pres': pres, 'pop': data[k]['pop']}
        date_key = int(data[k]['ts'])
        output_dict[date_key] = output_el

    return output_dict

def getWeather():
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"
    querystring = {"units": "M", "lang": "en", "lat": "57.62987", "lon": "39.87368"}
    headers = {
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
        'x-rapidapi-key': "74f54d1760msh812cda59ce42da2p16e44bjsn1a82dd53210c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = convertW(response.json()['data'])
    return data