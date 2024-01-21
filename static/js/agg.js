var global = 0 // global counting to prevent multi rendering of tables

function cell(requests, data) {
  if (data.colDef.field == "row_header") {
    return (`<b>${data.value}</b>`)
  } else {
    let request = requests[data.colDef.headerName];
    return `<a class="btn btn-success btn-sm" onclick='grew_match("${data.data.row_header}","${request}")'>${data.value}</a>`;
  }
}

function grew_match(treebank,request) {
  let url = `https://universal.grew.fr?corpus=${treebank}&request=${request}`
  console.log(url);
  window.open(url, '_blank');
}

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', () => {
  global += 1; // count the number of time this code is called
  let all_tables = document.querySelectorAll('.agg');
  
  if (global == all_tables.length) { // run the tables rendering only on the last call
    all_tables.forEach(table => {
      fetch('./'+table.id+'.json')
      .then((response) => response.json())
      .then((json) => {
        let grid = json.grid
        grid.defaultColDef.cellRenderer = (data => cell (json.requests, data));
        agGrid.createGrid(table, grid)
      });
    })
  }
})
