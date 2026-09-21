# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



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


def row(times):
    for i in range(times):
        print(" ")

def quickprint(space, side):
    if side == True:
        for i in board1:
            print(board1[i], end=space)
    else:
        for i in board2:
            print(board2[i], end=space)

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
    quickprint("         ", True)
    row(2)
    print("    " + str(store1) + "                                               " + str(store2))
    row(1)
    print("A: ", end="")
    quickprint( "         ", False)
    row(1)
    quickline(1, 55, "")
    row(1)
    print("   ", end="")
    quicknum("         ", True)

#Game functions ========================================================================


turn = True

def pocketcheck(pocket):
    if (pocket > 0 and pocket < 14 and pocket != 7):
        match pocket:
            case 1|2|3|4|5|6:
                return True
            case 8|9|10|11|12|13:
                return False
    else:
        return not turn

turn: bool = True#light up purposes ONLY

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

    stones = 0
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
        board[space] += 1

    sync()

def compile(stones, start):
    numlist = []

    for i in range(stones):
        start += 1
        if start > 13:
            start = 0

        match start:
            case 0|7:
                numlist.append(100)
                if turn == True and start == 0:
                    numlist.append(0)
                if turn == False and start == 7:
                    numlist.append(7)




        numlist.append(start)
    return numlist

def sync():
    board[0] = store1
    board[7] = store2
    for i in range(1,7):
        board1[i] = board[i]
    for i in range(8,14):
        board2[i] = board[i]










#=======================================================================================
printboard()
print(isvalidmove(1))
movestone(1)
printboard()

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
