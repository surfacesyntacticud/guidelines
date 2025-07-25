---
title: "Subject"
weight: 2
bookToc: true
---

# Subject

## Universal

The `Subject` feature is specific to SUD. It is used to annotate the control of infinitive subject.
In version 2.15, it is annotated in the Naija corpus and in the four French corpora.

{{<hint info>}}
See discussion [#29](https://github.com/surfacesyntacticud/guidelines/issues/29) on GitHub.
{{</hint>}}

{{<hint warning>}}
⚠️ In previous versions of SUD, control were annotated with the deep edge feature `@x`.

The `@x` feature is now deprecated and must not be used in new annotations.
{{</hint>}}

### Values

> **`Subject=SubjRaising`**
{{<conll>}}
# text = Les experts sont unanimes pour dater ce manuscrit du VIe siècle.
1	Les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	2	det	_	_
2	experts	expert	NOUN	_	Gender=Masc|Number=Plur	3	subj	_	_
3	sont	être	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	unanimes	unanime	ADJ	_	Gender=Masc|Number=Plur	3	comp:pred	_	_
5	pour	pour	ADP	_	_	3	mod	_	_
6	dater	dater	VERB	_	VerbForm=Inf	5	comp:obj	_	Subject=SubjRaising|highlight=red
7	ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	8	det	_	_
8	manuscrit	manuscrit	NOUN	_	Gender=Masc|Number=Sing	6	comp:obj	_	_
9-10	du	_	_	_	_	_	_	_	_
9	de	de	ADP	_	_	8	udep	_	_
10	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	12	det	_	_
11	VIe	VIe	ADJ	_	Gender=Masc|Number=Sing|NumType=Ord	12	mod	_	_
12	siècle	siècle	NOUN	_	Gender=Masc|Number=Sing	9	comp:obj	_	SpaceAfter=No
13	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

> **`Subject=ObjRaising`** 
{{<conll>}}
# text = D'un coup de pied, il le fait tomber de la main du prêtre, par terre.
1	D'	de	ADP	_	_	9	mod	_	SpaceAfter=No
2	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	3	det	_	_
3	coup	coup	NOUN	_	Gender=Masc|Number=Sing	1	comp:obj	_	_
4	de	de	ADP	_	_	3	udep	_	_
5	pied	pied	NOUN	_	Gender=Masc|Number=Sing	4	comp:obj	_	SpaceAfter=No
6	,	,	PUNCT	_	_	1	punct	_	_
7	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	9	subj@caus	_	_
8	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	9	comp:obj@agent	_	_
9	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
10	tomber	tomber	VERB	_	VerbForm=Inf	9	comp:aux@caus	_	Subject=ObjRaising|highlight=red
11	de	de	ADP	_	_	10	comp:obl	_	_
12	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	13	det	_	_
13	main	main	NOUN	_	Gender=Fem|Number=Sing	11	comp:obj	_	_
14-15	du	_	_	_	_	_	_	_	_
14	de	de	ADP	_	_	13	udep	_	_
15	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	16	det	_	_
16	prêtre	prêtre	NOUN	_	Gender=Masc|Number=Sing	14	comp:obj	_	SpaceAfter=No
17	,	,	PUNCT	_	_	18	punct	_	_
18	par	par	ADP	_	_	9	mod	_	_
19	terre	terre	NOUN	_	Gender=Fem|Number=Sing	18	comp:obj	_	SpaceAfter=No
20	.	.	PUNCT	_	_	9	punct	_	_
{{</conll>}}

> **`Subject=OblRaising`** 
{{<conll>}}
#text = Ce mécanisme peut permettre à la fraude de durer plusieurs années ;
1	Ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	2	det	_	_
2	mécanisme	mécanisme	NOUN	_	Gender=Masc|Number=Sing	3	subj	_	_
3	peut	pouvoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	permettre	permettre	VERB	_	VerbForm=Inf	3	comp:obj	_	Subject=SubjRaising|highlight=red
5	à	à	ADP	_	_	4	comp:obl	_	_
6	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	_	_
7	fraude	fraude	NOUN	_	Gender=Fem|Number=Sing	5	comp:obj	_	_
8	de	de	ADP	_	_	4	comp:obj	_	_
9	durer	durer	VERB	_	VerbForm=Inf	8	comp:obj	_	Subject=OblRaising|highlight=red
10	plusieurs	plusieurs	DET	_	Number=Plur|PronType=Ind	11	det	_	_
11	années	année	NOUN	_	Gender=Fem|Number=Plur	9	comp:obj	_	_
12	;	;	PUNCT	_	_	3	punct	_	_
{{</conll>}}

> **`Subject=Generic`** 
{{<conll>}}
#text = Dieu (Ned Flanders) leur apprend qu'il est interdit de manger les fruits de l'arbre.
1	Dieu	Dieu	PROPN	_	_	7	subj	_	_
2	(	(	PUNCT	_	_	3	punct	_	SpaceAfter=No
3	Ned	Ned	PROPN	_	_	1	conj:appos	_	_
4	Flanders	Flanders	PROPN	_	_	3	flat@name	_	SpaceAfter=No
5	)	)	PUNCT	_	_	3	punct	_	_
6	leur	lui	PRON	_	Number=Plur|Person=3|PronType=Prs	7	comp:obl	_	_
7	apprend	apprendre	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
8	qu'	que	SCONJ	_	_	7	comp:obj	_	SpaceAfter=No
9	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	10	subj@expl	_	_
10	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	comp:obj	_	_
11	interdit	interdire	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	10	comp:aux@pass	_	_
12	de	de	ADP	_	_	11	comp:obj@pass	_	_
13	manger	manger	VERB	_	VerbForm=Inf	12	comp:obj	_	Subject=Generic|highlight=red
14	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	15	det	_	_
15	fruits	fruit	NOUN	_	Gender=Masc|Number=Plur	13	comp:obj	_	_
16	de	de	ADP	_	_	15	udep	_	_
17	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	18	det	_	SpaceAfter=No
18	arbre	arbre	NOUN	_	Gender=Masc|Number=Sing	16	comp:obj	_	SpaceAfter=No
19	.	.	PUNCT	_	_	7	punct	_	_
{{</conll>}}


> **`Subject=Instantiated`** 
{{<conll>}}
#text = Condamné à dix ans, il passe le reste de sa vie en prison.
1	Condamné	condamner	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	7	mod	_	Subject=Instantiated|highlight=red
2	à	à	ADP	_	_	1	comp:obl	_	_
3	dix	dix	NUM	_	Number=Plur	4	det	_	_
4	ans	an	NOUN	_	Gender=Masc|Number=Plur	2	comp:obj	_	SpaceAfter=No
5	,	,	PUNCT	_	_	1	punct	_	_
6	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	7	subj	_	_
7	passe	passer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
8	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	9	det	_	_
9	reste	reste	NOUN	_	Gender=Masc|Number=Sing	7	comp:obj	_	_
10	de	de	ADP	_	_	9	udep	_	_
11	sa	son	DET	_	Gender=Fem|Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs	12	det	_	_
12	vie	vie	NOUN	_	Gender=Fem|Number=Sing	10	comp:obj	_	_
13	en	en	ADP	_	_	7	mod	_	_
14	prison	prison	NOUN	_	Gender=Fem|Number=Sing	13	comp:obj	_	SpaceAfter=No
15	.	.	PUNCT	_	_	7	punct	_	_
{{</conll>}}


{{<hint warning>}}
⚠️ Sometimes, the feature `Subject=NoRaising` is used.
It corresponds to an undespecified annotation covering both `Subject=Generic` or `Subject=Instantiated`.
You can find this annotation in the treebank [**French-Rhapsodie**](https://universal.grew.fr/?corpus=SUD_French-Rhapsodie@latest) and [**French_ParisStories**](https://universal.grew.fr/?corpus=SUD_French-ParisStories@latest).
{{</hint>}}


{{<conll>}}
#text = au début, il voulait pas venir dans la salle pour faire des activités.
1-2	au	_	_	_	_	_	_	_	_
1	à	à	ADP	_	_	6	mod	_	AlignBegin=24280|AlignEnd=24586
2	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	3	det	_	_
3	début	début	NOUN	_	Gender=Masc|Number=Sing	1	comp:obj	_	AlignBegin=24586|AlignEnd=24892|SpaceAfter=No
4	,	,	PUNCT	_	_	1	punct	_	AlignBegin=24892|AlignEnd=24892
5	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	6	subj	_	AlignBegin=24892|AlignEnd=25199
6	voulait	vouloir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	AlignBegin=25199|AlignEnd=25505
7	pas	pas	ADV	_	_	6	mod	_	AlignBegin=25505|AlignEnd=25811
8	venir	venir	VERB	_	VerbForm=Inf	6	comp:obj	_	AlignBegin=25811|AlignEnd=26117|Subject=SubjRaising
9	dans	dans	ADP	_	_	8	comp:obl	_	AlignBegin=26117|AlignEnd=26424
10	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	11	det	_	AlignBegin=26424|AlignEnd=26730
11	salle	salle	NOUN	_	Gender=Fem|Number=Sing	9	comp:obj	_	AlignBegin=26730|AlignEnd=27036
12	pour	pour	ADP	_	_	8	mod	_	AlignBegin=27036|AlignEnd=27345
13	faire	faire	VERB	_	VerbForm=Inf	12	comp:obj	_	AlignBegin=27345|AlignEnd=27654|Subject=NoRaising|highlight=red
14	des	un	DET	_	Definite=Ind|Number=Plur|PronType=Art	15	det	_	AlignBegin=27654|AlignEnd=27963
15	activités	activité	NOUN	_	Gender=Fem|Number=Plur	13	comp:obj	_	AlignBegin=27963|AlignEnd=28272|SpaceAfter=No
16	.	.	PUNCT	_	_	6	punct	_	AlignBegin=28272|AlignEnd=28272
{{</conll>}}









