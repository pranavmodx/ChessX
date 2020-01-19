from .piece import Piece
from board import BD_SZ, SQ_SZ


class Pawn(Piece): 
	value = 1 

	def __init__(self, p_no=None, colour='White', p_type='Pawn', captured=False):
		super().__init__(p_type, p_no, colour, captured)
		self.start_pos = True # Special case for pawns

	def valid_moves(self, is_flipped=False):
		valids = []

		if not is_flipped:
			if self.colour == 'Black':
				if self.start_pos:
					valids.append((self.pos[0], self.pos[1] + SQ_SZ))
					valids.append((self.pos[0], self.pos[1] + 2 * SQ_SZ))
					# self.start_pos = False
				else:
					valids.append((self.pos[0], self.pos[1] + SQ_SZ))

			else:
				if self.start_pos:
					valids.append((self.pos[0], self.pos[1] - SQ_SZ))
					valids.append((self.pos[0], self.pos[1] - 2 * SQ_SZ))
					# self.start_pos = False
				else:
					valids.append((self.pos[0], self.pos[1] - SQ_SZ))

		else:
			if self.colour == 'White':
				if self.start_pos:
					valids.append((self.pos[0], self.pos[1] + SQ_SZ))
					valids.append((self.pos[0], self.pos[1] + 2 * SQ_SZ))
					# self.start_pos = False
				else:
					valids.append((self.pos[0], self.pos[1] + SQ_SZ))

			else:
				if self.start_pos:
					valids.append((self.pos[0], self.pos[1] - SQ_SZ))
					valids.append((self.pos[0], self.pos[1] - 2 * SQ_SZ))
					# self.start_pos = False
				else:
					valids.append((self.pos[0], self.pos[1] - SQ_SZ))

		return valids
