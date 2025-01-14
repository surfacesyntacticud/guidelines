---
title: "-t-il"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---



# How to annotate a-*t-il* ? 

We choose this annotation for *-t-il* : 

{{<conll>}}
# sent_id = fr-ud-train_04636
# text = Que se passe-t-il ?
1	Que	que	PRON	_	Person=3|PronType=Int	3	comp:pred	_	wordform=que
2	se	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	3	comp@expl	_	_
3	passe	passer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	SpaceAfter=No
4	-t-il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj	_	wordform=il
5	?	?	PUNCT	_	_	3	punct	_	_
{{</conll>}}

Thus, we consider *-t-il* as a `PRON` with the lemma *lui*.
We consider *-t-il* as an allomorph of *il*.
*-t* is not a syntactic element, it is a morphophonological rule that introduces the sound /t/.

Similar annotation are used for *-t-elle* and *-t-on* 

{{< grew >}}
pattern { X [form="-t-il"|"-t-elle"|"-t-on"]}
{{< /grew >}}
