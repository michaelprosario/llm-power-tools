import requests
import json
import os
from exa_py import Exa

class ExaSearchProvider:
    def __init__(self):        
        pass

    def search(self, query):
        exa = Exa(os.getenv('EXA_API_KEY'))
        result = exa.search(query)
        return result

    def search_and_content(self, query):
        exa = Exa(os.getenv('EXA_API_KEY'))
        result = exa.search_and_contents(query)
        return result

    def answer(self, query):
        exa = Exa(os.getenv('EXA_API_KEY'))
        result = exa.answer(query)
        return result
 