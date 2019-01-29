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
		<h2>Are you sure u want to delete blog{{blog['title']}}?</h2>
		<form role="form" method="post" action="/newblogList">
			<input type="hidden" name="theBlogId" value="{{blog['bID']}}">
			<input type="hidden" name="theblogUser" value="{{blog['User']['Account']}}">
			<button type="submit" class="btn btn-success">Delete</button>
		</form>
	 </div>
</body>
</html>