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

    const result = gridInit.withSeed(' ',
      '#',
      3,
      3,
      [
        { row: 0, column: 1},
        { row: 1, column: 2},
        { row: 2, column: 0},
        { row: 2, column: 1},
        { row: 2, column: 2}
      ]);

    expect(result).to.deep.equal(expectedSeed);
  });

  it('throws when seed coordinates are out of bound', () => {
    const expectedSeed = [
        [' ', '#', ' '],
        [' ', ' ', '#'],
        ['#', '#', '#']
      ];

    const result = gridInit.withSeed.bind(null, ' ',
      '#',
      3,
      3,
      [
        { row: 0, column: 1},
        { row: 1, column: 2},
        { row: 2, column: 0},
        { row: 2, column: 1},
        { row: 2, column: 4}
      ]

    );

    expect(result).to.throw('Row in { 2 , 4 } is out of bounds. Max is 3');
  });
});

