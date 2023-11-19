import sys
#/Users/michaelciao/Downloads/CSCI89890/hubstuff/JavaZinc/testFiles.txt
testFiles = open("/Users/michaelciao/Downloads/CSCI89890/hubstuff/" + str(sys.argv[1])+"/testFiles.txt","r")
allTestFiles = testFiles.readlines()

for file in allTestFiles:
    f = open(file.strip(), "r+")
    print("__________________________________________________________________\n NEW FILE ALERT")
    print(file)
    #print(f.readlines()[0])
    print("______________________________\n")
    looking = False
    skipNextLine = False
    allLines = f.readlines()
    i = 0
    x = len(allLines)
    while i < x:
    #for i in range(len(allLines)):
        line = allLines[i]
        #print("LAST: " +allLines[len(allLines)-5] + " cur line is " + line)
  
        if "//" in allLines[i] and "https://" not in allLines[i] and "http://" not in allLines[i]:#ignore lines with comments in java
            i+=1
            continue
        if allLines[i] == '\n':
            i +=1
            continue
        if "catch" in line:
            i+=1
            continue
        if "private" in line or "public" in line or "protected" in line or "void" in line: #stop looking unless there is a test code indicator cuase there can be other methods
            looking = False
            i+=1
            continue
        if skipNextLine:
            skipNextLine = False
            i+=1
            continue
        
        #if "System.out.println" in line and "System.currentTimeMillis()" in line:
        if "swagLol" in line:
            # print("ignored")
            i+=1
            continue
        if "@Test" in line:
            # print(line)
            looking = True
            j = i
            while j < len(allLines)-1:
                j+=1
                if "public" in allLines[j] or "private" in allLines[j] or "protected" in allLines[j] or "void" in allLines[j]:
                    if  "throws" in  allLines[j+1]:
                        i = j+2
                    else:
                        i = j + 1
                    allLines.insert(i, "long swagLol = -1000;\n")
                    i+=1
                    break 
            #i+=1
            continue
        # elif "@Before" in line:
        #     looking = False
        # elif "@After" in line:
        #     looking = False
        # elif looking and allLines[i] != '\n' and allLines[i].strip()[-1] == '{':
        #     pCounter = 0 #parentheses counter
        #     l = -10
        #     for l in range(i,len(allLines)): #search from the current line to worst case the end of the file
        #         for c in allLines[l]:
        #             if c == '{':
        #                  print("p counter up")
        #                  pCounter +=1
        #             if c == '}':
        #                 print("p counter down")
        #                 pCounter-=1
        #         if pCounter == 0: 
        #             print("p counter all around")
        #             break   
        #     i = l + 2
        #elif "@" in line and "Override" not in line:
        elif "@" in line:
            looking = False
        #print("beofre "+ line)
        if '(' in line and looking:
            #print("after " + line)
        #if '(' in line and ')' in line and looking:
            #print("looking")
            identify = file.split('/') #split so we can get the project name
            bonusInfo = "P: "+  sys.argv[1]+ " F: "+ identify[len(identify)-1].strip()+ "  line #: " + str(i+2) + " Time: "

            #if "swagLol =" not in allLines[i-1]: # dont write more than one line if rerunning code and codebase already pulled
            pCounter = 0 #parentheses counter
            searchChar = '('
            searchChar1 = ')'
            #print( allLines[i])
            l = 0
            #print("before at line " + str(i)+ ": " + allLines[i])
            for l in range(i,len(allLines)): #search from the current line to worst case the end of the file
                if "//" in allLines[l] and "https://" not in allLines[l] and "http://" not in allLines[l]:
                    #print("eaeaeaeaeae")
                    continue
                for c in allLines[l]:
                    if c == searchChar:
                        #print("p counter up")
                        pCounter +=1
                    if c == searchChar1:
                        #print("p counter down")
                        pCounter-=1
                if pCounter == 0 and allLines[l][-2] !=',' and ')\n' not in allLines[l]  and '+\n' not in allLines[l]:#dual variable declaration of same kind in one line for comma
                    #print("p counter all around")
                    if allLines[l][-2] =='{':
                        pCounter = 1
                        searchChar = '{'
                        searchChar1 = '}'
                        continue
                    allLines.insert(l+1,"System.out.println(\"" + bonusInfo + "\" + (System.currentTimeMillis()-swagLol));\n")
                    break   
                
        
            

            #allLines.insert(i+1,"System.out.println("bonusInfo): \"  +System.currentTimeMillis());\n" )
            #allLines.insert(i+1,"System.out.println(\"" + bonusInfo + "\" + (System.currentTimeMillis()-swagLol));\n")
            ab = allLines[i-1].strip()
            #print(allLines[i-1] + " stripped " + ab[-1]+ " finding where to put the swaglol")
            #if allLines[i-1] != '\n' and len(ab) !=0 and (allLines[i-1].strip()[-1] == '=' or allLines[i-1].strip()[-1] == ',' or allLines[i-1].strip()[-1] != ';'):
            if allLines[i-1] != '\n' and len(ab) !=0 and (allLines[i-1].strip()[-1] == '=' or allLines[i-1].strip()[-1] == ',' or ab[-1].isalpha()): #assingning variables or double declaration with = or , 
                #print("activated activeate")
                
                #allLines.insert(i-1, "System.out.println(\"Bef(" + bonusInfo + "): \" +System.currentTimeMillis());\n")
                # if firstSwagLol:
                #     allLines.insert(i-1, "long swagLol = System.currentTimeMillis();\n")
                #     firstSwagLol = False
                # else:
                #     allLines.insert(i-1, "swagLol = System.currentTimeMillis();\n")
                if allLines[i-2] != '\n' and len(allLines[i-2].strip()) !=0 and allLines[i-2].strip()[-1] == '=':
                    #print("GO INSIDE  activeate")
                    allLines.insert(i-2, "swagLol = System.currentTimeMillis();\n")
                else:
                    allLines.insert(i-1, "swagLol = System.currentTimeMillis();\n")
                # print("order")
                # print(allLines[i-1])
                # print(allLines[i])
                # print("order")
            elif allLines[i] != '\n' and len(allLines[i].strip()) !=0 and allLines[i].strip()[0] == '.':
                allLines.insert(i-1, "swagLol = System.currentTimeMillis();\n")                                        
            else:
                #allLines.insert(i, "System.out.println(\"Bef(" + bonusInfo + "): \" +System.currentTimeMillis());\n")
                # if firstSwagLol:
                #     allLines.insert(i, "long swagLol = System.currentTimeMillis();\n")
                #     firstSwagLol = False
                # else:
                #     allLines.insert(i, "swagLol = System.currentTimeMillis();\n")
                allLines.insert(i, "swagLol = System.currentTimeMillis();\n")
            #print(allLines[i])
            #print(allLines[i+1])
            #print(allLines[i+2])
            i = l+1
            #skipNextLine = True
            x = len(allLines)
        i+=1
    f.seek(0)
    f.truncate(0)
    a = ''.join(allLines)
    #print(a)
    f.write(a)
    f.close()



    # for line in f.readlines():
    #     #print(line)
    #     if skipNextLine:
    #         skipNextLine = False
    #         continue
    #     if "@Test" in line:
    #         print(line)
    #         looking = True
    #         skipNextLine = True
    #     elif "@Before" in line:
    #         looking = False
    #     elif "@After" in line:
    #         looking = False
    #     if '(' in line and ')' in line and looking:
    #         print(line)
