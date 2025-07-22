---
title: "parataxis:insert"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---


# `parataxis:insert`

## Universal
The relation `parataxis:insert` is used for inserted clause.
Contrary to a parenthetical clause, an inserted clause could not form an independent sentence

{{<grew >}}
pattern { X -[parataxis:insert]-> Y }
{{</grew>}}

> French
{{< conll >}}
# text = La France est rose constate La Voix du Nord
# text_en = France is pink notes La Voix du Nord
1	La	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	_	Gloss=the
2	France	France	PROPN	_	_	3	subj	_	Gloss=France
3	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=is|highlight=red
4	rose	rose	ADJ	_	Number=Sing	3	comp:pred	_	Gloss=pink
5	constate	constater	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	3	parataxis:insert	_	Gloss=notes|highlight=red
6	La	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	_	Gloss=the
7	Voix	Voix	PROPN	_	ExtPOS=PROPN|Gender=Fem|Number=Sing	5	subj	_	Gloss=voice
8-9	du	_	_	_	_	_	_	_	_
8	de	de	ADP	_	_	7	mod	_	Gloss=of
9	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	10	det	_	Gloss=the
10	Nord	Nord	PROPN	_	_	8	comp:obj	_	Gloss=north
{{< /conll >}}










