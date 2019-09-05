import argparse
import math_lib as ml


def main():

    parser = argparse.ArgumentParser(
                  description='Accept Parameters',
                  prog='_take_numbers')
    parser.add_argument('--first_integer', '-f',
                        type=int,
                        required=True,
                        help='Provide an integer')
    parser.add_argument('--second_integer', '-s',
                        type=int,
                        required=True,
                        help='Provide an integer')
    args = parser.parse_args()
# Do math
    x3 = ml.add(args.first_integer, args.second_integer)
    x4 = ml.div(args.first_integer, args.second_integer)
    print('The sum of ' + str(args.first_integer) + ' and ' + str(args.second_integer) + ' is ' + str(x3))
    print('The result of ' + str(args.first_integer) + '/' + str(args.second_integer) + ' is ' + str(x4))


if __name__ == '__main__':
    main()
