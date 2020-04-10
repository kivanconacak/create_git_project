import os
from git import Repo
from github import Github


def start():
    print("Creating Git project :)")
    folder_name = input("Enter folder name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

#   get current directory
    path = os.getcwd()
    path = path + "/" + folder_name
    os.mkdir(path)

    f_path = path + "/" + "README.md"
    f = open(f_path, "w")
    f.write("Readme "+folder_name)
    f.close()

    Repo.init(path)
    repo = Repo(path)

    print('Repo at {} successfully loaded.'.format(path))
    repo.index.add(["README.md"])
    repo.index.commit('master')
    print('commit performed on README')

    user = Github(username, password).get_user()
    user.create_repo(folder_name)
    print("Successfully created repository {}".format(folder_name))

    repo_web = "https://github.com/"+username+"/"+folder_name+".git"

    origin = repo.create_remote('origin', repo_web)
    origin.fetch()
    origin.push('master')


if __name__ == "__main__":
    start()
