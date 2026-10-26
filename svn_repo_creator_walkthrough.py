import secrets

# SVN repo creator - Walkthrough - talks you through the steps

tech_username = "TechSupport" #Service account to add to all repositories
svn_path_on_server = r"/mnt/svn/" # path on the server to folder storing repositories
server_unc_path = "my_svn_server.co.uk"

def cleanup_name(project_name:str) -> str:
    project_name = project_name.strip(r"!£$%^&*()_+-={}[]:@~;'#,/<>?`¬") # remove special characters
    project_name = project_name.title()
    return project_name.replace(' ', '')

# Input:
# List of names
# Project name
project_name = input("what is the project name?")
users = input(
'''who needs access? 
please enter a comma seperated list e.g. aa11aaa, bb11bbb''')



usernames = users.split(",")

print("the usernames to grant access to are:")
filter("",usernames)
for i,username in enumerate(usernames):
    print(f'username: {username}')

#create password for each user
un_pw = {}
for username in usernames:
    un_pw[username] = secrets.token_urlsafe(10)

confirm_usernames = ""
for i in range(1,5): 
    if confirm_usernames not in ["y","n"]:
        confirm_usernames = input("please confirm the above list is correct (y/n)")
    elif 'y' in confirm_usernames:
        print("GREAT, here we go then, follow the instructions as they appear")
        print("INSTRUCTIONS")
        # STEP 1
        print("STEP 1) - to check the repo doesn't already exist, run the following\n\t if the command returns null then the repo doesn't exist")
        project_new_name = cleanup_name(project_name)
        print(f"    cd {svn_path_on_server}")
        print(f"    ls | grep {project_new_name}\n")
        input('press <ANY> key to continue')
        # STEP 2
        print("STEP 2 - create the repo\n")
        print(f"    svnadmin create {project_new_name}\n")
        input('press <ANY> key to continue')
        print("STEP 3 - configure the repository")
        print(f"    cp {svn_path_on_server}svnserve_template.conf {svn_path_on_server}{project_new_name}/conf/svnserve.conf \n")
        input('press <ANY> key to continue')
        print("STEP 4 - add usernames and passwords:\n")

        passwd_prep = ''.join(f'{key} = {val}\\n' for key, val in un_pw.items())

        print(f"    printf '[users]\\n{passwd_prep}' -> {svn_path_on_server}{project_new_name}/conf/passwd\n")
        input('press <ANY> key to continue')
        print("STEP 5 - send usernames to students:")
        for un,pw in un_pw.items():
            print(f'username for repo svn://{server_unc_path}/{project_new_name} \n \n {un} = {pw} \n \n ---------------')
        input('press <ANY> key to continue')
        break
    else:
        print('start again')
        break 
# Generates:
# svnconf.conf - login
# passwd - the password file


