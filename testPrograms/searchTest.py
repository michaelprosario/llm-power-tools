# adjust path to include the parent directory
import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from genAiPowerToolsInfra.exa_search_provider import ExaSearchProvider
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


load_dotenv()


service = ExaSearchProvider()

## search for blogs related to practical open source applications
query = "blog posts related to open source 3d model creation tools"
results = service.search(query=query)
print(results)

