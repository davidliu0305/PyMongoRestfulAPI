$(function()
{
	//document.Ready
	$.get('http://localhost:8085/blog-posts', function(r)
	{
		let template = $('#userList').html();
		let outputUsers = Mustache.render(template, r);
		$('#blogUserList').html(outputUsers);
	});
	// var exist = {};
	// $('select > option').each(function() {
		// if (exist[$(this).val()]){
        // $(this).remove();
		// }
		// else{
        // exist[$(this).val()] = true;
		// }
	// });
	$('#submit').click(function(){
		//var selectedUser = $("#selectID option: selected").val();
		var username = $('#username').val();	
		$.get('http://localhost:8085/blog-posts/'+username, function(r)
		{
			let temp = $('#blogsforUserTemp').html();
			let output = Mustache.render(temp, r);
			$('#blogdataPlaceholder').html(output);
		});
		
	});	
	
});	