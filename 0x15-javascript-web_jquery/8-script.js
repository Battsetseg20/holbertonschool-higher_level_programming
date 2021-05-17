$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    $.each(data['results'], function (i, item) {
	$('UL#list_movies').append('<li>' + item['title'] + '</li>');
    });
});
