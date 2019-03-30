#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:15:17 2019

@author: manasikulkarni

You have a boutique that specializes in words that don't have adjacent matching characters. Bobby,  competitor, has decided to get out of the word business altogether 
and you have bought his inventory. Your idea is to modify his inventory of words so they are suitable for sale in your store. To do this, you find all adjacent pairs of
matching characters and replace one of the characters with a different one. Determine the minimum number of characters that must be replaced to make a saleable word.

For example, you purchased words = [add,boook,break]. You will create an array with your results from the tests. Change d in adD, change o in boOok and no change is 
necessary in break. The return array result = [1,1,0]

"""
import math

def minimalOperations(words):
    result = []
    i = 0
    
    #Iterating over all words
    for w in words:
        x = 0
        i = 0
        
        while i < len(w):
            count = 1
            #To compare adjacent letters
            for j in range(i+1, len(w)):
                if w[i] != w[j]:
                    break
                else:
                    count += 1
                    
            if count > 1:
                #This will determine the number of letters to be replaced
                x += math.floor(count / 2)
                i += count
            else:
                i += 1
                
        if x > 0:
            result.append(x)
        else:
            result.append(0)
            
    return result
    

wordList = ['aab','abb','baaac','break','qqwerrrdffghiio','jjjjjooperttyyywq']            
res = minimalOperations(wordList)
print(res)
                