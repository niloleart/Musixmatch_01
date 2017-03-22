import programa, filters
### MAIN ###
programa.display_title_bar()
choice = ''
while choice != 'q':
    choice = programa.disp_choices()
    # Respond to the user's choice.
    if choice == '1':
        print(filters.filtra_llengua(programa.language_choice()))
        #filters.search_lyrics(ids)
    elif choice == '2':
        print("filtra genere")

    elif choice == '3':
        ids = filters.filtra_pais(programa.country_choice())
        filters.search_lyrics(ids)

    elif choice == 'q':
        print("\nGracies!!! Fins a la proxima")
        quit()

    else:
        print("\nI didn't understand that choice.\n")

