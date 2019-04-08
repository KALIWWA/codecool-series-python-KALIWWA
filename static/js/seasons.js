function collectData(show_id, season_id) {
	let seasonRequest = new XMLHttpRequest();
	seasonRequest.open('GET', '/tv-show/<show_id>/<season_id>');
	seasonRequest.addEventListener('load', function () {
		let seasonData = JSON.parse(seasonRequest.responseText);

	});
	seasonRequest.send();
}