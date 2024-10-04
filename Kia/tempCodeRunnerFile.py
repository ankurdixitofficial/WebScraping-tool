import requests

url = "https://www.kia.com/api/kia2_in/findAdealer.getStateCity.do"

payload = ""
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "0",
    "cookie": "renderid=rend02; WMONID=ZbqOU0F5_Et; JSESSIONID=node0mcsk4e239s47vibb3k6au64x3191804.node0; M2_BYPASS_TOKEN=6596322522499459941; aoVtxAexxyQ_=v1ffxUgw__YWJ",
    "csrf-token": "undefined",
    "dnt": "1",
    "origin": "https://www.kia.com",
    "priority": "u=1, i",
    "referer": "https://www.kia.com/in/buy/find-a-dealer.html",
    "^sec-ch-ua": "^\^Not/A",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\^Windows^^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)