---
title: "flat"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# `flat`

## Universal


The `flat` relation plays a similar role to the [`compound`](../compound/compound.md) one, and its exact usage also varies on a language-by-language basis. However, it is most frequently used to connect the various elements of proper names to one another, including titles and honorifics.

Some examples in **SUD_English-EWT**:
{{<grew corpus="SUD_English-EWT@2.13" >}}
pattern { X -[flat]-> Y }
{{</grew>}}


> English
{{<conll>}}
# sent_id = GUM_bio_emperor-18
# text = Emperor Joshua Norton, in full military regalia, circa 1880 or earlier
1	Emperor	Emperor	PROPN	NNP	Number=Sing	0	root	_	highlight=red
2	Joshua	Joshua	PROPN	NNP	Number=Sing	1	flat	_	highlight=red
3	Norton	Norton	PROPN	NNP	Number=Sing	2	flat	_	highlight=red
4	,	,	PUNCT	,	_	5	punct	_	_
5	in	in	ADP	IN	_	1	udep	_	_
6	full	full	ADJ	JJ	Degree=Pos	8	mod	_	_
7	military	military	ADJ	JJ	Degree=Pos	8	mod	_	_
8	regalia	regalia	NOUN	NNS	Number=Plur	5	comp:obj	_	_
9	,	,	PUNCT	,	Shared=Yes	11	punct	_	_
10	circa	circa	ADV	FW	_	11	mod	_	_
11	1880	1880	NUM	CD	NumForm=Digit|NumType=Card	1	mod@tmod	_	_
12	or	or	CCONJ	CC	_	13	cc	_	_
13	earlier	early	ADV	RBR	Degree=Cmp	11	conj	_	_
{{</conll>}}

> English
{{<conll>}}
# sent_id = GUM_interview_cyclone-24
# text = Once Cyclone Phailin comes on shore it will immediately begin to lose strength.
1	Once	once	SCONJ	IN	_	8	mod	_	_
2	Cyclone	Cyclone	PROPN	NNP	Number=Sing	4	subj	_	highlight=red
3	Phailin	Phailin	PROPN	NNP	Number=Sing	2	flat	_	highlight=red
4	comes	come	VERB	VBZ	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	1	comp:obj	_	_
5	on	on	ADP	IN	_	4	udep	_	_
6	shore	shore	NOUN	NN	Number=Sing	5	comp:obj	_	_
7	it	it	PRON	PRP	Case=Nom|Gender=Neut|Number=Sing|Person=3|PronType=Prs	8	subj	_	_
8	will	will	AUX	MD	VerbForm=Fin	0	root	_	_
9	immediately	immediately	ADV	RB	Degree=Pos	8	mod	_	_
10	begin	begin	VERB	VB	VerbForm=Inf	8	comp:aux	_	_
11	to	to	PART	TO	_	10	comp:obl	_	_
12	lose	lose	VERB	VB	VerbForm=Inf	11	comp:obj	_	_
13	strength	strength	NOUN	NN	Number=Sing	12	comp:obj	_	_
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
7	quarante	quarante	NUM	_	Number=Plur	9	det	_	highlight=red
8	quatre	quatre	NUM	_	Number=Plur	7	flat	_	highlight=red
9	pages	page	NOUN	_	Gender=Fem|Number=Plur	6	comp:obj	_	_
10	en	en	ADP	_	_	5	udep	_	_
11	grand	grand	ADJ	_	Gender=Masc|Number=Sing	12	mod	_	_
12	format	format	NOUN	_	Gender=Masc|Number=Sing	10	comp:obj	_	_
13	cartonné	cartonner	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	5	mod	_	SpaceAfter=No
14	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

The syntactic relation `flat` is mainly used with two deep syntactic features:
 - [`@name`](../../../../Deep/name) in proper names
 - [`@foreign`](../../../../Deep/foreign) in expressions in a different langauge

See [table](https://tables.grew.fr/?data=sud_deps/DEPS&cols=flat) for more `flat` based relations.


## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


