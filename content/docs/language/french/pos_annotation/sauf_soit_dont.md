 ---
title: "Sauf, soit, dont as CCONJ"
weight: 11
---

# _Sauf, soit, dont_ as CCONJ

_sauf, soit, dont_ can be used as markers in lists. They can link NP, as well as PP:
- _tous les couches, sauf la première_ 'all layers, except the first one'
- _partout, sauf en France_ 'everywhere, except in France'
This property brings these markers closer to coordinating conjunctions than to adpositions. We decided to analyze them as CCONJs.

We distinguish here between:

- **Coordination** (`conj:coord`)
- **Apposition** (`conj:appos`)

### __“sauf”__
**Function:** Subtractive connector, introduces an exception to a preceding phrase.  
**POS:** `CCONJ`  
**Deprel:** Prefer `conj:appos` over `conj:coord` when the second conjunct is a proper subset or exception.

{{< conll >}}
# sent_id = fr-ud-train_11240
# text = Toutes les chansons sont de Pete Townshend, sauf indication contraire.
# text_en = All songs by Pete Townshend unless otherwise noted.
# timestamp = 1751971588519
1	Toutes	tout	ADJ	_	Gender=Fem|Number=Plur	3	mod	_	wordform=toutes
2	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	3	det	_	_
3	chansons	chanson	NOUN	_	Number=Plur	4	subj	_	Gender[lex]=Fem
4	sont	être	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
5	de	de	ADP	_	_	4	comp:obl	_	_
6	Pete	Pete	PROPN	_	_	5	comp:obj	_	Gender[lex]=Unknown
7	Townshend	Townshend	PROPN	_	_	6	flat@name	_	Gender[lex]=Unknown|SpaceAfter=No
8	,	,	PUNCT	_	_	9	punct	_	_
9	sauf	sauf	CCONJ	_	_	4	conj:appos	_	_
10	indication	indication	NOUN	_	Number=Sing	9	comp:obj	_	Gender[lex]=Fem
11	contraire	contraire	ADJ	_	Number=Sing	10	mod	_	Gender[ctxt]=Fem|SpaceAfter=No
12	.	.	PUNCT	_	_	4	punct	_	_
{{< /conll >}}


### __“soit”__
**Function:** introduces alternatives.
**POS:** always CCONJ, even in non-standard or elliptical uses.
**Deprel:** `conj:coord` for disjunctions, `conj:appos` for appositional clarification.

> __Coordinative use__  

“soit” is a `CCONJ`, and the deprel `conj:coord` is used to connect the two prepositional phrases.

{{< conll >}}
# sent_id = fr-ud-train_02047
# text = Ceux qui arrivent à s'organiser, militer etc... finissent par être manipulé soit de l'intérieur, soit de l'extérieur.
# text_en = Those who manage to organize, campaign, etc. end up being manipulated either from within or from without.
# timestamp = 1749489420114.754
1	Ceux	celui	PRON	_	Gender=Masc|Number=Plur|Person=3|PronType=Dem	11	subj	_	wordform=ceux
2	qui	qui	PRON	_	PronType=Rel	3	subj	_	_
3	arrivent	arriver	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	1	mod@relcl	_	_
4	à	à	ADP	_	_	3	comp:obl	_	_
5	s'	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes|Shared=No	6	comp@expl	_	SpaceAfter=No
6	organiser	organiser	VERB	_	VerbForm=Inf	4	comp:obj	_	SpaceAfter=No|Subject=SubjRaising
7	,	,	PUNCT	_	_	8	punct	_	_
8	militer	militer	VERB	_	VerbForm=Inf	6	conj:coord	_	Subject=SubjRaising
9	etc	etc	ADV	_	_	8	conj:coord	_	SpaceAfter=No
10	...	...	PUNCT	_	_	9	punct	_	_
11	finissent	finir	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
12	par	par	ADP	_	_	11	comp:obl	_	_
13	être	être	AUX	_	VerbForm=Inf	12	comp:obj	_	Subject=SubjRaising
14	manipulé	manipuler	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass	13	comp:aux@pass	_	Tense[denom]=Past
15	soit	soit	CCONJ	_	Shared=No	16	cc	_	_
16	de	de	ADP	_	_	13	mod	_	_
17	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	18	det	_	Gender[ctxt]=Masc|SpaceAfter=No
18	intérieur	intérieur	NOUN	_	Number=Sing	16	comp:obj	_	Gender[lex]=Masc|SpaceAfter=No
19	,	,	PUNCT	_	_	21	punct	_	_
20	soit	soit	CCONJ	_	_	21	cc	_	_
21	de	de	ADP	_	_	16	conj:coord	_	_
22	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	23	det	_	Gender[ctxt]=Masc|SpaceAfter=No
23	extérieur	extérieur	NOUN	_	Number=Sing|Shared=No	21	comp:obj	_	Gender[lex]=Masc|SpaceAfter=No
24	.	.	PUNCT	_	_	11	punct	_	_
{{< /conll >}}

