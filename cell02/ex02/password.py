#!/usr/bin/env python3

def main():
    password = "Python is awesome"
    key = input()
    
    if (key == password):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        
main()