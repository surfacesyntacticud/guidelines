---
title: "@agent"
weight: 3
bookFlatSection: true
bookToc: true
---

# `@agent`

## Universal

The `@agent` feature is used for arguments that are deep subjects of their governor. A deep subject is an argument that is subject in the base construction but has been demoted in redistribution of argument position. Typical cases are passive, causative, and impersonal constructions.

> passive (English)
{{< conll >}}
# text = He was interviewed by Wikinews.
1	He	he	PRON	_	Case=Nom|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj@pass	_	_
2	was	be	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	_	_
3	interviewed	interview	VERB	_	Tense=Past|VerbForm=Part|Voice=Pass	2	comp:aux@pass	_	_
4	by	by	ADP	_	_	3	comp:obl@agent	_	_
5	Wikinews	Wikinews	PROPN	_	Number=Sing	4	comp:obj	_	_
6	.	.	PUNCT	.	_	2	punct	_	_
{{< /conll >}}

> Impersonal (French)
{{< conll >}}
# text = Il existe des variantes
# text_en = It exists variants
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj@expl	_	_
2	existe	exister	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	des	un	DET	_	Definite=Ind|Number=Plur|PronType=Art	4	det	_	_
4	variantes	variante	NOUN	_	Number=Plur	2	comp:obj@agent	_	Gender[lex]=Fem
{{< /conll >}}

It makes sense to analyze the deep subject of an impersonal construction as `comp:obj` and not `subj`, because:
- the verb agrees with the dummy subject *il* and not with the deep subject
- the deep subject is pronominalized by an object pronoun: *il en existe*
- French has a quite strong SVO order.
Note that in UD the dummy subject is analyzed has a pure `expl` and the deep subject as the subject.
{{< conll_ud >}}
# text = Il existe des variantes
# text_en = It exists variants
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	expl:subj	_	wordform=il
2	existe	exister	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	des	un	DET	_	Definite=Ind|Number=Plur|PronType=Art	4	det	_	_
4	variantes	variante	NOUN	_	Number=Plur	2	nsubj	_	Gender[lex]=Fem
{{< /conll_ud >}}

> Causative (French)
The demoted subject in French causatives can be `comp:obj` or `comp:obl`.
{{< conll >}}
# text = Il fait accélérer ses troupes
# text_en = He makes his troops go faster
1	Il	il	PRON	_	_	2	subj@caus	_	Gloss=he
2	fait	faire	AUX	_	_	0	root	_	Gloss=make
3	accélérer	accélérer	VERB	_	_	2	comp:aux@caus	_	Gloss=accelerate
4	ses	son	DET	_	_	5	det	_	Gloss=his
5	troupes	troupe	NOUN	_	_	2	comp:obj@agent	_	Gloss=troops
{{< /conll >}}

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
