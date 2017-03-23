from elasticsearch import Elasticsearch
import requests


def insert_es(list_artist_name, list_track_id, list_track_name, list_lyrics):
    ids = 1
    elastic = Elasticsearch()
    for ix in range(0, len(list_track_id), 1):
        res = elastic.index(index='test-index', doc_type='lyrics', id=ids, body={
            'artist': list_artist_name[ix],
            'track-id': list_track_id[ix],
            'track-name': list_track_name[ix],
            'lyrics': list_lyrics[ix],
        })
        ids += 1
        print(res['created'])
