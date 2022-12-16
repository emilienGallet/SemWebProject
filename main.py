# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    """Do the asked work, first import class"""

    from Onthologie import Onthologie
    from Query import Query

    """Import Libraries"""
    import rdflib
    import recurring_ical_events
    from icalendar import Calendar, Event
    from datetime import datetime
    from pytz import UTC  # timezone
    import xml.etree.ElementTree as ET

    """Import of ADE Calendar of CPS2 students"""
    cps2Calendar = "https://planning.univ-st-etienne.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4222&projectId=1&calType=ical&firstDate=2022-08-22&lastDate=2023-08-20"

    fileCalendar = open("ADECal.ics", "r")
    # TODO importer le fichier ADECal.ics de cps2Calendar avec urllib. Pas d'import manuel!! Si on veux des point faut que ça soit facil pour eux
    # TODO on extrait l'ontalogie qui décrit un calendrier avec la norme ICS
    cal = Calendar().from_ical(fileCalendar.read())
    start_date = (2019, 3, 5)
    end_date = (2023, 4, 1)
    events = recurring_ical_events.of(cal).between(start_date, end_date)

    # import de l'ontologie qui décrit le fonctionnement d'un calendrier
    url = "https://www.w3.org/2002/12/cal/ical"
    #curl https://www.w3.org/2002/12/cal/ical -H "Accept: applications/rdf+xml" > ical.rdf
    tree = ET.parse(str("ical.rdf"))

    # Itération pour chaque évènement et remplissage du graphe de connaissance
    for pos, event in enumerate(events):
        print(event)
        # start = event["DTSTART"].dt
        # duration = event["DTEND"].dt - event["DTSTART"].dt
        # print("start {} duration {}".format(start, duration))
    # TODO a partir de l'ontologie extraite on extrait les données du calendrier des CPS2
    # ces données extraites doivent inclure TODO une instance de RDF Grpah de https://schema.org/Event
    # TODO les données du calendrier des CPS2 sont inséré dans notre graphe de connaissance
    # TODO interogé notre base de donner avec des requêtes SpackQL
    # TODO Décrire le batiment de l'espace Fauriel en RDF
    # TODO https://territoire.emse.fr/ldp/ => envoyer une requete POST
    # plus d'info sur https://carbonldp.com/documentation/v5.x.x/rest-api/sparql-querying/
    # + TODO voir la gestion des conteneur https://www.w3.org/TR/ldp/#ldpc

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """Will prepare the sem Web project with requied import"""
    import subprocess
    import sys


    def install(*packages):
        for package in packages:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])


    install("rdflib", "icalendar", "recurring-ical-events", "requests")

    """ Do the asked work"""
    main()
    from rdflib import Graph, URIRef, Literal
    from rdflib.namespace import RDF, FOAF, XSD


