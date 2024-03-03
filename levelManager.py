import csv
import pygame 

class levelManager :
    def __init__(self, block_size) :
        self.level_data = []
        self.block_size = block_size

    
    def convertingToList(self, filename) : 
        with open( filename, "r") as csvfile:
            csv_data = csv.reader(csvfile, delimiter=",")
            for row in csv_data:
                self.level_data.append([int(i) for i in row])

               

    
    def drawing(self, screen) :
        #Reading the height(i) and the width(j)
        #Provide x and y where to draw 
        
        for y in range(len(self.level_data)) :
            for x in range(len(self.level_data[0])) :
                if self.level_data[y][x] == 0 :
                    pygame.draw.rect(screen, (255, 255, 255), [x * self.block_size, y * self.block_size, self.block_size, self.block_size])
    

    

                








