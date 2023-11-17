#!/bin/bash
input="/Users/michaelciao/Downloads/CSCI89890/smaller.txt"
variablename='https://github.com/'
ending='.git'
newarr=()
mkdir hubstuff
cd hubstuff
echo "yeet" > smaller.txt
while IFS= read -r line
do
  line=${line%$'\n'} 
  url="$variablename""$line""$ending"
  echo $url
  git clone $url
  echo "$line"
  IFS='/'

  read -ra newarr <<< "$line"
  echo "${newarr[0]}"
  chmod -R 777 ${newarr[1]}
  find ${newarr[1]} -name "pom.xml" >| poms.txt
  /usr/local/bin/python3.10 /Users/michaelciao/Downloads/CSCI89890/pomVersion.py 
  cd ${newarr[1]}
#   find . -name "*Test.java" > testFiles.txt
  find . -name "*.java" > testFiles.txt
  /usr/local/bin/python3.10 /Users/michaelciao/Downloads/CSCI89890/modifyTestFiles.py ${newarr[1]}
  mvn test > ${newarr[1]}.txt
  echo ${newarr[1]}.txt >> ../analyzeTheseF.txt
  mkdir ../files
  mv ${newarr[1]}.txt ../files
  cd ..
  IFS=''
done < "$input"




#find . -name "*Test.java" > testFiles.txt
#/usr/local/bin/python3.10 /Users/michaelciao/Downloads/CSCI89890/modifyTestFiles.py
#rm -r ${newarr[1]}

