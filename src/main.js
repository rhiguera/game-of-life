const gameOfLife      = require('./gameOfLife');
const gridInit        = require('./gridInit');

const aliveCellChar = '#';
const emptyCellChar = '_';

const seed = gridInit.withSeed(emptyCellChar,
  aliveCellChar,
  3,
  3,
  [
    { row: 0, cell: 1},
    { row: 1, cell: 2},
    { row: 2, cell: 0},
    { row: 2, cell: 1},
    { row: 2, cell: 2}
  ]
);

const game = gameOfLife(aliveCellChar, emptyCellChar, 25, 25, seed);

setInterval(() => game.draw(), 120);
