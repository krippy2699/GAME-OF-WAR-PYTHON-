#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
suits = ('Clubs','Hearts','Spades','Diamonds')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
value = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}


# In[2]:


class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.intval = value[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[3]:


from random import shuffle

class Deck():
    
    def __init__(self):
        
        self.whole_stack = []
        
        for sui in suits:
            for ran in ranks:
                card = Card(sui,ran)
                self.whole_stack.append(card)
                
    def deal_one(self):
        return self.whole_stack.pop()
    
    def shuffling(self):
        shuffle(self.whole_stack)
        


# In[4]:


class Player():
    
    def __init__(self,name):
        
        self.name = name
        self.stack = []
    
    def __str__(self):
        return f'{self.name} has {len(self.stack)} cards.'
        
    def add_cards(self,new_card):
        # for if this is an actual list of cards from a WAR bet extend the size of the list
        if type(new_card) == type([]):
            self.stack.extend(new_card)
        else:
            self.stack.append(new_card)
            
    def remove_one(self):
        return self.stack.pop(0)
        
        


# In[26]:


#This block creates 2 players and splits the deck of 52 cards 
#into 26 cards each
p1 = input('Enter player #1 name: ')
p2 = input('Enter player #2 name: ')
player1 = Player(p1)
player2 = Player(p2)

deck = Deck()
deck.shuffling() 

for items in range(26):
    player1.add_cards(deck.deal_one())
    player2.add_cards(deck.deal_one())


# In[28]:


round_num = 1
game_on = True
War_bet = []
Wars_on = False

while game_on == True:
    
    if len(player1.stack) == 0:
        game_on = False
        print(f'Congratulations {player2.name} you WON !')
        break
        
    if len(player2.stack) == 0:
        game_on = False
        print(f'Congratulations {player1.name} you WON !')
        break
        
    else:
    
        print(f'Round #{round_num}.')
        cardp1 = player1.remove_one()
        print(cardp1)
        cardp2 = player2.remove_one()
        print(cardp2)

        if cardp1.intval > cardp2.intval:
            print(f'{player1.name} won this round !')
            player1.add_cards(cardp2)
            player1.add_cards(cardp1)
            if Wars_on == True:
                player1.add_cards(War_bet)
                War_bet.clear()
                Wars_on = False

        elif cardp1.intval < cardp2.intval:
            print(f'{player2.name} won this round !')
            player2.add_cards(cardp1)
            player2.add_cards(cardp2)
            if Wars_on == True:
                player2.add_cards(War_bet)
                War_bet.clear()
                Wars_on = False
            
            
        else:
            print('----- WAR ! -----')
            Wars_on = True
            print('The bet was taken from each players ')
            print('Next bet decides who wins the WAR BET !')
            War_bet.append(cardp1)
            War_bet.append(cardp2)
            
            if len(player1.stack)<3:
                print(f'Congratulations {player2.name} you Won !')
                game_on = False
                break
                
            elif len(player2.stack)<3:
                print(f'Congratulations {player1.name} you Won ! ')
                game_on = False
                break
                
            for item in range(3):
                War_bet.append(player1.remove_one())
                War_bet.append(player2.remove_one())
            
        print(player1)
        print(player2)
        print('---------------')
        round_num+=1

print('Thank you for playing')
     


# In[ ]:



 
 
 


# In[ ]:




