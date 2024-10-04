import requests
import pandas as pd

url = "https://www.kia.com/api/kia2_in/findAdealer.getDealerList.do"

payload = "state=AP&city=S99&dealerType=A"
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "renderid=rend02; WMONID=ZbqOU0F5_Et; aoVtxAexxyQ_=v1ffxUgw__YWJ; cookie-agree=true; TS01675e00=018c6589df0988ca76d543cf77ba826e4b7afb9009c6447efc809427164846d6ddf17c1769543e9b6f6352423951b8cc8a881b31a4; JSESSIONID=node01d21k1x7lzlq7dfggvwxjvgf2581967.node0; M2_BYPASS_TOKEN=1457018443362356708",
    "csrf-token": "undefined",
    "dnt": "1",
    "origin": "https://www.kia.com",
    "priority": "u=1, i",
    "referer": "https://www.kia.com/in/buy/find-a-dealer/result.html?state=MH&city=W43",
    "^sec-ch-ua": "^Not/A",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^Windows^^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.post(url, data=payload, headers=headers)

# Parse the JSON response
data = response.json()

# Print the JSON response to understand its structure
print(data)

# Assuming the dealers are within the 'data' key in the JSON response
if "data" in data:
    dealers = data["data"]

    # Create a DataFrame from the list of dealers
    df = pd.DataFrame(dealers)

    # Save the DataFrame to a CSV file
    df.to_csv('dealers.csv', index=False)
else:
    print("No dealer data found in the response")
