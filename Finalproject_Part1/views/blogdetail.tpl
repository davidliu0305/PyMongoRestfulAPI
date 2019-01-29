<!DOCTYPE html>
<html lang="en">
<head>
  <title>{{blog['title']}}</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
    /* Set height of the grid so .sidenav can be 100% (adjust if needed) */
    .row.content {height: 1500px}
    
    /* Set gray background color and 100% height */
    .sidenav {
      background-color: #f1f1f1;
      height: 100%;
    }
    
    /* Set black background color, white text and some padding */
    footer {
      background-color: #555;
      color: white;
      padding: 15px;
    }
    
    /* On small screens, set height to 'auto' for sidenav and grid */
    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
      }
      .row.content {height: auto;} 
    }
  </style>
</head>
<body>
	 <div class="col-sm-9">
		<hr>
		<h2>{{blog['title']}}</h2>	
		<h5><span class="glyphicon glyphicon-time"></span> Post by {{blog['User']['Account']}},{{blog['Date']}}</h5>
		<p>{{blog['Content']}}</p>
		<h4>Leave a Comment:</h4>
      <form role="form" method="post" action="/blogCommentAdded">
        <div class="form-group">
		  <input type="hidden" name="blogIDCom" value="{{blog['bID']}}">	
          <textarea class="form-control" rows="3" name="blogContent" required></textarea>
        </div>
        <button type="submit" class="btn btn-success">Submit</button>
      </form>
      <br><br>
      %if blog['Comments']!=None:
			<p><span class="badge">{{len(blog['Comments'])}}</span> Comments:</p><br>
			%for comment in blog['Comments']:
				<div class="col-sm-10">
				<h4>{{comment['CommentBy']}} <small>{{comment['Date']}}</small></h4>
				<p>{{comment['Text']}}</p>
				<br>
				</div>
			%end	
	  %end
	  </div>
</body>
</html>