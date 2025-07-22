---
title: "@foreign"
weight: 3
bookFlatSection: true
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# `@foreign`

## Universal 

The `@foreign` feature is used with the `flat` relation for annotation of foreign language phrases.
Note that foreign tokens are tagged `upos=X` and `Foreign=Yes`. An `ExtPos` feature can indicate the role of the ofreign phrase.

> English
{{<conll>}}
# sent_id = en_partut-ud-1757
# text = The influence of Paris permeates La Comédie.
1	The	the	DET	RD	Definite=Def|PronType=Art	2	det	_	_
2	influence	influence	NOUN	S	Number=Sing	5	subj	_	_
3	of	of	ADP	E	_	2	udep	_	_
4	Paris	Paris	PROPN	SP	_	3	comp:obj	_	_
5	permeates	permeate	VERB	V	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
6	La	La	X	SW	ExtPos=PROPN|Foreign=Yes	5	comp:obj	_	_
7	Comédie	Comédie	X	SW	Foreign=Yes	6	flat@foreign	_	SpaceAfter=No
8	.	.	PUNCT	FS	_	5	punct	_	_
{{</conll>}}




