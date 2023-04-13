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


const grid = [
    [	0	,	0	,	0	,	0	,	0	,	4	,	0	,	5	,	2	],
    [	6	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	],
    [	9	,	0	,	5	,	0	,	2	,	0	,	0	,	3	,	0	],
    [	0	,	0	,	0	,	8	,	0	,	0	,	7	,	0	,	0	],
    [	2	,	0	,	3	,	0	,	4	,	0	,	0	,	9	,	0	],
    [	0	,	1	,	0	,	0	,	0	,	0	,	0	,	0	,	0	],
    [	5	,	0	,	1	,	0	,	0	,	7	,	9	,	0	,	0	],
    [	0	,	6	,	0	,	0	,	5	,	0	,	0	,	0	,	0	],
    [	0	,	4	,	0	,	0	,	0	,	0	,	0	,	1	,	0	] ]

if (solve(grid)) {
    for (let row = 0; row < grid.length; row++) {
        print(row);
    }
} else {
    print("No solution exists.");
}