import random
import json, ssl
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

#Hangman pics
HANGMAN_PICS = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       ☹   |
           |
           |
          ===''', '''
       +---+
       ☹   |
       |   |
           |
          ===''', '''
       +---+
       ☹   |
      /|   |
           |
          ===''', '''
       +---+
       ☹   |
      /|\  |
           |
          ===''', '''
       +---+
       ☹   |
      /|\  |
      /    |
          ===''', '''
       +---+
       ☹   |
      /|\  |
      / \  |
          ===''']
counter = 0
# print(HANGMAN_PICS[counter])
# counter+=1
# print(HANGMAN_PICS[counter])
# counter+=1
# print(HANGMAN_PICS[counter])
# counter+=1
# print(HANGMAN_PICS[counter])
# counter+=1
# print(HANGMAN_PICS[counter])
# counter+=1
# print(HANGMAN_PICS[counter])
# counter+=1


# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
cryptocoinURL = "https://random-data-api.com/api/crypto_coin/random_crypto_coin"
req = urllib.request.Request(cryptocoinURL)
r = json.loads(urllib.request.urlopen(req).read())

cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**r)

# print(cryptocoin.coin_name)

AttemptedLetters = []

print(len(cryptocoin.coin_name) * " _")

# print(cryptocoin.coin_name[0])

# if input == cryptocoin.coin_name[0]

specialChar = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "[", "]", "{", "}", "="]

def getInput():
   while(True):
      guess=input("What is your guess?").lower()
      if guess.isnumeric()== True :
         print("Must be a letter.")
         continue

      if len(guess) !=1 :
         print("Must be only one letter!")
         continue

      # for i in specialChar:
      if not guess.isalpha():
         print("Can't include special characters.")
         continue

      if (guess in AttemptedLetters):
         print("You already used this letter.")
         continue
      
      # if letter not in my word, increment counter
      if guess not in cryptocoin.coin_name:
         counter = counter + 1
         print(HANGMAN_PICS[counter])

      AttemptedLetters.append(guess)
      return guess


def printword():
   temp:str= ""
   len(cryptocoin.coin_name.lower())
   for letter in cryptocoin.coin_name.lower() :
      # print(letter)
      
      if letter in AttemptedLetters:
         temp+= letter
      else: 
         temp+= "_ "
   print(temp)
   # return temp

while True :
   print(HANGMAN_PICS[counter])
   getInput()
   printword()
   
   # break condition

   # if guessed :
   #    break
   # if counter == len(HANGMAN_PICS):
   #    print("LOST")
   #    break

