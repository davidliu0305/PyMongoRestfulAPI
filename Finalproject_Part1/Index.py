#import required modules
from bottle import route, run, template, static_file, os, request, redirect
from bson import ObjectId
import datetime

#connect to MongoDB
from pymongo import MongoClient
mongo_client = MongoClient("localhost", 27017)
db = mongo_client.BlogPostsDB
coll = db.BlogPost

#decorator to route all static files
@route('/static/<filename:path>')
#method to serve up static files
def server_static(filename):
	myPath = os.path.join(os.getcwd(), "static")
	return static_file(filename, root=myPath)
	
#index route
@route('/')
def login():
	#serve the pokemon list to home template 
	return template('login')

@route('/blogs', method='POST')
def bloglist():
	#look for the blog posts for a specific user
	#username = request.query.username
	username = request.forms.get("username")
	#password = request.query.password
	password = request.forms.get("password")
	print username
	results = coll.find({"User.Account":username,"User.Password":password})
	results = sorted(results, key=lambda k : datetime.datetime.strptime(k['Date'], '%Y-%m-%d'), reverse=True)
	#print results.count()
	if len(results):
		return template('bloglist',{"blogPosts":results,"user":username})
	else:
		return template('login')

@route('/blogdetail/<ID>')		
def blogDetail(ID):
	Blog = coll.find_one({"bID":ID})	
	return template('blogdetail',{"blog":Blog})	
	
@route('/blogupdate/<ID>')		
def blogUpdate(ID):
	Blog = coll.find_one({"bID":ID})	
	return template('blogUpdate',{"blog":Blog})

@route('/blogdelete/<ID>')		
def blogDelete(ID):
	Blog = coll.find_one({"bID":ID})	
	return template('blogDelete',{"blog":Blog})		
	
@route('/blogcreate/<username>')
def blogCreatePage(username):
	result = coll.find_one({"User.Account":username})
	user = result['User']
	print user
	return template('createblog',{"User":user})

@route('/blogList', method='POST')
def createNewBlog():
	title = request.forms.get("title")
	content = request.forms.get("content")
	username = request.forms.get("userAccount")
	date = datetime.datetime.today().strftime('%Y-%m-%d')
	print date
	blogId = str(coll.find({}).count() + 1)
	print blogId
	user = coll.find_one({"User.Account":username})['User']
	print user
	try:
		result = coll.insert_one({"title":title,"bID":blogId,"Comments":None,"Content":content,"User":user,"Date":date}).inserted_id
		print result
		results = coll.find({"User":user})
		results = sorted(results, key=lambda k : datetime.datetime.strptime(k['Date'], '%Y-%m-%d'), reverse=True)
		return template('bloglist',{"blogPosts":results,"user":user['Account']})
	except Exception as e:
		return template('errors',{"error": e})

@route('/updatedblogList', method='POST')
def updateBlog():
	bID = request.forms.get("blogID")
	title = request.forms.get("updatedtitle")
	content = request.forms.get("updatedcontent")
	username = request.forms.get("blogUser")
	user = coll.find_one({"User.Account":username})['User']
	print user
	date = datetime.datetime.today().strftime('%Y-%m-%d')
	print date
	try:
		result = coll.update_one({"bID":bID}, {"$set":{"title": title, "Content": content, "Date": date}})
		print result
		results = coll.find({"User":user})
		results = sorted(results, key=lambda k : datetime.datetime.strptime(k['Date'], '%Y-%m-%d'), reverse=True)
		return template('bloglist',{"blogPosts":results,"user":user['Account']})
	except Exception as e:
		return template('errors',{"error": e})
		
@route('/blogCommentAdded', method='POST')
def updateBlogComments():
	bID = request.forms.get("blogIDCom")
	Blog = coll.find_one({"bID":bID})
	newCommentText = request.forms.get("blogContent")
	newCommentDate = datetime.datetime.today().strftime('%Y-%m-%d')
	newCommentBy = Blog['User']['Account']
	newComment = {'Date':'','Text':'','CommentBy':''}
	newComment['Date'] = newCommentDate
	newComment['Text'] = newCommentText
	newComment['CommentBy'] = newCommentBy
	print newComment
	#append the new comment here
	Comments = Blog['Comments']
	if Comments == None:
		Comments = []
		Comments.append(newComment)
	else:
		Comments.append(newComment)
	try:
		result = coll.update_one({"bID":bID}, {"$set":{"Comments": Comments}})
		print result
		newBlog = coll.find_one({"bID":bID})	
		return template('blogdetail',{"blog":newBlog})
	except Exception as e:
		return template('errors',{"error": e})		

@route('/newblogList', method='POST')
def deleteBlog():
	bID = request.forms.get("theBlogId")
	username = request.forms.get("theblogUser")
	user = coll.find_one({"User.Account":username})['User']
	print user
	try:
		result = coll.delete_one({ "bID": bID })
		print result
		results = coll.find({"User":user})
		results = sorted(results, key=lambda k : datetime.datetime.strptime(k['Date'], '%Y-%m-%d'), reverse=True)
		return template('bloglist',{"blogPosts":results,"user":user['Account']})
	except Exception as e:
		return template('errors',{"error": e})
		
if __name__ == "__main__":	
	run(host='localhost', port=8084, debug=True, reloader=True)	