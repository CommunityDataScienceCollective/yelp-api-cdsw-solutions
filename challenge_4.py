# Answer to Challenge 4: Open a file and save the answers to a file instead of
# just printing them out.
#
# I'm printing the answer in tab-separated values format (TSV) into a file called "ice_cream_shops.tsv".

from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example search by location text and term. Take a look at
# http://www.yelp.com/developers/documentation/v2/search_api for
# the various options available.

response = yelp_api.search_query(term='ice cream', location='seattle, wa', sort=2, limit=20)

output_file = open("ice_cream_shops.tsv", 'w')

for business in response['businesses']:
    line_string = '{}\t{}\t{}\t{}\t{}\n'.format(business['name'], business['id'], business['rating'], business['review_count'], business['location']['display_address'])
    output_file.write(line_string)

output_file.close()

