# coding=utf-8
import os


def display_title_bar():
    os.system('clear')
    print("\t\t**********************************************")
    print("\t\t***  Benvinguda al nostre programa         ***")
    print("\t\t***   <- Nil - Janna - Claudia ->          ***")
    print("\t\t**********************************************")
    print("\n\n")
    print("\t<---------------------------------------------------------------------->")
    print("\t<---   Guardarem les lletres de les teves cançons preferides        --->")
    print("\t<---               Tria el filtre que més t'agradi                  --->")
    print("\t<---------------------------------------------------------------------->")
    print ("\n")
    print ("""\t\t\tRECORDA EMBOLCALLAR EL QUE ESCRIUS AMB " " """)


def disp_choices():
    print("\n[1] Filtra per IDIOMA.")
    print("[2] Filtra per GÈNERE.")
    print("[3] Filtra per PAÍS.")
    print("[4] BUSCA.")
    print("[5] Surt.")
    return input('Què vols fer?\n')


def language_choice():
    print("\nIntrodueix el codi ISO corresponent a l'idioma a cercar:")
    print ("Pots provar amb altres idiomes. Trobaràs la llista completa aquí: https://ca.wikipedia.org/wiki/ISO_639-1")
    print("CATAlÀ: ca\tCASTELLÀ: es\tANGLÉS: en\tFRANCÉS: fr\tITALIÀ: it")
    print("FINÉS: fi\tSUEC: sv\tNORUEC: nb\tALEMANY: de\tDANÉS: da")
    print("FEROÉS: fo\tEUSKERA: eu\tGALLEC: gl\tKURD: ku\tXINÉS: zh")
    return input()


def genre_choice():
    print("\nIntrodueix el codi del gènere pel qual vols filtrar:")
    print("Clàssica: 5\t Electrònica: 7\t\t Llatina: 17\t Pop: 14\t BSO: 16")
    print("Dance: 17\t HipHop/Rap: 18\t\t Rock: 21\t Folk: 1289\t Heavy Metal: 1153")
    return input()


def country_choice():
    print("\nIntrodueix el codi ISO corresponent al país a cercar:\t")
    print ("Pots provar amb altres països: Trobaràs la llista completa aquí: https://www.iso.org/obp/ui\n")
    print("ESPANYA: es\t ALEMANYA: de\tEEUU: eu\tFRANÇA: fr\tITALIA: it")
    print("FINLÀNDIA: fi\t SUÈCIA: se\tNORUEGA: no\tRUSSIA: ru\tDINAMARCA: dk")
    return input()


def add_es_choice():
    print ("\nVols afegir aquestes dades a la nostra DB?")
    print ("1 = Si")
    print ("0 = No")
    return input()


def disp_query_option():
    print ("\nQuin terme vols buscar")
    print("[1] ARTISTA")
    print("[2] CANÇÓ")
    print("[3] LLETRA")
    print("[4] TRACK ID\n")


