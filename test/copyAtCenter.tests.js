const path            = require('path');
const expect          = require('chai').expect;
const copyAtCenter    = require(path.join('..', 'src', 'copyAtCenter'));

describe('CopyAtCenter tests', () => {

  it('sets a grid with a given seed', () => {
    const inputGrid = [
      [' ', ' ', ' '],
      [' ', ' ', ' '],
      [' ', ' ', ' ']
    ];

    const seed = [
      [' ', '#', ' '],
      [' ', ' ', '#'],
      ['#', '#', '#']
    ];

    const result = copyAtCenter(inputGrid, seed);

    expect(result).to.deep.equal(seed);
    expect(result).to.not.equal(seed);
  });

  it('sets a large grid given a seed', () => {
    const inputGrid = [
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
    ];

    const seed = [
      ['#', ' ', ' ', ' ', '#'],
      ['#', ' ', ' ', ' ', '#'],
      ['#', ' ', ' ', ' ', '#'],
      ['#', ' ', ' ', ' ', '#'],
      ['#', ' ', ' ', ' ', '#'],
    ];

    const result = copyAtCenter(inputGrid, seed);

    expect(result).to.deep.equal(seed);
    expect(result).to.not.equal(seed);
  });
});
