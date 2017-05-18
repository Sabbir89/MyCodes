# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:05:49 2017

@author: SABBIR
"""

print('Please enter a char')
char =  input()
if char >= 'a' and char <= 'z' or char >='A' and char<='Z':
    if char in 'aeiouAEIOU':
        print('Vowel')
    else:
        print('Consonent')
else:
    print('Nothing')