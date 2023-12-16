let treebank = "SUD_French-GSD@latest"

function grew_match_search(msg) {
	let url = "https://universal.grew.fr?corpus="+treebank+"&request="+msg
	window.open(encodeURI(url));
}