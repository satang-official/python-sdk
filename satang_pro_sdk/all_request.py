import requests

def get_request(url,params={},headers='',payload='',):
    return requests.request("GET", requests.get(url,params=params).url, headers=headers, data=payload)

def post_requst(url,headers,payload=''):
    return requests.request("POST", url, headers=headers, data=payload)

def delete_request(url,headers,payload=''):
    return requests.request("DELETE", url, headers=headers, data=payload)