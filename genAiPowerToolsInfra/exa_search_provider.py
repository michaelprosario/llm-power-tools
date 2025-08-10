import requests
import json
import os
from exa_py import Exa

class ExaSearchProvider:
    def __init__(self):        
        pass

    def search(self, query):
        exa = Exa(os.getenv('EXA_API_KEY'))
        result = exa.search_and_contents(
        query,
        type="auto",
        text=True,
        
        )

        

        print(result)
        return result


 