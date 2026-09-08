import pygame

'''create a new solider'''
def create_solider():
    return {"img": pygame.image.load('soldier.png'),
            "list_of_body_position":[(0,0),(1,0),(0,1),(1,1),(0,2),(1,2)] ,
            "list_of_legs_position":[(0,3),(1,3)],

    }
