import argparse
import json
import sys
from grewpy import Request, Corpus, set_config

def escape_request(r):
	"""replace quotes by the urlencoding (%22) for proper rendering when grew-match is called"""
	return str(r).replace("\"", "%22")

request = Request("pattern { X[upos] }")
clust_key = "X.upos"
def extended_request (clust_value):
	return Request(f"pattern {{ X[upos={clust_value}] }}")

def load_json_file(filepath):
	try:
		with open(filepath, "r", encoding='utf-8') as f:
			return json.load(f)
	except Exception as e:
		print(f"Error reading {filepath}: {e}")
		sys.exit(1)

def get_unique_keys(nested_dict):
    unique_keys = set()  # Initialize an empty set to store unique keys
    for inner_dict in nested_dict.values():  # Iterate through values of the main dictionary
        if isinstance(inner_dict, dict):  # Ensure the value is a dictionary
            unique_keys.update(inner_dict.keys())  # Update the set with keys from the inner dictionary


def main(corpora_file):
	corpora = {x["id"]: x["directory"] for x in load_json_file(corpora_file)}
	clustered_counts = {}
	for corpus_name, corpus_directory in corpora.items():
		corpus = Corpus(corpus_directory)
		clustered_counts[corpus_name] = corpus.count(request, clustering_keys=[clust_key])
		corpus.clean()
	all_keys = set()
	for clustered_count in clustered_counts.values():
		all_keys.update(clustered_count.keys())
	grew_requests = {req_id: extended_request (req_id) for req_id in all_keys }

	main_dict = {}
	for corpus_name in corpora.keys():
		clustered_count = clustered_counts[corpus_name]
		main_dict[corpus_name] = {req_id: clustered_count.get(req_id, 0) for req_id in all_keys}

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
				"width": 100,
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
	parser.add_argument('--corpora_file', required=True, help='Path to the JSON file containing the corpora')
	parser.add_argument('--config', default="sud", help='Config of the corpora (default: sud)')
	args = parser.parse_args()
	
	set_config(args.config)

	main(args.corpora_file)
