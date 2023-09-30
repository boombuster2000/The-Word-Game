from os import system
import random
import time

def clearscreen():
    system('CLS')
    print("===================================")
    print("~~~ The Word Game ~~~")
    print("Created by Ethan Williams")
    print("===================================")
    print("\n")

def gen_number():
    Number = random.randrange(0,10)
    return Number

def get_endings():
    with open('./Endings.txt', encoding = 'utf8') as file:
        Endings = file.readlines()
        return Endings

def game():
    Verb = input("Enter a verb: ")
    Adjective = input("Enter an adjective: ")
    Noun = input("Enter a noun: ")
    return Verb, Adjective, Noun

def save_sentence(Sentence):
     with open("./Sentences.txt", 'a', encoding='utf8') as file:
         file.write(''.join(Sentence))


while True:
    clearscreen()
    get_endings()
    Inputs = game()
    Sentence = ("The " + Inputs[1] + " " + Inputs[2] + " can " + Inputs[0]+ " " + get_endings()[gen_number()] + "\n")
    print(Sentence)
    save_sentence(Sentence)
    
    time.sleep(5)