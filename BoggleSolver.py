'''
Steven Luu - 1630072
Wednesday, May 16
R. Vincent, instructor
Final Project
'''
import time

#The purpose of this program is to solve boggle word puzzles in .txt forms
#It outputs all possible words and points of a word set

def boggle(board):
    result = set()
    if 'QU' in board:                                       #Curve ball of Boggle. This step is obligatory or else the board wouldn't remain a square
        board = board.replace('QU', 'q')                    #The letters Qu take up 1 spot in the board, but counts for two letters
        for k in WORDS:                                     #Modify entire dictionary into 'variable' string q
            if 'QU' in k:                                   
                WORDS.add(k.replace('QU', 'q'))
                WORDS.discard(k)
        for l in PREFIXES:                                  #Same modfication as the dictionary
            if 'QU' in l:
                PREFIXES.add(l.replace('QU', 'q'))
                PREFIXES.discard(l)    
    def continue_path(prefix, path):                        #Recursive function that will go through all characters
        if prefix in WORDS and len(prefix) >= 3:            #Words are only legal if they are more than 3 letters
            result.add(prefix)
        if prefix in PREFIXES:                                      #prefix of words 
            for j in neighbors(path[-1], int(len(board)**0.5)):     #Last element of the path, so the last letter of the combination of letter in the prefix
                if j not in path and board[j] != '0':               #Make sure we are NOT OUT OF BOUND AND NOT BACKTRACKING!
                    continue_path(prefix +board[j], path + [j])     #Go to the next location
    for (x, y) in enumerate(board):                         #creates variable x and y for function continue_path. x is the potential combination of words and y is a list of the path taken
        if y != '0':                                        #If the projected path is out of bounds, stop continuing on that path
            continue_path(y, [x])                           #continues until the bottom right character of the board has found all combinations of words
    for p in result:                                                #Exception only applies to Boards with curveball QU
        if 'q' in p:                                                #Retransform the results from 'q' to 'QU' to make sure the score is correct.
            result.add(p.replace('q', 'QU'))
            result.discard(p)
    return sorted(result)


def prefixes(word):
    return [word[:i] for i in range(len(word))]             #Creates prefixes from longed
             
def readwordlist(filename):                                 #Basic fuction to return dictionary into a set
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))      #Prefix will be used
    return wordset, prefixset                               #returns a set of dictionary words and prefix


def neighbors(i, x):                                        
    return (i-x-1, i-x, i-x+1,                              #all 8 possible directions a letter can travel to
            i-1,        i+1,
            i+x-1, i+x, i+x+1)

def graphready(board):                                      #a function to make the list easier to read by my functon. Side and corner vertexes will not have edges leading to corners
    b_text = board.replace(' ', '')
    blist = b_text.split()
    topper = len(blist) + 2
    for i in range(0,len(blist)):
        blist[i] = '0' + blist[i] + '0'                     #adds 0 in front and in back of row     Looks something like this:
    blist.append('0'*topper)                                #add 0's to the bottom                          000000
    blist.insert(0,'0'*topper)                              #add 0's to the top                             0xxxx0
    return ''.join(blist).upper()                           #                                               0xxxx0
                                                            #                                               0xxxx0
                                                            #                                               0xxxx0
                                                            #                                               000000
                                
def points(boggle):                                         #http://www.spoj.com/problems/BOGGLE/
    r = 0                                                   #rules were taking off this website
    for i in boggle:
        if len(i) <= 4:                                     #3-4 letters :1 point
            r += 1
        elif len(i) == 5:                                   #5 letters: 2 points
            r += 2
        elif len(i) == 6:                                   #6 letters: 3 points
            r += 3
        elif len(i) == 7:                                   #7 letters: 5 points
            r += 5
        elif len(i) > 7:                                    #8 and more: 11 points
            r += 11
    return r

while True:
    x = input("Input boggle file number or -1 for custom board:")
    strlist = ""
    if x != "-1":
        f = open('boggle/board-points' + x +'.txt', 'r')
        f.readline().strip()      #Removes the first line of text, it is useless, it is only there to represent the board size
        board = f.read()
    #Custom board
    #TODO
    else:
        size = input("Enter size of board")
        for i in range(int(size)):
            row = input("Row " + str(i + 1) + ": ")
            strlist += row.upper() + '\n'        
        board = strlist
    start_time = time.time()
    WORDS, PREFIXES = readwordlist('boggle/dictionary-yawl.txt')                #Variables for the set of words and prefixes used
    print(board)
    boardready = graphready(board)
    print('WORDS FOUND:', boggle(boardready))
    print('Total points:', points(boggle(boardready)))
    print('Solved in around:', time.time()-start_time, 'seconds', '\n')         #computing time






    

    
    

