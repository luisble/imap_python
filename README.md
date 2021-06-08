# Leitura de e-mails protocolo IMAP

Exemplo de uso do IMAP com Python

Criar uma estrutura de pastas html/anexos/<br>
Criar um arquivo conf.json na pasta conf com os seguintes dados:

~~~json
{
    "email":
        {
        "host"          : "mail.exemple.com",
        "port"          : "993",
        "user"          : "meuemail@mail.com",
        "pwd"           : "XXXXXXX",
        "folder_att"    : "anexos/",
        "folder_html"   : "html/",
        "mail_folder"   : "INBOX",
        "upd_folder"    : "Uploaded"
       }
 }
~~~