#!/usr/bin/env python3
"""
Author : Julie Ripplinger <julie.ripplinger.phd@gmail.com>
Date   : 2023-10-03
Purpose: Choose the article
"""

import argparse
# import os
# import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see and will announce')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f"Ahoy, Captain, {article} {word.upper()} off the larboard bow!")

# --------------------------------------------------
if __name__ == '__main__':
    main()
