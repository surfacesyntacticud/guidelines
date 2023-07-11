# Cleft constructions

  

As shown in the page about the [`comp:cleft`](../../../general_guideline/Syntactic_relations/comp/comp_cleft.md) relation,  the cleft constructions are analysed with a `comp:cleft` relation going from the head of the main sentence to the head of the complement.

  

* With **qui** and **que** direct object, the cleft clause is analysed as a relative clause. in particular, **qui** and **que** are analysed as relative pronouns (PRON).

<!-- tabs:start -->
#### **Example**


{{< conll >}}
# sent_id = fr-ud-train_10423
# text = C'est l'équipe des Vengeurs de l'âge d'or qui est reconstituée sous l'égide du SHIELD, un peu comme Rob Liefeld et son studio l'avaient tenté avec la version Heroes Reborn.
1	C'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	2	subj@expl	_	SpaceAfter=No|wordform=c'
2	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	4	det	_	SpaceAfter=No
4	équipe	équipe	NOUN	_	Gender=Fem|Number=Sing	2	comp:pred	_	_
5-6	des	_	_	_	_	_	_	_	_
5	de	de	ADP	_	_	4	udep	_	_
6	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	7	det	_	_
7	Vengeurs	vengeur	NOUN	_	Gender=Masc|Number=Plur	5	comp:obj	_	wordform=vengeurs
8	de	de	ADP	_	_	7	udep	_	_
9	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	10	det	_	SpaceAfter=No
10	âge	âge	NOUN	_	Gender=Masc|Number=Sing	8	comp:obj	_	_
11	d'	de	ADP	_	_	10	udep	_	SpaceAfter=No
12	or	or	NOUN	_	Gender=Masc|Number=Sing	11	comp:obj	_	_
13	qui	qui	PRON	_	PronType=Rel	14	subj@pass	_	_
14	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	2	comp:cleft	_	_
15	reconstituée	reconstituer	VERB	_	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	14	comp:aux@pass	_	_
16	sous	sous	ADP	_	_	14	mod	_	_
17	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	18	det	_	SpaceAfter=No
18	égide	égide	NOUN	_	Gender=Fem|Number=Sing	16	comp:obj	_	_
19-20	du	_	_	_	_	_	_	_	_
19	de	de	ADP	_	_	18	udep	_	_
20	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	21	det	_	_
21	SHIELD	SHIELD	PROPN	_	Gender=Masc|Number=Sing	19	comp:obj	_	SpaceAfter=No
{{< /conll >}}
<!-- tabs:end -->



In the other cases, the cleft clause is analysed as a complement clause, with **que** as a SCONJ.
<!-- tabs:start -->
#### **Example**

{{< conll >}}
# sent_id = fr-ud-train_01065
# text = C'est d'ailleurs à ce style que se rattache la majorité du mobilier.
# text_en = Most of the furniture is actually associated with this style.
1	C'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	2	subj@expl	_	SpaceAfter=No|wordform=c'
2	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	d'	de	ADP	_	ExtPos=ADV	2	mod	_	Idiom=Yes|SpaceAfter=No
4	ailleurs	ailleurs	ADV	_	_	3	comp:obj	_	InIdiom=Yes
5	à	à	ADP	_	_	2	comp:pred	_	_
6	ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	7	det	_	_
7	style	style	NOUN	_	Gender=Masc|Number=Sing	5	comp:obj	_	_
8	que	que	SCONJ	_	_	2	comp:cleft	_	_
9	se	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	10	comp@pass	_	_
10	rattache	rattacher	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	comp:obj	_	_
11	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	12	det	_	_
12	majorité	majorité	NOUN	_	Gender=Fem|Number=Sing	10	subj@pass	_	_
13-14	du	_	_	_	_	_	_	_	_
13	de	de	ADP	_	_	12	udep	_	_
14	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	15	det	_	_
15	mobilier	mobilier	NOUN	_	Gender=Masc|Number=Sing	13	comp:obj	_	SpaceAfter=No
16	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}
<!-- tabs:end -->
