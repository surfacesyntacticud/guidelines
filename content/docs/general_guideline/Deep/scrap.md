---
title: "@scrap"
weight: 10
---

# `@scrap`

In spoken data, sometimes speakers utter a half-finished construction.
In that case, it may happen that a word cannot be attached to its head, because the speaker decided not to utter it.

{{<grew>}}
pattern { GOV -[deep=scrap]-> DEP }
{{</grew>}}

# Universal

> **French**
{{<conll>}}
# text = Je lis son le portrait de notre de votre héros
# text_en = I'im reading his the portrayal of our of your hero
1	je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	Gloss=I
2	lis	lire	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=read
3	son	son	DET	_	Number=Sing|PossNumber=Sing|PossPerson=3|PronType=Prs	5	det	_	Gloss=his
4	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	3	conj:dicto	_	Gloss=the
5	portrait	portrait	NOUN	_	Gender=Masc|Number=Sing	2	comp:obj	_	Gloss=portrayal
6	de	de	ADP	_	_	5	udep	_	Gloss=of|highlight=red
7	notre	son	DET	_	Number=Sing|Person=3|PossNumber=Plur|PossPerson=1|PronType=Prs	6	comp:obj@scrap	_	Gloss=our|highlight=red
8	de	de	ADP	_	_	6	conj:dicto	_	Gloss=of
9	votre	son	DET	_	Number=Sing|Person=3|PossNumber=Plur|PossPerson=2|PronType=Prs	10	det	_	Gloss=your
10	héros	héros	NOUN	_	Gender=Masc	8	comp:obj	_	Gloss=hero
{{</conll>}}

In this example, the construction *Je lis son le portrait de notre de votre héros* (English: *I’m reading his the portrayal of our of your hero*).
This construction causes some issues because the word *notre* cannot be attached to its semantic head *héros* because of the presence of the second *de*.
For these cases, the two words *de* are linked with a `conj:dicto` relation and the word *notre* is linked to the first *de* as an incomplete object `comp:obj@scrap`.




## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


