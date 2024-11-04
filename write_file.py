filename = 'my_first_file.txt'

file = open(filename,mode='w')

movies = ['Scream','IT','The Nun','Anabelle','Friday The 13th']

for movie in movies:
    # print(movie)
    file.write(movie)
    file.write('\n')