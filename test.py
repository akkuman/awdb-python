# -*- coding:utf-8 -*-

import sys
import awdb
import random
import time


def get_random_ip():
    return ".".join([str(x) for x in [random.randrange(0,255),
                     random.randrange(0,255),
                     random.randrange(0,255),
                     random.randrange(0,255)]])

def main():
    filename = r'C:\Users\Downloads\reader\python\IP_city_2020W12_single_WGS84.awdb'
    reader = awdb.open_database(filename)
    while True:
        ip = get_random_ip()
        #ip = '8.8.8.8'
        #ip = '2001:DB8:0:23:8:800:200C:417A'
        print(ip)
        (record, prefix_len) = reader.get_with_prefix_len(ip)
        continent = record.get("continent",b'').decode("utf-8") if sys.version_info[0]==3 else record.get("continent",'')
        country = record.get("country",b'').decode("utf-8") if sys.version_info[0]==3 else record.get("country",'')
        zipcode = record.get("zipcode",b'').decode("utf-8") if sys.version_info[0]==3 else record.get("zipcode",'')
        timezone = record.get("timezone",b'').decode("utf-8") if sys.version_info[0]==3 else record.get("timezone",'')
        accuracy = record.get("accuracy",b'').decode("utf-8") if sys.version_info[0]==3 else record.get("accuracy",'')
        source = record.get("source",b'').decode("utf-8") if sys.version_info[0]==3 else record.get("source",'')
        owner = record.get("owner",b'').decode("utf-8") if sys.version_info[0]==3 else record.get("owner",'')

        print("continent:"+continent)
        print("country:"+country)
        print("zipcode:"+zipcode)
        print("timezone:"+timezone)
        print("accuracy:"+accuracy)
        print("source:"+source)
        print("owner:"+owner)

        multiAreas = record.get("multiAreas",{})
        if multiAreas:
            for area in multiAreas:
                prov = area.get("prov",b"").decode("utf-8") if sys.version_info[0]==3 else area.get("prov","")
                city = area.get("city",b"").decode("utf-8") if sys.version_info[0]==3 else area.get("city","")
                district = area.get("district",b"").decode("utf-8") if sys.version_info[0]==3 else area.get("district","")
                lat = area.get("lat",b"").decode("utf-8") if sys.version_info[0]==3 else area.get("lat","")
                lng = area.get("lng",b"").decode("utf-8") if sys.version_info[0]==3 else area.get("lng","")
                radius = area.get("radius",b"").decode("utf-8") if sys.version_info[0]==3 else area.get("radius","")
                print("prov:"+prov)
                print("city:"+city)
                print("district:"+district)
                print("lat:"+lat)
                print("lng:"+lng)
                print("radius:"+radius)
                print('---')
        time.sleep(1)
    reader.close()


if __name__ == '__main__':
    main()


