import random
from enum import IntEnum


uscore = 0
cscore = 0


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


valid = [0, 1, 2]


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    all_choices = ", ".join(choices)
    user_choice = int(input(f"Enter a choice ({all_choices}): "))
    while user_choice not in valid:
        print('''
                INVALID INPUT!!!
                  Choose again   
                  ''')
        user_choice = int(input(f"Enter a choice ({all_choices}): "))
    action = Action(user_choice)
    return action


def get_comp_selection():
    num = random.randint(0, 2)
    action = Action(num)
    return action


def decide_winner(u, c):
    if u == c:
        case_tie(u)
    elif u == Action.Rock:
        if c == Action.Scissors:
            case_rxs()
        else:
            case_rxp()
    elif u == Action.Paper:
        if c == Action.Rock:
            case_pxr()
        else:
            case_pxs()
    elif u == Action.Scissors:
        if c == Action.Paper:
            case_sxp()
        else:
            case_sxr()


def case_tie(a):
    if a == Action.Rock:
        print('''
                    User                         Computer
                
                    _______                     _______
              -----'    ____)                 (____    '-----
                       (_____)               (_____)
                      (_____)                 (_____)
                      (____)                   (____)
              -----.__(___)                     (___)__.-----
                       
                                   DRAW
              ''')
    elif a == Action.Paper:
        print('''
                    User                          Computer
                
                 _______                             _______
           -----'    ____)____                 ____(____    '-----
                         ______)            (______
                         _______)          (_______
                       _______)              (_______
           -----.__________)                    (__________.-----
                       
                                   DRAW
              ''')
    else:
        print('''
                    User                         Computer

                  _______                          _______
            -----'   ____)____                ____(____   '-----
                         ______)            (______
                      __________)          (__________
                    (____)                        (____)
            -----.__(___)                          (___)__.-----                     
                                   DRAW

              ''')


def case_rxp():
    print('''
                    User                          Computer

                    _______                          _______
              -----'    ____)                   ____(____    '-----
                       (_____)               (______
                      (_____)              (_______
                      (____)                  (_______
              -----.__(___)                      (__________.-----

                                You Lose
              '''
          )
    global cscore
    cscore += 1


def case_rxs():
    print('''
                    User                             Computer

                    _______                        _______
              -----'    ____)                 ____(____   '-----
                       (_____)              (______
                      (_____)              (__________
                      (____)                      (____)
              -----.__(___)                        (___)__.-----

                                YOU WIN!!!
                  '''
          )
    global uscore
    uscore += 1


def case_pxr():
    print('''
                        User                          Computer

                     _______                      _______
               -----'    ____)____              (____    '-----
                             ______)           (_____)
                             _______)           (_____)
                           _______)              (____)
               -----.__________)                  (___)__.-----

                                    YOU WIN!!!
                  ''')
    global uscore
    uscore += 1


def case_pxs():
    print('''
                        User                          Computer

                     _______                            _______
               -----'    ____)____                 ____(____   '-----
                             ______)             (______
                             _______)           (__________
                           _______)                    (____)
               -----.__________)                        (___)__.-----

                                       You Lose
                      ''')
    global cscore
    cscore += 1


def case_sxr():
    print('''
                        User                         Computer

                      _______                        _______
                -----'   ____)____                 (____    '-----
                             ______)              (_____)
                          __________)              (_____)
                        (____)                      (____)
                -----.__(___)                        (___)__.-----  

                                      You Lose
                  ''')
    global cscore
    cscore += 1


def case_sxp():
    print('''
                            User                         Computer

                      _______                              _______
                -----'   ____)____                    ____(____    '-----
                             ______)               (______
                          __________)            (_______
                        (____)                      (_______
                -----.__(___)                          (__________.-----

                                      YOU WIN!!!
                      ''')
    global uscore
    uscore += 1


x = 1
while x == 1:
    userChoice = get_user_selection()
    compChoice = get_comp_selection()
    decide_winner(userChoice, compChoice)

    again = ('y', 'n')
    repeatGame = input("Play again ? (Y/N): ")
    while repeatGame not in again:
        print(f'''
                    Choose Y for Yes, or N for No...
                    What's {repeatGame} ???
                      ◔ _◔
              ''')
        repeatGame = input("Play again ? (Y/N): ")
    if repeatGame.lower() == "n":
        x = 0

print(f'''
            You                HAL  9000
             {uscore}                     {cscore}
      ''')

if uscore > cscore:
    print("       RPS CHAMPION!!!       ")
elif uscore == cscore:
    print("            DRAW           ")
else:
    print("    Better Luck Next Time")
