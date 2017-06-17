const neighborCounter = require('./neighborCounter');
const cellLifeTime    = require('./cellLifeTime');
const copyAtCenter    = require('./copyAtCenter');
const gridInit        = require('./gridInit');

let neighbors;
let currentCellChar;
let currentEmptyChar;
let grid;

module.exports = function(cellChar, emptyChar, rows, columns, seed) {
  grid = gridInit.empty(emptyChar, rows, columns);

  copyAtCenter(grid, seed);

  neighbors = neighborCounter(cellChar);
  currentCellChar = cellChar;
  currentEmptyChar = emptyChar;

  return start(grid);
}

function start(grid) {
  draw(grid);

  return () => {
    const newGrid = [];
    for(let rowIndex = 0; rowIndex < grid.length; rowIndex += 1) {
      newGrid.push([]);
      for(let columnIndex = 0; columnIndex < grid[rowIndex].length; columnIndex += 1) {

        const neighborCount = neighbors(rowIndex, columnIndex, grid);

        const alive = grid[rowIndex][columnIndex] === currentCellChar;
        const shouldItLive = cellLifeTime.shouldItLive(alive, neighborCount);

        newGrid[rowIndex][columnIndex] = shouldItLive ? currentCellChar : currentEmptyChar;
      }
    }

    grid = newGrid;

    draw(grid);
  }
}

function draw(grid) {
  process.stdout.write('\033c');
  grid.forEach(row => console.log(row.join('')));
}
