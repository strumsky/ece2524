#!/usr/bin/env python

import re
from sys import stdin,stdout,stderr

def startGame():
    stand = raw_input('\n\033[1;33m()\033[1;31mxxxx\033[1;33m{\033[1;30m===============>\033[0m\nPlease enter your name: ')
    playerName = '\033[1;34m' + stand + ' the Strong\033[0m'
    print ("Your name is " + playerName)
    stderr.write("\nThe journey begins...\n")
    steps = raw_input('\nHow many steps do you want to take into the forest? ')

    if(steps == "0" or steps == "1" or steps == "2"):
        stdout.write('This is a \033[1;31mmonster\033[0m.')
    elif(steps == "3"):
        stdout.write('Nothing is there.')
    elif(steps == "4" or steps == "5" or steps == "6"):
        stdout.write('This is a \033[1;32mwild animal\033[0m.')
    elif(steps == "7" or steps == "8" or steps == "9"):
        stdout.write('This is a \033[1;35mzombie\033[0m.')
    else:
        stdout.write('Nothing is there.')
    stdout.write('\n')
    stdout.write('BATTLE SEQUENCE\n')

if __name__=='__main__':
    from sys import stdin, stdout, stderr
    startGame()
