---
title: "compound"
weight: 4
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# `compound`

## Universal

SUD shares with with UD its `compound` relation, though the exact usage of this relationship is determined on a language-by-language basis.
SUD annotations for some languages, such as French, do not use the `compound` relation at all.

> __English__
{{< conll >}}
1	Put	put	VERB	VB	Mood=Imp|Person=2|VerbForm=Fin	0	root	_	_
2	the	the	DET	DT	Definite=Def|PronType=Art	4	det	_	_
3	cider	cider	NOUN	NN	Number=Sing	4	compound	_	highlight=red
4	vinegar	vinegar	NOUN	NN	Number=Sing	1	comp:obj	_	highlight=red
5	into	into	ADP	IN	_	1	udep	_	_
6	a	a	DET	DT	Definite=Ind|PronType=Art	8	det	_	_
7	small	small	ADJ	JJ	Degree=Pos	8	mod	_	_
8	bowl	bowl	NOUN	NN	Number=Sing	5	comp:obj	_	_
9	and	and	CCONJ	CC	_	10	cc	_	_
10	add	add	VERB	VB	Mood=Imp|Person=2|VerbForm=Fin	1	conj	_	_
11	the	the	DET	DT	Definite=Def|PronType=Art	13	det	_	_
12	soy	soy	NOUN	NN	Number=Sing	13	compound	_	highlight=red
13	milk	milk	NOUN	NN	Number=Sing|Shared=No	10	comp:obj	_	highlight=red
{{< /conll >}}

More examples in **SUD_English-EWT**:
{{<grew corpus="SUD_English-EWT@2.15" >}}
pattern { X -[compound]-> Y }
{{</grew>}}

Naija in particular makes heavy use of this relation, which is used to link nouns to virtually any other nouns which play a modifying role.
However, it is also used to annotate phrasal verbs as well as a more limited subset of relations between nouns and adjectives, such as *dry cleaner*, which are considered fixed expressions whose meaning cannot be directly understood from its constituent parts.
For more information, see [Naija's page](../../../../language/naija/syntax/compound_phrasal_verbs).

See examples in **SUD_Naija-NSC**:
{{<grew corpus="SUD_Naija-NSC@2.15" >}}
pattern { X -[compound]-> Y }
{{</grew>}}

In many cases, the existence of a `compound` relation can be determined with a series of linguistic tests.
For example, it might be impossible to insert an adjective between two elements of a compound.
In English, `compound`s are phonologically distinct, pronounced with an intonation similar to that of a single word.
Consider the difference in pronunciation between *real estate*, a bona fide `compound`, and *real property*, an adjective and a noun connected with a simple `mod` relation.


## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


