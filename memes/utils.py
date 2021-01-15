import json
import random

import requests
from django.core.exceptions import ValidationError

MEMES_API_URL = "https://api.imgflip.com/get_memes"
REQUIRED_NUMBER_OF_MEMES = 5

def get_memes():
    memes_api_response = requests.get(MEMES_API_URL)
    status_code = memes_api_response.status_code

    random_memes = []

    if status_code == 200:
        all_memes = json.loads(memes_api_response.content)

        memes_count = len(all_memes['data']['memes'])

        for i in range(REQUIRED_NUMBER_OF_MEMES):
            random_memes.append(all_memes['data']['memes'][random.randint(0, memes_count)])

    return status_code, random_memes


