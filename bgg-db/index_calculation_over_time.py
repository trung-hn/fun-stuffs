# %%
import requests, xmltodict
from datetime import datetime

url = "https://api.geekdo.com/xmlapi2/plays?username=supermanvungtau"

# set content type to  jsson
headers = {"Accept": "application/json"}

history = []
for pg in range(1, 100):
    response = requests.get(
        url, headers=headers, params={"ussername": "supermanvungtau", "page": pg}
    )

    # convert xml response to json
    json_response = xmltodict.parse(response.content)

    if "play" not in json_response["plays"]:
        break

    for play in json_response["plays"]["play"]:
        history.append(
            (play["@quantity"], datetime.strptime(play["@date"], "%Y-%m-%d"))
        )

print(history)
print(sum([int(q) for q, _ in history]))

# %%
