# Features

Grid -- Front end

Chunking -- Back end

objects -- Back end

world-gen -- Front end

camera -- Back end

player -- Front end

enemey -- Front end

Obstacle -- Front end

Movement -- Front end

physics -- front end

## Grid

Holds chunk data assuming 3.

#### Grid2D

Uses a global x, y posistion so 68 , 106 might be zone 3, 7 and chunk 7, 2 within that zone

Will by defualt use zoning

## Chunking (Back end)

Holds data about a 16 x 16 chunk

Asuming id system is used each item will be a u8 giving a total memory usage of 3.6 Kb

However Each object needs to be stored induvidualy so we will need to

have a big array with all objects

Will only commuincate with the grid object

### Zoneing (Optional)

Holds a array of 16 x 16 chunks will be used for terrain generation (I hope)
