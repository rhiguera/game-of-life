const path            = require('path');
const expect          = require('chai').expect;
const cellLifeTime    = require(path.join('..', 'src', 'cellLifeTime'));

describe('Cell lifetime', () => {
  it('should live with two neighbors', () => {

    const result = cellLifeTime.shouldItLive(true, 2);

    expect(result).to.be.true;
  });

  it('should live with three neighbors', () => {

    const result = cellLifeTime.shouldItLive(true, 3);

    expect(result).to.be.true;
  });

  it('should die with fewer than 2 neighbors', () => {

    const result = cellLifeTime.shouldItLive(true, 1);

    expect(result).to.be.false;
  });

  it('should die with 0 neighbors', () => {

    const result = cellLifeTime.shouldItLive(true, 0);

    expect(result).to.be.false;
  });

  it('should die with more than three neighbors', () => {

    const result = cellLifeTime.shouldItLive(true, 4);

    expect(result).to.be.false;
  });

  it('should live when dead and has 3 neighbors', () => {

    const result = cellLifeTime.shouldItLive(false, 3);

    expect(result).to.be.true;
  });

});
