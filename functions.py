import requests, json, datetime
from settings import database_id, headers
# Create a Page
def create_page(properties: dict):
    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": { "database_id": database_id },
        "properties": properties
    }
    data = json.dumps(newPageData)
    return requests.post(createUrl, headers=headers, data=data)

def create_notepad_entry():
    return create_page({
        "Name": {
                "title": [
                    {
                        "text": {
                            "content":  datetime.datetime.now().strftime("%D %H:%M")
                        }
                    }
                ]
            },
    })