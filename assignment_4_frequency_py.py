# -*- coding: utf-8 -*-
"""Assignment 4 frequency.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hz_5ZXEFIzDjlRXsOZEbT3DzJYLImWDI
"""

def most_frequent():
  string = input("Enter a string:")
  freq = {}
  for character in string:
    if character in freq:
      freq[character] += 1
    else:
      freq[character] = 1
  freq_list = [(freq[character], character) for character in freq]
  freq_list.sort(reverse=True)
  for frequency, character in freq_list:
    print(character, '=', '{:02d}'.format(frequency))
most_frequent()