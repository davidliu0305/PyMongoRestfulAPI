<!DOCTYPE html>
<html>
	<head>
		<title>{{user}}'s Blogs</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="container">
			<a href="/blogcreate/{{user}}">Add a new blog post</a>
			<h2>{{user}}'s Blogs</h2>
			<table style="width:100%">
				<thead>
					 <tr>
						<th>Title</th>
						<th>Date</th>
					</tr>
				</thead>
				<tbody>
					%for b in blogPosts:
						<tr>
							<td>{{b['title']}}</td>
							<td>{{b['Date']}}</td>
							<td><a href="/blogdetail/{{b['bID']}}">View Detail</a></td>
							<td><a href="/blogupdate/{{b['bID']}}">Update</a></td>
							<td><a href="/blogdelete/{{b['bID']}}">Delete</a></td>
						</tr>
					%end		
				</tbody>
			</table>
		</div>	
	</body>
</html>	