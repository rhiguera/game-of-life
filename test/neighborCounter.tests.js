const path            = require('path');
const expect          = require('chai').expect;
const neighborCounter = require(path.join('..', 'src', 'neighborCounter'));

describe('neighborCounter tests', () => {
  it('returns 8 when all surrounded', () => {
    const cellGrid = '#'
    const inputGrid = [
      ['#', '#', '#'],
      ['#', '#', '#'],
      ['#', '#', '#']
    ];
    const neighbors = neighborCounter(cellGrid);

    const result = neighbors(1, 1, inputGrid);

    expect(result).to.eql(8);
  });

  it('returns 4 when star is formed', () => {
    const cellGrid = '#'
    const inputGrid = [
      [' ', '#', ' '],
      ['#', '#', '#'],
      [' ', '#', ' ']
    ];
    const neighbors = neighborCounter(cellGrid);

    const result = neighbors(1, 1, inputGrid);

    expect(result).to.eql(4);
  });

  it('returns 4 when across is filled', () => {
    const cellGrid = '#'
    const inputGrid = [
      ['#', ' ', '#'],
      [' ', '#', ' '],
      ['#', ' ', '#']
    ];
    const neighbors = neighborCounter(cellGrid);

    const result = neighbors(1, 1, inputGrid);

    expect(result).to.eql(4);
  });

  it('returns 3 for upperLeft corner', () => {
    const cellGrid = '#'
    const inputGrid = [
      ['#', '#', ' '],
      ['#', '#', ' '],
      [' ', ' ', ' ']
    ];
    const neighbors = neighborCounter(cellGrid);

    const result = neighbors(0, 0, inputGrid);

    expect(result).to.eql(3);
  });

  it('returns 3 for lowerRight corner', () => {
    const cellGrid = '#'
    const inputGrid = [
      [' ', ' ', ' '],
      [' ', '#', '#'],
      [' ', '#', '#']
    ];
    const neighbors = neighborCounter(cellGrid);

    const result = neighbors(2, 2, inputGrid);

    expect(result).to.eql(3);
  });
});
