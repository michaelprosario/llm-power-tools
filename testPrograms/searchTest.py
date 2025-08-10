# adjust path to include the parent directory
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from genAiPowerToolsInfra.exa_search_provider import ExaSearchProvider
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()


service = ExaSearchProvider()

### basic search demo
# print("START basic search")

# query = "blog posts related to open source 3d model creation tools"
# searchResults = service.search(query=query)

# for result in searchResults.results:
#     print(result)

# print("END basic search demo")

### search and content
print("START search and content")

query = "Making a tool/plugin for semantic kernel"
searchResults = service.search_and_content(query=query)

for result in searchResults.results:
    print(result)
print("END search and content demo")

