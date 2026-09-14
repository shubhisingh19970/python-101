#Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.



#1
movie = {
    'title':'Life of Pi',
    'Year':2012,
    'Cate':['John','Jill','Jack']

}
print(movie)
#If we want to print parts of it
print(movie['title'])

#If you want to update the dictionary
movie['title'] = 'The Holy'
print(movie.get('title'))
#If u wanna set something that doesn't exists
print(movie.get('budget','not found'))
movie['budget'] = 250000
print(movie.get('budget'))

#If u wanna update the whole dictionary 

movie.update({'tittle':'The Holy',
              'year':1975,'cast':['John','Jack','Wes']})
print(movie)

# If u wanna delete entries 
#del movie ['year']
#print(movie)

#pop command 
year = movie.pop ('year')
print(year)

#If u want the length of the dictionary how many entries there are
print(len(movie))
print(movie.keys())
print(movie.values())
print(movie.items())
