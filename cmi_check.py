from itertools import count
from datacube_ows.ows_configuration import (ConfigException, OWSConfig,
                                            OWSFolder, read_config)
import re
import urllib.request, json

raw_cfg = read_config("ows_refactored.ows_root_cfg.ows_cfg")
CMI_URL_PREFIX = "https://cmi.ga.gov.au/data-products/dea/"
CMI_JSON_PREFIX = "https://cmi.ga.gov.au/api/v1/data-product/json/"

def loop_through_layers(ls):
    count_missing = 0
    cmi_url = CMI_URL_PREFIX +ls["name"]
    try:
        cmi_page = urllib.request.urlopen(cmi_url)
        uid = re.findall(r'\d+', cmi_page.url)[0]
        if uid:
            with urllib.request.urlopen(f"{CMI_JSON_PREFIX}{uid}?_format=json") as url:
                data = json.loads(url.read().decode())
                if data[0]['product_title'] != ls["title"]:
                    print(ls["name"])
                    print(f"cmi recorded title: \t {data[0]['product_title']} \nows layer title: \t {ls['title']}")
#                                 print(data[0]['product_what_this_product_offers'])
    except:
        count_missing += 1
    return count_missing

count_missing = 0

for l in raw_cfg["layers"]:
    for li in l["layers"]:
        if "name" in li:
            count_missing += loop_through_layers(li)

        else:
            for ls in li["layers"]:
                if "name" in ls:
                    count_missing += loop_through_layers(ls)

print(f"number of product missing in cmi: {count_missing}")