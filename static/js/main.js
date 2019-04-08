function collectData() {
	let showsRequest = new XMLHttpRequest();
	showsRequest.open('GET', '/table');
	showsRequest.addEventListener('load', function () {
		let shows = JSON.parse(showsRequest.responseText);
		console.log(shows);
		showsTable(shows);
	});
	showsRequest.send();
}

function showsTable(shows) {
	let mainTable = document.getElementById('mainTable');
	let tableHeaders = `
              <thead>
                <tr>
                    <th>Title</th>
                    <th>Year</th>
                    <th>Time</th>
                    <th>Genres</th>
                    <th>Rating</th>
                    <th>Trailer</th>
                    <th>WWW</th>
                </tr>
                </thead>
                <tbody id="tableBody"></tbody>
            `;
	mainTable.insertAdjacentHTML('afterbegin', tableHeaders);

	for (let i = 0; i <= shows.length; i++) {
		let tableBody = document.getElementById('tableBody')

		let tableRow = `
				<tr>
                    <td><a href="/tv-show/${shows[i]['id']}">${shows[i]['title']}</a></td>
                    <td>${shows[i]['year']}</td>
                    <td>${shows[i]['runtime']}</td>
                    <td>${shows[i]['genres']}</td>
                    <td>${shows[i]['rating']}</td>
                    <td><a href="${shows[i]['trailer']}">${shows[i]['trailer']}</a></td>
                    <td><a href="${shows[i]['homepage']}">${shows[i]['homepage']}</a></td>
                </tr>
		`;
		tableBody.insertAdjacentHTML('beforeend', tableRow);
	}

}


collectData();