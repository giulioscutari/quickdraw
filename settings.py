from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the environment variables
database_id = os.getenv('NOTION_DATABASE_ID')
token = os.getenv('NOTION_INTEGRATION_SECRET')
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}