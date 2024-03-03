import csv
import pygame 

class levelManager :
    def __init__(self) :
        pass

<<<<<<< HEAD
    
    def convertingToList(self, filename) : 
        self.level_data = []
        with open( filename, "r") as csvfile:
            csv_data = csv.reader(csvfile, delimiter=",")
            for row in csv_data:
                self.level_data.append(row)

               

    
    def drawing(self, screen) :
        #Reading the height(i) and the width(j)
        #Provide x and y where to draw 
        
        for i in range(len(self.level_data)) :
            for j in range(len(self.level_data)) :
                if self.level_data[i][j] == 0 :
                    pygame.draw.rect(screen, (255, 255, 255) [i, j, 20, 20])

    

                








=======
    def TestList():
        List = [[0, 1, 0], [1, 0, 1]]
        for i in List :
            for j in i :
                if j == 0 :
                    pass                
    
>>>>>>> 8704f8c6ece8453e07ceaab367b84e7a2c2ffcb2
