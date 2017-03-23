import json
import requests.packages.urllib3
import requests
from collections import deque
requests.packages.urllib3.disable_warnings()
api_key = "1f7a92f087232149093fe79f5ce0452b"


def filtra_llengua(llengua):
    response = requests.get("http://api.musixmatch.com/ws/1.1/track.search",
                            params={
                                'apikey': api_key,
                                'page_size': 2,
                                'page': 1,
                                's_track_rating': 'desc',
                                'f_lyrics_language': llengua,
                                'f_has_lyrics': 1
                            })
    response_data = response.json()
    message = response_data.get('message')
    body = message.get('body')
    tracklists = body.get('track_list')
    return tracklists


def filtra_pais(pais):
    response = requests.get("https://api.musixmatch.com/ws/1.1/chart.tracks.get",
                            params={
                                'apikey': api_key,
                                'page_size': 2,
                                'page': 1,
                                'country': pais,
                                'f_has_lyrics': 1
                            })
    response_data = response.json()
    message = response_data.get("message")
    body = message.get("body")
    tracklists = body.get('track_list')
    return tracklists


def filtra_genere(genere):
    response = requests.get("https://api.musixmatch.com/ws/1.1/track.search",
                            params={
                                'apikey': api_key,
                                'page_size': 2,
                                'page': 1,
                                's_track_rating': 'desc',
                                'f_has_lyrics': 1,
                                'f_music_genre_id': genere
                            })
    response_data = response.json()
    message = response_data.get("message")
    body = message.get("body")
    tracklists = body.get('track_list')
    return tracklists


def search_lyrics(id_list):
    for id_lyric in id_list:
        lyric = requests.get('https://api.musixmatch.com/ws/1.1/track.lyrics.get',
                             params={
                                 'apikey': api_key,
                                 'track_id': id_lyric
                             })
        try:
            response_lyric = lyric.json()
            lletra = response_lyric.get('message')
            cos = lletra.get('body')
            lletres = cos.get('lyrics')
            l = lletres.get('lyrics_body')
        except json.decoder.JSONDecoder:
            print ("Cannot Decode JSON")
    return l


def print_lletres(lletres):
    for ll in lletres:
        print(ll.encode('utf-8'))
        print ("\n\n")


def print_whole(list_track_id, list_artists, list_track_names, list_lyrics):
    for i in range(0, len(list_track_id), 1):
        print ""
        print ("TRACK ID: " + str(list_track_id[i]))
        print ("ARTIST: " + list_artists[i])
        print ("TRACK NAME: " + list_track_names[i])
        print ("LLETRA: \n" + list_lyrics[i])
        print ""