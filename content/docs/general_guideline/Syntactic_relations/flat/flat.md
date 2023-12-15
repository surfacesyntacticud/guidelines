---
title: "flat"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# Flat

## Universal 


The `flat` relation plays a similar role to the [`compound`](../compound/compound.md) one, and its exact usage also varies on a language-by-language basis. However, it is most frequently used to connect the various elements of proper names to one another, including titles and honorifics.

> pattern { GOV-[flat]->DEP }
  
> English
{{<conll>}}
# sent_id = GUM_bio_emperor-18
# text = Emperor Joshua Norton, in full military regalia, circa 1880 or earlier
1	Emperor	Emperor	PROPN	NNP	Number=Sing	0	root	_	Discourse=context-background:49->52:8|Entity=(1-person-giv:act-cf1*-1,2,3-coref-Emperor_Norton
2	Joshua	Joshua	PROPN	NNP	Number=Sing	1	flat	_	_
3	Norton	Norton	PROPN	NNP	Number=Sing	2	flat	_	SpaceAfter=No
4	,	,	PUNCT	,	_	5	punct	_	_
5	in	in	ADP	IN	_	1	udep	_	_
6	full	full	ADJ	JJ	Degree=Pos	8	mod	_	Entity=(75-abstract-new-cf3-3-sgl
7	military	military	ADJ	JJ	Degree=Pos	8	mod	_	_
8	regalia	regalia	NOUN	NNS	Number=Plur	5	comp:obj	_	Entity=75)|SpaceAfter=No
9	,	,	PUNCT	,	Shared=Yes	11	punct	_	_
10	circa	circa	ADV	FW	_	11	mod	_	_
11	1880	1880	NUM	CD	NumForm=Digit|NumType=Card	1	mod@tmod	_	Entity=(4-time-giv:inact-cf2-1-coref)|XML=<date when:::"1880"></date>
12	or	or	CCONJ	CC	_	13	cc	_	_
13	earlier	early	ADV	RBR	Degree=Cmp	11	conj	_	Entity=1)
{{</conll>}}

> English
{{<conll>}}
# sent_id = GUM_interview_cyclone-24
# text = Once Cyclone Phailin comes on shore it will immediately begin to lose strength.
1	Once	once	SCONJ	IN	_	8	mod	_	Discourse=context-circumstance:50->51:0
2	Cyclone	Cyclone	PROPN	NNP	Number=Sing	4	subj	_	Entity=(3-event-giv:act-cf1*-1,2-coref-Cyclone_Phailin
3	Phailin	Phailin	PROPN	NNP	Number=Sing	2	flat	_	Entity=3)
4	comes	come	VERB	VBZ	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	1	comp:obj	_	_
5	on	on	ADP	IN	_	4	udep	_	_
6	shore	shore	NOUN	NN	Number=Sing	5	comp:obj	_	Entity=(46-place-new-cf3-1-sgl)
7	it	it	PRON	PRP	Case=Nom|Gender=Neut|Number=Sing|Person=3|PronType=Prs	8	subj	_	Discourse=joint-other_m:51->9:1|Entity=(3-event-giv:act-cf1*-1-ana-Cyclone_Phailin)
8	will	will	AUX	MD	VerbForm=Fin	0	root	_	_
9	immediately	immediately	ADV	RB	Degree=Pos	8	mod	_	_
10	begin	begin	VERB	VB	VerbForm=Inf	8	comp:aux	_	_
11	to	to	PART	TO	_	10	comp:obl	_	_
12	lose	lose	VERB	VB	VerbForm=Inf	11	comp:obj	_	Subject=SubjRaising
13	strength	strength	NOUN	NN	Number=Sing	12	comp:obj	_	Entity=(9-abstract-giv:inact-cf2-1-coref)|SpaceAfter=No
14	.	.	PUNCT	.	_	8	punct	_	_
{{</conll>}}
  

The `flat` relation can also be used to link individual elements of numbers to one another.

  
> French
{{<conll>}}
# sent_id = fr-ud-train_04922
# text = Il s'agit d'album de quarante quatre pages en grand format cartonné.
# text_en = This is a large format hardback album of forty-four pages.
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@expl	_	wordform=il
2	s'	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	3	comp@expl	_	SpaceAfter=No
3	agit	agir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	d'	de	ADP	_	_	3	comp:obl	_	SpaceAfter=No
5	album	album	NOUN	_	Gender=Masc|Number=Sing	4	comp:obj	_	_
6	de	de	ADP	_	_	5	udep	_	_
7	quarante	quarante	NUM	_	Number=Plur	9	det	_	_
8	quatre	quatre	NUM	_	Number=Plur	7	flat	_	_
9	pages	page	NOUN	_	Gender=Fem|Number=Plur	6	comp:obj	_	_
10	en	en	ADP	_	_	5	udep	_	_
11	grand	grand	ADJ	_	Gender=Masc|Number=Sing	12	mod	_	_
12	format	format	NOUN	_	Gender=Masc|Number=Sing	10	comp:obj	_	_
13	cartonné	cartonner	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	5	mod	_	SpaceAfter=No
14	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

The syntactic relation ̀`flat` can have the deep `[name](../../Deep/name.md)` to annotated the composed proper name. 




## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


