import argparse
import json
import sys
from grewpy import Request, Corpus, set_config

def escape_request(r):
	"""replace quotes by the urlencoding (%22) for proper rendering when grew-match is called"""
	return str(r).replace("\"", "%22")

def load_json_file(filepath):
	try:
		with open(filepath, "r", encoding='utf-8') as f:
			return json.load(f)
	except Exception as e:
		print(f"Error reading {filepath}: {e}")
		sys.exit(1)

def main(request_file, corpora_file):
	grew_requests = {x["id"]: Request.from_json(x["request"]) for x in load_json_file(request_file)}
	corpora = {x["id"]: x["directory"] for x in load_json_file(corpora_file)}

	main_dict = {}
	for corpus_name, corpus_directory in corpora.items():
		corpus = Corpus(corpus_directory)
		main_dict[corpus_name] = {req_id: corpus.count(grew_requests[req_id]) for req_id in grew_requests}
		corpus.clean()

	requests = {req_id: escape_request(grew_requests[req_id]) for req_id in grew_requests}
	column_defs = [{"field": "row_header", "headerName": "Treebank", "pinned": "left", "lockPinned": True}]
	column_defs += [{"field": req_id, "headerName": req_id} for req_id in grew_requests]

	row_data = [
		{"row_header": corpus_name, **{req_id: main_dict[corpus_name][req_id] for req_id in main_dict[corpus_name]}}
		for corpus_name in main_dict
	]

	data = {
		"requests": requests,
		"grid": {
			"defaultColDef": {
				"width": 150,
				"sortable": True,
				"sortingOrder": ["desc", "asc"],
				"resizable": True
			},
			"columnDefs": column_defs,
			"rowData": row_data
		}
	}

	print(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Build an ag-grid table from requests and corpora.')
	parser.add_argument('--request_file', required=True, help='Path to the JSON file containing the requests')
	parser.add_argument('--corpora_file', required=True, help='Path to the JSON file containing the corpora')
	parser.add_argument('--config', default="sud", help='Config of the corpora (default: sud)')
	args = parser.parse_args()
	
	set_config(args.config)

	main(args.request_file, args.corpora_file)