> __Appositive use__  

“soit” is a `CCONJ`, and the deprel `conj:appos` is used to link together the appositive element with the first element.

{{< conll >}}
# sent_id = fr-ud-train_05057
# text = Ilonse se situe à une heure de Nice soit 72 km.
# text_en = Ilonse is located one hour from Nice, or 72 km.
# timestamp = 1751986389702
1	Ilonse	Ilonse	PROPN	_	_	3	subj@pass	_	Gender[lex]=Unknown
2	se	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	3	comp@pass	_	_
3	situe	situer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	à	à	ADP	_	_	3	comp:obl	_	_
5	une	un	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	6	det	_	_
6	heure	heure	NOUN	_	Number=Sing	4	comp:obj	_	Gender[lex]=Fem
7	de	de	ADP	_	_	6	udep	_	_
8	Nice	Nice	PROPN	_	_	7	comp:obj	_	Gender[lex]=Unknown
9	soit	soit	CCONJ	_	_	11	mod	_	_
10	72	72	NUM	_	ExtPos=DET	11	det	_	Number[lex]=Plur
11	km	km	NOUN	_	Number=Plur	6	conj:appos	_	Gender[lex]=Masc|SpaceAfter=No
12	.	.	PUNCT	_	_	3	punct	_	_
{{< /conll >}}

### __“dont”__

**Function:** two distinct uses:  
Relative pronoun ⇒ `PRON` introducing a relative clause.  
Appositive connector ⇒ `CCONJ` introducing an appositive subpart.

> __Relative use__  

“dont” is a `PRON`, part of `mod@relcl`.

{{< conll >}}
# sent_id = fr-ud-train_01125
# text = Il a trois frères, dont l'un est l'entomologiste Théodore Lacordaire.
# text_en = He has three brothers, one of whom is the entomologist Théodore Lacordaire.
# timestamp = 1751292598730
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj	_	Case=Nom|wordform=il
2	a	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	trois	trois	NUM	_	ExtPos=DET	4	det	_	Number[lex]=Plur
4	frères	frère	NOUN	_	Number=Plur	2	comp:obj	_	Gender[lex]=Masc|SpaceAfter=No
5	,	,	PUNCT	_	_	9	punct	_	_
6	dont	dont	PRON	_	PronType=Rel	8	udep	_	_
7	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	8	det	_	Gender[ctxt]=Masc|SpaceAfter=No
8	un	un	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Ind	9	subj	_	_
9	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	4	mod@relcl	_	_
10	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	11	det	_	Gender[ctxt]=Masc|SpaceAfter=No
11	entomologiste	entomologiste	NOUN	_	Number=Sing	9	comp:pred	_	Gender[lex]=Masc
12	Théodore	Théodore	PROPN	_	_	11	conj:appos	_	Gender[lex]=Unknown
13	Lacordaire	Lacordaire	PROPN	_	_	12	flat@name	_	Gender[lex]=Unknown|SpaceAfter=No
14	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}


> __Appositive use__  

dont” is a `CCONJ`, and the deprel`conj:appos` is used to link together the appositive element with the first element.

{{< conll >}}
# sent_id = annodis.er_00386
# text = Pas moins d'une douzaine d'hommes étaient mobilisés dont l'équipe cynophile.
# text_en = No fewer than a dozen men were mobilized, including the canine team.
# timestamp = 1752070709034
1	Pas	pas	ADV	_	Polarity=Neg	2	mod	_	_
2	moins	moins	ADV	_	ExtPos=PRON	8	subj@pass	_	_
3	d'	de	ADP	_	_	2	comp:obl	_	SpaceAfter=No
4	une	un	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	5	det	_	_
5	douzaine	douzaine	NOUN	_	Number=Sing	3	comp:obj	_	Gender[lex]=Fem
6	d'	de	ADP	_	_	5	udep	_	SpaceAfter=No
7	hommes	homme	NOUN	_	Number=Plur	6	comp:obj	_	Gender[lex]=Masc
8	étaient	être	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	_
9	mobilisés	mobiliser	VERB	_	Gender=Masc|Number=Plur|VerbForm=Part|Voice=Pass	8	comp:aux@pass	_	Tense[denom]=Past
10	dont	dont	CCONJ	_	PronType=Rel	12	udep	_	_
11	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	12	det	_	Gender[ctxt]=Fem|SpaceAfter=No
12	équipe	équipe	NOUN	_	Number=Sing	5	conj:appos	_	Gender[lex]=Fem
13	cynophile	cynophile	ADJ	_	Number=Sing	12	mod	_	Gender[ctxt]=Fem|SpaceAfter=No
14	.	.	PUNCT	_	_	12	punct	_	_
{{< /conll >}}



