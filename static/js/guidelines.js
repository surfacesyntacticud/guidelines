let def = "SUD_French-GSD@latest"

function grew_match_cluster(req, key1, whether1, key2, whether2, corpus) {
	// console.log ("req ==> "+req);
	// console.log ("key1 ==> "+key1);
	// console.log ("whether1 ==> "+whether1);
	// console.log ("key2 ==> "+key2);
	// console.log ("whether2 ==> "+whether2);
	let url = "https://universal.grew.fr"
	if (corpus) {
    url += "?corpus="+corpus
	} else {
    url += "?corpus="+def
	}
	url += "&request="+req
	if (key1) { url += "&clust1_key="+key1 }
	if (whether1) { url += "&clust1_whether="+whether1 }
	if (key2) { url += "&clust2_key="+key2 }
	if (whether2) { url += "&clust2_whether="+whether2 }
	window.open(encodeURI(url));
}
