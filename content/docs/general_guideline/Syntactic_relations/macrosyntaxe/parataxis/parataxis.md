---
title: "parataxis"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---
# `parataxis`

## Universal


The `parataxis` relation is used to analyse two elements that are placed side by side with no explicit marker of coordination, subordination, or argument relation with the head word. 

{{<grew >}}
pattern { X -[parataxis]-> Y }
{{</grew>}}

### Incisive proposal 

> __French__
{{<conll>}}
# text = Il faudra encore du temps », avait-il déclaré.
1	Il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj@expl	_	_
2	faudra	falloir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin	0	root	_	highlight=red
3	encore	encore	ADV	_	_	2	mod	_	_
4	du	du	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	5	det	_	_
5	temps	temps	NOUN	_	Gender=Masc|Number=Sing	2	comp:obj	_	_
6	»	»	PUNCT	_	_	8	punct	_	SpaceAfter=No
7	,	,	PUNCT	_	_	8	punct	_	_
8	avait	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	2	parataxis	_	SpaceAfter=No|highlight=red
9	-il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	8	subj	_	_
10	déclaré	déclarer	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	8	comp:aux@tense	_	SpaceAfter=No
11	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

> __English__
{{<conll>}}
# text = Kim couldn't spend the night, I told you.
1	Kim	Kim	PROPN	NNP	Number=Sing	2	subj	_	_
2-3	couldn't	_	_	_	_	_	_	_	_
2	could	could	AUX	MD	Number=Sing|Person=3|VerbForm=Fin	0	root	_	highlight=red
3	n't	not	PART	RB	Polarity=Neg	2	mod	_	_
4	spend	spend	VERB	VB	VerbForm=Inf	2	comp:aux	_	_
5	the	the	DET	DT	Definite=Def|PronType=Art	6	det	_	_
6	night	night	NOUN	NN	Number=Sing	4	comp:obj	_	_
7	,	,	PUNCT	,	_	9	punct	_	_
8	I	I	PRON	PRP	Case=Nom|Number=Sing|Person=1|PronType=Prs	9	subj	_	_
9	told	tell	VERB	VBD	Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin	2	parataxis	_	highlight=red
10	you	you	PRON	PRP	Case=Acc|Number=Sing|Person=2|PronType=Prs	9	comp:obl	_	_
11	.	.	PUNCT	.	_	2	punct	_	_
{{</conll>}}


> __French__
{{<conll>}}
# text = Très demandé, vous le connaissez sûrement, Jean M est toujours dévoué, un vrai professionnel qui ne compte pas ses heures pour nous soigner.
1	Très	très	ADV	_	_	2	mod	_	_
2	demandé	demander	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	11	mod	_	SpaceAfter=No|Subject=Instantiated
3	,	,	PUNCT	_	_	2	punct	_	_
4	vous	il	PRON	_	Number=Plur|Person=2|PronType=Prs	6	subj	_	_
5	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	6	comp:obj	_	_
6	connaissez	connaître	VERB	_	Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	11	parataxis	_	highlight=red
7	sûrement	sûrement	ADV	_	_	6	mod	_	SpaceAfter=No
8	,	,	PUNCT	_	_	6	punct	_	_
9	Jean	Jean	PROPN	_	Gender=Masc|Number=Sing	11	subj	_	_
10	M	M	SYM	_	ExtPos=PROPN	9	mod	_	_
11	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	|highlight=red
12	toujours	toujours	ADV	_	_	11	mod	_	_
13	dévoué	dévoué	ADJ	_	Gender=Masc|Number=Sing	11	comp:pred	_	SpaceAfter=No
14	,	,	PUNCT	_	_	17	punct	_	_
15	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	17	det	_	_
16	vrai	vrai	ADJ	_	Gender=Masc|Number=Sing	17	mod	_	_
17	professionnel	professionnel	NOUN	_	Gender=Masc|Number=Sing	9	conj:appos	_	_
18	qui	qui	PRON	_	PronType=Rel	20	subj	_	_
19	ne	ne	ADV	_	Polarity=Neg	20	mod	_	_
20	compte	compter	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	17	mod@relcl	_	_
21	pas	pas	ADV	_	Polarity=Neg	20	mod	_	_
22	ses	son	DET	_	Number=Plur|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs	23	det	_	_
23	heures	heure	NOUN	_	Gender=Fem|Number=Plur	20	comp:obj	_	_
24	pour	pour	ADP	_	_	20	mod	_	_
25	nous	le	PRON	_	Number=Plur|Person=1|PronType=Prs	26	comp:obj	_	_
26	soigner	soigner	VERB	_	VerbForm=Inf	24	comp:obj	_	SpaceAfter=No|Subject=SubjRaising
27	.	.	PUNCT	_	_	11	punct	_	_
{{</conll>}}




