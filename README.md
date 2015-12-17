# MaxentLanguageIdentification
The language identification module as used in the following paper: http://www.clips.ua.ac.be/sites/default/files/coco.pdf

If you use this model, please cite the paper as follows:

@inproceedings {hoogeveen2011,
	title = {CorpusCollie - A Web Corpus Mining Tool for Resource-Scarce Languages},
	booktitle = {Proceedings of Conference on Human Language Technology for Development},
	year = {2011},
	pages = {44-49},
	publisher = {Bibliotheca Alexandrina},
	organization = {Bibliotheca Alexandrina},
	address = {Alexandria, Egypt},
	attachments = {http://www.clips.ua.ac.be/sites/default/files/coco.pdf},
	author = {Hoogeveen, Doris and De Pauw, Guy}
}

The script can be used to perform language identification using a maxent classifier and a set of language models.

USAGE: language_identification.py <inputfile> <maxent_dir>

<inputfile> is the file you would like to know the language off. This should be a plain text file encoded in UTF-8.
<maxent_dir> is the path to the directory that contains maxent.exe

The script will output the iso name of the guesed language.

Example: language_identification.py inputfile /home/hoogeveen/maxent/

Prerequisite: Wine needs to be installed to be able to run the classifier.
