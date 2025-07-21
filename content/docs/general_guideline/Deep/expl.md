---
title: "@expl"
weight: 3
bookFlatSection: true
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# `@expl`: expletive

## Universal 

The `@expl` feature is used for arguments of predicates without semantic content (impersonal subjects for instance). In UD, such elements ara analyzed with `expl`, without indicating their surface syntactic function. The feature `@expl`allows us to compibe the surface syntactic relation with these more semantic information.

> Impersonal subject (English)
{{< conll >}}
1	it	it	PRON	_	_	2	subj@expl	_	_
2	is	be	AUX	_	_	0	root	_	_
3	also	also	ADV	_	_	4	mod	_	_
4	desirable	desirable	ADJ	_	_	2	comp:pred	_	_
5	to	to	PART	_	_	2	comp:obj@agent	_	_
6	retain	retain	VERB	_	_	5	comp:obj	_	_
7	them	them	PRON	_	_	6	comp:obj	_	_
{{< /conll >}}

{{< conll >}}
1	it	it	PRON	_	_	2	subj@expl	_	_
2	rains	rain	VERB	_	_	0	root	_	_
3	a	a	DET	_	_	4	det	_	_
4	lot	lot	NOUN	_	_	2	mod	_	_
5	in	in	PART	_	_	2	mod	_	_
6	England	England	PROPN	_	_	5	comp:obj	_	_
{{< /conll >}}

In the conversion UD => SUD of `expl`, we use the relation `comp@expl`:
{{< conll >}}
# text = There was no explanation.
1	There	there	PRON	EX	_	2	comp@expl	_	_
2	was	be	VERB	VBD	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	_	Cxn=Existential-CopPred-ThereExpl
3	no	no	DET	DT	PronType=Neg	4	det	_	_
4	explanation	explanation	NOUN	NN	Number=Sing	2	subj	_	CxnElt=2:Existential-CopPred-ThereExpl.Pivot|SpaceAfter=No
5	.	.	PUNCT	.	_	2	punct	_	_
{{< /conll >}}

This feature can also be used to annotate clitic doubling, such as repeated subjects in certain French interrogative constructions.

> Clitic doubling (French)
{{< conll >}}
# text = Jean vient-il demain ?
# text_en = Is Jean coming tomorrow?
1	Jean	Jean	PROPN	_	_	2	subj	_	Gloss=Jean
2	vient	venir	VERB	_	_	0	root	_	Gloss=come
3	-il	il	PRON	_	_	2	subj@expl	_	Gloss=he
4	demain	demain	ADV	_	_	2	mod	_	Gloss=tomorrow
5	?	?	PUNCT	_	_	2	punct	_	Gloss=?
{{< /conll >}}



TODO
### Overview

### Specific Pattern


