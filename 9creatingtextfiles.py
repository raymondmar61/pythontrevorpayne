#Trevor Payne 9 Creating Text Files

#text files help create other python files, c, c++, html, xml files because all text based files.  Write script to write other scripts.
#today create a script create a text file with text file name as date and 30 blank lines in the text file

import time as t
from os import path #path checks file if not already created.  No overwriting.

def createFile(dest):
	'''The script creates a text file at the passed in location, names file based on date'''
	#print(dest) #print statement used to dest createFile () function
	date = t.localtime(t.time()) #get current time/date and save to date
	#FileName = Month_Date_Year.txt
	print(date) #time.struct_time(tm_year=2016, tm_mon=7, tm_mday=19, tm_hour=17, tm_min=43, tm_sec=21, tm_wday=1, tm_yday=201, tm_isdst=1)
	name = "%d_%d_%d.txt" % (date[1], date[2], (date[0] % 100)) #output in month_date_year.txt format
	if not (path.isfile(dest + name)): #checks if file already exists.  If not, then create file
		filenew = open(dest + name, "w")
		filenew.write("\n"*30) #write a new line 30 times
		filenew.close()

if (__name__ == "__main__"): #if file name main or the file is the main file, then call function createFile(dest)
	#destination varabile is location file to be saved
	destination = "/home/mar/Python/trevorpayne/"
	createFile(destination) #createFile(destination).  Call function createFile() passing destination to dest
	input("done!!!") #raw_input doesn't work in python 3.5.  Use input("done!!!")
