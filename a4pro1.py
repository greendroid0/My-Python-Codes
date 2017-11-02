movie_stars = [('Jack Nicholson',75),('Marlon Brando', 45),('Robert De Niro',
114),('Al Pacino', 56),('Daniel Day-Lewis', 29),('Marilyn Monroe', 33),
('Tom Hanks', 84),('Anthony Hopkins', 131),('Meryl Streep', 81),
('Denzel Washington', 56)] 
movie_stars = sorted(movie_stars, key=lambda movie_stars:movie_stars[1])
movie_stars = list(reversed(movie_stars))
print("Name", "\t\t", "Appearances")
print("---------------","","-----------")
for movie in movie_stars:
	print(movie[0], end="")
	for i in range(len(movie[0]), 21):
		print(" ", end="")
	print(movie[1])
