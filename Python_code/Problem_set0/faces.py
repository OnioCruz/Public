#!/bin/usr/env python3

def main():
    user_input = input("Please enter old school emoticons: ")
    new_school_emojis = convert(user_input)
    print(new_school_emojis)


def convert(n):
    updated_emoji = n.replace(':)', '🙂').replace(':(', '🙁')
    return updated_emoji


main()
