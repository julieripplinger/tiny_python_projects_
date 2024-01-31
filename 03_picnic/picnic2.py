#!/usr/bin/env python3
"""
Author : Julie Ripplinger <julie.ripplinger.phd@gmail.com>
Date   : 2023-10-13
Purpose: Print items on picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print items on picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        type=str,
                        nargs='+',
                        help='Items we are bringing')

    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num_items = len(items)
    # print(args.items)
    # print(args.sorted)

    if args.sorted:
        items = sorted(items)

    bringing = ""
    if num_items == 1:
        bringing = items[0]
    elif num_items <= 2:
        # bringing = f"{items[0]} and {items[1]}"
        bringing = ' and '.join(items)
    else:
        # items[-1] = 'and ' + items[-1]
        # bringing =  (', '.join(items))
        bringing = ', '.join(items[:-1]) + ', and ' + items[-1]

    print(f"You are bringing {bringing}.")
# --------------------------------------------------
if __name__ == '__main__':
    main()
