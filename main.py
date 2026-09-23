# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Look Upon My Works Ye Mighty And Despair

# Convenience Functions =========================================================================================
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
        for i in range(1, 7):
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
    quicknum("        ", False)
    row(1)
    quickline(1, 55, "")
    print(" ")
    print("B: ", end="")
    quickprint("         ", False)
    row(2)
    print("    " + str(store2) + "                                               " + str(store1))
    row(1)
    print("A: ", end="")
    quickprint("         ", True)
    row(1)
    quickline(1, 55, "")
    row(1)
    print("   ", end="")
    quicknum("         ", True)


# Game functions ========================================================================


def pocketcheck(pocket):
    if (pocket > 0 and pocket < 14 and pocket != 7):
        match pocket:
            case 1 | 2 | 3 | 4 | 5 | 6:
                return True
            case 8 | 9 | 10 | 11 | 12 | 13:
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

            else:
                stones = board2[pocket]

            board[pocket] = 0
        case "invalid":
            return "invalid"

    spaces = compile(stones, pocket)
    print("POCKET:", pocket)
    print("STONES:", stones)
    print("SPACES:", spaces)
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
    global turn
    numlist = []

    for i in range(stones):
        start += 1
        if start > 13:
            start = 0

        match start:
            case 0 | 7:
                if (start == 0 and not turn) or (start == 7 and turn):
                    numlist.append(100)
                else:
                    start += 1
                    numlist.append(start)

            case 1 | 2 | 3 | 4 | 5 | 6 | 8 | 9 | 10 | 11 | 12 | 13:
                numlist.append(start)

    return numlist


def sync():
    for i in range(1, 7):
        board1[i] = board[i]
    for i in range(8, 14):
        board2[i] = board[i]


def taketurn():
    move = 0
    global turn

    match turn:
        case True:
            row(2)
            print("player A's turn")
            row(1)
            print("potential moves:", end=" ")
            for i in range(1, 7):
                if isvalidmove(i) == "valid":
                    print(i, end=" ")

            row(2)
            while movestone(move) == "invalid":

                print('Enter your move: ', end='')
                try:
                    move = int(input())

                except ValueError:
                    print("Enter a valid integer")

        case False:
            row(2)
            print("player B's turn")
            row(1)
            print("potential moves:", end=" ")
            for i in range(8, 14):
                if isvalidmove(i) == "valid":
                    print(i, end=" ")

            row(2)
            while movestone(move) == "invalid":
                print('Enter your move:', end='')
                move = int(input())


def capture(end):
    global store1
    global store2
    opposite = 14 - end
    match turn:
        case True:
            if end in board1 and board1[end] == 1 and board2[opposite] > 0:
                store1 += board2[opposite] + 1
                board2[opposite] = 0
                board1[end] = 0
        case False:
            if end in board2 and board2[end] == 1 and board1[opposite] > 0:
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
        endside = True
        return flag

    flag = True

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

    if store1 > store2:
        print("Player A has won with " + str(store1) + " stones")
    elif store2 > store1:
        print("Player B has won with " + str(store2) + " stones")
    else:
        print("Tie of " + str(store1))


# =======================================================================================
def set():
    for i in board2:
        board2[i] = 0


while not wincon():
    printboard()
    taketurn()
    row(2)

end()

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
