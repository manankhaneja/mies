# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:52:24 2018

@author: Manan Khaneja
"""
import fileinput
import os


def concatination(dir_path, outpath, outfile_name):
    assert os.path.isdir(dir_path), "I did not find the directory"
    print("\n")
    outfile_path = outpath + "\\" + outfile_name
    filenames = os.listdir(dir_path)
    complete_names=[]
    for index in range(0,len(filenames),1):
        complete_names.append(os.path.join(dir_path,filenames[index]))
    with open(outfile_path, 'a+') as fout , fileinput.input(complete_names) as fin:
        for line in fin:
            fout.write(line)
def main():
    roll = input("Enter your roll number \n")
    user_input =input("Enter the full path of your directory:  \n")
    assert os.path.isdir(user_input), "I did not find the directory"
    print("\n")
    all_files=os.listdir(user_input)
    cmd = "mkdir " + user_input + "\\" + roll
    os.system(cmd)
    outpath = user_input + "\\" + roll 
    for index in range(len(all_files)):
        if "week" or "Week" in all_files[index]:
            address = user_input + "\\" + all_files[index] + "\\" + roll + "\\" + "New Data Collection" 
            directory = os.listdir(address)
            address = address + "\\" + directory[0] + "\\" + "Keyboard Database" + "\\" + "sentence" 
            address_happy = address + "\\" + "Emotional" + "\\" + "Happy"
            address_sad = address + "\\" + "Emotional" + "\\" + "Sad"
            address_neutral = address + "\\" + "Neutral"
            concatination(address_happy, outpath, "happy.txt")
            concatination(address_sad, outpath, "sad.txt")
            concatination(address_neutral, outpath, "neutral.txt")
            
if __name__=='__main__':
    main()