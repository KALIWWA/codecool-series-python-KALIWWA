function collectActors() {
	const actorsRequest = new XMLHttpRequest();
	actorsRequest.open('GET', '/actors-data');
	actorsRequest.addEventListener('load', function () {
		let actorsData = JSON.parse(this.responseText);
		console.log(actorsData);
	});

	actorsRequest.send();
}

collectActors();