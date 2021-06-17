import requests
import json

GIANT_BOMB_SEARCH_URL = 'http://www.giantbomb.com/api/search/'
API_KEY = '1f09de1bd3cbbfaa45a35846ec346592e620622f'
FIELDS = 'name,aliases,developers,genres,original_release_date,original_game_rating'


def search_giant_bomb(api_key, query):
    if api_key is (None or ''):
        api_key = API_KEY

    # querying giant bomb api
    result = requests.get(url=GIANT_BOMB_SEARCH_URL + '?api_key=' + api_key + '&format=json&query="' + query +
                              '"&resources=game&field_list=' + FIELDS,
                          headers={'user-agent': 'newcoder'})

    # extracting data in json format
    data = json.loads(result.text)
    return data
