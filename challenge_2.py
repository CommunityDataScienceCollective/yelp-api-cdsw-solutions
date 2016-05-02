# Answer to Challenge 1: Change your search in some way described in the API
# documentation (e.g., use a category filter) 
#
# I've changed this to print ice cream places in Seattle using the category
# filter. I used the term "icecream" which I found documented on this page in
# the API documentation:
#
# https://www.yelp.com/developers/documentation/v2/all_category_list

from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example search by location text and term. Take a look at
# http://www.yelp.com/developers/documentation/v2/search_api for
# the various options available.

print('***** 5 best rated ice cream places in Seattle, WA *****')

response = yelp_api.search_query(category_filter='icecream', location='seattle, wa', sort=2, limit=5)

print('region center (lat,long): {},{}\n'.format(response['region']['center']['latitude'], response['region']['center']['longitude']))

for business in response['businesses']:
    print('{}\n\tYelp ID: {}\n\trating: {} ({} reviews)\n\taddress: {}'.format(business['name'], business['id'], business['rating'], business['review_count'], business['location']['display_address']))

