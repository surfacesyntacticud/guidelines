---
title: "mod"
weight: 2
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# `mod` 

## Universal

The `mod` relation is used for modifiers of verbs, nouns, adjectives, adverbs, auxiliaries, adpositions and conjunctions.

> **English**
{{< conll >}}
# text = Great service
1	Great	great	ADJ	JJ	Degree=Pos	2	mod	_	_
2	service	service	NOUN	NN	Number=Sing	0	root	_	_
{{< /conll >}}

> **English**
{{< conll >}}
1	a	a	DET	_	_	2	det	_	_
2	country	country	NOUN	_	_	0	root	_	_
3	with	with	ADP	_	_	2	mod	_	_
4	so	so	ADV	_	_	5	mod	_	_
5	many	many	ADJ	_	_	8	mod	_	_
6	different	different	ADJ	_	_	8	mod	_	_
7	language	language	NOUN	_	_	8	compound	_	_
8	groups	group	NOUN	_	_	3	comp:obj	_	_
{{< /conll >}}

> **French**
{{< conll >}}
# sent_id = fr-ud-train_00006
# text = je reviendrais avec plaisir !
# text_en = I'll be back with pleasure!
1	je	moi	PRON	_	_	2	subj	_	Gloss=I
2	reviendrais	revenir	VERB	_	_	0	root	_	highlight=red|Gloss=be_back
3	avec	avec	ADP	_	_	2	mod	_	highlight=red|Gloss=with
4	plaisir	plaisir	NOUN	_	_	3	comp:obj	_	Gloss=pleasure
5	!	!	PUNCT	_	_	2	punct	_	_
{{< /conll >}}


### Deep syntactic features
The relation `mod` can have the deep feature `mod@relcl` for relative clauses (see [@relcl](../Deep/relcl.md)).

> __English__
{{< conll >}}
# sent_id = newsgroup-groups.google.com_Meditation20052_06390a5f75b2e1f2_ENG_20050316_091700-0045
# newpar id = newsgroup-groups.google.com_Meditation20052_06390a5f75b2e1f2_ENG_20050316_091700-p0008
# text = Another thing you can try.
1	Another	another	DET	DT	PronType=Ind	2	det	_	_
2	thing	thing	NOUN	NN	Number=Sing	0	root	_	highlight=red
3	you	you	PRON	PRP	Case=Nom|Person=2|PronType=Prs	4	subj	_	_
4	can	can	AUX	MD	VerbForm=Fin	2	mod@relcl	_	highlight=red
5	try	try	VERB	VB	VerbForm=Inf	4	comp:aux	_	SpaceAfter=No
6	.	.	PUNCT	.	_	2	punct	_	_
{{< /conll >}}

Some other deep syntactic relations can be found, for instance in __SUD_French-Rhapsodie__:
{{<grew key1="e.label" corpus="SUD_French-Rhapsodie@latest" >}}
pattern { e: X -[1=mod, deep=*]-> Y; }
{{</grew>}}





