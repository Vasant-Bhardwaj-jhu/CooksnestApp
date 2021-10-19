# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from eventbrite import Eventbrite


def events():
    r = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=ej61WZqV3qdUNUEnmAJ6I4WFrDDT7nmw')
    print(r.status_code)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    events()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
