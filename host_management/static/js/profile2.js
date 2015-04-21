/**
 * Created by GoldenGate on 10/12/14.
 */

$(document).ready(function() {
	$.ajax({
		url: '/table_post/',
		type: 'POST',
		dataType: 'json',
		contentType: 'application/json',
		data: JSON.stringify({
			userName: 'a name',
			userTitle: ' a title'
		})
	});
});
