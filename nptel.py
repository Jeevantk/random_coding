import urllib2
import urllib
import requests
import sys
import os


def download_lecture(lecture_number,flag):

	lecture_number_str=""

	lecture_number_str=str(lecture_number)

			

	filename="Lecture"+lecture_number_str+".mp4"


	download_link="http://nptel.ac.in/courses/106106143/"+lecture_number_str+".mp4"
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

	lecture_number=5
	flag=1
	course_title="Reinforcement Learning"
	os.makedirs(course_title)
	os.chdir(course_title)
	while(True):
		print ("Downloading lecture Number "+ str(lecture_number))
		flag=download_lecture(lecture_number,flag)
		if not flag:
			lecture_number+=1
		lecture_number+=1	



