import json
import requests
regions = ['Asia','Europe','MEA','New+Zealand','United+States']
hotels = []
def test_hotels_number():
    for region in regions:
        url = f"https://www.millenniumhotels.com/api/search/destinations?keywords=&regionName={region}"
        get_response = requests.get(url)
        if get_response.status_code == 200:
            # print(get_response.text)
            result = json.loads(get_response.text)
            hotelMsgs = result.get('data').get('hotels')
            for hotelMsg in hotelMsgs:
                hotels.append(hotelMsg.get('name'))
    print(len(hotels))
    assert len(hotels) == 121
# [print(hotel) for hotel in hotels]
