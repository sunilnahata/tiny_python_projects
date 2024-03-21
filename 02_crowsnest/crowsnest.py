#!/usr/bin/env python3
"""
Author : Sunil Nahata 
Date   : 2024-03-21
Purpose: Choose the article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = ""
    
    if word[0].lower() in 'aeiou':
        article = "an"
    else:
        article = "a"

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!") 

# --------------------------------------------------
if __name__ == '__main__':
    main()
