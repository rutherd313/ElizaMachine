# # -*- coding: utf-8 -*-
""" Eliza homework. Conversation with a computer """
__author__="John Dueno"

emotions_1 = ['good', 'great', 'happy', 'well', 'content', 'merry', 'joyful', 'jovial', 'delighted', 'disgusted', 'distressed', 'amazing']
emotions_2 = ['bad', 'sad', 'unwell', 'miserable', 'unhappy', 'despondent', 'saddened', 'frightened']

family = ['mother', 'mom', 'father', 'dad', 'brother', 'sister', 'friend', 'cousin', 'aunt', 'boyfriend',
          'girlfriend', 'boyfriend', 'uncle', 'pet', 'dog', 'cat']
locations = ['school', 'home', 'gym', 'market', 'work', 'restaurant', 'party', 'park', 'beach', 'movie']
actions = ['study', 'play', 'catch', 'eat', 'music', 'talk', 'shop', 'shop', 'sing', 'joke', 'dance', 'relax', 'sleep', 'lift', 'nap', 'fishing', 'watch']

end = ['bye', 'goodbye', 'adios']
familiar_list = ["Mhh, I've recalled that action from somewhere before", "That sounds familiar", "That rings a bell"]
unfamiliar_list = ["That may be the first time I've known of this.", "That doesn't sound familiar", "That doesn't ring a bell"]

import random
import re

def greet():
    name = input('Hello, I am Eliza, what is your name? ').strip()
    name_index = name.split(' ')
    name_index_pos = name_index.pop()
    return "Hello " + name_index_pos

def emotion():
    enter_feeling = input("How are you today? ").strip()
    feeling_index = enter_feeling.split(' ')
    for f in feeling_index:
        for n in emotions_1:
            for b in emotions_2:
                if n == f:
                    n_regx = [re.sub('ed$', enter_feeling, s) for s in feeling_index]
                    if n_regx:
                        return "Glad to know you feel " + n.removesuffix('ed') + " today!"
                    else: "Glad to know you feel " + n
                elif b == f:
                    b_regx = [re.sub('ened$', enter_feeling, s) for s in feeling_index]
                    if b_regx:
                        return "Sorry to know you are feeling " + b.removesuffix('ened')
                    else: return "Sorry to know you are feeling " + b
    else:
        return "It's alright to feel " + f + " every now and again!"

def act(acts):
    for x in acts:
        for y in actions:
            if x == y:
                return random.choice(familiar_list)
    else:
        return random.choice(unfamiliar_list)

def plans():
    todo = input("What do you like to do in your free time? ").strip()
    plans_index = todo.split(' ')
    for p in plans_index:
        for f in family:
            for l in locations:
                if f == p:
                    print("People and their relationships are interesting to me.")
                    todo_fam = input("What do you like to do with your " + p + "? ")
                    todo_fam_index = todo_fam.split(' ')
                    return act(todo_fam_index)

                elif l == p:
                    print("I've never been to a " + l + " before.")
                    todo_place = input("What is it that you do in a " + l + "? ")
                    todo_place_index = todo_place.split(' ')
                    return act(todo_place_index)
    else:
        print("I'm not familiar with this.")
        todo_else = input("Can you tell me more? ")
        todo_else_index = todo_else.split(' ')
        return act(todo_else_index)

class end_loop(Exception): pass

def expand():
    expand_input = input("What does this make you feel? (Type 'bye' or 'goodbye' to terminate conversation) ")
    expand_input_index = expand_input.split(' ')
    for ei in expand_input_index:
        for e in end:
            for b in emotions_2:
                for g in emotions_1:
                    if ei == g:
                        print("I'm glad that makes you feel " + g + "!")
                        expand()
                    elif ei == b:
                        print("Sorry that makes you feel " + b)
                        expand()
                    elif ei == e:
                        print("Nice talking with you!")
                        raise end_loop

    else:
        print("Very intriguing")
        expand()


z = True
try:
    while z:
        print(greet())
        print(emotion())
        print(plans())
        print(expand())
except end_loop:
    pass