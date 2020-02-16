from pieces import Piece


class Pawn(Piece): 
	value = 1 

	def __init__(self, p_no=None, colour='White', p_type='Pawn'):
		super().__init__(p_type, p_no, colour)
		self.start_pos = True # Special case for pawns - double push

	def valid_moves(self, is_flipped=False):
		x = self.pos[0]
		y = self.pos[1]

		SQ_SZ = self.size()
		BD_SZ = SQ_SZ * 8

		valids = []
		start_pos = self.start_pos

		def gen_valids1():
			valids = []

			valids.append((x - SQ_SZ, y + SQ_SZ))
			valids.append((x + SQ_SZ, y + SQ_SZ))
			valids.append((x, y + SQ_SZ))

			if start_pos:
				valids.append((x, y + 2 * SQ_SZ))

			return valids

		def gen_valids2():
			valids = []

			valids.append((x - SQ_SZ, y - SQ_SZ))
			valids.append((x + SQ_SZ, y - SQ_SZ))
			valids.append((x, y - SQ_SZ))

			if start_pos:
				valids.append((x, y - 2 * SQ_SZ))

			return valids

		if not is_flipped:
			if self.colour == 'Black':
				valids = gen_valids1()
			else:
				valids = gen_valids2()

		else:
			if self.colour == 'White':
				valids = gen_valids1()
			else:
				valids = gen_valids2()

		return valids
