---
title: "Reported speech"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# Reported Speech in Spoken Corpora

## Universal 

Reported speech has a feature `Reported=Yes` on its head.
It is generally the `comp:obj` of a speech verb, such as _dire_ 'to say'. 

{{<grew corpus="SUD_French-Rhapsodie@latest">}}
pattern { X -[comp:obj]-> Y; Y[Reported=Yes] }
{{</grew>}}

> French
{{<conll>}}
# text = je fais oui, oui, j'ai l'impression de t'avoir déjà vue !
1	je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	AlignBegin=11315|AlignEnd=11458
2	fais	faire	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=11458|AlignEnd=11601
3	oui	oui	ADV	_	ExtPos=INTJ	8	discourse	_	AlignBegin=11601|AlignEnd=11743|SpaceAfter=No
4	,	,	PUNCT	_	_	5	punct	_	AlignBegin=11743|AlignEnd=11743
5	oui	oui	ADV	_	ExtPos=INTJ	3	conj:coord	_	AlignBegin=11743|AlignEnd=11886|SpaceAfter=No
6	,	,	PUNCT	_	_	5	punct	_	AlignBegin=11886|AlignEnd=11886
7	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	8	subj	_	AlignBegin=11886|AlignEnd=12024|SpaceAfter=No
8	ai	avoir	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	2	comp:obj	_	AlignBegin=12024|AlignEnd=12162|Reported=Yes|highlight=red
9	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	10	det	_	AlignBegin=12162|AlignEnd=12300|SpaceAfter=No
10	impression	impression	NOUN	_	Gender=Fem|Number=Sing	8	comp:obj@lvc	_	AlignBegin=12300|AlignEnd=12438
11	de	de	ADP	_	_	10	udep	_	AlignBegin=12438|AlignEnd=12577
12	t'	le	PRON	_	Number=Sing|Person=2|PronType=Prs	15	comp:obj	_	AlignBegin=12577|AlignEnd=12715|SpaceAfter=No
13	avoir	avoir	AUX	_	VerbForm=Inf	11	comp:obj	_	AlignBegin=12715|AlignEnd=12853|Subject=SubjRaising
14	déjà	déjà	ADV	_	_	13	mod	_	AlignBegin=12853|AlignEnd=12991
15	vue	voir	VERB	_	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part	13	comp:aux@tense	_	AlignBegin=12991|AlignEnd=13129
16	!	!	PUNCT	_	_	2	punct	_	AlignBegin=13129|AlignEnd=13129
{{</conll>}}

{{< hint warning>}}
Reported speech was previously annotated using the syntactic relation `parataxis:obj`, but this is now considered obsolete.
{{</hint>}}
