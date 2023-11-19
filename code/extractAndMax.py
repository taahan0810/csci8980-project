# import required module
import os
# assign directory
directory = 'hubstuff/files' #MIGHT NEED TO CHANGFE IF YOU WANT TO USE HUBSTUFFSMALL

numMax = 50
maxSomeNum = [] #max some number of numbers
searchBase = [] #the lines of those times that were inserted into maxSomeNum

results = open("toptests.txt", "w") # write the results to 
useLess = open("unsuccesful.txt", "w") # write the results to 
useFull = open("succesful.txt", "w") # write the results to 


numFile = 0 
for filename in os.listdir(directory):
    foundUseful = False # assumption to non useful file first
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        curFile = open(f)
        lines = curFile.readlines()


        for line in lines:
        # for b in range(82):
        #     line = lines[b]
            #print(line)
            if "P:" in line and "F:" in line and "line #" in line and "Time:": 
                foundUseful = True #this file is useful since at least one 'Time:' was extracted
                l = line.split(": ")
                val = int(l[4].strip())
                if len(maxSomeNum) < numMax: # append the first numMax non 0 times to the maxSomeNum array
                    maxSomeNum.append(val)
                    searchBase.append(line)
                    maxSomeNum.sort(reverse=True)
                    print(maxSomeNum)
                else:
                    if val > maxSomeNum[0]:
                        print('inserting at start: ' + str(val))
                        maxSomeNum.insert(0,val)
                        maxSomeNum.pop(numMax)
                        searchBase.append(line)
                        
                    elif val > maxSomeNum[numMax-1]:
                        print('inserting ' + str(val))
                        for b in range(numMax-2,-1,-1):
                            if val < maxSomeNum[b]:
                                print("after " + str(maxSomeNum[b]))
                                maxSomeNum.insert(b+1, val)
                                maxSomeNum.pop(numMax)
                                break
                        searchBase.append(line)

        print(maxSomeNum)
        print(len(searchBase))
    if foundUseful == False:
        useLess.write(filename + '\n')
    else:
        useFull.write(filename + '\n')
    numFile+=1 #used to ensure only for the first file do we accept the first ten time values

for m in maxSomeNum:
    for line in searchBase:
        l = line.split(": ")
        val = int(l[4].strip())
        if val == m:
            results.write(line)
            break
useLess.close
results.close()
        


#apply to multiple projects


# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         curFile = open(f)
#         lines = curFile.readlines()
#         print(f)
#         print(i)
#         i+=1
