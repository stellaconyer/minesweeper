import random

class Board(object):

	def __init__(self, row, col, mines):
		# Generate board and place mines randomly
		pass

	def printBoard(self):
		# Brint string representation of the board
		pass

	def placeMine(self):
		pass	

	def placeFlag(self):
		pass

	def __getitem__(self,(row,col)):
		return self.cell[row][column]

	class Cell(object):
		def __init__(self):
			#is_mine
			#is_visible
			#is_flag
			pass

		def generateNeighborList(self, row, col):
			pass

		def countSurroundingMines(self):
			pass

		def cellDisplay(self):
			# Shows what string element to display for the cell
			#If visible, display count of surrounding mines
			pass




board = Board(10, 10, 10)