---
title: "INTJ"
weight: 1
bookToc: true
---

# Interjection

## Universal 

See [UD `INTJ` page](https://universaldependencies.org/u/pos/INTJ.html) for a definition.

> **French**
{{<conll>}} 
# text = ah, non, mais, pour les gens, euh, je …
1	ah	ah	INTJ	_	_	9	discourse	_	AlignBegin=85009|AlignEnd=85405|SpaceAfter=No|highlight=red
2	,	,	PUNCT	_	_	1	punct	_	AlignBegin=85405|AlignEnd=85405
3	non	non	ADV	_	_	0	root	_	AlignBegin=85405|AlignEnd=85801|SpaceAfter=No
4	,	,	PUNCT	_	_	3	punct	_	AlignBegin=85801|AlignEnd=85801
5	mais	mais	CCONJ	_	_	7	cc	_	AlignBegin=85801|AlignEnd=86197|SpaceAfter=No
6	,	,	PUNCT	_	_	7	punct	_	AlignBegin=86197|AlignEnd=86197
7	pour	pour	ADP	_	_	3	conj:dicto	_	AlignBegin=86197|AlignEnd=86593
8	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art|Shared=No	9	det	_	AlignBegin=86593|AlignEnd=86988
9	gens	gens	NOUN	_	Number=Plur	7	comp:obj	_	AlignBegin=86988|AlignEnd=87384|SpaceAfter=No
10	,	,	PUNCT	_	_	11	punct	_	AlignBegin=87384|AlignEnd=87384
11	euh	euh	INTJ	_	_	9	discourse	_	AlignBegin=87384|AlignEnd=87780|SpaceAfter=No|highlight=red
12	,	,	PUNCT	_	_	13	punct	_	AlignBegin=87780|AlignEnd=87780
13	je	moi	PRON	_	Number=Sing|Person=1|PronType=Prs	9	conj:dicto	_	AlignBegin=87780|AlignEnd=88176
14	…	…	PUNCT	_	_	3	punct	_	AlignBegin=88176|AlignEnd=88176
{{</conll>}} 

## French

### Overview

Pure interjections (such as *ah*, *hein*, *ouais*, *euh*…) are analysed as `INTJ`.
Discourse markers coming from other POS (such as *enfin*, *chouette*, *disons*…);
except 4 of them which are frequent and are analysed as pure `INTJ`: *bon*, *ben*, *quoi*, and *tiens*.

{{<conll>}} 
# text_en = So it was the price of, I mean, the price of a full course you know.
# text = Donc le prix d'un, enfin ouais c'était, le prix d'un repas en fait hein.
1	donc	donc	ADV	_	_	10	discourse	_	_
2	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	3	det	_	_
3	prix	prix	NOUN	_	Gender=Masc|Number=Sing	10	dislocated	_	_
4	d'	de	ADP	_	_	3	udep	_	SpaceAfter=No
5	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	4	comp:obj@scrap	_	SpaceAfter=No
6	,	,	PUNCT	_	_	7	punct	_	_
7	enfin	enfin	ADV	_	ExtPos=INTJ	3	discourse	_	highlight=red
8	ouais	ouais	INTJ	_	_	3	discourse	_	_
9	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	10	subj	_	SpaceAfter=No
10	était	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	SpaceAfter=No
11	,	,	PUNCT	_	_	13	punct	_	_
12	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	13	det	_	_
13	prix	prix	NOUN	_	Gender=Masc|Number=Sing	10	comp:pred	_	_
14	d'	de	ADP	_	_	13	udep	_	SpaceAfter=No
15	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	16	det	_	_
16	repas	repas	NOUN	_	Gender=Masc|Number=Sing	14	comp:obj	_	_
17	en	en	ADP	_	ExtPos=ADV	10	discourse	_	Idiom=Yes
18	fait	fait	NOUN	_	Gender=Masc|Number=Sing	17	comp:obj	_	InIdiom=Yes
19	hein	hein	INTJ	_	_	10	discourse	_	SpaceAfter=No
20	.	.	PUNCT	_	_	10	punct	_	_
{{</conll>}}

### Specific Pattern

#### other part of speech as interjection  

Some rare idioms (such as *ah bon*, *oh la la*…), keep their original POS but have an additional `ExtPos=INTJ`.

{{<grew>}}
pattern { N [ExtPos=INTJ, Idiom] }
{{</grew>}}

{{<conll>}}
# macrosyntax = $L3 "oh la" Maxi Rodriguez qui va tirer // -$
# sent_id = Rhap_D2003-56
# speaker = L3
# text = oh la, Maxi Rodriguez qui va tirer.
1	oh	oh	INTJ	_	ExtPos=INTJ	7	discourse	_	Idiom=Yes|highlight=red
2	la	la	INTJ	_	_	1	unk	_	InIdiom=Yes|SpaceAfter=No|highlight=red
3	,	,	PUNCT	_	_	2	punct	_	_
4	Maxi	Maxi	PROPN	_	_	0	root	_	_
5	Rodriguez	Rodriguez	PROPN	_	_	4	flat@name	_	_
6	qui	qui	PRON	_	PronType=Rel	7	subj	_	_
7	va	aller	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	4	mod@relcl	_	_
8	tirer	tirer	VERB	_	VerbForm=Inf	7	comp:obj	_	|SpaceAfter=No|Subject=SubjRaising
9	.	.	PUNCT	_	_	4	punct	_	_
{{</conll>}}

#### Tables

Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_INTJ >}}
