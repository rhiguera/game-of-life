const path            = require('path');
const expect          = require('chai').expect;
const gridInit          = require(path.join('..', 'src', 'gridInit'));


describe('Grid init tests', () => {
  it('returns an empty grid', () => {
    const expectedOutput = [
      [' ', ' ', ' '],
      [' ', ' ', ' '],
      [' ', ' ', ' ']
    ];

    const result = gridInit.empty(' ', 3, 3);
    expect(result).to.deep.equal(expectedOutput);
  });

  it('returns a grid with seed', () => {
    const expectedSeed = [
        [' ', '#', ' '],
        [' ', ' ', '#'],
        ['#', '#', '#']
      ];

    const result = gridInit.withSeed(' ', '#', 3, 3, [ [0, 1], [1, 2], [2, 0], [2, 1], [2, 2] ]);

    expect(result).to.deep.equal(expectedSeed);
  });
});

