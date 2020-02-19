import requests


def get_joke():
    endpoint = "https://official-joke-api.appspot.com/jokes"
    # joke_type = "general"
    joke_type = "programming"
    # joke_qty = "ten"
    joke_qty = "random"

    joke = requests.get('/'.join([endpoint, joke_type, joke_qty])).json()
    return joke[0]["setup"], joke[0]["punchline"]


if __name__ == "__main__":
    print(get_joke())
