print("Input format: enter rows separated by new lines and in the form a b c d")
print("To finish entering rows, press Enter twice")
print("Ctrl+C to exit")
while True:
	print("Enter matrix:")
	matrix = []
	while True:
		row = input("")
		if row == "":
			print("\\begin{bmatrix}", end="")
			for i in range(len(matrix)):
				for j in range(len(matrix[i])):
					if (j == len(matrix[i]) - 1) and (i != len(matrix) - 1):
						print(matrix[i][j], " \\\\ ", sep="", end="")
					elif (j == len(matrix[i]) - 1) and (i == len(matrix) - 1):
						print(matrix[i][j], sep="", end="")
					else:
						print(matrix[i][j], " & ", sep="", end="")
			print("\\end{bmatrix}\n")
			break
		row = row.split(" ")
		matrix.append(row)


