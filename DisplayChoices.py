# coding=utf-8
from time import sleep
import os


### FUNCTIONS ###
def display_title_bar():
    os.system('clear')
    sleep(1)
    print("\t**********************************************")
    print("\t***  Benvingut al nostre programa          ***")
    print("\t***   <- Nil - Janna - Claudia ->          ***")
    print("\t**********************************************")
    print("\n\n")
    print("\n\t<---------------------------------------------------------------------->")
    print("\t<---   Guardarem les lletres de les teves cançons preferides        --->")
    print("\t<---               Tria el filtre que més t'agradi                 --->")
    print("\t<---------------------------------------------------------------------->")
    print ("\n\n")
    print ("""\tRECORDA EMBOLCALLAR EL QUE ESCRIUS AMB " " """)

def disp_choices():
    print("\n[1] Filter by LANGUAGE.")
    print("[2] Filter by GENRE.")
    print("[3] Filter by COUNTRY.")
    print("[q] Quit.")
    return input('What would you like to do?\n')

    # Respond to the user's choice.


def language_choice():
    print("\nIntrodueix el codi corresponent per al teu filtre:")
    print("CATAlÀ: ca")
    print("CASTELLÀ: es")
    print("ANGLÉS: en")
    print("ITALIÀ: it\n")
    return input()


def genre_choice():
    print("\nIntrodueix el genere pel qual vols filtrar:\t")
    return input("")


def country_choice():
    print("\nIntrodueix el codi corresponent al pais per al teu filtre:\t")
    print ("Els codis valids son els alpha-2 corresponents a l'ISO 3166:\n")
    print ("\t\t\thttps://www.iso.org/obp/ui\n")
    return input()



