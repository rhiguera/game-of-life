const path            = require('path');
const expect          = require('chai').expect;
const gameOfLife      = require(path.join('..', 'src', 'gameOfLife'));

describe('Game of life Tests', () => {
  describe('On update', () => {
    it('should return the expected grid after two cycles', () => {
      const inputGrid = [
        ['_', '#', '_'],
        ['_', '_', '#'],
        ['_', '#', '#']
      ];

      const expectedGrid = [
        ['_', '_', '_'],
        ['_', '_', '#'],
        ['_', '#', '#']
      ];

      const game = gameOfLife('#', '_', 3, 3, inputGrid);
      const result = game.update(inputGrid);

      expect(result).to.deep.equal(expectedGrid);
    });
  });
})

