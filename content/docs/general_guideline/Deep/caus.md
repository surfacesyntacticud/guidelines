---
title: "@caus"
weight: 3
bookFlatSection: true
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# `@caus`: Causative

## Universal

The `@caus` feature is used for causative constructions:
- the promoted subject is analyzed `subj@caus`(while the demoted subject, if present, should have a `@agent` deep subrelation;
- the relation between the causative auxiliary (when the causative construction uses one) and the verb is `comp:aux@caus`.

> Causative construction (French)
{{< conll >}}
# text = Il fait accélérer ses troupes
# text_en = He makes his troops go faster
1	Il	il	PRON	_	_	2	subj@caus	_	Gloss=he
2	fait	faire	AUX	_	_	0	root	_	Gloss=make
3	accélérer	accélérer	VERB	_	_	2	comp:aux@caus	_	Gloss=accelerate
4	ses	son	DET	_	_	5	det	_	Gloss=his
5	troupes	troupe	NOUN	_	_	2	comp:obj@agent	_	Gloss=troops
{{< /conll >}}


