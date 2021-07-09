import json
import math
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def fetch(params):
    url = "https://api.github.com/"
    httprequest = Request(url + params, headers={"Accept": "application/json"})

    try:
        response = urlopen(httprequest)
        return json.loads(response.read().decode())
    except HTTPError as e:
        print(e.reason)
        exit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('No Username provided. Your command should be like below:\npython star.py the_username')
        exit()

    username = sys.argv[1]

    user = fetch(f'users/{username}')

    if not user['public_repos']:
        print(f"{username} doesn't have any public repository.")
        exit()

    pages = math.ceil(user['public_repos'] / 100)
    star = 0
    highest_name = 0
    repo_star_map = {}

    for i in range(pages):
        repos = fetch(f'users/{username}/repos?per_page=100&page={i+1}')

        for repo in repos:
            repo_star_map[repo['html_url']] = repo['stargazers_count']
            star += repo['stargazers_count']
            highest_name = max(highest_name, len(repo['html_url']))

    print(f'Total ⭐️ {star}')

    for repo, star in sorted(repo_star_map.items(), key=lambda x: x[1], reverse=True):
        print(f"{repo:-<{highest_name}} ⭐️ {star}")
