---
title: "Pronominal verbs"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

## Pronominal verbs


Reflexive marker (_se_, _me_, _te_, _nous_, _vous_) are analysed as a reflexive pronoun `Reflex=Yes` with one of the lemmas _moi_, _toi_, _soi_, _nous_, _vous_)

Four relations are considered for the reflexive marker _se_: `comp:obj`, `comp:obl`, `comp@expl`, and `comp@pass`.

{{<grew key1="e.label" corpus="SUD_French-GSD@latest" >}}
pattern { 
  X [Reflex=Yes, lemma = "moi"|"toi"|"soi"|"nous"|"vous"];
  e: Y -> X;
}
{{</grew>}}



The semantic distinction between reflexive meaning (_je me rase_) and reciprocal meaning (_ils s'aiment_) is not marked. 

> `comp:obj`: Reflexive pronouns replacing a direct object.
{{<conll>}}
# text = donc ils se retournent
# text_en = and then they turn around
1	donc	donc	ADV	_	_	4	cc	_	_
2	ils	eux	PRON	_	Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs	4	subj	_	_
3	se	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	4	comp:obj	_	highlight=red
4	retournent	retourner	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	highlight=red
{{</conll>}}

> `comp:obl`: Reflexive pronouns replacing an oblique complement.
{{<conll>}}
# sent_id = ParisStories_2019_experienceFac_22
# text = ils se racontent leurs vacances.
1	ils	eux	PRON	_	Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs	3	subj	_	_
2	se	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	3	comp:obl	_	highlight=red
3	racontent	raconter	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	highlight=red
4	leurs	son	DET	_	Number=Plur|Number[psor]=Plur|Person[psor]=3|Poss=Yes|PronType=Prs	5	det	_	_
5	vacances	vacance	NOUN	_	_	3	comp:obj	_	Gender[lex]=Fem|Number[ctxt]=Plur|SpaceAfter=No
6	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

> `comp@expl` : For pronominal verbs *i.e.* verbs that can only be used with a relexive pronoun (such as _se souvenir_, _s'évaporer_, etc.), or lexicalised verb senses (such as _s'entendre_).
{{<conll>}}
# sent_id = ParisStories_2020_campBedouin_14
# text = tu te souviens ?
# text_en = do you remember?
1	tu	toi	PRON	_	Emph=No|Number=Sing|Person=2|PronType=Prs	3	subj	_	_
2	te	toi	PRON	_	Emph=No|Number=Sing|Person=2|PronType=Prs	3	comp@expl	_	InIdiom=Yes|highlight=red
3	souviens	souvenir	VERB	_	ExtPos=VERB|Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	Idiom=Yes|highlight=red
4	?	?	PUNCT	_	_	3	punct	_	_
{{</conll>}}

> `comp@pass`: For passive reflexive constructions, where the the object has been promoted in the subject position: _je vend des livres_ => _les livres se vendent bien_. The marker _se_ is still analysed as a reflexive pronoun, even if it has no pronominal vlue.
{{<conll>}}
# sent_id = ParisStories_2019_peripitiesVoiture_26
# text = donc ça s'est fait.
# text_en = so it was done 
1	donc	donc	ADV	_	_	4	mod	_	_
2	ça	ça	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	4	subj	_	_
3	s'	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	5	comp@pass	_	SpaceAfter=No|highlight=red
4	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
5	fait	faire	VERB	_	Gender=Masc|VerbForm=Part	4	comp:aux@tense	_	Number[ctxt]=Sing|SpaceAfter=No|Tense[denom]=Past|highlight=red
6	.	.	PUNCT	_	_	4	punct	_	_
{{</conll>}}

{{< hint warning >}}
See [#38](https://github.com/surfacesyntacticud/guidelines/issues/38)
{{< /hint >}}

