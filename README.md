# BIO-to-BIOLU

The [CoNLL 2003 NER dataset](http://www.aclweb.org/anthology/W03-0419) is annotated using the BIO labeling scheme. Each word is labelled in accordance with its location relative to a named entity (NE), using the three following markers:

* **B-**   for the first token of a NE, 
* **I-**   for tokens inside NE's, 
* **O-**   for tokens outside any NE. 

A labelling scheme shown to outperform BIO is the BIOLU scheme [[Ratinov and Roth, 2009](http://www.aclweb.org/anthology/W09-1119)], where two additional markers are included:
* **L-**   for the last tokens of NE's, 
* **U-**   for unit length NE's.

This Python script converts a BIO-encoded file to BIOLU.

## Usage
Run the following in the command line, where you specify the path of the original BIO encoded file and the name of your converted file.

```shell
python biolu_encode.py bio_path biolu_path
```

Tested for Python 3.6.

## Examples
_eng-biolu.toy_ is the result when converting _eng.toy_
