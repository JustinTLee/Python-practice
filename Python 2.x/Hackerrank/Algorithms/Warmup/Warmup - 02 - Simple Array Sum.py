#!/bin/python

n = input()
arr = map(int, raw_input().strip().split(' '))
arr = [int(arrel) for arrel in arr]

print sum(arr)