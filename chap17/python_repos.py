import requests

# make the api call
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:starts+stars:>10000"

headers = {"Accept" : "application/vnd.github.v3+json"}
r = requests.get(url, headers)
if r.status_code == 200:
    response_dict = r.json()
    print(response_dict['total_count'])
    print(response_dict["incomplete_results"])
    print(len(response_dict['items']))
else:
    print("error")