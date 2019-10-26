# -*- coding: utf -*-

import click


class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


def print_info(message):
    click.echo((Colors.BLUE) + (Colors.BOLD) +
               ("i ") + (Colors.ENDC) + (str(message)))


def print_success(message):
    click.echo((Colors.GREEN) + (Colors.BOLD) +
               ("✔ ") + (Colors.ENDC) + (str(message)))


def print_warning(message):
    click.echo((Colors.YELLOW) + (Colors.BOLD) +
               ("! ") + (Colors.ENDC) + (str(message)))


def print_error(message):
    click.echo((Colors.RED) + (Colors.BOLD) +
               ("✗ ") + (Colors.ENDC) + (str(message)))
