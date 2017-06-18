const gameOfLife      = require('./gameOfLife');
const gridInit        = require('./gridInit');

const aliveCellChar = '#';
const emptyCellChar = '_';

const seed = gridInit.withSeed(emptyCellChar,
  aliveCellChar,
  3,
  3,
  [
    { row: 0, column: 1},
    { row: 1, column: 2},
    { row: 2, column: 0},
    { row: 2, column: 1},
    { row: 2, column: 2}
  ]
);

const game = gameOfLife(aliveCellChar, emptyCellChar, 25, 25, seed);

setInterval(() => game.draw(), 70);
