# MaxentLanguageIdentification
The language identification module as used in: http://www.clips.ua.ac.be/sites/default/files/coco.pdf

If you use this model, please cite the paper as follows:

@inproceedings {hoogeveen2011,<br />
	title = {CorpusCollie - A Web Corpus Mining Tool for Resource-Scarce Languages},<br />
	booktitle = {Proceedings of Conference on Human Language Technology for Development},<br />
	year = {2011},<br />
	pages = {44-49},<br />
	publisher = {Bibliotheca Alexandrina},<br />
	organization = {Bibliotheca Alexandrina},<br />
	address = {Alexandria, Egypt},<br />
	attachments = {http://www.clips.ua.ac.be/sites/default/files/coco.pdf},<br />
	author = {Hoogeveen, Doris and De Pauw, Guy}<br />
}

The script can be used to perform language identification using a maxent classifier and a set of language models.

USAGE: language_identification.py \<inputfile\> \<maxent_dir\>

\<inputfile\> is the file you would like to know the language off. This should be a plain text file encoded in UTF-8.<br />
\<maxent_dir\> is the path to the directory that contains maxent.exe

The script will output the iso name of the guessed language.

Example: language_identification.py inputfile /home/hoogeveen/maxent/

Prerequisite: Wine needs to be installed to be able to run the classifier.

The test text in 'inputfile' is a Dutch story by Toon Tellegen, taken from http://www.dbnl.org/tekst/tell003lang01_01/tell003lang01_01_0001.php <br />
I do not own the rights to this text in any way.
