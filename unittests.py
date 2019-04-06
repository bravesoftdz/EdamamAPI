import unittest

from recipesearchapi.recipesearchapi import RecipeSearchAPI


class TestRecipeSearchAPIMethods(unittest.TestCase):
    def test_init_attributes(self):
        appid = "1ab"
        apikey = "2ef"
        api = RecipeSearchAPI(appid, apikey)
        self.assertEqual(api.app_id, appid)
        self.assertEqual(api.api_key, apikey)


if __name__ == '__main__':
    unittest.main()
