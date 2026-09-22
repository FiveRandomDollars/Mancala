# This is a sample Python script.
from idlelib import sidebar
from unittest import case

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Look Upon My Works Ye Mighty And Despair

#Convenience Functions =========================================================================================
board = {
    0: 0, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4,
    7: 0, 8: 4, 9: 4, 10: 4, 11: 4, 12: 4, 13: 4}

board1 = {
    1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4,
}

board2 = {
    8: 4, 9: 4, 10: 4, 11: 4, 12: 4, 13: 4
}

store1 = 0;
store2 = 0;
turn = True
endside = False


def row(times):
    for i in range(times):
        print(" ")

def quickprint(space, side):
    if side == True:
        for i in board1:
            print(board1[i], end=space)
    else:
        for i in range (1, 7):
            print(board2[14 - i], end=space)

def quickline(start, end, space):
    for i in range(start, end):
        print("-", end=space)

def quicknum(space, rev):
    if rev == True:
        for i in range(1, 7):
            print(i, end=space)
    else:
        for i in range(1, 7):
            print(14 - i, end=space)






def printboard():
    print("   ", end="")
    quicknum("        ",  False)
    row(1)
    quickline(1, 55, "")
    print(" ")
    print("B: ", end = "")
    quickprint("         ", False)
    row(2)
    print("    " + str(store1) + "                                               " + str(store2))
    row(1)
    print("A: ", end="")
    quickprint( "         ", True)
    row(1)
    quickline(1, 55, "")
    row(1)
    print("   ", end="")
    quicknum("         ", True)

#Game functions ========================================================================




def pocketcheck(pocket):
    if (pocket > 0 and pocket < 14 and pocket != 7):
        match pocket:
            case 1|2|3|4|5|6:
                return True
            case 8|9|10|11|12|13:
                return False
    else:
        return not turn



def isvalidmove(pocket):
    global turn

    if pocketcheck(pocket) != turn:
        return "invalid"

    match turn:
        case True:
            if board1[pocket] > 0:
                return "valid"

            else:
                return "invalid"


        case False:
            if board2[pocket] > 0:
                return "valid"

            else:
                return "invalid"



def movestone(pocket):
    global store1, store2, turn
    stones = 0
    last = 0
    match isvalidmove(pocket):

        case "valid":
            if turn == True:
                stones = board1[pocket]
                board1[pocket] = 0
            else:
                stones = board2[pocket]
                board2[pocket] = 0
        case "invalid":
            return "invalid"

    spaces = compile(stones, pocket)
    for space in spaces:

        last = space
        if space != 100:
            board[space] += 1
        else:
            match turn:

                case True:
                    store1 += 1

                case False:
                    store2 += 1

    board[pocket] = 0
    sync()
    if last != 100:
        capture(last)
    if last != 100:
        turn = not turn

def compile(stones, start):
    numlist = []

    for i in range(stones):
        start += 1
        if start > 13:
            start = 0

        match start:
            case 0|7:
                numlist.append(100)

            case 1|2|3|4|5|6|8|9|10|11|12|13:
                numlist.append(start)

    return numlist

def sync():
    board[0] = store1
    board[7] = store2
    for i in range(1,7):
        board1[i] = board[i]
    for i in range(8,14):
        board2[i] = board[i]

def taketurn():
    move = 0
    global turn

    match turn:
        case True:
            row(2)
            print("player A's turn")
            row(1)
            print("potential moves:", end = " ")
            for i in range(1,7):
                if isvalidmove(i) == "valid":
                    print(i, end = " ")

            row(2)
            while movestone(move) == "invalid":

                print('Enter your move:', end = '')
                move = int(input())



        case False:
            row(2)
            print("player B's turn")
            row(1)
            print("potential moves:", end=" ")
            for i in range(8, 14):
                if isvalidmove(i) == "valid":
                    print(i, end = " ")

            row(2)
            while movestone(move) == "invalid":
                print('Enter your move:', end = '')
                move = int(input())

def capture(end):
    global store1
    global store2
    match turn:
        case True:
            if end in board1 and board1[end] == 1:
                opposite = 14 - end
                store1 += board2[opposite] + 1
                board2[opposite] = 0
                board1[end] = 0
        case False:
            if end in board2 and board2[end] == 1:
                opposite = 14 - end
                store2 += board1[opposite] + 1
                board1[opposite] = 0
                board2[end] = 0

def wincon():
    global endside
    flag = True

    for i in board1:
        if board1[i] != 0:
            flag = False
            break

    if flag == True:
        engside = True

    else:
        for i in board2:
            if board2[i] != 0:
                flag = False
                break

    return flag

def end():
    global store1
    global store2
    global endside
    match endside:
        case True:
            for i in board2:
                store2 += board2[i]
                board2[i] = 0

        case False:
            for i in board1:
                store1 += board1[i]
                board1[i] = 0




#=======================================================================================


while not wincon():
    printboard()
    taketurn()
    row(2)
end()


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
