 ---
title: "pronouns"
weight: 11
---

# Pronouns in French

## Universal

French pronouns encode grammatical features such as person, number, case, and sometimes gender. However, several forms are ambiguous or exhibit inconsistent annotation in current treebanks. This guide clarifies how to annotate pronouns more consistently, particularly regarding French.

### __Lemma normalization__
Pronoun lemmas should be unified across paradigms to reflect core referential identity rather than surface distinctions.

> __Subject pronouns__  

In many current annotations, the singular pronouns “il” and “elle” are assigned the lemma `lui`, while the plural pronouns “ils” and “elles” have a different lemma, `eux`.
This distinction is unnecessary and inconsistent because these pronouns share core referential properties and syntactic distribution.
Therefore, we propose unifying both singular and plural third-person pronouns under the single lemma `lui`, rather than maintaining separate lemmas like `eux`.

> __Reflexive pronouns__  

The pronoun “me” is currently annotated with two different lemmas depending on reflexivity:
- `moi` when interchangeable with “lui”
- `soi` when inherently reflexive (e.g., “je me souviens”)

Here we use a single third-person reflexive pronoun lemma (e.g., `soi`) in all inherently reflexive constructions, and disambiguate others using contextual syntax. 

Many cases are semantically ambiguous, and some commutations change verb meaning. Treating French as having only a third-person reflexive pronoun aligns with typological precedent.


### __Gender suppression__
The pronoun “lui” is often annotated with `Gender=Masc`, but this is misleading in indirect object contexts, where lui can refer to either a masculine or feminine antecedent. In these cases, gender is not recoverable from the form and should therefore not be encoded.

This suppression improves consistency, particularly when compared to “leur”, which is never annotated with a gender feature despite being functionally parallel.

{{< conll >}}
# macrosyntax = je lui ai dit [ " ben " "tu vois" je vends des livres // ] //
# sent_id = Rhap_D2001-110
# speaker = L2
# text = je lui ai dit, ben, tu vois, je vends des livres.
# text_en = I told them, you see, I’m selling books.
# timestamp = 1751291059990
1	je	moi	PRON	_	Case=Nom|Emph=No|Number=Sing|Person=1|PronType=Prs	3	subj	_	_
2	lui	lui	PRON	_	Case=Dat|Emph=No|Number=Sing|Person=3|PronType=Prs	4	comp:obl	_	_
3	ai	avoir	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
4	dit	dire	VERB	_	Gender=Masc|VerbForm=Part|Voice=Act	3	comp:aux@tense	_	Number[ctxt]=Sing|SpaceAfter=No|Tense[denom]=Past
5	,	,	PUNCT	_	_	12	punct	_	_
6	ben	ben	INTJ	_	_	12	discourse	_	SpaceAfter=No
7	,	,	PUNCT	_	_	6	punct	_	_
8	tu	toi	PRON	_	Case=Nom|Emph=No|Number=Sing|Person=2|PronType=Prs	9	subj	_	_
9	vois	voir	VERB	_	Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	12	discourse	_	SpaceAfter=No
10	,	,	PUNCT	_	_	9	punct	_	_
11	je	moi	PRON	_	Case=Nom|Emph=No|Number=Sing|Person=1|PronType=Prs	12	subj	_	_
12	vends	vendre	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	4	comp:obj	_	Reported=Yes
13	des	un	DET	_	Definite=Ind|Number=Plur|PronType=Art	14	det	_	_
14	livres	livre	NOUN	_	_	12	comp:obj	_	Gender[lex]=Masc|Number[ctxt]=Plur|SpaceAfter=No
15	.	.	PUNCT	_	_	3	punct	_	_
{{< /conll >}}

In contrast, “lui” retains `Gender=Masc` when used emphatically and contrasted with “elle”. In such cases, gender is semantically recoverable and should be retained.


### __Feature `Case`__
In practice, the `Case` feature for weak pronouns is reliably recoverable based on the syntactic relation (`subj`, `comp:obj`, `comp:obl`). Therefore, forms like “me”, “te”, “nous”, and “vous” can be disambiguated without ambiguity in most cases.

> __Nominative__  

