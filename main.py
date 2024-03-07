import redgifs

links = []

api = redgifs.API()
api.login()

feeds = api.get_feeds()

gifs = feeds.horizontal_gifs

links = [item.urls.embed_url for item in gifs]

num = 0