import os
from print_color import print
from datetime import datetime
def CleanURL(name_directory="Default"):
    dir_www = os.listdir("./db/www/")
    wwww_db = []
    separador_db = ["|",":",";"]
    for www in dir_www:
        with open(f'./db/www/{www}') as f:
            lines = f.readlines()
            for lines_cleans in lines:
                lines_db = lines_cleans.replace("\n","")
                if(len(lines_db)>=2):
                    wwww_db.append(lines_db)
    for separador in separador_db:
        for wwwws in wwww_db:
            try:
                lines = wwwws.split(separador)
                if(len(lines)>=3):
                    lines_reverse = list(reversed(lines))
                    user = lines_reverse[1]
                    password = lines_reverse[0]
                    if(len(user)>=2 and len(password)>-2):     
                        time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                        time_file = datetime.now().strftime('%d_%m_%Y')
                        dir = f"./key/www/{time_file}"
                        dir_name = f"./key/www/{time_file}/{name_directory}"
                        if not os.path.exists(dir):
                            os.makedirs(dir)
                        if not os.path.exists(dir_name):
                            os.makedirs(dir_name)
                        with open(f"{dir_name}/log.txt", "a+") as file1:
                            file1.write(f"{user}|{password}\n")
                        print(f"USER: {user} | PASSWORD: {password}", tag=f' {time} | URL | 200 | {separador} ', tag_color='green', color='magenta', background='grey')
            except:
                pass
CleanURL()
def CleanMail():
    dir_www = os.listdir("./db/email/")
    email_db = []
    separador_db = ["|",":",";"]
    for www in dir_www:
        with open(f'./db/email/{www}') as f:
            lines = f.readlines()
            for lines_cleans in lines:
                lines_db = lines_cleans.replace("\n","")
                if(len(lines_db)>=2):
                    email_db.append(lines_db)
    for separador in separador_db:
        for emails in email_db:
            try:
                lines = emails.split(separador)
                email_line = lines[0]
                password_line = lines[1]
                if(len(lines)>=2):
                    lines_domain = email_line.split("@")
                    domain = lines_domain[1]
                    time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    time_file = datetime.now().strftime('%d_%m_%Y')
                    dir = f"./key/email/{time_file}"
                    dir_name = f"./key/email/{time_file}/{domain}"
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                    if not os.path.exists(dir_name):
                        os.makedirs(dir_name)
                    with open(f"{dir_name}/log.txt", "a+") as file1:
                        file1.write(f"{email_line}|{password_line}\n")
                    print(f"EMAIL: {email_line} | PASSWORD: {password_line}", tag=f' {time} | E-MAIL | 200 | {domain} ', tag_color='green', color='magenta', background='grey')

            except:
                pass
    try:
        for emails in email_db:
            lines_domain = emails.split("@")
            domain = lines_domain[1]
            time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            time_file = datetime.now().strftime('%d_%m_%Y')
            dir = f"./key/email/{time_file}"
            dir_name = f"./key/email/{time_file}/{domain}"
            if not os.path.exists(dir):
                os.makedirs(dir)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            with open(f"{dir_name}/log.txt", "a+") as file1:
                file1.write(f"{emails}\n")
            print(f"EMAIL: {emails} ", tag=f' {time} | E-MAIL | 200 | {domain} ', tag_color='green', color='magenta', background='grey')
    except:
        pass