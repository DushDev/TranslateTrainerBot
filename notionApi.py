# Initialisation
import requests, json
from dotenv import dotenv_values

secrets = dotenv_values(".env")

token = secrets["NOTION_TOKEN"]
databaseID =secrets["DB_ID"]
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}


def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data

print(readDatabase(databaseID, headers))