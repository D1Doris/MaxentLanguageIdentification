#!/usr/bin/python

# This script is written by Doris Hoogeveen, date 5th of August 2015.
# For problems or more information please contact her at doris dot hoogeveen at gemail dot com.

import sys, os, re
import subprocess, codecs, operator

def main(inputfile, maxentpath):
    lg_object = lang_guesser(inputfile, maxentpath)
    lg_object.guess_language()
    # Or, if you want to add a new language to the model
    #lg_object = lang_guesser(inputfile, maxentpath)
    #lg_object.add_language('xxx') # Where 'xxx' is the Ethnologue code of the new language (http://www.ethnologue.com/)	

class lang_guesser():
    def __init__(self, inputfile, maxentpath):
	self.inputfile = inputfile
	self.maxentpath = maxentpath

    def _prepare_test_data(self):
	''' Sorts the trigrams in the inputfile and writes them to a test file. '''
	trigramdict = self._make_trigrams()

	test = open(self.maxentpath + 'TEST', 'w')
    	trigramlist = sorted(trigramdict, key=trigramdict.__getitem__, reverse=True)
    	test.write('WTF ') # WTF is a dummy classification. The classifier needs this.
    	for i in trigramlist:
	    test.write(i + ' ')
    	test.write('\n')	
    	test.close()


    def _make_trigrams(self):
	''' Turns the text in the inputfile into character trigrams and returns a dictionary with their frequencies. '''
	open_file = codecs.open(self.inputfile, 'r', 'utf-8')
        text = open_file.read()
        open_file.close()

	text = re.sub('\s+', ' ', text) # Get rid of excessive white space
        text = re.sub('[^\w ]', '', text)
	text = re.sub(' ', '_', text)
	text = text.lower()

	unigrams = list(text)
	trigrams = {}
	top = len(unigrams)
	top = top - 2
	for i in range(0,top):
	    trigram = unigrams[i] + unigrams[i+1] + unigrams[i+2]
	    trigrams.setdefault(trigram, 0)
	    trigrams[trigram] += 1
	return trigrams

    def guess_language(self):
	''' Classifies the contents of TEST. '''
	self._prepare_test_data()
	output,_ = subprocess.Popen(["wine", self.maxentpath + "maxent.exe", "-p", "-m", self.maxentpath + "model", self.maxentpath + "TEST", "-o", self.maxentpath + "TEST_out.txt", "--detail"], stdout=subprocess.PIPE).communicate()

	test_out_open = open(self.maxentpath + 'TEST_out.txt', 'r')
	test_out_read = test_out_open.read()
	test_out_open.close()

	tuplepat = re.compile(r'([a-z][a-z][a-z])\t(0\.[0-9]+)')
	tuples = re.findall(tuplepat, test_out_read)
	tuples.sort(key=operator.itemgetter(1))
	tuples.reverse()
	print "Guessed language:", tuples[0][0]

			
    def add_language(self, newlangcode):
        ''' Uses the data in the inputfile to construct a new language model and retrains the classifier. '''
        trigramdict = self._make_trigrams()
	trigramlist = sorted(trigramdict, key=trigramdict.__getitem__, reverse=True)
	trainfile = codecs.open(self.maxentpath + 'TRAIN', 'a', 'utf-8')
	trainfile.write(newlangcode + ' ')
	if len(trigramlist) < 400: # We need the most frequent 400 trigrams for the model, or all of them if we have less
	    for i in trigramlist:
		trainfile.write(i + ' ')
	else:
	    for i in range(0,400):
		trainfile.write(trigramlist[i] + ' ')
	trainfile.write('\n')
	trainfile.close()
	self.retrain_classifier()

    def retrain_classifier(self):
	''' Retrains the maxent classifier. '''
	output,_ = subprocess.Popen(["wine", self.maxentpath + "maxent.exe", "-v", "-i", "4", "--gis", self.maxentpath + "TRAIN", "-m", self.maxentpath + "model"], stdout=subprocess.PIPE).communicate()
	print "Retrained the model."

def usage():
    usage_text = '''
    This script can be used to perform language identification using a maxent classifier and a set of language models.

    USAGE: ''' + os.path.basename(__file__) + ''' <inputfile> <maxent_dir>

    <inputfile> is the file you would like to know the language off. This should be a plain text file encoded in UTF-8.
    <maxent_dir> is the path to the directory that contains maxent.exe

    The script will output the iso name of the guesed language.

    Example: ''' + os.path.basename(__file__) + ''' inputfile /home/hoogeveen/maxent/

    Prerequisite: Wine needs to be installed to be able to run the classifier.

'''
    print usage_text
    exit()

if __name__ == '__main__':
    if len(sys.argv[1:]) == 2:
	inputfile = sys.argv[1]
	maxentpath = sys.argv[2]
	if not maxentpath.endswith('/'):
	    maxentpath += '/'
	main(inputfile, maxentpath)
    else:
	usage()
