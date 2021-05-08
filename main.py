import sys
import argparse
import libs_.UserClass as uc
from libs_.utils import add_user


def takeUsernameAndPassword():
    username = input('username : ')
    # password = getpass('password : ')
    password = input('password : ')
    return (username, password)


def help():
    commands = [
        "show_my_assets",
        "show_my_balance",
        "show_my_transactions",
        "buy",
        "sell",
        "help"
    ]
    print("available commands are:")
    print(commands)


def process(user, command):
    choices = {
        "show_my_assets": user.show_my_assets,
        "show_my_balance": user.show_my_balance,
        "show_my_transactions": user.blockchain.show_my_transactions,

        "buy": user.buy,
        "sell": user.sell,
        "help": help
    }
    # try:
    function = choices[command]
    function()
    # except:
    #     print("command does not exist.")


def activate_cmd(user):
    """
    available commands:
    1. show_my_assets
    2. show_my_balance
    3. show_my_transactions
    4. buy
    5. sell
    6. exit
    7. quit
    8. logout
    9.help
    """
    while True:
        print(">>>", end = "")
        command = input()
        if command == "exit" or command == "quit" or command == 'logout':
            user.commit_changes()
            print('committed changes. exiting...')
            break
        else:
            process(user, command)


def main():
    # try:
    user = uc.User(takeUsernameAndPassword())
    print("login successful !")
    # except:
    #     print("login failed! check your password")
    #     sys.exit()

    user.update_blockchain()
    activate_cmd(user)


if __name__ == '__main__':
    choices = {'main': main, 'add_user': add_user}
    parser = argparse.ArgumentParser()
    parser.add_argument('-add_user', type=int, default = 0)
    args = parser.parse_args()

    if args.add_user == 0:
        main()
    else:
        add_user(args.add_user)

