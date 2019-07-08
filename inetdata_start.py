#
# Example File for retrieving data from the internet
#

import urllib.request

def main():
    webURL = urllib.request.urlopen("http://www.google.com")
    print("Code Result: " + str(webURL.getcode()))
    data = webURL.read()
    print(data)

if __name__ == "__main__":
    main()