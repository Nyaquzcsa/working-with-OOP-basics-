class names_of_goat_anime():
    '''This document is to just follow general convention'''
    def __init__(self, name, year, genre, still_running):
        self.name = name
        self.year = year
        self.genre = genre
        self.still_running = still_running
    
    def table_of_anime(self):
        print(f' Name: {self.name}, premier year {self.year}, genre : {self.genre}, still_running : {self.still_running} ' )

a1 = names_of_goat_anime('Dragonball', 1980, 'Shounen', True)
a2 = names_of_goat_anime('Naruto', 2002, 'Shounen', True)
a3 = names_of_goat_anime('Bleach', 2004, 'Shounen/Action', False)
a4 = names_of_goat_anime('AOT', 2015, "Horror", False)

a1.table_of_anime()
a2.table_of_anime()
a3.table_of_anime()
a4.table_of_anime()
