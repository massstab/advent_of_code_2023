#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.23
   Kurs:      Advent of Code
   Topic:     Camel Cards
"""

with open("python/data/day_07.txt") as f:
    lines = f.readlines()

for line in lines:
    hands = line[:5]
    bid = int(line[6:])
    print(hands)
    print(bid)

possible_cards = {"A": 0, "K": 1, "Q": 2, "J":3, "T":4, "9":5, "8":6, "7":7, "6":8, "5":9, "4":10, "3":11, "2":12}

print(possible_cards)