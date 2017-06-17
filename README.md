# Conway's Game of Life in Node.js
by [Hector Yeomans](http://hyeomans.com)

Conway's Game of Life is a simulation "zero player" game where the initial state will trigger the evolution of the game.

You can interact with Game of Life by giving in different input patterns.

# How to use

You will need Node.js installed in your computer to be able to run.

* Clone this repo: [git@github.com:hyeomans/game-of-life.git](git@github.com:hyeomans/game-of-life.git)
* `cd game-of-life`
* `npm install`
* `npm start`

# Add your own pattern

Adding a new pattern could be added by using `gridInit.withSeed` function. This function will let you define:

* An emptyCell character
* An aliveCell character
* The size of the input grid by rows and columns
* An array of coordinates where an alive cell has to be present on the defined grid.

# Contributing

Submit your PR
