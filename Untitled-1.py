import requests

req = requests.get(
    "https://api.edamam.com/search?q=chicken&app_id=0890373f&app_key=5c5cb11c82dd77cd32e808aa96589367&from=0&to=3&calories=591-722&health=alcohol-free").json()
