---
title: "@lvc"
weight: 3
bookFlatSection: true
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# `@lvc`: Light Verb Construction 

## Universal 

A light verb construction (LVC) is a type of verbal structure in which a verb is coupled with another element – typically a noun phrase – which provides the primary semantic value. Common examples of LVCs in English include *take a walk*, *give a kiss*, or *have a drink*. In SUD, LVCs are marked with the deep feature `@lvc`.

Note that in case of a LVC, the arguments of the LVC attached to the predicative noun are `comp`and not `udep`.

> Light verb construction (French) 
{{< conll >}}
# text = faire face à la situation
# text_en = He faces the situation
1	Il	il	PRON	_	_	2	subj	_	Gloss=he
2	fait	faire	VERB	_	_	0	root	_	Gloss=makes
3	face	face	NOUN	_	_	2	comp:obj@lvc	_	Gloss=face
4	à	à	ADP	_	_	3	comp:obl	_	Gloss=to
5	la	le	DET	_	_	6	det	_	Gloss=the
6	situation	situation	NOUN	_	_	4	comp:obj	_	Gloss=situation
{{< /conll >}}


The complements of these constructions are sometimes attached to the noun rather than the verb because:
- the noun can form a phrase with the complement: _the projectile has the tendency to get in the way_ &rarr; _this tendency to get in the way needs to be resolved_
- it's the noun that is the predicate and controls the valency. In the previous example, _has_ is a binary predicate, not a ternary predicate.

This first criterion explains the differing interpretations of the following two sentences. _A date with his girlfriend_ forms a perfectly coherent phrase which allows for reformulations such as _the date with his girlfriend, it was pleasant_. However, _part in the discussion_ is less semantically transparent and therefore less prone to such reformulations. Because of this, the verb _take_ is treated as the head of the complement.

> Attachment of dependents of the LVC (English)
{{< conll >}}
1	He	he	PRON	_	_	2	subj	_	_
2	has	have	VERB	_	_	0	root	_	_
3	a	a	DET	_	_	4	det	_	_
4	date	date	NOUN	_	_	2	comp:obj@lvc	_	_
5	with	with	ADJ	_	_	4	mod	_	_
6	his	his	DET	_	_	7	det	_	_
7	girlfriend	girlfriend	NOUN	_	_	5	comp:obj	_	_
{{< /conll >}}

{{< conll >}}
1	take	take	VERB	_	_	0	root	_	_
2	part	part	NOUN	_	_	1	comp:obj@lvc	_	_
3	in	in	ADP	_	_	1	comp:obl	_	_
4	the	the	DET	_	_	5	det	_	_
5	discussion	discussion	NOUN	_	_	3	comp:obj	_	_
{{< /conll >}}

See [issue #5](https://github.com/surfacesyntacticud/guidelines/issues/5) for a discussion about light verb construction annotation in SUD.
### Overview

### Specific Pattern


