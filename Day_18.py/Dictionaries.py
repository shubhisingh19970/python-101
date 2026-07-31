movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
print("{Dictionaries}")

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
movie['title'] = 'The Holy Grail'
movie['budget'] = 250000
print(movie)

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
movie['budget'] = 250000
del movie['year']
print(movie)


movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

print(len(movie))

print(movie.keys())

for key in movie:
    print(key)

for key, value in movie.items():
    print(key, value)