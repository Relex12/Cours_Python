from math import fabs

def papillon (n):
	"""Réalise un papillon avec des étoiles"""

	i = 1
	j = 1
	print (" ")
	while j < n/2:
		print ("* " * i, "  " * int (fabs(n-2*i-1)), "* " * i)
		i+=1
		j+=1
	print ("* " * n)
	j+=1
	i-=1
	while j <= n:
		print ("* " * i, "  " * int (fabs(n-2*i-1)), "* " * i)
		i-=1
		j+=1


if __name__ == '__main__':
	i = 1
	while i < 105:
		papillon (i)
		i+=1
	while i > 0:
		papillon (i)
		i-=1
