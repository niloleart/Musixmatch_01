from elasticsearch import Elasticsearch
import requests


def insert_es(elastic, ids, list_artist_name, list_track_id, list_track_name, list_lyrics):
    res = elastic.index(index='musix', doc_type='lyrics', id=ids, body={
        'artist': list_artist_name,
        'track-id': list_track_id,
        'track-name': list_track_name,
        'lyrics': list_lyrics,
    })
    print(res['created'])
