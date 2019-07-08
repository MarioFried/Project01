#
# Example File for Parsing and Processing JSON
#
import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])

    count = theJSON['metadata']['count']
    print(str(count) + " Events Recorded")

    for i in theJSON['features']:
        print(i['properties']['place'])

    print("-------------------------\n")

    for i in theJSON['features']:
        if i['properties']['mag'] >= 4.0:
            print("%2.f" % i['properties']['mag'], i['properties']['place'])


def main():
    urlDATA = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webURL = urllib.request.urlopen(urlDATA)
    print("Result Code: " + str(webURL.getcode()))
    if (webURL.getcode() == 200):
        data_url = webURL.read()
        printResults(data_url)
    else:
        print("received error, cannot parse results")


if __name__ == "__main__" :
    main()