---
title: "@agent"
weight: 3
bookFlatSection: true
bookToc: true
---

# `@agent`

## Universal

The `@agent` feature is used for arguments that are agents of their governor at the semantic level in various constructions (e.g., causative, passive, impersonal, etc.).

> English
{{< conll >}}
# sent_id = GUM_interview_shalev-6
# s_prominence = 2
# s_type = decl
# transition = continue
# text = He was interviewed by Wikinews.
1	He	he	PRON	_	Case=Nom|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj@pass	_	_
2	was	be	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	_	_
3	interviewed	interview	VERB	_	Tense=Past|VerbForm=Part|Voice=Pass	2	comp:aux@pass	_	_
4	by	by	ADP	_	_	3	comp:obl@agent	_	_
5	Wikinews	Wikinews	PROPN	_	Number=Sing	4	comp:obj	_	_
6	.	.	PUNCT	.	_	2	punct	_	_
{{< /conll >}}

> English
{{< conll >}}
1	it	it	PRON	_	_	2	subj	_	_
2	occurred	occur	VERB	_	_	0	root	_	_
3	to	to	ADP	_	_	2	comp:obl	_	_
4	Quinn	Quinn	PROPN	_	_	3	comp:obj	_	_
5	that	that	SCONJ	_	_	2	comp:obj@agent	_	_
6	perhaps	perhaps	ADV	_	_	8	mod	_	_
7	Stillmann	Stillmann	PROPN	_	_	8	subj	_	_
8	was	be	PROPN	_	_	5	comp:obj	_	_
9	blind	blind	ADJ	_	_	8	comp:pred	_	_
{{< /conll >}}

> French 
{{< conll >}}
# text = Food was cooked by many hands
1	Food	food	NOUN	_	_	2	subj	_	_
2	was	be	AUX	_	_	0	root	_	_
3	cooked	cook	VERB	_	_	2	comp:aux@pass	_	_
4	by	by	ADP	_	_	3	comp:obl@agent	_	_
5	many	many	ADJ	_	_	6	mod	_	_
6	hands	hand	NOUN	_	_	4	comp:obj	_	_
{{< /conll >}}

> French
{{< conll >}}
# text = Il fait accélérer ses troupes
# text_en = He makes his troops go faster
1	Il	il	PRON	_	_	2	subj@caus	_	Gloss=he
2	fait	faire	AUX	_	_	0	root	_	Gloss=make
3	accélérer	accélérer	VERB	_	_	2	comp:aux@caus	_	Gloss=accelerate
4	ses	son	DET	_	_	5	det	_	Gloss=his
5	troupes	troupe	NOUN	_	_	2	comp:obj@agent	_	Gloss=troops
{{< /conll >}}

> French 
{{< conll >}}
# text = Il nous fait manger une pizza
# text_en = You're making us eat a pizza
1	tu	il	PRON	_	Number=Sing|Person=2|PronType=Prs	3	subj@caus	_	Gloss=you
2	nous	lui	PRON	_	Number=Plur|Person=1|PronType=Prs	3	comp:obl@agent	_	Gloss=us
3	fais	faire	AUX	_	Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=make
4	manger	manger	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=eat
5	une	un	DET	_	_	6	det	_	Gloss=a
6	pizza	pizza	PUNCT	_	_	4	punct	_	Gloss=pizza
{{< /conll >}}



## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


