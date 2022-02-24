



with open('text.txt') as claves: 
    keys = [clave for clave in claves]
    user = keys[0].replace('\n', '')



url = 'https://api.spotify.com/v1'

ep_artist = '/artist/{artist_id}'

id_dy = '4VMYDCV2IEDYJArk749S6m'

url_completa = url + ep_artist.format(artist_id=id_dy)


import requests

from requests_oauthlib import OAuth2Session


token_url = 'https://accounts.spotify.com/api/token'

params = {'grant_type' : 'client_credentials'}

headers = {'Authorization' : 'Basic ' + user}


r = requests.post(token_url, data = params, headers = headers)
r.json()    

my_token = r.json()['access_token']


header = {'Authorization' : 'Bearer {}'.format(my_token)}

r = requests.get(url + ep_artist.format(artist_id = id_dy), headers= header)
r.status_code
r.json()