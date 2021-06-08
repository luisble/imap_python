import json
#### Le o arquivo conf.json na pasta conf com a estrutura
'''
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
'''

def confEmail():
    try:
        with open('conf/conf.json', 'r') as j:
            json_data = json.load(j)        
    except IOError as ex:
        print('Erro ao abrir o arquivo. Erro: {}'.format(ex))    
        json_data = {}
    except Exception as ex:
        print('Erro desconhecido. Erro: {}'.format(ex))    
        json_data = {}
    return json_data["email"]
