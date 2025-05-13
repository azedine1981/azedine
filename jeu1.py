#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 21:54:04 2025

@author: rah1981
"""
 import pygame
 pygame.init()
 fen.display.set_mode((600,400))
 fen.display.set_caption("un jeu")
 
 
 
 running=True
 While running:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running == False

 pygame.quit()