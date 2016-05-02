# Answer to Challenge 3: Instead of rating information, print out phone
# numbers... but what we will do if we don't have phone numbers?

from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example search by location text and term. Take a look at
# http://www.yelp.com/developers/documentation/v2/search_api for
# the various options available.

print('***** 5 best rated ice cream places in Seattle, WA *****')

response = yelp_api.search_query(term='ice cream', location='seattle, wa', sort=2, limit=5)

print('region center (lat,long): {},{}\n'.format(response['region']['center']['latitude'], response['region']['center']['longitude']))

for business in response['businesses']:
    if 'display_phone' in business:
        phone_number = business['display_phone']
    else:
        phone_number = "NO PHONE NUMBER AVAILABLE"

    print('{}\n\tYelp ID: {}\n\tPhone Number: {}'.format(business['name'], business['id'], phone_number))

