import requests
import pandas as pd

# Read city and state data from CSV
df = pd.read_csv('city_keys.csv')

url = "https://www.kia.com/api/kia2_in/findAdealer.getDealerList.do"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# Create an empty list to store all dealer data
all_dealers = []

# Loop through each row (city, state) in the DataFrame
for index, row in df.iterrows():
    city = row['city_key']
    state = row['state_key']

    # Construct the payload for POST request
    payload = {
        "state": state,
        "city": city,
        "dealerType": "A"  # Assuming dealerType A is a constant value for your case
    }

    # Send POST request
    try:
        response = requests.post(url, data=payload, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Assuming the dealers are within the 'data' key in the JSON response
            if "data" in data:
                dealers = data["data"]

                # Extend the list with dealers for this (state, city) combination
                all_dealers.extend(dealers)
            else:
                print(f"No dealer data found for state {state} and city {city}")
        else:
            print(f"Request failed for state {state} and city {city}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed for state {state} and city {city}: {str(e)}")

# Create a DataFrame from all_dealers list
df_all_dealers = pd.DataFrame(all_dealers)

# Save the DataFrame to a single CSV file
df_all_dealers.to_csv('all_dealers.csv', index=False)

print("All dealer data saved to all_dealers.csv")
