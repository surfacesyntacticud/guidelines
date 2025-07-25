---
title: "comp"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# `comp` 

## Universal  

The `comp` relation (without extension) is used when one has difficulty deciding between `comp:obj` and `comp:obl`.

## French

{{<grew key1="e.label" corpus="SUD_French-GSD@latest" >}}
pattern { e: X -[1=comp, !2]-> Y }
{{</grew>}}


### Overview

In **French**, the `comp` label is frequently used to annotate reflexive pronouns and other pronominal clitics which contribute to the formation of pronominal verbs when it is difficult to determine the role of the pronoun.
In constructions such as *Il s'en sort* (en: *He's doing well*) the pronoun *se* no longer provides the semantic value of an argument of the verb.
However, it fits so well into the typical argument structure that it is hard to recognize that it cannot be de-pronominalized.
For this reason, it is annotated with the `comp` relation.

> {{< conll >}}
# text = Il s'en sort bien
# text_en = He's doing well
1	Il	il	PRON	_	_	4	subj	_	Gloss=he
2	s'	se	PRON	_	_	4	comp	_	Gloss=himself
3	en	en	PRON	_	_	4	comp	_	Gloss=of
4	sort	sortir	VERB	_	_	0	root	_	Gloss=go out
5	bien	bien	ADV	_	_	4	mod	_	Gloss=well
{{< /conll >}}


> {{< conll >}}
# text = Il se souvient
# text_en = He remembers
1	Il	il	PRON	_	_	3	subj	_	Gloss=he
2	se	se	PRON	_	_	3	comp	_	Gloss=himself
3	souvient	souvenir	VERB	_	_	0	root	_	Gloss=remembers
{{< /conll >}}

> {{< conll >}}
# text = Christine en veut à son amie
# text_en = Christine is angry at her friend
1	Christine	Christine	PROPN	_	_	3	subj	_	Gloss=Christine
2	en	en	PRON	_	_	3	comp	_	Gloss=of
3	veut	vouloir	VERB	_	_	0	root	_	Gloss=want
4	à	à	ADP	_	_	3	comp:obl	_	Gloss=to
5	son	son	DET	_	_	6	det	_	Gloss=her
6	amie	ami	NOUN	_	_	4	comp:obj	_	Gloss=friend
{{< /conll >}}

### Deep syntactic features

In the case of **passive reflexive constructions**, the pronoun is labelled `comp` with the deep syntactic feature [`@pass`](../../Deep/pass.md).


> {{< conll >}}
# text = Il se situe à environ 13 kilomètres au nord-ouest
# text_en = It is situated about 13 kilometers to the north-west
1	Il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@pass	_	Gloss=it
2	se	se	PRON	_	Person=3|PronType=Prs	3	comp@pass	_	Gloss=is
3	situe	situer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=situated
4	à	à	ADP	_	_	3	comp:obl	_	Gloss=at
5	environ	environ	ADV	_	_	6	mod	_	Gloss=about
6	13	13	NUM	_	_	7	det	_	Gloss=13
7	kilomètres	kilomètre	NOUN	_	Gender=Masc|Number=Plur	4	comp:obj	_	Gloss=kilometers
8-9	au	_	_	_	_	_	_	_	_
8	à	à	ADP	_	_	7	udep	_	Gloss=to
9	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|Person=3|PronType=Art	10	det	_	Gloss=the
10	nord-ouest	nord-ouest	NOUN	_	Gender=Masc|Number=Sing	8	comp:obj	_	Gloss=north-west
{{< /conll >}}

We can also have the deep syntactic feature [`@expl`](../../Deep/expl.md) for the label `comp`. 

> {{<conll>}}
# text = euh, il y a un stade aussi à côté.
1	euh	euh	INTJ	_	_	5	discourse	_	SpaceAfter=No
2	,	,	PUNCT	_	_	1	punct	_	_
3	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	5	subj@expl	_	_
4	y	y	PRON	_	Person=3|PronType=Prs	5	comp@expl	_	_
5	a	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
6	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	7	det	_	_
7	stade	stade	NOUN	_	Gender=Masc|Number=Sing	5	comp:obj	_	_
8	aussi	aussi	ADV	_	_	5	mod	_	_
9	à	à	ADP	_	_	5	mod	_	_
10	côté	côté	NOUN	_	Gender=Masc|Number=Sing	9	comp:obj	_	SpaceAfter=No
11	.	.	PUNCT	_	_	5	punct	_	_
{{</conll>}}

More information can be found on the French [pronomional verb](../../../language/French/syntax/french_pronominal_verb.md) page or on the page about the annotation of the idiom [*il y a*](../../../language/French/syntax/il_y_a.md).

{{<agg comp_french>}}


