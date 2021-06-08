import getpass, imaplib, pprint, datetime, io
from imap_tools import MailBox, AND

host=input('Insira servidor do IMAP: ')
port=input('Insira porta do IMAP: ')
user = input('Insira seu email: ')
pwd = getpass.getpass('Insira sua senha: ')

timeout=15
folder_att = 'anexos/'
folder_html = 'html/'


# get list of email subjects from INBOX folder - equivalent verbose version
mailbox = MailBox(host)
mailbox.login(user, pwd, initial_folder='INBOX')  # or mailbox.folder.set instead 3d arg
for msg in mailbox.fetch(AND(all=True)):
    print('UID    : ', msg.uid)
    print('De     : ', msg.from_)
    print('Assunto: ', msg.subject)
    print('Data   : ', msg.date.strftime('%d/%m/%Y %H:%M:%S'))
    for to in msg.to:
        print('Para   : ', to)
    for cc in msg.cc:
        print('Cópia  : ', cc)
    for bcc in msg.bcc:
        print('Cópia Oculta: ', bcc)
    print('Texto : ', msg.text)
    msgHTML = msg.html
    indice = msgHTML.find('src="cid:')
    novoHTML = ''
    while indice >= 0:
        novoHTML= novoHTML + msgHTML[0:indice+5] + folder_att
        msgHTML = msgHTML[indice+9:]
        arroba = msgHTML.find('@')
        if indice >= 0:
            aspas = msgHTML.find('"')
            novoHTML= novoHTML + msgHTML[0:arroba]
            msgHTML = msgHTML[aspas:]
        indice = msgHTML.find('src="cid:')
    novoHTML= novoHTML + msgHTML
    with io.open(folder_html+'{}'.format(msg.uid+'.html'), 'w', encoding='utf-8') as f:
            f.write(novoHTML)   
    for att in msg.attachments:
        print(' *** Anexo ***')
        print('Arquivo  : ', att.filename)
        print('Tipo     : ', att.content_type)
        print('Anexo ID :', att.content_id)
        print('Tamanho  : ', att.size)
        with open(folder_html + folder_att+'{}'.format(att.filename), 'wb') as f:
            f.write(att.payload)        

mailbox.logout()