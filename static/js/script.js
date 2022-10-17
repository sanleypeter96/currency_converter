// fetch("../data/jsonData.json")
// .then(function(response){
// 	return response.json();
// })
// .then(function(jsonData){
// 	let placeholder = document.querySelector("#data-output");
// 	let out = "";
// 	for(let data of jsonData){
// 		out += `
// 			<tr>
// 				<td>${data.Source_Currency} </td>
// 				<td>${data.Destination_Currency}</td>
// 				<td>${data.Source_Amount}</td>
// 				<td>${data.Rate}</td>
// 				<td>${data.Converted_Amount}</td>
// 			</tr>
// 		`;
// 	}

// 	placeholder.innerHTML = out;
// });