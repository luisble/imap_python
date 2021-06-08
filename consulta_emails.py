from conf.config import confEmail
import datetime, io
from imap_tools import MailBox, AND

if __name__ == '__main__':

    ## ConfEmail retorna um JSON com as configurações
    jsonMail = confEmail()
    
    # get list of email subjects from INBOX folder - equivalent verbose version
    with MailBox(jsonMail["host"]).login(jsonMail["user"], jsonMail["pwd"], initial_folder=jsonMail["mail_folder"]) as mailbox:
        lista_msg = []
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
                novoHTML= novoHTML + msgHTML[0:indice+5] + jsonMail["folder_att"]
                msgHTML = msgHTML[indice+9:]
                arroba = msgHTML.find('@')
                if indice >= 0:
                    aspas = msgHTML.find('"')
                    novoHTML= novoHTML + msgHTML[0:arroba]
                    msgHTML = msgHTML[aspas:]
                indice = msgHTML.find('src="cid:')
            novoHTML= novoHTML + msgHTML
            with io.open(jsonMail["folder_html"]+'{}'.format(msg.uid+'.html'), 'w', encoding='utf-8') as f:
                f.write(novoHTML)   
            for att in msg.attachments:
                print(' *** Anexo ***')
                print('Arquivo  : ', att.filename)
                print('Tipo     : ', att.content_type)
                print('Anexo ID :', att.content_id)
                print('Tamanho  : ', att.size)
                with open(jsonMail["folder_html"] + jsonMail["folder_att"]+'{}'.format(att.filename), 'wb') as f:
                    f.write(att.payload)        
            lista_msg.append(msg.uid)
        for msg in lista_msg:
            # Move as mensagens tratadas para a pasta de mensagens carregadas
            mailbox.move(msg, jsonMail["upd_folder"])

