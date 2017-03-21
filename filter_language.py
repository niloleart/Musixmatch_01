import json
import requests
from collections import deque
api_key = "1f7a92f087232149093fe79f5ce0452b"
language = 'ca'
track_id_list = deque([])
artist_list = deque([])
album_list = deque([])
track_list = deque([])
lyrics_list = deque([])

response = requests.get("http://api.musixmatch.com/ws/1.1/track.search",
                        params={
                            'apikey': api_key,
                            'page_size': 5,
                            'page': 1,
                            's_track_rating': 'desc',
                            'f_lyrics_language': language,
                        })

try:
    response_data = response.json()
    message = response_data.get('message')
    body = message.get('body')
    tracklists = body.get('track_list')
    for t in tracklists:
        t = t.get('track')
        print('track_name: '+(t.get('track_name')).encode('utf-8'))
        track_list.append((t.get('track_name')).encode('utf-8'))

        print('track id {}'.format(t.get('track_id')))
        track_id_list.append(t.get('track_id'))

        print('artist_name: '+(t.get('artist_name')).encode('utf-8'))
        artist_list.append((t.get('artist_name')).encode('utf-8'))
        print('')


except json.decoder.JSONDecoder:
    print("Cannot Decode JSON")

for id_lyric in track_id_list:
    lyric = requests.get('https://api.musixmatch.com/ws/1.1/track.lyrics.get',
                         params={
                             'apikey': api_key,
                             'track_id': id_lyric
                         })
    try:
        response_lyric= lyric.json()
        lletra = response_lyric.get('message')
        cos = lletra.get('body')
        lletres = cos.get('lyrics')
        l=lletres.get('lyrics_body')
        lyrics_list.append(l)
#TODO guardar lletres en un fitxer
    except json.decoder.JSONDecoder:
        print ("Cannot Decode JSON")
print(lyrics_list)