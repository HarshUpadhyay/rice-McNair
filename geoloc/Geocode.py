import csv
import sys
import urllib
import json
import requests


input_file = sys.argv[1]

print "Reading data from ",input_file
#input_file = 'Chicago Adresses for geocode v2.txt'
output_file = open('{}_coords'.format(input_file), 'w')
api_key = "AIzaSyBdCQXvmCEkMfcpmMPGZVCE3t2jjYJKHcA"
api_url = "https://maps.googleapis.com/maps/api/geocode/json?"

f = open(input_file, 'r')
reader = csv.reader(f, delimiter="\t")
business_list = list(reader)
output_file.write('{}\t{}\t{}\n'.format("Name", "Latitude", "Longitude"))
business_list = business_list[1:]


for business in business_list:
    biz_name, biz_addr = business[0], business[1]
    str_key, str_addr = urllib.urlencode({'key':api_key}), urllib.urlencode({'address':biz_addr})
    data = json.loads(requests.get(api_url+str_addr+'&'+str_key).text)
    location = data["results"][0]["geometry"]["location"]
    output_file.write('{}\t{}\t{}\n'.format(biz_name, location["lat"], location["lng"]))

f.close()
output_file.close()