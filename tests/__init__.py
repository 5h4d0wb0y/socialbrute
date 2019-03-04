import random
import imaplib
from imaplib import IMAP4
import mechanize
import cookielib

def load():
  global br, glob
  br = mechanize.Browser()
  cj = cookielib.LWPCookieJar()
  br.set_handle_robots(False)
  br.set_handle_equiv(True)
  br.set_handle_referer(True)
  br.set_handle_redirect(True)
  br.set_cookiejar(cj)
  br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
  

def check_facebook():
  load()
  url = 'https://www.facebook.com/login.php?login_attempt=1'
  br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')] #random.choice(glob.user_agents))]
  site = br.open(url)  
  br.select_form(id='login_form')
  br.form['email'] = "testing"
  br.form['pass'] = "password"
  br.submit()
  log = br.geturl()
  if ('login_attempt' in log):
    return True
  else:
    return False


def check_gmail():
  return True
  #host = 'imap.gmail.com'
  #port = 993
  #try:
  #  IMAP4 = imaplib.IMAP4_SSL(host, port)
  #  session = IMAP4.login("testing", "password")
  #except imaplib.IMAP4.error:
  #  if (session == 'Invalid credentials'):
  #    return True


def check_hotmail():
  return True
  #host = 'imap-mail.outlook.com'
  #port = 993
  #try:
  #  IMAP4 = imaplib.IMAP4_SSL(host, port)
  #  session = IMAP4.login("testing", "password")
  #except imaplib.IMAP4.error:
  #  if (session == 'Invalid credentials'):
  #    return True


def check_instagram():
  return True
  # TODO: change mechanize with selenium because it interacts with js
  #load()
  #url = 'https://www.instagram.com/accounts/login/'
  #br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')] #random.choice(glob.user_agents))]
  #site = br.open(url)
  #br.select_form(nr=0)
  #br.form['username'] = "testing"
  #br.form['password'] = "password"
  #br.submit()
  #log = br.geturl()
  #if (log == url) and ('login_attempt' in log):
  #  return True
  #else:
  #  return False


def check_linkedin():
  load()
  url = 'https://linkedin.com/'
  br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')] #random.choice(glob.user_agents))]
  site = br.open(url)
  br.select_form(nr=0)
  br.form['session_key'] = "testing"
  br.form['session_password'] = "password"
  br.submit()
  log = br.geturl()
  if ('login-submit' in log):
      return True
  else:
      return False

def check_twitter():
  load()
  url = 'https://mobile.twitter.com/login'
  br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')] #random.choice(glob.user_agents))]
  site = br.open(url)
  br.select_form(nr=0)
  br.form['session[username_or_email]'] = "testing"
  br.form['session[password]'] = "password"
  br.submit()
  log = br.geturl()
  if ('error' in log):
      return True
  else:
      return False

def check_vk():
  load()
  url = 'https://vk.com/login'
  br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')] #random.choice(glob.user_agents))]
  site = br.open(url)
  br.select_form(nr=0)
  br.form['email'] = "testing"
  br.form['pass'] = "password"
  br.submit()
  log = br.geturl()
  if ('email=testing' in log):
    return True
  else:
    return False

def check_yahoo():
  return True
  #host = 'imap.mail.yahoo.com'
  #port = 993
  #try:
  #  IMAP4 = imaplib.IMAP4_SSL(host, port)
  #  session = IMAP4.login("testing", "password")
  #except imaplib.IMAP4.error:
  #  if (session == 'Invalid credentials'):
  #    return True