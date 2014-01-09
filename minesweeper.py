import random

class Board(object):

	def __init__(self, rows, cols, mines):
		'''Generate board and place mines randomly'''
		pass

	def __str__(self):
		'''Print string representation of the board'''
		pass

	def placeMine(self):
		pass	

	def placeFlag(self):
		pass

class Cell(object):
	def __init__(self, row, col, board):
		#is_mine
		#is_visible
		#is_flag
		pass

	def generateNeighborList(self):
		neighborList = []
		return neighborList

	def countSurroundingMines(self):
		'''Call neighborList on cell, iterate through list and generate mine count'''
		pass

	def cellDisplay(self):
		'''Shows what string element to display for the cell
		If visible, display count of surrounding mines'''
		pass




board = Board(10, 10, 10)