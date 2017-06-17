const gameOfLife      = require('./gameOfLife');
const gridInit        = require('./gridInit');

const aliveCellChar = '#';
const emptyCellChar = '_';

const seed = gridInit.withSeed(emptyCellChar,
  aliveCellChar,
  3,
  3,
  [ [0, 1], [1, 2], [2, 0], [2, 1], [2, 2] ]
);

const draw = gameOfLife(aliveCellChar, emptyCellChar, 25, 25, seed);

setInterval(() => draw(), 70);
