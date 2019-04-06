import sys
import requests


"""
API for pulling data from the Edamam Recipe Search API
"""
class RecipeSearchAPI(object):
    def __init__(self, app_id, api_key):
        """ initialize recipesearchapi object with app_id and api_key """
        self.app_id = app_id
        self.api_key = api_key
        self.search_api_path = "https://api.edamam.com/search"
