

haitian_creole_tables:
	python3 build_ag-grid_table.py \
	--request_file haitian_creole/requests/request_haitian_creole_subj.json \
	--corpora_file haitian_creole/sud_haitian_creole.json \
	> ../static/tables/table_output_haitian_creole_subj.json

french_tables:
	python3 build_ag-grid_table.py \
	--request_file french/requests/request_french_subj.json \
	--corpora_file french/sud_french.json \
	> ../static/tables/table_output_french_subj.json

zaar:
	python3 build_table_cluster.py \
	--corpora_file zaar_corpus.json \
	> ../static/tables/zaar_pos_clust.json
