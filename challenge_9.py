# Answer to Challenge 9: Make an interactive version that prompts users for
# input.
#
# This is an interactive version of challenge_8.py

from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example search by location text and term. Take a look at
# http://www.yelp.com/developers/documentation/v2/search_api for
# the various options available.

search_term = input("What do you want to search for: ")

response = yelp_api.search_query(term=search_term, location='seattle, wa', sort=2, limit=20)

counter = 0
for business in response['businesses']:
    if business['review_count'] >= 100:
        counter = counter + 1

print("of the 20 highest rated restaurants in seattle, {} have 100 or fewer reviews".format(counter))


