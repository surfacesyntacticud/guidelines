"""
Pour lancer le script : 

python3 build_ag-grid_table.py --request_file chemin/vers/requetes/json --corpora_file chemin/vers/json/corpus
"""
import datetime
import argparse
import sys
import json
from grewpy import Request, Corpus, set_config

set_config('sud')

def esc_request (r):
  string_request = str(r)
  # replace quotes by the urlencoding (%22) for proper rendering when grew-match is called
  string_request = string_request.replace("\"", "%22")
  return string_request

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--request_file', help='Path to the JSON file containing the requests')
    parser.add_argument('--corpora_file', help='Path to the JSON file containing the corpora')
    args = parser.parse_args()

    request_file = args.request_file
    corpora_file = args.corpora_file


    with open(request_file, "rb") as f:
      grew_requests = { x["id"]: Request.from_json(x["request"]) for x in json.load(f) }

    with open(corpora_file, "rb") as f:
      json_data = json.load(f)
      corpora = { x["id"]: x["directory"] for x in json_data["corpora"] }

    if __name__ == '__main__':
      main_dict = {}
      for corpus_name in corpora:
        corpus = Corpus(corpora[corpus_name])

        main_dict[corpus_name] = { id: corpus.count(grew_requests[id]) for id in grew_requests }
        corpus.clean()

      requests = { id: esc_request(grew_requests[id]) for id in grew_requests }
      columnDefs = [ { "field": "row_header", "headerName": "Treebank", "pinned": "left", "lockPinned": True} ] 
      columnDefs += [ {"field": id, "headerName": id } for id in grew_requests ]

      rowData = [ {"row_header": k1 } | { k2: main_dict[k1][k2] for k2 in main_dict[k1]} for k1 in main_dict]

      data = {
        "requests": requests,
        "grid": {
          "defaultColDef": {
            "width": 150,
            "sortable": True,
            "sortingOrder": ["desc", "asc"],
            "resizable": True
          },
          "columnDefs": columnDefs,
          "rowData": rowData
        }
      }

      print (json.dumps(data, indent=2, ensure_ascii=False))
