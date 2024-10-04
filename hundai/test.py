import aiohttp
import asyncio
import csv
import json

# Define the ranges for latitude and longitude
min_latitude = 8.4  
max_latitude = 37.6
min_longitude = 68.7
max_longitude = 97.25

# Increment of 0.5 degrees (1° = approx 111 km)
increment_lat = 0.5
increment_lon = 0.5

# Hyundai API URL
base_url = "https://api.hyundai.co.in/service/dealer/getDealersByLatLonModel"
dealer_category_id = 1
distance = 100  # Set maximum distance to 100 km
model_id = ""
location = "IN"
language = "en"

# Async function to make API call
async def get_dealers(session, lat, lon):
    params = {
        "dealerCategoryId": dealer_category_id,
        "latitude": lat,
        "longitude": lon,
        "distance": distance,
        "modelId": model_id,
        "loc": location,
        "lan": language
    }
    async with session.get(base_url, params=params) as response:
        try:
            data = await response.json()
            return lat, lon, data
        except Exception as e:
            print(f"Error decoding JSON for lat {lat}, lon {lon}: {e}")
            return lat, lon, []

# Async function to handle the gathering and writing process
async def gather_and_write_data():
    # Define the CSV file name
    csv_file_name = 'dealers_hyundai_raw_async.csv'

    # Write the data to the CSV file
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Latitude", "Longitude", "Raw JSON"])

        # Create a list of all latitude and longitude pairs
        lat_lon_pairs = [(lat / 10.0, lon / 10.0) for lat in range(int(min_latitude * 10), int(max_latitude * 10 + 1), int(increment_lat * 10))
                         for lon in range(int(min_longitude * 10), int(max_longitude * 10 + 1), int(increment_lon * 10))]

        # Create an aiohttp session
        async with aiohttp.ClientSession() as session:
            tasks = []
            for lat, lon in lat_lon_pairs:
                task = asyncio.ensure_future(get_dealers(session, lat, lon))
                tasks.append(task)

            # Gather the results as they complete
            for future in asyncio.as_completed(tasks):
                lat, lon, dealers = await future
                if dealers:
                    writer.writerow([lat, lon, json.dumps(dealers)])
                    print(f"Latitude: {lat}, Longitude: {lon}")  # Print current latitude and longitude

    print(f"CSV file '{csv_file_name}' has been created successfully.")

# Run the async event loop
asyncio.run(gather_and_write_data())
