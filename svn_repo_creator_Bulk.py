import secrets
from tkinter import filedialog
import csv, os
import datetime

tech_username = "TechSupport" #Service account to add to all repositories
svn_path_on_server = r"/mnt/svn/" # path on the server to folder storing repositories
server_unc_path = "my_svn_server.co.uk"

output_location = filedialog.askdirectory()
print(output_location)

# SVN repo creator - BULK - this will create private repos for students based on a list of usernames

def cleanup_name(project_name:str) -> str:
    '''
    Removes any illegal characters from the username
    '''
    project_name = project_name.strip(r"!£$%^&*()_+-={}[]:@~;'#,/<>?`¬") # remove special characters
    project_name = project_name.title()
    return project_name.replace(' ', '')

# Input:
# List of names
# Project name
#project_name = input("what is the project name?")
users = input(
'''who needs a repo? 
please enter a comma seperated list e.g. user_name_1, user_name_2''')

usernames = users.split(",")

print("the repos to generate are:")
filter("",usernames)
for i,username in enumerate(usernames):
    print(f'username: {username}')

print("cd /mnt/svn")

commands_to_run = []
commands_to_run.append(f"cd {svn_path_on_server}")

#create password for each user
repos_and_accounts = []

for username in usernames:
    creds = [username,secrets.token_urlsafe(5)]
    admin_creds = [tech_username,secrets.token_urlsafe(5)]
    repo_name = f'{username}_PrivateRepo'
    commands_to_run.append(f"svnadmin create {repo_name}")
    commands_to_run.append(f"cp {svn_path_on_server}svnserve_template.conf {svn_path_on_server}{repo_name}/conf/svnserve.conf")
    commands_to_run.append(f"printf '[users]\\n{creds[0]} = {creds[1]}\\n{admin_creds[0]} = {admin_creds[1]}\\n' -> {svn_path_on_server}{repo_name}/conf/passwd")
    repos_and_accounts.append([f'svn://{server_unc_path}/{repo_name}',creds[0],creds[1],admin_creds[0],admin_creds[1]])

print('===== COPY AND PASTE THE FOLLOWING LINES INTO PuTTY=====\n')
for command in commands_to_run:
    print(command)
today = datetime.datetime.today().strftime('%Y-%m-%d')
output_filename =os.path.join(output_location,f'{today}_SVN_accounts.csv')

print(f'SAVE the following dump to file - {output_filename}')
with open(output_filename,'w',newline='') as csvfile:
    csvWriter = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvWriter.writerow(['repository url','username','password','admin user','admin pass'])
    for repo in repos_and_accounts:
        csvWriter.writerow(repo)

input('press <ANY> key to continue')
