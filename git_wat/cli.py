import argparse

from . import github

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
get_token_parser = subparsers.add_parser('get-token')


def get_token(args):
    github.prompt()

get_token_parser.set_defaults(func=get_token)


def main():
    args = parser.parse_args()
    args.func(args)
