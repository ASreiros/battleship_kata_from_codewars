# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
#
# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.
#
#
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.
#
# The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.



def validate_battlefield(field):
	flag = True
	ships = {
		"four": 1,
		"three": 2,
		"two": 3,
		"one": 4
	}
	skip = []
	for n in range(len(field)):
		if not flag:
			break
		for m in range(len(field[n])):
			if not flag:
				break
			address = f'{n}{m}'
			if address not in skip:
				print(address, "  ", field[n][m])
				if field[n][m] == 1:
					skip.append(f'{n}{m}')
					length = 1
					vertical = False
					horizontal = False
# check diagonal
					if n < 9:
						if m < 9:
							if field[n+1][m+1] == 1:
								print("diagonal")
								flag = False
						if m > 0:
							if field[n+1][m-1] == 1:
								print("diagonal")
								flag = False
					if n < 9:
						if field[n+1][m] == 1:
							vertical = True
					if m < 9:
						if field[n][m+1] == 1:
							horizontal = True
					print("horizontal:", horizontal, "vertical:", vertical)
					if horizontal and vertical:
						flag = False
# 	check horizontal
					elif horizontal:
						current = m
						check = True
						while check:
							current += 1
							if current < 10:
								if field[n][current] == 1:
									print(f"cheking {n}{current}")
									length += 1
									skip.append(f'{n}{current}')
									if n > 0:
										if field[n-1][current] == 1:
											flag = False
									if n < 9:
										if field[n+1][current] == 1:
											flag = False
								else:
									check = False
									if length == 2:
										ships["two"] -= 1
										print(address, "ship['two']", length)
									elif length == 3:
										ships["three"] -= 1
										print(address, "ship['three']", length)
									elif length == 4:
										ships["four"] -= 1
										print(address, "ship['four']", length)
									else:
										flag = False
										print(address, "wrong", length)
							else:
								check = False
								if length == 2:
									ships["two"] -= 1
									print(address, "ship['two']", length)
								elif length == 3:
									ships["three"] -= 1
									print(address, "ship['three']", length)
								elif length == 4:
									ships["four"] -= 1
									print(address, "ship['four']", length)
								else:
									flag = False
									print(address, "wrong", length)
					elif vertical:
						current = n
						check = True
						while check:
							current += 1
							if current < 10:
								if field[current][m] == 1:
									print(f"cheking {current}{m}")
									length += 1
									skip.append(f'{current}{m}')
									if m > 0:
										if field[current][m-1] == 1:
											flag = False
									if m < 9:
										if field[current][m+1] == 1:
											flag = False
								else:
									check = False
									if length == 2:
										ships["two"] -= 1
										print(address, "ship['two']", length)
									elif length == 3:
										ships["three"] -= 1
										print(address, "ship['three']", length)
									elif length == 4:
										ships["four"] -= 1
										print(address, "ship['four']", length)
									else:
										flag = False
										print(address, "wrong", length)
							else:
								check = False
								if length == 2:
									ships["two"] -= 1
									print(address, "ship['two']", length)
								elif length == 3:
									ships["three"] -= 1
									print(address, "ship['three']", length)
								elif length == 4:
									ships["four"] -= 1
									print(address, "ship['four']", length)
								else:
									flag = False
									print(address, "wrong", length)
						pass
					else:
						ships["one"] -= 1
						print(address, "ship['one']", length)
	print(ships)
	if ships["one"] != 0 or ships["two"] != 0 or ships["three"] != 0 or ships["four"] != 0:
		flag = False
	return flag


battleField =  [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
				[1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
				[1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
				[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
				[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

testfield =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]



print(validate_battlefield(testfield))