Subject pronouns (e.g., “je”, “tu”, “il”, “nous”, “vous”, on”) should receive `Case=Nom` when they are in subject position (`subj`).

{{< conll >}}
# macrosyntax = tu vas tout droit //
# sent_id = Rhap_M0010-4
# text = tu vas tout droit.
# text_en = you go straight.
# timestamp = 1751289338319
1	tu	toi	PRON	_	Case=Nom|Emph=No|Number=Sing|Person=2|PronType=Prs	2	subj	_	_
2	vas	aller	VERB	_	Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	_
3	tout	tout	ADV	_	_	4	mod	_	_
4	droit	droit	ADJ	_	Gender=Masc	2	comp:obj	_	Number[ctxt]=Sing|SpaceAfter=No
5	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}


> __Accusative__  

Direct object pronouns (e.g., “me”, “te”, “le”, “la”, “les”) should receive `Case=Acc` when used as `comp:obj`. This excludes emphatic forms (e.g., “moi”) and already annotated cases.

{{< conll >}}
# macrosyntax = vous le savez //
# sent_id = Rhap_M2006-36
# text = vous le savez.
# text_en = you know it.
# timestamp = 1751290810221
1	vous	vous	PRON	_	Case=Nom|Emph=No|Number=Plur|Person=2|PronType=Prs	3	subj	_	Polite=Unknown
2	le	le	PRON	_	Case=Acc|Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj	_	_
3	savez	savoir	VERB	_	Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	SpaceAfter=No
4	.	.	PUNCT	_	_	3	punct	_	_

{{< /conll }}

> __Dative__  

Indirect object pronouns (e.g., “me”, “te”, “lui”, “leur”) should receive `Case=Dat` when used in oblique object function `comp:obl`.

{{< conll >}}
# macrosyntax = vous vous trouvez au Gosier //
# sent_id = Rhap_M2006-32
# text = vous vous trouvez au Gosier.
# text_en = you find yourself in Gosier.
# timestamp = 1751291059971
1	vous	vous	PRON	_	Case=Nom|Emph=No|Number=Plur|Person=2|PronType=Prs	3	subj	_	Polite=Unknown
2	vous	vous	PRON	_	Case=Dat|Emph=No|Number=Plur|Person=2|PronType=Prs	3	comp:obl	_	Polite=Unknown
3	trouvez	trouver	VERB	_	Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	_
4-5	au	_	_	_	_	_	_	_	_
4	à	à	ADP	_	_	3	comp:obl	_	_
5	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	6	det	_	_
6	Gosier	Gosier	PROPN	_	_	4	comp:obj	_	Gender[lex]=Unknown|SpaceAfter=No
7	.	.	PUNCT	_	_	3	punct	_	_

{{< /conll >}}

### __Feature `Emph`__
So-called **formes fortes** such as “moi”, “toi”, “lui-même”, “elles-mêmes” are marked with `Emph=Yes`. They typically do not receive a `Case` feature. And pronouns with a `Case` feature aren’t emphatic forms and receive `Emph=No`.

{{< conll >}}
# macrosyntax = $L2 moi < j'ai été fidèle  " oui "  //
# sent_id = Rhap_D2007-63
# speaker = L2
# text = moi, j'ai été fidèle, oui.
# text_en = I, have been faithful, yes.
# timestamp = 1751296225636
1	moi	moi	PRON	_	Emph=Yes|Number=Sing|Person=1|PronType=Prs	4	dislocated:subj	_	SpaceAfter=No
2	,	,	PUNCT	_	_	1	punct	_	_
3	j'	moi	PRON	_	Case=Nom|Emph=No|Number=Sing|Person=1|PronType=Prs	4	subj	_	SpaceAfter=No
4	ai	avoir	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
5	été	être	AUX	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	4	comp:aux@tense	_	_
6	fidèle	fidèle	ADJ	_	_	5	comp:pred	_	Gender[ctxt]=Masc|Number[ctxt]=Sing|SpaceAfter=No
7	,	,	PUNCT	_	_	8	punct	_	_
8	oui	oui	INTJ	_	_	6	discourse	_	SpaceAfter=No
9	.	.	PUNCT	_	_	4	punct	_	_

{{< /conll >}}



