---
title: "@relcl"
weight: 3
bookFlatSection: true
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# `@relcl`: Relative clause

## Universal

The `@relcl` feature is used for the relation between the head of a relative clause and its antecedent.
See [table](https://tables.grew.fr/?data=sud_deps/DEPS&cols=@relcl) for the use of `@relcl` in SUD 2.16.

> English 
{{< conll >}}
1	This	this	PRON	_	_	2	subj	_	_
2	is	be	AUX	_	_	0	root	_	_
3	money	money	NOUN	_	_	2	comp:pred	_	_
4	you	you	PRON	_	_	5	subj	_	_
5	've	have	AUX	_	_	3	mod@relcl	_	_
6	earned	earn	VERB	_	_	5	comp:aux@tense	_	_
{{< /conll >}}

> Russian
{{< conll >}}
# sent_id = w02004065
# text = Существуют разные теории, почему место было покинуто.
# text_en = There are different theories about the reasons for leaving the place.
1	Существуют	существовать	VERB	VBC	Aspect=Imp|Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act	0	root	_	_
2	разные	разный	ADJ	JJ	Case=Nom|Degree=Pos|Number=Plur	3	mod	_	_
3	теории	теория	NOUN	NN	Animacy=Inan|Case=Nom|Gender=Fem|Number=Plur	1	subj	_	SpaceAfter=No
4	,	,	PUNCT	,	_	7	punct	_	_
5	почему	почему	ADV	WRB	Degree=Pos	7	mod	_	_
6	место	место	NOUN	NN	Animacy=Inan|Case=Nom|Gender=Neut|Number=Sing	7	subj@pass	_	_
7	было	быть	AUX	VBC	Aspect=Imp|Gender=Neut|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act	3	mod@relcl	_	_
8	покинуто	покинуть	VERB	VBNH	Aspect=Perf|Gender=Neut|Number=Sing|Tense=Past|Variant=Short|VerbForm=Part|Voice=Pass	7	comp:aux@pass	_	SpaceAfter=No
9	.	.	PUNCT	.	_	1	punct	_	_
{{< /conll >}}






