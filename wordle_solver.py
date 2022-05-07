import sys
from prettytable import PrettyTable
''' MAIN ENTRY POINT '''

if __name__ == '__main__':
    tbl = PrettyTable(['Number', 'Word'])

    print("Good starting words: \nFRAME, GRAZE, WINDY, PAINT, GOURD, SWING, VAPES \nAUDIO, FARTS, ADIEU, OUIJA "
          "\nREADY, PEARS, CHIEF, TOUCH\n")
    words = open('dictionary2.txt', 'r')
    '''
    #while True:
    #tbl.clear_rows()
    done = input("Press 'c' to  exit, enter to continue:")
    print("\n")
    if done == "c":
        words.close()
        sys.exit("Goodbye")
    '''
    # Starting program sequence.
    while True:
        #word = ""
        word = input("Please type the letters you know, use space for unknown: ")
        if len(word) != 5:
            continue
        else:
            #wordArr = []
            wordArr = list(word)
            break
    #unknown = ""
    unknown = input("Please type the letters you know, but don't have the position: ")
    #unknownArr = []
    unknownArr = list(unknown)
    #banned = ""
    banned = input("Enter the characters that are eliminated: ")
    #banArr = []
    banArr = list(banned)
    print(wordArr)

    cnt = 0
    #tbl.clear_rows()
    for i in words:
        #print(i)
        skip = ""
        for p in banArr:            # Checks eliminated characters against the array.
            if p in i:
                skip = "yes"
        for y in unknownArr:        # Checks the characters we don't know position of.
            if y not in i:
                skip = "yes"
        if skip == "yes":           # Can restart loop.
            continue
        lineRead = list(i)
        j = 0
        if len(i) >= 5:
            while j <= 5:
                if j == 5:
                    cnt += 1
                    tbl.add_row([cnt, i.strip()])
                    #print(i)
                    break
                if wordArr[j] == ' ' and j <= 4:
                    j += 1
                elif wordArr[j] == lineRead[j] and j <= 4:
                    j += 1
                else:
                    j += 5
                    break
        else:
            continue
    tbl.align = "l"
    resultString = tbl.get_string(sortby="Number", reversesort=False)
    print(resultString)
