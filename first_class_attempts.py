# creating a class 

class names_of_goat_anime():
    '''This document is to just follow general convention'''
    def __int__(self, name, year, genre, still_running):
        self.name = name
        self.year = year
        self.genre = genre
        self.still_running = still_running
    
    def table_of_anime(self):
        print(f' Name: {name}, premier year {year}, genre : {genre}, still_running : {still_running} ' )

a1 = ('Dragonball', 1980, 'Shounen', True)
a2 = ('Naruto', 2002, 'Shounen', True)
a3 = ('Bleach', 2004, 'Shounen/Action', False)
a4 = ('AOT', 2015, "Horror", False)

print(a1.table_of_anime)
print(a2.table_of_anime)
print(a3.table_of_anime)
print(a4.table_of_anime)