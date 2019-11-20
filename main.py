#!/usr/bin/env python3
'''Citation Engine'''

# Wed 20 Nov 2019 12:45:19 PM IST

import argparse
import json

from citation import Citation


def main(args: argparse.Namespace) -> None:
    '''Driver code'''

    style = {
        'mla': Citation.mla,
        'apa': Citation.apa,
        'ieee': Citation.ieee,
        'chicago': Citation.chicago
    }

    with open(args.input) as f:
        refs = json.loads(f.read())

    with open(args.output, 'w') as f:
        for i in style.get(args.format)(refs):
            f.write(i)


if __name__ == '__main__':
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        '--input',
                        help='Name of json file to input bibliography')

    parser.add_argument('-o', '--output', help='Name of output html file')

    parser.add_argument(
        '-f',
        '--format',
        help='Citation format [apa, mla (default), ieee, chicago]',
        default='mla')
    parsed_args = parser.parse_args()

    if parsed_args.input is None or parsed_args.output is None or parsed_args.format is None:
        parser.print_help()
        sys.exit(1)

    main(parsed_args)
