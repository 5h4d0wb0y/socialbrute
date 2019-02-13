```
 $$$$$$\                      $$\           $$\ $$$$$$$\                        $$\
$$  __$$\                     \__|          $$ |$$  __$$\                       $$ |
$$ /  \__| $$$$$$\   $$$$$$$\ $$\  $$$$$$\  $$ |$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\
\$$$$$$\  $$  __$$\ $$  _____|$$ | \____$$\ $$ |$$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\
 \____$$\ $$ /  $$ |$$ /      $$ | $$$$$$$ |$$ |$$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |
$$\   $$ |$$ |  $$ |$$ |      $$ |$$  __$$ |$$ |$$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$ |$$ |$$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\
 \______/  \______/  \_______|\__| \_______|\__|\_______/ \__|       \______/    \____/  \_______|
```

<p align="center">
  <p align="center">
    <a href="https://github.com/5h4d0wb0y/socialbrute/releases/latest"><img alt="Release" src="https://img.shields.io/github/release/5h4d0wb0y/socialbrute.svg?style=flat-square"></a>
    <a href="https://github.com/5h4d0wb0y/socialbrute/blob/master/LICENSE.md"><img alt="Software License" src="https://img.shields.io/badge/license-GPL3-brightgreen.svg?style=flat-square"></a>
    <a href="https://travis-ci.org/5h4d0wb0y/socialbrute"><img alt="Travis" src="https://img.shields.io/travis/5h4d0wb0y/socialbrute/master.svg?style=flat-square"></a>
    <a href="https://codecov.io/gh/5h4d0wb0y/socialbrute"><img alt="Code Coverage" src="https://img.shields.io/codecov/c/github/5h4d0wb0y/socialbrute/master.svg?style=flat-square"></a>
    <a href="https://github.com/5h4d0wb0y/socialbrute/graphs/commit-activity"><img alt="Maintained" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg"></a>
  </p>
</p>

# SocialBrute

SocialBrute attempts to crack a social network using a brute force dictionary attack.

It supports:

- [x] Facebook
- [x] Gmail
- [x] Hotmail
- [x] Yahoo
- [x] VK
- [x] LinkedIn
- [x] Twitter
- [x] Instagram


## How to Install

```
git clone https://github.com/5h4d0wb0y/socialbrute.git
cd socialbrute
pip install -r requirements.txt
```

## Usage

From the `-h` or `--help` help menu: 

```
usage: socialbrute [-h] [-u <username>] [-s <social>] [-w <wordlist>]
                   [-d DELAY]

optional arguments:
  -h, --help            show this help message and exit
  -u <username>, --username <username>
                        Specify a username to crack
  -s <social>, --social <social>
                        Choose a social network between ['baidu', 'facebook',
                        'gmail', 'hotmail', 'instagram', 'linkedin',
                        'twitter', 'vk', 'yahoo']
  -w <wordlist>, --wordlist <wordlist>
                        Specify a wordlist path
  -d DELAY, --delay DELAY
                        Provide the number of seconds the program delays as
                        each password is tried
```

**Examples**

Trying to crack a Facebook account:

    ./socialbrute -s facebook -u YOUR_MAIL -w /root/wordlist.txt -d 1


## License

It is released under the MIT license.


## Credits

SocialBrute was developed by [5h4d0wb0y](https://twitter.com/5h4d0wb0y).
