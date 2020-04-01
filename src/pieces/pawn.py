from pieces import Piece


class Pawn(Piece): 
	value = 1 

	def __init__(self, p_no=None, colour='White'):
		super().__init__(p_no, colour)
		self.start_pos = True # Special case for pawn - double push

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

	def handle_move(self, board, sq1_pos, sq2_pos, under_check=False):
		piece2 = board.fetch_piece_by_turn(sq2_pos, self.next_turn())

		dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

		if not piece2:
			if dist_x == 0 and sq2_pos in self.valid_moves():
				self.move(sq2_pos)

				if board.is_controlled_sq(board.king_pos[self.colour], self.colour):
					self.move(sq1_pos)
					return 0

				if self.start_pos:
					self.start_pos = False

				return 1

		else:
			if sq2_pos in self.valid_moves():
				# If there's a piece directly in front of self
				# 1 or 2 squares (2 if at start pos)
				if (abs(dist_y) != board.SQ_SZ and \
					abs(dist_y) != 2 * board.SQ_SZ) \
					or abs(dist_x) == board.SQ_SZ:
					if self.colour != piece2.colour:
						piece2.captured = True
						self.move(sq2_pos)

						if under_check:
							if board.is_controlled_sq(board.king_pos[self.colour], self.colour):
								piece2.captured = False
								self.move(sq1_pos)
								return 0

						if self.start_pos == True:
							self.start_pos = False

						return 1

		if board.king_pos[self.colour] in self.valid_moves(board.is_flipped) or \
			board.is_controlled_sq(board.king_pos[self.colour], self.colour):
			return -1
