# AUX or VERB?

It is sometimes not trivial to chose between the part of speech `AUX` and `VERB` for **être**.

## AUX

**être** is an AUX:
 - when it has a predicative complement (it is considered as a copula)

{{< conll >}}
# sent_id = fr-ud-train_05039
# text = L'entrée est gratuite.
1	L'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	2	det	_	SpaceAfter=No
2	entrée	entrée	NOUN	_	Gender=Fem|Number=Sing	3	subj	_	_
3	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	gratuite	gratuit	ADJ	_	Gender=Fem|Number=Sing	3	comp:pred	_	SpaceAfter=No
5	.	.	PUNCT	_	_	3	punct	_	_
{{< /conll >}}

{{< conll >}}
# sent_id = fr-ud-train_12904
# text = C'est notre cantine !
1	C'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	2	subj	_	SpaceAfter=No
2	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	notre	son	DET	_	Number=Sing|Number[psor]=Plur|Person[psor]=1|Poss=Yes|PronType=Prs	4	det	_	_
4	cantine	cantine	NOUN	_	Gender=Fem|Number=Sing	2	comp:pred	_	_
5	!	!	PUNCT	_	_	2	punct	_	_
{{< /conll >}}

 - when it is a tense auxiliary
 - when it is a passive auxiliary

## VERB

**être** is a VERB:
 - when it has an existensial meaning (*je pense donc je suis* -***I think therefore I am***)
 - when it has a locative argument
 - when it has another argument, which is not a predicative argument (*je suis pour la dépénalisation du cannabis* -***I am for the decriminalization of cannabis***)

> Exitensial meaning

{{< conll >}}
# text = Pourquoi en serait-il autrement cette fois-ci ?
1	Pourquoi	pourquoi	ADV	_	_	3	mod	_	_
2	en	en	PRON	_	Emph=No|Person=3|PronType=Prs	3	comp@expl	_	_
3	serait	être	VERB	_	Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	SpaceAfter=No
4	-il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj	_	_
5	autrement	autrement	ADV	_	_	3	mod	_	_
9	?	?	PUNCT	_	_	3	punct	_	_
{{< /conll >}}

> Locative argument

{{< conll >}}
# text = Ils sont sur Cherbourg depuis 2007.
1	Ils	eux	PRON	_	Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs	2	subj	_	_
2	sont	être	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	sur	sur	ADP	_	_	2	comp:obl	_	_
4	Cherbourg	Cherbourg	PROPN	_	_	3	comp:obj	_	_
5	depuis	depuis	ADP	_	_	2	mod	_	_
6	2007	2007	NUM	_	Number=Plur	5	comp:obj	_	SpaceAfter=No
7	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}


{{< hint info >}}
See issue [#11](https://github.com/surfacesyntacticud/guidelines/issues/11) about the distinction between `AUX` and `VERB`.
{{< /hint >}}

---

{{< agg french_etre_aux_verb >}}
