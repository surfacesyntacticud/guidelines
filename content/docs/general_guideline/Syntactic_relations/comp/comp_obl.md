---
title: "comp:obl"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# comp:obl

## Universal 

The `comp:obl` relation is used for oblique arguments of verbs, adjectives, adverbs, nouns or pronouns, regardless of their form. Unlike UD, SUD does not make a distinction between indirect objects and oblique arguments. SUD instead makes the distinction between arguments and modifiers.

The relation `comp:obl` can have these deep features:
- [`@agent`](../../Deep/agent.md)
- [`@lvc`](../../Deep/lvc.md)

```grew
pattern { GOV-[comp:obl]->DEP }
```

> **English UD**
{{< conll >}}
1	it	it	PRON	_	_	2	nsubj	_	_
2	belongs	belong	VERB	_	_	0	root	_	_
3	to	to	ADP	_	_	5	case	_	_
4	a	a	DET	_	_	5	det	_	_
5	past	past	NOUN	_	_	2	obl	_	_
{{< /conll >}}

> **English SUD**
{{< conll >}}
1	it	it	PROPN	_	_	2	subj	_	_
2	belongs	belong	VERB	_	_	0	root	_	_
3	to	to	ADP	_	_	2	comp:obl	_	_
4	a	a	DET	_	_	5	det	_	_
5	past	past	NOUN	_	_	3	comp:obj	_	_
{{< /conll >}}


### Oblique complement of a verb

> **English**
{{< conll >}}
1	coming	come	VERB	_	_	0	root	_	_
2	into	into	ADP	_	_	1	comp:obl	_	_
3	the	the	DET	_	_	4	det	_	_
4	area	area	NOUN	_	_	2	comp:obj	_	_
5	to	to	PART	_	_	1	comp:obl	_	_
6	see	see	VERB	_	_	5	comp:obj	_	_
7	concerts	concert	NOUN	_	_	6	comp:obj	_	_
{{< /conll >}}

> **English**
{{< conll >}}
1	He	he	PRON	PRP	Case=Nom|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj	_	Entity=(person-8)
2	gives	give	VERB	VBZ	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	you	you	PRON	PRP	Case=Acc|Person=2|PronType=Prs	2	comp:obl	_	Entity=(person-2)
4	a	a	DET	DT	Definite=Ind|PronType=Art	6	det	_	Entity=(abstract-96
5	hooded	hooded	ADJ	JJ	Degree=Pos	6	mod	_	_
6	look	look	NOUN	NN	Number=Sing	2	comp:obj	_	Entity=abstract-96)|SpaceAfter=No
7	.	.	PUNCT	.	_	2	punct	_	_
{{< /conll >}}


The `comp:obl` relation is also used for clausal complements commuting with an adpositional complement.

Consider the two following examples:


> **French**
{{< conll >}}
# text_en = He's afraid of the spider
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj	_	Gloss=he
2	a	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=have
3	peur	peur	NOUN	_	Gender=Fem|Number=Sing	2	comp:obj@lvc	_	Gloss=fear
4	de	de	ADP	_	_	3	comp:obl	_	Gloss=of
5	l'	le	DET	_	Definite=Def|Number=Sing|Person=3|PronType=Art	6	det	_	Gloss=the
6	araignée	araignée	PROPN	_	_	4	comp:obj	_	Gloss=spider
{{< /conll >}}

> **French**
{{< conll >}}
# text = j'ai peur que ça marche
# text_en = I'm afraid that it works
1	j'	je	PRON	_	_	2	subj	_	Gloss=I
2	ai	avoir	VERB	_	_	0	root	_	Gloss=have
3	peur	peur	NOUN	_	_	2	comp:obj@lvc	_	Gloss=fear
4	que	que	SCONJ	_	_	3	comp:obl	_	Gloss=that
5	ça	ça	PRON	_	_	6	subj	_	Gloss=this
6	marche	marcher	VERB	_	_	4	comp:obj	_	Gloss=works
{{< /conll >}}

In the last sentence, *que ça marche* commutes with *de l'araignée*, therefore the relation going from *peur* to the head of the complement is labelled `comp:obl`.

### Oblique complement of a noun

Like the example above shows (*Il a peur de l'araignée*) `comp:obl` can also be used for the complement of a noun. This happens when the noun is part of a light verb construction. For more information about these constructions, please visit our [dedicated page](../../Deep/lvc.md).

> **French**
{{< conll >}}
# text = la Chine fait face à de sérieux problèmes
# text_en = China is facing serious problems
1	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|Person=3|PronType=Art	2	det	_	Gloss=the
2	Chine	Chine	PROPN	_	_	3	subj	_	Gloss=China
3	fait	faire	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=does
4	face	face	NOUN	_	Gender=Fem|Number=Sing	3	comp:obj@lvc	_	Gloss=face
5	à	à	ADP	_	_	4	comp:obl	_	Gloss=to
6	de	un	DET	_	Definite=Ind|Number=Plur|Person=3|PronType=Art	8	det	_	Gloss=of
7	sérieux	sérieux	ADJ	_	Gender=Masc|Number=Plur	8	mod	_	Gloss=serious
8	problèmes	problème	NOUN	_	Gender=Masc|Number=Plur	5	comp:obj	_	Gloss=problems
{{< /conll >}}

### Oblique complement of an adverb or an adjective

> **French**
{{< conll >}}
# sent_id = fr-ud-train_02712
# text = Nous n'hésiterons pas à la recommander auprès de notre entourage.
1	Nous	nous	PRON	_	Emph=No|Number=Plur|Person=1|PronType=Prs	3	subj	_	wordform=nous
2	n'	ne	ADV	_	Polarity=Neg	3	mod	_	SpaceAfter=No
3	hésiterons	hésiter	VERB	_	Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin	0	root	_	_
4	pas	pas	ADV	_	Polarity=Neg	3	mod	_	_
5	à	à	ADP	_	_	3	comp:obl	_	_
6	la	lui	PRON	_	Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs	7	comp:obj	_	_
7	recommander	recommander	VERB	_	VerbForm=Inf	5	comp:obj	_	Subject=SubjRaising
8	auprès	auprès	ADV	_	_	7	mod	_	_
9	de	de	ADP	_	_	8	comp:obl	_	_
10	notre	son	DET	_	Number=Sing|Number[psor]=Plur|Person[psor]=1|Poss=Yes|PronType=Prs	11	det	_	_
11	entourage	entourage	NOUN	_	Gender=Masc|Number=Sing	9	comp:obj	_	SpaceAfter=No
12	.	.	PUNCT	_	_	3	punct	_	_
{{< /conll >}}

> **English**
{{< conll >}}
# text = I'm sure you do
1	I	I	PRON	PRP	Case=Nom|Number=Sing|Person=1|PronType=Prs	2	subj	_	_
2	'm	be	AUX	VBP	Mood=Ind|Tense=Pres|VerbForm=Fin	0	root	_	_
3	sure	sure	ADJ	JJ	Degree=Pos	2	comp:pred	_	_
4	you	you	PRON	PRP	Case=Nom|Person=2|PronType=Prs	5	subj	_	_
5	do	do	VERB	VBP	Mood=Ind|Tense=Pres|VerbForm=Fin	3	comp:obl	_	_
{{< /conll >}}






## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


