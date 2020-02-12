from .piece import Piece


class Pawn(Piece): 
	value = 1 

	def __init__(self, p_no=None, colour='White', p_type='Pawn'):
		super().__init__(p_type, p_no, colour)
		self.start_pos = True # Special case for pawns

	def valid_moves(self, is_flipped=False):
		x = self.pos[0]
		y = self.pos[1]
		sq_size = self.size()
		bd_size = sq_size * 8
		valids = []

		if not is_flipped:
			if self.colour == 'Black':
				valids.append((x - sq_size, y + sq_size))
				valids.append((x + sq_size, y + sq_size))

				if self.start_pos:
					valids.append((x, y + sq_size))
					valids.append((x, y + 2 * sq_size))
				else:
					valids.append((x, y + sq_size))

			else:
				valids.append((x - sq_size, y - sq_size))
				valids.append((x + sq_size, y - sq_size))

				if self.start_pos:
					valids.append((x, y - sq_size))
					valids.append((x, y - 2 * sq_size))
				else:
					valids.append((x, y - sq_size))

		else:
			if self.colour == 'White':
				valids.append((x - sq_size, y + sq_size))
				valids.append((x + sq_size, y + sq_size))

				if self.start_pos:
					valids.append((x, y + sq_size))
					valids.append((x, y + 2 * sq_size))
				else:
					valids.append((x, y + sq_size))

			else:
				valids.append((x - sq_size, y - sq_size))
				valids.append((x + sq_size, y - sq_size))

				if self.start_pos:
					valids.append((x, y - sq_size))
					valids.append((x, y - 2 * sq_size))
				else:
					valids.append((x, y - sq_size))

		return valids
