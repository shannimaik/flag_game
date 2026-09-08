# ----------------------IMPORTS------------------------
import pygame
import sys
# import Soldier
import consts
import screen
# endregion--------------------------------------------


state = {"is_window_open":True,
         "state": False}













def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN():
            if event.key == pygame.K_RIGHT:
                pass

            elif event.key == pygame.K_LEFT:
                pass

            elif event.key == pygame.K_UP:
                pass

            elif event.key == pygame.K_DOWN:
                pass


