import json
import pprint
from elasticsearch import Elasticsearch
import requests
import Functions


def insert_es(elastic, ids, list_artist_name, list_track_id, list_track_name, list_lyrics):
    res = elastic.index(index='musix', doc_type='lyrics', id=ids, body={
        'artist': list_artist_name,
        'track-id': list_track_id,
        'track-name': list_track_name,
        'lyrics': list_lyrics,
    })
#    if res['created'] or res['result'] == 'updated':
#        print ("S'ha afegit correctament a la base de dades")
#    else:
#        print ("Sembla que hi ha hagut un problema!\nTorna a provar-ho.")


def search_artist(elastic, index, artista):
    res = elastic.search(index=index, doc_type="lyrics", body={"query": {"match": {"artist": artista}}})
    Functions.print_search(res)


def search_id(elastic, index, ids):
    res = elastic.search(index=index, doc_type="lyrics", body={"query": {"match": {"track-id": ids}}})
    Functions.print_search(res)


def search_track(elastic, index, track):
    res = elastic.search(index=index, doc_type="lyrics", body={"query": {"match": {"track-name": track}}})
    Functions.print_search(res)


def search_lyrics(elastic, index, lyrics):
    res = elastic.search(index=index, doc_type="lyrics", body={"query": {"match": {"lyrics": lyrics}}})
    Functions.print_search(res)