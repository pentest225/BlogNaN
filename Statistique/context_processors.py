import requests
import json
from . import models

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if ip == '127.0.0.1':
        ipify = 'http://api.ipify.org/?format=json'
        try :
            requette=requests.get(ipify)
            if requette.status_code == 200:
                donne = json.loads(requette.text)
                ip=donne['ip']
        except:
            print('error getting local ip')
    url = "https://ipapi.com/ip_api.php?ip={}"
    try:
        req = requests.get(url.format(ip))
        if req.status_code == 200 :
            data = json.loads(req.text)
            latitude = data['latitude']
            longitude = data['longitude']
            pays = data['country_name']
            ville = data['city']
            continent = data['continent_name']
            reseau = data['connection']['isp']
            client = models.Client(
                ip=ip,
                pays=pays,
                ville=ville,
                continent=continent,
                reseau=reseau,
                latitude=latitude,
                longitude=longitude,
                page=request.path,
            )
            client.save()
    except :
        print('error')
    return {'ip':ip}