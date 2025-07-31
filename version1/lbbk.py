import os
def headcheck(content, x): 
    check = False
    while check == False:
        if "**/@]" in content[0:x]:
            instructions = content [0:x]
            check = True
        else:
            x = x + 1
    return instructions, x #return the header instructions and the amount of characters before header ends
def spacecheck(content,lend, y):
    check = False
    y = lend + 1
    while check == False:
        if "&" in content[lend:y]:
            spacef = content [lend:y]
            check = True
        else:
            y = y + 1
    return spacef, y #return the header instructions and the amount of characters before header ends
def findend(content, symbol, startpos):
    y = 0
    check = False
    y = startpos + 1
    while check == False:
        if symbol in content[startpos:y]:
            spacef = content [startpos:y]
            check = True
        else:
            y = y + 1
    return spacef #return the the number after repeat and the line num
def reverse_slice(instructions, times):
    start = instructions.find(times)
    end = start + len(times)
    return start, end
def findline(content, dline):
    body_lines = content.splitlines(True)
    numline = int(dline)  # Make sure dline is an integer
    if numline <= len(body_lines):
        fline = body_lines[numline - 1]  # Indexing lines in Python starts at 0
        return fline
    else:
        print("Line doesn't exist. File only has", len(body_lines), "lines.")
        return None
def removerepeat(instructions, lstart, end):
    instructions = instructions.replace(instructions[lstart:end], '')
    return instructions
def donothing():
    nothing = 0
print("Enter mode. 1 = Read .LBBK, 2 = Convert .TXT to .LBBK")
mode = int(input())
if mode == 1:
    print("Enter path of the .LBBK file")
    path = input()
    filehandle = open(path)
    content = filehandle.read()
    length = len(content)
    x = 0
    instructions, x = headcheck(content, x) #check content for the header
    content = content[x:length]
    igcount = instructions.count("IGNORE")
    n = 0
    count = instructions.count("REPEAT")
    u = 0
    if igcount > 0:
        for i in range(igcount):
            u = u + 1
        if u == 1:
            lstart, lend = reverse_slice(instructions, "IGNORE")
            y = 0
            linenum_str, cend = spacecheck(instructions, lend, y)
            linenum_str = linenum_str.strip().rstrip("&")
            linenumignore = int(linenum_str) + 1
            igline = findline(content, linenumignore)
            if igline:
                content = content.replace(igline, '', 1)
        else:
            k= 0 
            while k != count:
                lstart, lend = reverse_slice(instructions, "IGNORE")
                y = 0
                linenum_str, cend = spacecheck(instructions, lend, y)
                linenum_str = linenum_str.strip().rstrip("&")
                linenumignore = int(linenum_str) + 1
                cend = int(cend)
                igline = findline(content, linenumignore)
                if igline:
                    content = content.replace(igline, '', 1)
                instructions = removerepeat(instructions, lstart, cend)
                k = k + 1

    if count > 0:
        for i in range(count):
            n = n + 1
        if n == 1:
            start, _ = reverse_slice(instructions, "X")
            start = start + 1
            endstr = findend(instructions, "#", start)  # fix: search in instructions, not full content
            repeatnum = endstr.strip().rstrip("#")
            lstart, lend = reverse_slice(instructions, "REPEAT")
            y = 0
            numlen, empty = spacecheck(content, lend, y) # check for space after the number following repeat       THIS IS THE LUNE NUMBER!!!
            numlen = numlen.strip().rstrip("&") #remove the and which signals numstop and remove any spaces
            newend = lstart + int(numlen) #add length of number to the start of the number so all of it is recorded
            linenum = instructions[lstart:newend] #the repeat command
            fline = findline(content, numlen)
            z = 0
            while z != int(repeatnum):
                print(fline)
                z = z + 1
        else:
            k = 0
            while k != count:
                start, end = reverse_slice(instructions, "X")
                start = start + 1
                endstr = findend(instructions, "#", start)  # fix: search in instructions, not full content
                repeatnum = endstr.strip().rstrip("#")
                lstart, lend = reverse_slice(instructions, "REPEAT")
                y = 0
                numlen, empty = spacecheck(instructions, lend, y) # check for space after the number following repeat       THIS IS THE LUNE NUMBER!!!
                numlen = numlen.strip().rstrip("&") #remove the and which signals numstop and remove any spaces
                newend = lstart + int(numlen) #add length of number to the start of the number so all of it is recorded
                linenum = instructions[lstart:newend] #the repeat command
                fline = findline(content, numlen)
                z = 0
                while z != int(repeatnum):
                    print(fline)
                    z = z + 1
                k = k + 1
                instructions = removerepeat(instructions, lstart, end)
    else:
        donothing()
    print(content[x:length])
elif mode == 2:
    print("Enter path of the .TXT file")
    path = input()
    print("Enter desired output path of the .LBBK file (just the folder path)")
    outpath = input()
    base = os.path.basename(path)
    filename_without_ext = os.path.splitext(base)[0]
    if not outpath.endswith("\\") and not outpath.endswith("/"):
        outpath += "\\"
    outfilename = outpath + filename_without_ext + ".lbbk"
    with open(path, "r", encoding="utf-8") as f_in, open(outfilename, "w", encoding="utf-8") as f_out:
        f_out.write(f_in.read())
        print(f"Successfully converted {path} to {outfilename}")
else:
    donothing()
print("Press enter to close")
anything = input()
