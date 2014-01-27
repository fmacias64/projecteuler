import os
import fileinput
from fileinput import FileInput
import glob
import string, sys
from string import Template
import re

addinitlogging=Template('	private static final Logger log = LoggerFactory.getLogger($classname.class);'+os.linesep)
addamendhistory=Template(\
'* '+os.linesep+\
'* NAME    : John Liang'+os.linesep+\
'* VERSION : 1.4        DATE: 24-Jan-2014               REF: P446'+os.linesep+\
'* PURPOSE : Updated logging to accommodate configuration setting change.'+os.linesep)

testpath='/Users/john/workspace/pys/mg_test'
workspacepath='/Users/john/workspace/pys/mg_test'
importslf4jstr='import org.slf4j.Logger;'+os.linesep+'import org.slf4j.LoggerFactory;'+os.linesep

def getClassName(str):
   rex='public class ([a-zA-Z0-9]+) '
   m=re.search(rex,str)
   classname=m.group(1)
   if len(classname)>0:
      return classname
   else:
      raise Exception('Cannot find class name from input['+str+']')
   return None

def getAmendHistoryIndexLineno(filename):
   f=open(filename,'r')
   lines=f.readlines()
   f.close()
   for index, line in enumerate(lines):
      if "*/" in line:
         return index+1
   return -1

def getAmendHistoryIndexLineno2(fileinput):
   for line in fileinput:
      if "*/" in line:
         return fileinput.filelineno()+1
   return -1

def processAddlog(searchPattern):
    processing_addlog=False
    for line in fileinput.input(glob.glob(searchPattern),inplace=1):
    	if "public class" in line:
    		processing_addlog=True
    		classnameLine=line
    	else:
    		if processing_addlog and "{" not in line:
    			sys.stdout.write(addinitlogging.substitute( \
    				classname=getClassName(classnameLine)))
    			processing_addlog=False
        sys.stdout.write(line)
    fileinput.close()



def processingRemoveMglog(searchPattern):
    processing_remove_mglog=False
    for line in fileinput.input(glob.glob(searchPattern),inplace=1):
        if "MgLogger" in line and not line.startswith('import'):
            processing_remove_mglog=True
        if processing_remove_mglog:
            processing_remove_mglog=False
            continue
        sys.stdout.write(line)
    fileinput.close()

def processingReplaceMglogSlf4j(searchPattern):
    processing_replace_mglog_slf4j=False
    for line in fileinput.input(glob.glob(searchPattern),inplace=1):
        if line.startswith('import') and "MgLogger" in line:
            processing_replace_mglog_slf4j=True
        if processing_replace_mglog_slf4j:
            processing_replace_mglog_slf4j=False
            sys.stdout.write(importslf4jstr)
            continue
        sys.stdout.write(line)
    fileinput.close()

# def processingAddAmendHistory(searchPattern):
#     amendhistoryLineno = -1
#     for line in fileinput.input(glob.glob(searchPattern),inplace=1):
#         if fileinput.isfirstline():
#             amendhistoryLineno = \
#                 getAmendHistoryIndexLineno(fileinput.filename())
#         if amendhistoryLineno == fileinput.filelineno():
#             sys.stdout.write(addamendhistory.substitute())
#         sys.stdout.write(line)
#     fileinput.close()

def processingAddAmendHistory(searchPattern):
    input=FileInput(files=tuple(glob.glob(searchPattern)),inplace=1)
    for line in input:
        if "*/" in line:#find out amend history last line
            sys.stdout.write(addamendhistory.substitute())
        sys.stdout.write(line)
    input.close()

def processlines(processfunc, searchPattern):
	processfunc(searchPattern)


def _test():
    print 'begin testing the script...'
    print 'running in path:',os.getcwd()
    searchPattern="*.java"
    print 'files searching patter:', searchPattern
    os.chdir(testpath)
    #begin to process
    processlines(processAddlog, searchPattern)
    processlines(processingRemoveMglog, searchPattern)
    processlines(processingReplaceMglogSlf4j, searchPattern)
    processlines(processingAddAmendHistory, searchPattern)
    #end of process
    os.chdir(workspacepath)

if __name__=='__main__':
    _test()
