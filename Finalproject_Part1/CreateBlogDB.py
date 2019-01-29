#make sure that you have the MongoDB daemon running first
#import static blog data from file
from BlogPosts import blog_posts

#import Mongo client module from Pymongo
from pymongo import MongoClient

#instantiate Mongo client
mongo_client = MongoClient("localhost", 27017)

#lazy reference to PokemonDB
db = mongo_client.BlogPostsDB

#lazy reference to Pokemon Document Collection
coll = db.BlogPost

#insert docs to MongoDB collection
result = coll.insert_many(blog_posts).inserted_ids

#output confirmation
print("{} records added to the database ".format(len(result)))