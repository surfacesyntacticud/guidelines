---
title: "Reported speech"
weight: 3
bookToc: true
---


# Reported speech

Reported speech has a feature `Reported=Yes` on its head.
It is generally the `comp:obj`of a speech verb, such as _dire_ 'to say'.

**en mode**: Reported speech can be introduced by the idomatic preposition _en mode_.

{{<conll>}}
# text_en = he was like are you really sure miss, uh.
# text = il était là en mode mais vous êtes sûre madame, euh.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj	_	_
2	était	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	_
3	là	là	ADV	_	_	2	comp:pred	_	_
4	en	en	ADP	_	_	2	mod	_	ExtPos=ADP|Idiom=Yes
5	mode	mode	NOUN	_	Number=Sing	4	comp:obj	_	InIdiom=Yes
6	mais	mais	CCONJ	_	_	8	cc	_	_
7	vous	il	PRON	_	Number=Plur|Person=2|PronType=Prs	8	subj	_	_
8	êtes	être	AUX	_	Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	5	comp:obj	_	Reported=Yes
9	sûre	sûr	ADJ	_	Gender=Fem|Number=Sing	8	comp:pred	_	_
10	madame	madame	NOUN	_	Gender=Fem|Number=Sing	8	vocative	_	SpaceAfter=No
11	,	,	PUNCT	_	_	12	punct	_	_
12	euh	euh	INTJ	_	_	8	discourse	_	SpaceAfter=No
13	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

**être là**
Sometimes, _en mode_ is absent and there is a direct relation between the idiom _être là_ and the reported speech, which we decide to label `comp:obj`.

{{<conll>}}
# text_en = ah, and me, I, I was like, my god what is this guy.
# text = ah, et moi, je me, j'étais là, mon dieu mais c'est quoi ce gars.
1	ah	ah	INTJ	_	_	10	discourse	_	SpaceAfter=No
2	,	,	PUNCT	_	_	1	punct	_	_
3	et	et	CCONJ	_	_	10	cc	_	_
4	moi	lui	PRON	_	Number=Sing|Person=1|PronType=Prs	10	dislocated	_	SpaceAfter=No
5	,	,	PUNCT	_	_	4	punct	_	_
6	je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	10	subj	_	_
7	me	se	PRON	_	Number=Sing|Person=1|PronType=Prs	6	unk@scrap	_	SpaceAfter=No
8	,	,	PUNCT	_	_	6	punct	_	_
9	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	6	conj:dicto	_	SpaceAfter=No
10	étais	être	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin	0	root	_	_
11	là	là	ADV	_	_	10	comp:pred	_	SpaceAfter=No
12	,	,	PUNCT	_	_	10	punct	_	_
13	mon	son	DET	_	Number=Sing|Number[psor]=Sing|Person[psor]=1|PronType=Prs	14	det	_	_
14	dieu	dieu	NOUN	_	_	17	discourse	_	ExtPos=INTJ
15	mais	mais	CCONJ	_	_	17	cc	_	_
16	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	17	subj	_	SpaceAfter=No
17	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	10	comp:obj	_	Reported=Yes
18	quoi	quoi	PRON	_	Person=3|PronType=Int	17	comp:pred	_	_
19	ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	20	det	_	_
20	gars	gars	NOUN	_	Gender=Masc	17	dislocated	_	SpaceAfter=No
21	.	.	PUNCT	_	_	10	punct	_	_
{{</conll>}}
