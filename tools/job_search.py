import http.client
from urllib.parse import quote_plus

def job_search(searchTerm):
    conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com")

    headers = { 
        'x-rapidapi-host': "jsearch.p.rapidapi.com",
        'x-rapidapi-key': "fixMe"
    }

    # escape characters for url search
    searchTerm = quote_plus(searchTerm)

    conn.request("GET", f"/search?query={searchTerm}&page=1&num_pages=1&country=us&date_posted=all", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


print(job_search("python jobs orlando"))