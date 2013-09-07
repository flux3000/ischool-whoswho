#!/usr/bin/python

import urllib
import urllib2
import urlparse
import re, string
from bs4 import BeautifulSoup

def RequestResponse(url):
    '''
    This method makes an HTTP request over the network (just like a web browser)
    and returns the contents of the requested url.
    '''
    try:
        response = urllib2.urlopen(url)
        return response
    except urllib2.URLError as err:
        print("Error opening url {} .\nError is: {}".format(url, err))
        return False


def getNames(url, output=True):
    
    response = RequestResponse(url)
    if not response: return
    soup = BeautifulSoup(response.read())
    
    students = []
    student_list = soup.find_all("table", "person-teaser")
    
    for student_entry in student_list:

        student_img = student_entry.img['src'].split('/')[-1]
        
        ''' Uncomment this to download the images. '''
        #urllib.urlretrieve("http://www.ischool.berkeley.edu/files/imagecache/profile-pic/" + str(student_img), "static/profilephotos/" + student_img)
        
        student_name = student_entry.find("div", "title").text.encode('ascii', 'replace')
        student_year = student_entry.find("div", "field-field-person-degree-year").text
        try:
            student_focus = student_entry.find("div", "field-field-person-focus").text[6:]
        except:
            student_focus = ""
            
        #print('{}\t{}\t{}\t{}'.format(student_name.strip(), student_img, student_year.strip(), student_focus.strip()))
        students.append('{}\t{}\t{}\t{}'.format(student_name.strip(), student_img, student_year.strip(), student_focus.strip()))
    
    
    ''' write the names and info to a tab-delimited text file. Note that it won't pick up the genders - you have to manually enter those. Open the file in excel and make a new column after focus and fill with either M or F.'''
    outputfile = open('studentdata', "a")
    for i in students:
        outputfile.write(i)
        outputfile.write("\n")
    outputfile.close()
    print "Student names saved."      
       
if __name__ == '__main__':

    getNames('http://www.ischool.berkeley.edu/people/students/mims')
    getNames('http://www.ischool.berkeley.edu/people/students/phd')
