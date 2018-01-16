import argparse

parser = argparse.ArgumentParser(description='Sum two integers.')

parser.add_argument('-a', "--a_value", dest="a", help="A integers", type=int)
parser.add_argument('-b', "--b_value", dest="b", help="B integers", type=int)

args = parser.parse_args()
print(args)
print(args.a)
print(args.b)
print(args.a + args.b)
