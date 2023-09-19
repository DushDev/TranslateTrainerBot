# Initialisation
import requests, json
from dotenv import dotenv_values
import os
from notion_client import Client
from pprint import pprint
import random


secrets = dotenv_values(".env")

token = secrets["NOTION_TOKEN"]
databaseID =secrets["DB_ID"]
page =secrets["PAGE"]
# headers = {
#     "Authorization": "Bearer " + token,
#     "Content-Type": "application/json",
#     "Notion-Version": "2022-02-22"
# }

notion = Client(auth=token)


def write_row(Word, Translate):
    # create a new database row
    new_row = notion.pages.create(
        **{
            "parent": {"database_id": databaseID},
            "properties": {
                "Name": {
                    "title": [  
                        {
                            "text": {
                                "content": Word
                                }
                            }
                        ]
                    },
                "Translate": {
                    "rich_text": [
                        {
                            "text": {
                                "content": Translate
                                }
                            }
                        ]
                    }
                }
            }
        )

def get_list_of_words():
    j = 0
    result = ''
    db_rows = notion.databases.query(database_id=databaseID)

    for row in db_rows['results']:
        j+=1
        # write to console a Name and Translate of database rows in "Name - Translate" format
        result += str(j) + ". " + row['properties']['Name']['title'][0]['text']['content'].capitalize() + " - " + row['properties']['Translate']['rich_text'][0]['text']['content'] + "\n"
    return result

def get_all_worlds_obj(db_rows):
    result = {}
    for row in db_rows['results']:
        result[row['properties']['Name']['title'][0]['text']['content']] = { 'translate': row['properties']['Translate']['rich_text'][0]['text']['content'], 'status': row['properties']['Status']['status']}
    return result
def get_all_worlds_array(db_rows):
    result = []
    for row in db_rows['results']:
        result.append({'word':[row['properties']['Name']['title'][0]['text']['content']], 'translate': row['properties']['Translate']['rich_text'][0]['text']['content'], 'status': row['properties']['Status']['status']})
    return result

def get_words_for_learning():
    db_rows = notion.databases.query(database_id=databaseID)
    words = get_all_worlds_array(db_rows)
    j=0
    result = ""
    while j < 5:
        j+=1
        randomWord = words[random.randint(0, len(words)-1)]
        # write to console a Name and Translate of database rows in "Name - Translate" format
        result += str(j) + "\. " + randomWord['word'][0].capitalize() + " \- ||" + randomWord['translate'] + "||\n"
    return result.replace('/([|{\[\]*_~}+)(#>!=\-.])/gm', '\\$1')