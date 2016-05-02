# Answer to Challenge 7: What is the highest rated business in Seattle?

from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example search by location text and term. Take a look at
# http://www.yelp.com/developers/documentation/v2/search_api for
# the various options available.

response = yelp_api.search_query(term='restaurants', location='seattle, wa', sort=2, limit=1)

for business in response['businesses']:
    print('{}\n\trating: {} ({} reviews)'.format(business['name'], business['rating'], business['review_count']))

