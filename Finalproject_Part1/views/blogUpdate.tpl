<!DOCTYPE html>
<html>
	<head>
		<title>Create a new blog</title>
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
		<h2>{{blog['User']['Account']}}'s blog</h2>
		<form role="form" method="post" action="/updatedblogList">
			<div class="form-group">
				<input type="hidden" name="blogUser" value="{{blog['User']['Account']}}">
				<input type="hidden" name="blogID" value="{{blog['bID']}}">
				<h4><small>Title</small></h4>
				<textarea class="form-control" rows="1" name="updatedtitle" required>{{blog['title']}}</textarea>
				<h4><small>Content</small></h4>
				<textarea class="form-control" rows="4" name="updatedcontent" required>{{blog['Content']}}</textarea>
			</div>
			<button type="submit" class="btn btn-success">Update</button>
		</form>
		</div>
	</body>
</html>	