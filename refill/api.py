import urllib.request
import json
from urllib.request import Request


def Fda_search(query):
    Fda_key ='ty3g74vlPobGSx1IGmDyN51j7lRyPzfmMlKx2Ct1'
    url = 'https://api.fda.gov/drug/label.json?api_key='+Fda_key+'&search='
    drug_name = query.replace(' ', '+')
    final_url= url+drug_name+'&count=openfda.product_type.exact&limit=1'
    #print(final_url)
    headers={}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    fi_url = Request(final_url, headers=headers)
    json_obj = urllib.request.urlopen(fi_url)
    req_data =json_obj
    data = json.load(req_data)
    for item in data['results']:
        return item['term']

