# BIO-to-BIOLU

The CoNLL 2003 Shared Task data is annotated using the BIO labeling scheme. This scheme marks the categories of named entities and their span: _B_ for the first NE token, _I_ for tokens inside NE's, and _O_ for tokens outside any entity. 

A labelling scheme shown to outperform BIO is the BIOLU scheme, where two additional markers are included, _L_ for the last tokens of NE's, and _U_ for unit length entities.

This script converts a BIO-encoded file to BIOLU.
