# -*- coding: utf-8 -*-

"""Console script for socialbrute."""
import os
import sys
import click
from terminaltables import SingleTable #AsciiTable

import socialbrute
from socialbrute.socialbrute import *
from socialbrute.helpers import Colors
from socialbrute import __author__, __version__

SOCIALS = [
    "aol",
    "facebook",
    "gmail",
    "hotmail",
    "instagram",
    "twitter",
    "vk",
    "yahoo"
]

def show_banner():
    click.echo(Colors.GREEN)
    click.echo(" $$$$$$\                      $$\           $$\ $$$$$$$\                        $$\  ")
    click.echo("$$  __$$\                     \__|          $$ |$$  __$$\                       $$ | ")
    click.echo("$$ /  \__| $$$$$$\   $$$$$$$\ $$\  $$$$$$\  $$ |$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\ ")
    click.echo("\$$$$$$\  $$  __$$\ $$  _____|$$ | \____$$\ $$ |$$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\ ")
    click.echo(" \____$$\ $$ /  $$ |$$ /      $$ | $$$$$$$ |$$ |$$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |")
    click.echo("$$\   $$ |$$ |  $$ |$$ |      $$ |$$  __$$ |$$ |$$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|")
    click.echo("\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$ |$$ |$$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\ ")
    click.echo(" \______/  \______/  \_______|\__| \_______|\__|\_______/ \__|       \______/    \____/  \_______| \n" + (Colors.ENDC))
    click.echo("                              --[    Version: " + (Colors.YELLOW) + (Colors.BOLD) + (__version__) + (Colors.ENDC) + "      ]--")
    click.echo("                              --[     Author: " + (Colors.CYAN) + (Colors.BOLD) + (__author__) + (Colors.ENDC) + "  ]--\n\n")

def prompt_proxy(ctx, param, use_proxy):
    if use_proxy:
        host = ctx.params.get('proxy_host')
        if not host:
            host = click.prompt('Proxy host', default='localhost')

        port = ctx.params.get('proxy_port')
        if not port:
            port = click.prompt('Proxy port', default=9050)
        
        user = ctx.params.get('proxy_user')
        if not user:
            user = click.prompt('Proxy user', default=None)

        pwd = ctx.params.get('proxy_pass')
        if not pwd:
            pwd = click.prompt('Proxy user\'s password', default=None)
        return (host, port, user, pwd)

@click.command()
@click.option('--use-proxy/--no-proxy', is_flag=True, default=False, help='Set a proxy to use', callback=prompt_proxy)
@click.option('--proxy-host', is_eager=True, help='Set the proxy host')
@click.option('--proxy-port', is_eager=True, type=int, help='Specify the proxy port')
@click.option('--proxy-user', is_eager=True, help='Set the proxy user')
@click.option('--proxy-pass', is_eager=True, help='Set the proxy user\'s password')
@click.option('-u', '--username', help='Set the username')
@click.option('-s', '--social', type=click.Choice(SOCIALS), help='Set the social network')
@click.option('-w', '--wordlist', type=click.Path(), help='Set the wordlist path')
@click.option('-d', '--delay', type=int, default=1, help='Provide the number of seconds the program delays as each password is tried')
@click.option('--interactive/--no-interactive', is_flag=True, default=False, help='Set the browser emulation interactive')
def main(use_proxy, proxy_host, proxy_port, proxy_user, proxy_pass, username, social, wordlist, delay, interactive, token):
    """Console script for socialbrute."""
    if not username:
            print_error("Missing '-u' or '--username' argument!")
            sys.exit(-1)

    if not social:
        print_error("Missing '-s' or '--social' argument!")
        sys.exit(-1)

    if social not in SOCIALS:
        data = []
        for x in SOCIALS:
            data.append("%s%s%s" % (Colors.PURPLE, x, Colors.ENDC))
        t = SingleTable([data], "%s%s Available Social Networks %s" % (Colors.YELLOW, Colors.BOLD, Colors.ENDC))
        print(t.table)
        print("\n")
        print_error("Wrong '-s' or '--social' argument!")
        return 0

    if not wordlist:
        print_error("Missing '-w' or '--wordlist' argument!")
        return 0
    
    if not os.path.isfile(wordlist):
        print_error('The wordlist does not exist.')
        return 0

    interact = not interactive

    if use_proxy:
        proxy = {
            'host': proxy_host,
            'port': proxy_port,
            'user': proxy_user,
            'pass': proxy_pass,
        }
        sb = Socialbrute(interactive=interact, proxy=proxy)
    else:
        sb = Socialbrute(interactive=interact)

    sb.run(social, username, wordlist, delay)
    
    sb.stop()

    return 0


if __name__ == "__main__":
    show_banner()
    sys.exit(main())  # pragma: no cover
