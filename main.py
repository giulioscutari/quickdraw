from functions import *
from pprint import pprint


res = create_notepad_entry()
print(res.json().get('url'))