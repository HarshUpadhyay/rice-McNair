import csv
import sys
import urllib


input_file = sys.argv[1]

print input_file

api_key = "AIzaSyBdCQXvmCEkMfcpmMPGZVCE3t2jjYJKHcA"
api_url = "https://maps.googleapis.com/maps/api/geocode/json?"

with open(input_file, 'rb') as f:
    reader = csv.reader(f)
    business_list = list(reader)

for business in business_list:
    biz_name = business[0]
    biz_addr = business[1]
    query = urllib.urlencode({'address' : biz_addr})
