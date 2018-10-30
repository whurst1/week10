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

import numpy.random as nr 

# Class Definitions

class landscape:
    """This class holds all individuals across the landscape"""

    def __init__(self,nRows=5,nColumns=5,startSize=50):
        self.nRows = nRows
        self.nColumns = nColumns
        self.startSize = startSize
        self.sections = self.setup(self.nRows,self.nColumns)
        for _ in range(self.startSize):
            self.sections[0][0].individuals.append(ind())


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
        """Print all id numbers of cells in landscape"""
        for row in self.sections:
            print("New row:")
            for col in row:
                print(col.id)
                print("Number of individuals: %d" % (len(col.individuals)))


class cell:
    """This class represents a grid square on our landscape."""

    def __init__(self,id):
        self.id = id
        self.individuals = []

class ind:
    """This class represents individuals in our population."""
    
    def __init__(self,name="",rowPos=0,colPos=0):
        self.name = name
        self.offspring = []
        self.meanOffNum = 2.0
        self.rowPos = rowPos
        self.colPos = colPos

    def reproduce(self):
        """Return list of offspring"""
        numOff = nr.poisson(self.meanOffNum)
        offspringList = []
        for _ in range(numOff):
            offspringList.append(ind())
        return offspringList

    def disperse(self):
        """Move, if necessary, to new cell."""
        

# Do stuff 

myLandscape = landscape()
myLandscape.printLandscape()