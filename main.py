import os
from git import Repo
from github import Github
from tkinter import filedialog
from tkinter import *


def start():
    print("Creating Git project :)")
    folder_name = input("Enter project name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

#   get current directory
    try:
        root = Tk()
        root.withdraw()
        path = filedialog.askdirectory(title = "Choose the directory that the project will be stored")
        path = path + "/" + folder_name
        os.mkdir(path)
    except:
        print("File directory already exist!")
        input("Fail! Press any key to terminate")
        return

    f_path = path + "/" + "README.md"
    f = open(f_path, "w")
    f.write("Readme "+folder_name)
    f.close()

    try:
        Repo.init(path)
        repo = Repo(path)
    except:
        print("Git Repo cannot initialize locally!")
        input("Fail! Press any key to terminate")
        return

    print('Repo at {} successfully loaded.'.format(path))
    repo.index.add(["README.md"])
    repo.index.commit('master')
    print('Commit performed on README')

    try:
        user = Github(username, password).get_user()
        user.create_repo(folder_name)
        print("Successfully created repository at GitHub {}".format(folder_name))
    except:
        print("Git login unsuccessful, please enter valid username and password!")
        input("Fail! Press any key to terminate")
        return

    repo_web = "https://github.com/"+username+"/"+folder_name+".git"

    try:
        origin = repo.create_remote('origin', repo_web)
        origin.fetch()
        origin.push('master')
    except:
        print("Remote repo push unsuccessful!")
        input("Fail! Press any key to terminate")
        return

    input("Finish! Press any key to terminate")


if __name__ == "__main__":
    start()
