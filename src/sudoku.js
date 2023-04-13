function parseInput() {
  const board = [];
  for (let i = 1; i <= 9; i++) {
    const row = [];
    for (let j = 1; j <= 9; j++) {
      const cell = document.getElementsByName(`cell-${i}-${j}`)[0];
      row.push(cell.value ? parseInt(cell.value) : 0);
    }
    board.push(row);
  }
  return board;
}

function findEmptyLocation(grid) {
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        if (grid[row][col] === 0) {
          return [row, col];
        }
      }
    }
    return null;
  }
  
function isValid(grid, row, col, num) {
  for (let i = 0; i < 9; i++) {
    if (grid[row][i] === num) {
      return false;
    }
    if (grid[i][col] === num) {
      return false;
    }
    if (grid[Math.floor(row / 3) * 3 + Math.floor(i / 3)][Math.floor(col / 3) * 3 + (i % 3)] === num) {
      return false;
    }
  }
  return true;
}
  
function solve(grid) {
  const emptyLoc = findEmptyLocation(grid);
  if (!emptyLoc) {
    return true;
  }
  const [row, col] = emptyLoc;
  for (let num = 1; num <= 9; num++) {
    if (isValid(grid, row, col, num)) {
      grid[row][col] = num;
      if (solve(grid)) {
        return true;
      }
      grid[row][col] = 0;
    }
  }
  return false;
}

function solveSudoku() {

  const inputTable = document.getElementsByTagName("table")[0];
  const inputRows = inputTable.getElementsByTagName("tr");
  const inputValues = [];
  for (let i = 0; i < inputRows.length; i++) {
    const inputCols = inputRows[i].getElementsByTagName("td");
    const rowValues = [];
    for (let j = 0; j < inputCols.length; j++) {
      item = parseInt(inputCols[j].firstChild.value);
      if (isNaN(item)) item = 0;
      rowValues.push(item);
    }
    inputValues.push(rowValues);
  }

  solve(inputValues);
  printOut(inputValues);
  document.getElementById("resultHeader").style.display = "block";
}

function printOut(inputValues) {
  const resultTable = document.getElementById("resultTable");
  resultTable.innerHTML = "";
  for (let i = 0; i < inputValues.length; i++) {
    const resultRow = document.createElement("tr");
    for (let j = 0; j < inputValues[i].length; j++) {
      const resultCol = document.createElement("td");
      resultCol.textContent = inputValues[i][j];
      resultRow.appendChild(resultCol);
    }
    resultTable.appendChild(resultRow);
  }
}