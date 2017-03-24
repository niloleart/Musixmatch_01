# coding=utf-8
from collections import deque
from elasticsearch import Elasticsearch
import DisplayChoices
import Functions
import ElasticSearch
### MAIN ###
choice = ''
es = Elasticsearch()
index = 'musix'
DisplayChoices.display_title_bar()
ids = 1

while choice != 5:
    aux = 0
    choice = DisplayChoices.disp_choices()
    list_track_id = deque([])
    list_artists = deque([])
    list_lyrics = deque([])
    list_track_names = deque([])
    if choice == 1:
        tracks = Functions.filtra_llengua(DisplayChoices.language_choice())
        for t in tracks:
            t = t.get('track')
            list_track_names.append((t.get('track_name')))
            list_track_id.append(t.get('track_id'))
            list_artists.append((t.get('artist_name')))
            list_lyrics.append(Functions.search_lyrics(list_track_id))

    elif choice == 2:
        tracks = Functions.filtra_genere(DisplayChoices.genre_choice())
        for t in tracks:
            t = t.get('track')
            list_track_names.append((t.get('track_name')))
            list_track_id.append(t.get('track_id'))
            list_artists.append((t.get('artist_name')))
            list_lyrics.append(Functions.search_lyrics(list_track_id))

    elif choice == 3:
        tracks = Functions.filtra_pais(DisplayChoices.country_choice())
        for t in tracks:
            t = t.get('track')
            list_track_names.append((t.get('track_name')))
            list_track_id.append(t.get('track_id'))
            list_artists.append((t.get('artist_name')))
            list_lyrics.append(Functions.search_lyrics(list_track_id))

    elif choice == 4:
        q_choice = DisplayChoices.disp_query_option()
        if q_choice == 1:
            q_choice = input("Quin ARTISTA vols buscar?\n")
            ElasticSearch.search_artist(es, index, q_choice)
        if q_choice == 2:
            q_choice = input("Quina CANÇÓ vols buscar?\n")
            ElasticSearch.search_track(es, index, q_choice)
        if q_choice == 3:
            q_choice = input("Introdueix alguna paraula que vulguis buscar a les nostres lletres\n")
            ElasticSearch.search_lyrics(es, index, q_choice)
        if q_choice == 4:
            q_choice = input("Introdueix una ID\n")
            ElasticSearch.search_id(es, index, q_choice)

    elif choice == 5:
        print("\nGràcies!!! Fins la propera :D")
        quit()

    else:
        aux = 1
        print("\nDeus haver entrat alguna cosa malament! Torna a provar-ho siusplau :)\n")

    if choice != 4 and aux == 0:
        choice_add_es = DisplayChoices.add_es_choice()
        if choice_add_es == 1:
            for x in range(0, len(list_artists), 1):
                ElasticSearch.insert_es(es, ids, list_artists[x], list_track_id[x], list_track_names[x], list_lyrics[x])
                ids += 1
        else:
            print ("No afegirem res doncs!")

    #Functions.print_whole(list_track_id, list_artists, list_track_names, list_lyrics)