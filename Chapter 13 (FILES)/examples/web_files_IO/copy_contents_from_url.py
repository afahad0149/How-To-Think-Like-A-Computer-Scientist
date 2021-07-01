import urllib.request

url = "http://textfiles.com/adventure/aencounter.txt"
destination_filename = "sample.txt"

urllib.request.urlretrieve(url, destination_filename)