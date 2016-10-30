# This program is to develop a random cipher
# The cipher's length is between 10 and 20,
# including figures(0-9), 26 letters and some common symbols.
# -*- coding: utf-8 -*-

import random
import easygui
import sys

# class begins
class RandomCipher:

    def __init__(self):
        self.__symbol = ('~', '!', '@', '#', '$', '%', '&',
                         '*', '(', ')', '_', '?', '.')       # 13 common symbols in cipher
        self.__original_cipher = []                                                         # save the original password
        self.__password = ""                                                                #save the final cipher with string


    def __developRandomSymbol(self):
        symbol_num = random.randint(1, 3)   # the number of symbols in cipher

        for i in range(symbol_num):    # develop the symbols
            self.__original_cipher.append(self.__symbol[random.randint(0, 12)])


    def __developRandomNumber(self):
        num_of_number = random.randint(5, 10)

        for i in range(num_of_number):   # develop the numbers
            self.__original_cipher.append(str(random.randint(0, 9)))


    def __developRandomLetter(self):
        letter_num = random.randint(4, 7)

        for i in range(letter_num):     # develop the letters
            self.__original_cipher.append(chr(random.randint(97, 122)))


    def MakeCipher(self):
    	# create original cipher
    	self.__developRandomSymbol()
    	self.__developRandomNumber()
    	self.__developRandomLetter()

    	# create final cipher
    	random.shuffle(self.__original_cipher)          # sort the original cipher to create the final cipher
    	self.__password = ''.join(self.__original_cipher)  # transform the final cipher to string


    def __str__(self):
    	msg = "Now got your ciper:\n"+self.__password
    	return msg

# class ends


# main function begins
flavor = easygui.buttonbox("""Welcome to random cipher developer!\n\n
	     Click "OK"to continue, "CANCLE" to exit. """,
	     choices = ['OK', 'CANCLE'])

if flavor == 'OK':
	easygui.buttonbox("Now, be ready to reate your password.",
		               choices = ['next'])

	cipher = RandomCipher()
	cipher.MakeCipher()          # develop the cipher

	easygui.buttonbox(cipher, choices = ['Yes, I know.'])
	easygui.msgbox("Thanks to use!")
	sys.exit()

else:
	easygui.msgbox("Thanks to use!")
	sys.exit()
