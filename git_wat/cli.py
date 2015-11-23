import argparse

from . import github
from .git import git
from os.path import basename, realpath


def init(args):
    accountname = git(['config', 'wat.account'])
    client = github.Client.from_config(accountname)
    client.create_repo(basename(realpath('.')))


def get_token(args):
    github.prompt()


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

get_token_parser = subparsers.add_parser('get-token')
get_token_parser.set_defaults(func=get_token)

create_repo_parser = subparsers.add_parser('init')
create_repo_parser.set_defaults(func=init)


def main():
    args = parser.parse_args()
    args.func(args)
