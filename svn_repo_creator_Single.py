import secrets

# SVN repo creator - for creating a single repository from a list of student usernames

def cleanup_name(project_name:str) -> str:
    project_name = project_name.strip(r"!£$%^&*()_+-={}[]:@~;'#,/<>?`¬") # remove special characters
    project_name = project_name.title()
    return project_name.replace(' ', '')

# Input:
# List of names
# Project name
tech_username = "TechSupport" #Service account to add to all repositories
svn_path_on_server = r"/mnt/svn/" # path on the server to folder storing repositories
server_unc_path = "my_svn_server.co.uk"

project_name = input("what is the project name?")
users = input(
'''who needs access? 
please enter a comma seperated list e.g. aa11aaa, bb11bbb''')
usernames = users.split(",")
usernames.append(tech_username)

print("the usernames to grant access to are:")
filter("",usernames)
for i,username in enumerate(usernames):
    print(f'username: {username}')

#create password for each user
un_pw = {}
for username in usernames:
    un_pw[username] = secrets.token_urlsafe(10)

confirm_usernames = ""
# try to ask user for the list of usernames 5 times before we give up.
for i in range(1,5): 
    if confirm_usernames not in ["y","n"]:
        confirm_usernames = input("please confirm the above list is correct (y/n)")
    elif 'y' in confirm_usernames:
        # STEP 1
        project_new_name = cleanup_name(project_name)
        print('===== COPY AND PASTE THE FOLLOWING LINES INTO PuTTY=====\n')
        print(f"cd {svn_path_on_server}")
        print(f"svnadmin create {project_new_name}\n")
        print(f"cp {svn_path_on_server}svnserve_template.conf {svn_path_on_server}{project_new_name}/conf/svnserve.conf \n")
        
        passwd_prep = ''.join(f'{key} = {val}\\n' for key, val in un_pw.items())
        print(f"printf '[users]\\n{passwd_prep}' -> {svn_path_on_server}{project_new_name}/conf/passwd\n\n")
        print('===== Send the following lines to the students =====\n')
        for un,pw in un_pw.items():
            if un != 'CTATech':
                print(f'username for repo svn://{server_unc_path}/{project_new_name} \n \n {un} = {pw} \n \n ---------------')
         
        print("")
        print("===== Save the following credentials for tech support =====\n")
        print(f"Username: {tech_username}")
        print(f"Password: {un_pw[tech_username]}\n")
        print("===========================================================\n")
        input('press <ANY> key to quit')
        exit()
    elif 'n' in confirm_usernames:
        exit()
# Generates:
# svnconf.conf - login
# passwd - the password file


