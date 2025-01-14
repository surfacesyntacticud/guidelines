---
title: "Numeral"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Numeral

## Written in Letter

Numbers composed of more than one word, such as *five hundred* or *six thousand* are primarily chained together with the [`flat`](../Syntactic_relations/shared_ud/flat/flat.md) relation.
If the number contains the coordinating conjunction *and*, such as in *one hundred and one*, the integer directly preceding the coordinating conjunction is connected to one directly following it with a [`conj:coord`](../Syntactic_relations/conj/conj_coord.md) relation.

{{< grew >}}
pattern { X1 [upos=NUM]; X2 [upos=NUM]; X1 -[flat]-> X2 }
{{< /grew >}}

> Naija
{{<conll>}}
1	#	#	PUNCT	_	_	3	punct	_	AlignBegin=136812|AlignEnd=137203|Gloss=PUNCT
2	den	den	ADV	_	_	3	mod:periph	_	Gloss=den
3	housing	housing	NOUN	_	_	0	root	_	Gloss=housing
4	and	and	CCONJ	_	_	5	cc	_	Gloss=and
5	clothing	clothing	NOUN	_	_	3	conj:coord	_	Gloss=clothing
6	of	of	ADP	_	_	5	mod	_	Gloss=of
7	sixty	sixty	NUM	_	NumType=Card	6	comp:obj	_	Gloss=sixty.CARD|highlight=red
8	five	five	NUM	_	NumType=Card	7	flat	_	Gloss=five.CARD|highlight=red
9	million	million	NUM	_	NumType=Card	8	flat	_	Gloss=million.CARD|highlight=red
10	//	//	PUNCT	_	_	3	punct	_	Gloss=PUNCT

{{</conll>}}


> English
{{<conll>}}
1	you	you	PRON	_	Case=Nom|Person=2|PronType=Prs	2	subj	_	Gloss=NOM.2
2	invest	invest	VERB	_	_	0	root	_	Gloss=invest
3	#	#	PUNCT	_	_	4	punct	_	Gloss=PUNCT
4	one	one	NUM	_	NumType=Card	2	comp:obj	_	Gloss=one|highlight=red
5	hundred	hundred	NUM	_	NumType=Card	4	flat	_	Gloss=hundred.CARD|highlight=red
6	and	and	CCONJ	_	_	7	cc	_	Gloss=and
7	thirty	thirty	NUM	_	NumType=Card	5	conj:coord	_	Gloss=thirty.CARD
8	seven	seven	NUM	_	NumType=Card	7	flat	_	Gloss=seven.CARD
9	thousand	thousand	NUM	_	NumType=Card	8	flat	_	Gloss=thousand.CARD
{{</conll>}}

> French
{{<conll>}}
# text = c'était en deux mille douze.
1	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	2	subj	_	SpaceAfter=No
2	était	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	_
3	en	en	ADP	_	_	2	mod	_	_
4	deux	deux	NUM	_	Number=Plur	3	comp:obj	_	highlight=red
5	mille	mille	NUM	_	_	4	flat	_	highlight=red
6	douze	douze	NUM	_	Number=Plur	5	flat	_	SpaceAfter=No|highlight=red
7	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

