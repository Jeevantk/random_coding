import urllib2
import urllib
import requests
import sys
import os


def download_lecture(module_number,lecture_number,flag):
	module_number_str=""

	lecture_number_str=""


	if module_number/10==0:
		module_number_str="0"+str(module_number)
	else:
		module_number_str=str(module_number)

	if lecture_number/10==0:
		lecture_number_str="0"+str(lecture_number)
	else:
		lecture_number_str=str(lecture_number)	

	filename="mod"+module_number_str+"lec"+lecture_number_str+".mp4"


	download_link="http://npteldownloads.iitm.ac.in/downloads_mp4/106106156/mod"+module_number_str+"lec"+lecture_number_str+".mp4"
	request = requests.get(download_link)

	

	#print module_number
	if request.status_code == 200:
		rsp = urllib2.urlopen(download_link)
		with open(filename,'wb') as f:
			f.write(rsp.read())
		return 1
	else:
		if flag==0:
			sys.exit(0)
		return 0 
	

if __name__ == "__main__":
	
	module_number=1
	lecture_number=1
	flag=1
	course_title="Introduction_to_Modern_App_development"
	os.makedirs(course_title)
	os.chdir(course_title)
	while(True):
		print ("Downloading lecture Number "+ str(lecture_number))
		flag=download_lecture(module_number,lecture_number,flag)
		if not flag:
			module_number+=1
			lecture_number-=1
		lecture_number+=1	



