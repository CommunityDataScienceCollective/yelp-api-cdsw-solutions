# Answer to Challenge 8: How many of the 20 most highly rated restaurants have
# 100 or more reviews?
#
# The point here is to realize a funny thing about Yelp data. It's hard to


from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example search by location text and term. Take a look at
# http://www.yelp.com/developers/documentation/v2/search_api for
# the various options available.

response = yelp_api.search_query(term='restaurants', location='seattle, wa', sort=2, limit=20)

counter = 0
for business in response['businesses']:
    if business['review_count'] >= 100:
        counter = counter + 1

print("of the 20 highest rated restaurants in seattle, {} have 100 or fewer reviews".format(counter))

