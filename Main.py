# coding=utf-8
from collections import deque

import DisplayChoices, Functions
### MAIN ###
choice = ''


DisplayChoices.display_title_bar()

while choice != 'q':
    choice = DisplayChoices.disp_choices()
    list_track_id = deque([])
    list_artists = deque([])
    list_track_names = deque([])
    if choice == '1':
        tracks = Functions.filtra_llengua(DisplayChoices.language_choice())
        for t in tracks:
            t = t.get('track')
            list_track_names.append((t.get('track_name')))
            list_track_id.append(t.get('track_id'))
            list_artists.append((t.get('artist_name')))
        lletres = Functions.search_lyrics(list_track_id)
        Functions.print_lletres(lletres)

    elif choice == '2':
        tracks = Functions.filtra_genere(DisplayChoices.genre_choice())
        for t in tracks:
            t = t.get('track')
            list_track_names.append((t.get('track_name')))
            list_track_id.append(t.get('track_id'))
            list_artists.append((t.get('artist_name')))
        lletres = Functions.search_lyrics(list_track_id)
        Functions.print_lletres(lletres)

    elif choice == '3':
        tracks = Functions.filtra_pais(DisplayChoices.country_choice())
        for t in tracks:
            t = t.get('track')
            list_track_names.append((t.get('track_name')))
            list_track_id.append(t.get('track_id'))
            list_artists.append((t.get('artist_name')))
        lletres = Functions.search_lyrics(list_track_id)
        Functions.print_lletres(lletres)

    elif choice == 'q':
        print("\nGràcies!!! Fins la propera :D")
        quit()

    else:
        print("\nDeus haver entrat alguna cosa malament! Torna a provar-ho siusplau :)\n")
print (list_track_id)
