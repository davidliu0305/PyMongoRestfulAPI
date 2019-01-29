from bottle import route, run, request, response, get, delete, post, hook
from bson.json_util import dumps
from bson import ObjectId
from BlogPosts_conn import coll
from pymongo.errors import PyMongoError
import re
import datetime

@get('/blog-posts')
def get_blogposts():
	"""method to provide all Blogposts data"""
	try:
		try:
			#find all types and sort by type value
			blog_list = coll.find({}, {"title": True, "Content": True, "_id": True, "User":True}).sort("title")
			#if the list is not found it is because the collection is empty or does not exist
			if blog_list is None:
				raise EnvironmentError
		except PyMongoError:
			raise EnvironmentError
	except EnvironmentError:
		response.status = 500						#Internal Server Error
		return ({"error":"Blog list Data is Not Available"})
		
	response.headers['Cache-Control'] = 'cache'		#permit caching
	return dumps({"BlogList": blog_list})			#return list in json format

@get('/blog-posts/<username>')
def get_blogpostsByUser(username):
	"""method to provide blog posts data by user"""
	try:
		try:
			#get one pokemon type that matches user type param
			blogsForUser = coll.find({"User.Account":username}, {"title": True, "Content": True, "_id": True, "User": True, "Date": True, "Comments": True})
			#test to see if the type was not found. Raise value error if not found
			if blogsForUser is None:
				raise ValueError
		except PyMongoError:
			raise EnvironmentError
	except ValueError:
		response.status = 400						#bad request
		return ({"error":"User not found"})
	except EnvironmentError:
		response.status = 500						#Internal Server Error
		return ({"error":"Blog Data is Not Available"})		
		
	response.headers['Cache-Control'] = 'cache'		#permit caching
	return dumps({"Blog_List_for_this_User":blogsForUser})			#dump document in JSON format
	
@delete('/blog-posts/<id>')
def remove_blogpost(id):
	"""method to remove one pokemon type via Object ID value"""
	try:	
		#build reg ex
		pattern = r'^[a-fA-F0-9]{24}$'
		#see if the reg ex pattern matches the objectid passed to method	
		
		if re.search(pattern, id) is None:
			raise TypeError	
		try:
			id = ObjectId(id)
			results = coll.delete_one({"_id":id})
			#pokemon not found
			if results.deleted_count == 0:
				raise ValueError
		except PyMongoError:
			raise EnvironmentError
			
	except TypeError:
		response.status = 400						#bad object id val
		return ({"error": "Unacceptable ObjectID value"})
	except ValueError:
		response.status = 404						#pokemon type not found
		return ({"error": "Blog post Not Found"})
	except EnvironmentError:
		response.status = 500						#Internal Server Error
		return ({"error": "Blog post Data is Not Available"})
	
	response.headers['Cache-Control'] = 'no-cache'
	return ({"num_deleted": results.deleted_count})		

# @put('/blog-posts/<id>')
# def update_blogpost(id):
	# return null	
	
@post('/setblogposts')
def set_blogpost():
	id = request.params.get('id')
	title = request.params.get('title')
	content = request.params.get('content')
	date = datetime.datetime.today().strftime('%Y-%m-%d')
	print id
	
	try:
		#build reg ex
		pattern = r'^[a-fA-F0-9]{24}$'
		#see if the reg ex pattern matches the objectid passed to method
		if re.search(pattern, id) is None:
			raise TypeError
		
		if (title is None) or (content is None):
			raise ValueError	
	
		try:
			id = ObjectId(id)
			results = coll.update_one({"_id":id}, {"$set": {"title":title, "Content":content, "Date":date}}, upsert=True)
		except PyMongoError:
			raise EnvironmentError
			
	except TypeError:
		response.status = 400						#bad request
		return ({"error": "Unacceptable ObjectID value"})
	except ValueError:
		response.status = 400						#bad request
		return ({"error": "Incorrect parameter values in request - title, content and date are required"})
	except EnvironmentError:
		response.status = 500						#Internal Server Error
		return ({"error": "Blog Data is Not Available"})

	response.headers['Cache-Control'] = 'no-cache'
	return ({"num_mod": results.modified_count, "_id":str(results.upserted_id)})
	




@hook('after_request')
def enable_cors():
	"""Permit cross site requests and format response as json"""
	response.headers['Content-Type']='application/json'
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods']='PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers']='Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


run(host = 'localhost', port = 8085, debug=True, reloader=True)