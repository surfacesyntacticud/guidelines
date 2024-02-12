---
title: "à part"
weight: 3
bookToc: true
---

# The bigram of lemma *à part* and related constructions

The bigram of lemmas _à_[`ADP`] + _part_[`NOUN`] can be used in several idiomatic expressions:
 - as an adverbal idiom (cf. [Wiktionary](https://fr.wiktionary.org/wiki/%C3%A0_part#fr-adv-1))
 - as an adjectival idiom (cf. [Wiktionary](https://fr.wiktionary.org/wiki/%C3%A0_part#fr-adj-1))
 - as a prepositional idiom (cf. [Wiktionary](https://fr.wiktionary.org/wiki/%C3%A0_part#fr-prép-1))
 - in the larger preposional idiom _mis à part_ (cf. [Wiktionary](https://fr.wiktionary.org/wiki/mis_%C3%A0_part))
 - in the larger adjectival idiom _à part entière_ (cf. [Wiktionary](https://fr.wiktionary.org/wiki/%C3%A0_part_enti%C3%A8re))
 - in the larger adverbial idiom _à parts égales_ (cf. [Wiktionary](https://fr.wiktionary.org/wiki/%C3%A0_parts_%C3%A9gales))

## Adverbal idiom

_à part_ can be an adverbal idiom, meaning _separately_

{{< conll >}}
# sent_id = fr-ud-train_03378
# text = Je mets l'Algérie à part.
# text_en = I'll leave Algeria aside.
1	Je	moi	PRON	_	Emph=No|Number=Sing|Person=1|PronType=Prs	2	subj	_	wordform=je
2	mets	mettre	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
3	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	4	det	_	SpaceAfter=No
4	Algérie	Algérie	PROPN	_	Number=Sing	2	comp:obj	_	_
5	à	à	ADP	_	ExtPos=ADV	2	comp:obl	_	Idiom=Yes|highlight=red
6	part	part	NOUN	_	Gender=Fem|Number=Sing	5	comp:obj	_	InIdiom=Yes|SpaceAfter=No|highlight=red
7	.	.	PUNCT	_	_	2	punct	_	_

{{< /conll >}}

{{<grew>}}
pattern {
  N1 [lemma="à", Idiom=Yes, ExtPos=ADV]; N2 [lemma="part"]; N1 < N2;
}
without { N3[lemma="entier"|"égal"] }
{{</grew>}}

## Adjectival idiom

_à part_ can be an adjectival idiom, meaning either _separate_ or _exceptional_.

{{< conll >}}
# sent_id = fr-ud-train_03783
# text = Les courses d'obstacles sont une discipline à part, avec un jargon hippique particulier.
# text_en = Obstacle racing is a discipline in its own right, with its own special jargon.
1	Les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	2	det	_	wordform=les
2	courses	course	NOUN	_	Gender=Fem|Number=Plur	5	subj	_	_
3	d'	de	ADP	_	_	2	udep	_	SpaceAfter=No
4	obstacles	obstacle	NOUN	_	Gender=Masc|Number=Plur	3	comp:obj	_	_
5	sont	être	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
6	une	un	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	7	det	_	_
7	discipline	discipline	NOUN	_	Gender=Fem|Number=Sing	5	comp:pred	_	_
8	à	à	ADP	_	ExtPos=ADJ	7	mod	_	Idiom=Yes|highlight=red
9	part	part	NOUN	_	Gender=Fem|Number=Sing	8	comp:obj	_	InIdiom=Yes|SpaceAfter=No|highlight=red
10	,	,	PUNCT	_	_	11	punct	_	_
11	avec	avec	ADP	_	_	7	udep	_	_
12	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	13	det	_	_
13	jargon	jargon	NOUN	_	Gender=Masc|Number=Sing	11	comp:obj	_	_
14	hippique	hippique	ADJ	_	Gender=Masc|Number=Sing	13	mod	_	_
15	particulier	particulier	ADJ	_	Gender=Masc|Number=Sing	13	mod	_	SpaceAfter=No
16	.	.	PUNCT	_	_	5	punct	_	_

{{< /conll >}}

{{<grew>}}
pattern {
  N1 [lemma="à", Idiom=Yes, ExtPos=ADJ]; N2 [lemma="part"]; N1 < N2;
}
without { N3[lemma="entier"|"égal"] }
{{</grew>}}

## Prepositional idiom

{{< conll >}}
# sent_id = fr-ud-train_08556
# text = il ne reste aucune trace à part une photographie
# text_en = no trace remains except for a photograph
10	il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	12	subj@expl	_	_
11	ne	ne	ADV	_	Polarity=Neg	12	mod	_	_
12	reste	rester	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
13	aucune	aucun	DET	_	Gender=Fem|Number=Sing|PronType=Neg	14	det	_	_
14	trace	trace	NOUN	_	Gender=Fem|Number=Sing	12	comp:obj@agent	_	_
15	à	à	ADP	_	ExtPos=ADP	12	mod	_	Idiom=Yes|highlight=red
16	part	part	NOUN	_	Gender=Fem|Number=Sing	15	comp:obj	_	InIdiom=Yes|highlight=red
17	une	un	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	18	det	_	_
18	photographie	photographie	NOUN	_	Gender=Fem|Number=Sing	15	comp:obj	_	SpaceAfter=No

{{< /conll >}}

{{<grew>}}
pattern {
  N1 [lemma="à", Idiom=Yes, ExtPos=ADP]; N2 [lemma="part"]; N1 < N2;
}
{{</grew>}}

## The preposional idiom _mis à part_ 

_mis à part_ can be used as a preposional idiom (also with the two other forms _mise à part_ or _mises à part_ when it introduces a feminine singular (resp. plural) entity). It then means _exept_

{{< conll >}}
# sent_id = fr-ud-train_03548
# text = Ils rencontrent rarement les humains, mise à part une incursion occasionnelle dans une communauté rurale
1	Ils	eux	PRON	_	Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs|Shared=No	2	subj	_	wordform=ils
2	rencontrent	rencontrer	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	rarement	rarement	ADV	_	_	2	mod	_	_
4	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	5	det	_	_
5	humains	humains	NOUN	_	Gender=Masc|Number=Plur	2	comp:obj	_	SpaceAfter=No
6	,	,	PUNCT	_	_	7	punct	_	_
7	mise	mettre	VERB	_	ExtPos=ADP|Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	2	mod	_	Idiom=Yes|highlight=red
8	à	à	ADP	_	_	7	comp:obl	_	InIdiom=Yes|highlight=redx  
9	part	part	NOUN	_	Gender=Fem|Number=Sing	8	comp:obj	_	InIdiom=Yes|highlight=red
10	une	un	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	11	det	_	_
11	incursion	incursion	NOUN	_	Gender=Fem|Number=Sing	7	comp:obj	_	_
12	occasionnelle	occasionnel	ADJ	_	Gender=Fem|Number=Sing	11	mod	_	_
13	dans	dans	ADP	_	_	11	udep	_	_
14	une	un	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	15	det	_	_
15	communauté	communauté	NOUN	_	Gender=Fem|Number=Sing	13	comp:obj	_	_
16	rurale	rural	ADJ	_	Gender=Fem|Number=Sing	15	mod	_	_
{{< /conll >}}

{{<grew>}}
pattern {
  N1 [lemma="mettre", Idiom=Yes, ExtPos=ADP]; N2 [lemma="à"]; N3 [lemma="part"]; N1 < N2; N2 < N3;
}
{{</grew>}}

## The adjectival idiom _à part entière_

_à part entière_ can be used as an adjectival idiom which means _in its own right_

{{< conll >}}
# sent_id = fr-ud-train_11187
# text = Il fut élu membre associé de la Royal Academy en 1861 et membre à part entière en 1869
# text_en = He was elected an Associate Member of the Royal Academy in 1861 and a full member in 1862.
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs|Shared=Yes	2	subj@pass	_	wordform=il
2	fut	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	_	_
3	élu	élire	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	2	comp:aux@pass	_	_
4	membre	membre	NOUN	_	Gender=Masc|Number=Sing	3	comp:pred	_	_
5	associé	associer	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	4	mod	_	_
6	de	de	ADP	_	_	4	udep	_	_
7	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	8	det	_	_
8	Royal	Royal	PROPN	_	Gender=Fem|Number=Sing	6	comp:obj	_	_
9	Academy	Academy	PROPN	_	_	8	flat@name	_	_
10	en	en	ADP	_	_	2	mod	_	_
11	1861	1861	NUM	_	Number=Plur	10	comp:obj	_	_
12	et	et	CCONJ	_	_	13	cc	_	_
13	membre	membre	NOUN	_	Gender=Masc|Number=Sing	2	conj:coord	_	_
14	à	à	ADP	_	ExtPos=ADV|Shared=No	13	mod	_	Idiom=Yes|highlight=red
15	part	part	NOUN	_	Gender=Fem|Number=Sing	14	comp:obj	_	InIdiom=Yes|highlight=red
16	entière	entier	ADJ	_	Gender=Fem|Number=Sing	15	mod	_	InIdiom=Yes|highlight=red
17	en	en	ADP	_	Shared=No	13	orphan	_	_
18	1869	1869	NUM	_	Number=Plur	17	comp:obj	_	_
19	;	;	PUNCT	_	_	2	punct	_	_
{{< /conll >}}

{{<grew>}}
pattern {
  N1 [lemma="à", Idiom=Yes, ExtPos=ADJ]; N2 [lemma="part"]; N3 [lemma="entier"]; N1 < N2; N2 < N3;
}
{{</grew>}}

## The adverbial idiom _à parts égales_

The adverbial idiom _à parts égales_ means _equally_ (for a repartition)

{{< conll >}}
# sent_id = fr-ud-train_09228
# text = Il est financé à part égale par l'État et les Départements (au prorata du nombre d'habitants).
# note = The sentence was shortened and typos were fixed
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj@pass	_	wordform=il
2	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	financé	financer	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	2	comp:aux@pass	_	_
4	à	à	ADP	_	ExtPos=ADV	3	mod	_	Idiom=Yes|highlight=red
5	parts	part	NOUN	_	Gender=Fem|Number=Plur	4	comp:obj	_	InIdiom=Yes|highlight=red
6	égales	égal	ADJ	_	Gender=Fem|Number=Plur	5	mod	_	InIdiom=Yes|highlight=red
7	par	par	ADP	_	_	3	comp:obl@agent	_	_
8	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art|Shared=No	9	det	_	SpaceAfter=No
9	État	État	NOUN	_	Gender=Masc|Number=Sing	7	comp:obj	_	wordform=état
10	et	et	CCONJ	_	_	12	cc	_	_
11	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	12	det	_	_
12	Départements	département	NOUN	_	Gender=Masc|Number=Plur	9	conj:coord	_	wordform=départements
{{< /conll >}}

{{<grew>}}
pattern {
  N1 [lemma="à", Idiom=Yes, ExtPos=ADV]; N2 [lemma="part"]; N3 [lemma="égal"]; N1 < N2; N2 < N3;
}
{{</grew>}}
