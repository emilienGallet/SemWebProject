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

    """Import of ADE Calendar of CPS2 students"""
    cps2Calendar = "https://planning.univ-st-etienne.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4222&projectId=1&calType=ical&firstDate=2022-08-22&lastDate=2023-08-20"

    # TODO importer le fichier ADECal.ics de cps2Calendar avec urllib. Pas d'import manuel!! Si on veux des point faut que ça soit facil pour eux


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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
