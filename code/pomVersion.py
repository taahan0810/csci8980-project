testFiles = open("poms.txt","r")
pomFileLoc = testFiles.readlines()

print(pomFileLoc[0])
pomFile = open(pomFileLoc[0].strip(), "r+")
pomContent = pomFile.readlines()
looking = False
lookingTimes = 0
for l in range(len(pomContent)):
    line = pomContent[l]
    #print(line)
    if "artifactId" in line and "maven-compiler-plugin" in line:
        looking = True
        continue
    if "<target>" in line and looking:
        print("target acuqired")
        lookingTimes += 1
        lis = line.replace('<', '>').split('>')
        print(lis)
        for obj in lis:
            try:
                if "jdk.version" in obj or float(obj)< 1.8 :
                    print(1.8)
                    pomContent[l] = "<target>1.8</target>\n"
                    #write new line
            except:
                continue 
    elif "<source>" in line and looking:
        print(lookingTimes)
        print("source found")
        lookingTimes += 1
        lis = line.replace('<', '>').split('>')
        print(lis)
        #a = "<source>1.7</source>"
        #a = a.replace('<','>').split('>')
        for obj in lis:
            try:
                if "jdk.version" in obj or float(obj)< 1.8 :
                    print(1.8)
                    pomContent[l] = "<source>1.8</source>\n"
                    #write new line
            except:
                continue    
    
    
    if lookingTimes >=2:
        break
    
            
pomFile.seek(0)
pomFile.truncate(0)
a = ''.join(pomContent)
pomFile.write(a)
pomFile.close()
