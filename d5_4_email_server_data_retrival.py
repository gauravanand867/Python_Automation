import imaplib

e=input('Enter email: ')
p=input('Enter Password: ')
g=imaplib.IMAP4_SSL('imap.gmail.com')		#imap.gmail.com is host name of gmail
g.login(e,p)
g.select('INBOX')
a,b=g.status('INBOX','(UNSEEN)')			#a is for status (i.e OK if everything is fine)

c=str(b[0])
n=c[18:19]


print("There are "+n+' unread mail in your mailbox')