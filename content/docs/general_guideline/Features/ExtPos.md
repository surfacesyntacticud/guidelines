---
title: "ExtPos"
weight: 10
---

# `ExtPos`

## Universal

Even if the feature `ExtPos` is also now used by [some UD treebanks](https://tables.grew.fr/?data=ud_feats/FEATS&cols=ExtPos), we consider it here as a *SUD feature*.




The `ExtPos` feature was introduced to facilitate the annotation of idioms, titles, and other multi-word units which behave like a certain part of speech, even though none of their constituents necessarily carry that part of speech. This feature allows the annotator to preserve the internal syntactic relationships between the components of these units.

See [Idioms and titles](../Misc/Idioms_Titles.md) for examples.

The usage of `ExtPos` was also generalized to cases of single tokens which are given a `upos` but they are used in the syntactic structure with another role.

## Naija

{{<grew key1="X.upos" key2="X.ExtPos" corpus="SUD_Naija-NSC@latest" >}}
pattern { X [ExtPos] }
{{</grew>}}

In Naija, it is mostly used for adjective used as verbs.

> Naija
{{< conll >}}
# text_en = It'll get better.
1	e	im	PRON	_	Case=Nom|Number=Sing|Person=3|PronType=Prs	2	subj	_	AlignBegin=307749|AlignEnd=308144|Gloss=NOM.SG.3
2	go	go	AUX	_	Aspect=Prosp	0	root	_	AlignBegin=308144|AlignEnd=308540|Gloss=PROSP
3	better	beta	ADJ	_	Degree=Cmp|ExtPos=VERB	2	comp:aux	_	AlignBegin=308540|AlignEnd=308935|Gloss=good.CMPR|highlight=red
4	//	//	PUNCT	_	_	2	punct	_	AlignBegin=308935|AlignEnd=308935|Gloss=PUNCT
{{< /conll >}}


## French 

### Overview

{{<grew key1="X.upos" key2="X.ExtPos" corpus="SUD_French-GSD@latest" >}}
pattern { X [ExtPos] }
{{</grew>}}
 
### Specific Pattern

#### Adverb used as pronoun 

- *beaucoup* de + NOUN
- *près* de + NOUN
- *peu* de + NOUN

> *peu* is an ADV used as a PRON:
{{<conll>}}
# text = Elle y incarnera la Poussette de Manon peu de temps après.
1	Elle	lui	PRON	_	Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs	3	subj	_	_
2	y	y	PRON	_	Emph=No|Person=3|PronType=Prs	3	mod	_	_
3	incarnera	incarner	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin	0	root	_	_
4	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	5	det	_	_
5	Poussette	poussette	NOUN	_	Gender=Fem|Number=Sing	3	comp:obj	_	_
6	de	de	ADP	_	_	5	udep	_	_
7	Manon	Manon	PROPN	_	_	6	comp:obj	_	_
8	peu	peu	ADV	_	ExtPos=PRON	11	mod	_	highlight=red
9	de	de	ADP	_	_	8	comp:obl	_	_
10	temps	temps	NOUN	_	Gender=Masc|Number=Sing	9	comp:obj	_	_
11	après	après	ADV	_	_	3	mod	_	SpaceAfter=No
12	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

#### Noun used as adverbs 

- _**grâce** à_
- _**face** à_
- _**suite** à_

> *grâce* is an NOUN used as an ADV:
{{<conll>}}
# text = Elle s'impose grâce à un bond à 7,23 m établi à son sixième et dernier essai.
1	Elle	lui	PRON	_	Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs	3	subj@pass	_	_
2	s'	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	3	comp@pass	_	SpaceAfter=No
3	impose	imposer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	grâce	grâce	NOUN	_	ExtPos=ADV	3	mod	_	highlight=red
5	à	à	ADP	_	_	4	comp:obl	_	_
6	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	7	det	_	_
7	bond	bond	NOUN	_	Gender=Masc|Number=Sing	5	comp:obj	_	_
8	à	à	ADP	_	_	7	udep	_	_
9	7,23	7,23	NUM	_	Number=Plur	10	det	_	_
10	m	mètre	NOUN	_	Gender=Masc|Number=Plur	8	comp:obj	_	_
11	établi	établir	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	7	mod	_	_
12	à	à	ADP	_	_	11	mod	_	_
13	son	son	DET	_	Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs	17	det	_	_
14	sixième	sixième	ADJ	_	Gender=Masc|Number=Sing	17	mod	_	_
15	et	et	CCONJ	_	_	16	cc	_	_
16	dernier	dernier	ADJ	_	Gender=Masc|Number=Sing	14	conj:coord	_	_
17	essai	essai	NOUN	_	Gender=Masc|Number=Sing	12	comp:obj	_	SpaceAfter=No
18	.	.	PUNCT	_	_	3	punct	_	_

{{</conll>}}

#### Symbols 

> Most of the tokens with `upos=SYM` have an `ExtPos` feature
{{<conll>}}
# sent_id = fr-ud-train_02956
# text = Le Nasdaq a quant à lui cédé 8,1%
1	Le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	_
2	Nasdaq	Nasdaq	PROPN	_	Gender=Masc|Number=Sing	3	subj	_	_
3	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	quant	quant	ADV	_	ExtPos=ADP	3	mod	_	Idiom=Yes
5	à	à	ADP	_	_	4	unk	_	InIdiom=Yes
6	lui	lui	PRON	_	Emph=Yes|Gender=Masc|Number=Sing|Person=3|PronType=Prs	4	comp:obj	_	_
7	cédé	céder	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act	3	comp:aux@tense	_	_
8	8,1	8,1	NUM	_	Number=Plur	9	det	_	SpaceAfter=No
9	%	%	SYM	_	ExtPos=NOUN|Number=Plur	7	comp:obj	_	SpaceAfter=No|highlight=red
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_ExtPos >}}






## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


