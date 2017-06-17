const path            = require('path');
const expect          = require('chai').expect;
const glider          = require(path.join('..', 'src', 'glider'));

describe('Glider tests', () => {

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

    const result = glider(inputGrid, seed);

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

    const result = glider(inputGrid, seed);

    expect(result).to.deep.equal(seed);
    expect(result).to.not.equal(seed);
  });
});
