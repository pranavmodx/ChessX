from .piece import Piece


class Pawn(Piece): 
	value = 1 

	def __init__(self, p_no=None, colour='White', p_type='Pawn'):
		super().__init__(p_type, p_no, colour)
		self.start_pos = True # Special case for pawns

	def valid_moves(self, is_flipped=False):
		x = self.pos[0]
		y = self.pos[1]
		SQ_SZ = self.size()
		BD_SZ = SQ_SZ * 8
		valids = []

		if not is_flipped:
			if self.colour == 'Black':
				valids.append((x - SQ_SZ, y + SQ_SZ))
				valids.append((x + SQ_SZ, y + SQ_SZ))

				if self.start_pos:
					valids.append((x, y + SQ_SZ))
					valids.append((x, y + 2 * SQ_SZ))
				else:
					valids.append((x, y + SQ_SZ))

			else:
				valids.append((x - SQ_SZ, y - SQ_SZ))
				valids.append((x + SQ_SZ, y - SQ_SZ))

				if self.start_pos:
					valids.append((x, y - SQ_SZ))
					valids.append((x, y - 2 * SQ_SZ))
				else:
					valids.append((x, y - SQ_SZ))

		else:
			if self.colour == 'White':
				valids.append((x - SQ_SZ, y + SQ_SZ))
				valids.append((x + SQ_SZ, y + SQ_SZ))

				if self.start_pos:
					valids.append((x, y + SQ_SZ))
					valids.append((x, y + 2 * SQ_SZ))
				else:
					valids.append((x, y + SQ_SZ))

			else:
				valids.append((x - SQ_SZ, y - SQ_SZ))
				valids.append((x + SQ_SZ, y - SQ_SZ))

				if self.start_pos:
					valids.append((x, y - SQ_SZ))
					valids.append((x, y - 2 * SQ_SZ))
				else:
					valids.append((x, y - SQ_SZ))

		return valids
