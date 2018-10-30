#!/usr/bin/env python

# Simulation to model demography on a landscape. This simulation 
# will include:
# - birth
# - death
# - dispersal

# First Version
# - Asexual reproduction
# - Annual generation times
# - Poisson-distributed number of offspring
# - Discrete landscape
# - Max dispersal of 1 grid
# - No diagonal dispersal
# - Equal probability of different directions
# - Non-zero probably of not dispersing
# - Starts in the middle
# - Start size of 50
# - No carrying capacity

# Object types
# - Individuals
# - Landscape
# - Cell

# Class Definitions

class landscape:
    """This class holds all individuals across the landscape"""

    def __init__(self,nRows=5,nColumns=5):
        self.nRows = nRows
        self.nColumns = nColumns
        self.sections = self.setup(self.nRows,self.nColumns)

    def setup(self,nRows,nColumns):
        """Sets up the landscape as a list of lists containing cells."""
        cellID = 0
        land = []
        for rowNum in range(nRows):
            row = []
            for colNum in range(nColumns):
                row.append(cell(cellID))
                cellID = cellID + 1
            land.append(row)
        return land

    def printLandscape(self):
        for row in self.sections:
            for col in row:
                 print(col.id)

class cell:
    """This class represents a grid square on our landscape."""

    def __init__(self,id):
        self.id = id


# Do stuff 

myLandscape = landscape()
myLandscape.printLandscape()