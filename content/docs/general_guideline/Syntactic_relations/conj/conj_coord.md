---
title: "conj:coord"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---


# `conj:coord` 

{{< hint info >}}
For more general information about coordination, see the [coordination construction page](../../Universal_construction/coordination.md).
{{< /hint >}}

The `conj:coord` relation is used to link elements connected with a coordinating conjunction such as *and* and *or*.
The conjunction itself is linked to the second element with a `cc` relation.
It is analogous to [`conj`](https://universaldependencies.org/u/dep/conj.html) relation in UD.

{{<grew corpus="SUD_French-Rhapsodie@2.15" >}}
pattern { X -[conj:coord]-> Y }
{{</grew>}}


> **French**
{{< conll >}}
# text = Elle saura conjuguer le changement et la cohésion sociale l' esprit d' initiative et la sécurité la modernité et le bien vivre ensemble
# text_en = She will be able to combine change and social cohesion, a spirit of initiative and security, modernity and living well together.
1	Elle	il	PRON	_	Gender=Fem|Number=Sing|Person=3|PronType=Prs	2	subj	_	Gloss=she
2	saura	savoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin	0	root	_	Gloss=will_know
3	conjuguer	conjuguer	VERB	_	VerbForm=Inf	2	comp:obj	_	Gloss=conjugate|Subject=SubjRaising
4	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	5	det	_	Gloss=the
5	changement	changement	NOUN	_	Gender=Masc|Number=Sing	3	comp:obj	_	Gloss=change
6	et	et	CCONJ	_	_	8	cc	_	Gloss=and
7	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	8	det	_	Gloss=the
8	cohésion	cohésion	NOUN	_	Gender=Fem|Number=Sing	5	conj:coord	_	Gloss=cohesion
9	sociale	social	ADJ	_	Gender=Fem|Number=Sing	8	mod	_	Gloss=social
10	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	11	det	_	Gloss=the
11	esprit	esprit	NOUN	_	Gender=Masc|Number=Sing	8	conj:coord	_	Gloss=spirit
12	d'	de	ADP	_	_	11	udep	_	Gloss=of
13	initiative	initiative	NOUN	_	Gender=Fem|Number=Sing	12	comp:obj	_	Gloss=initiative
14	et	et	CCONJ	_	_	16	cc	_	Gloss=and
15	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	16	det	_	Gloss=the
16	sécurité	sécurité	NOUN	_	Gender=Fem|Number=Sing	11	conj:coord	_	Gloss=security
17	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	18	det	_	Gloss=the
18	modernité	modernité	NOUN	_	Gender=Fem|Number=Sing	16	conj:coord	_	Gloss=modernity
19	et	et	CCONJ	_	_	22	cc	_	Gloss=and
20	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	22	det	_	Gloss=the
21	bien	bien	ADV	_	_	22	mod	_	Gloss=well
22	vivre	vivre	VERB	_	VerbForm=Inf	18	conj:coord	_	Gloss=living
23	ensemble	ensemble	ADV	_	_	22	mod	_	Gloss=together
{{< /conll >}}

> **Naija**
{{< conll >}}
# sent_id = KAD_22_Chatting-At-The-Restaurant_DG__134
# sound_url = http://www.tal.univ-paris3.fr/trameur/iTrameur-naija/mp3/KAD_22_Chatting-At-The-Restaurant_DG.mp3
# speaker_id = Sp205
# text = I finish < she con post am out for { Instagram |c Facebook |c Whatsapp |c Everywhere } //
# text_en = I finished and she posted it on Instagram, Facebook, Whatsapp, everywhere.
# text_ortho = I finish, she con post am out for Instagram, Facebook, Whatsapp, Everywhere.
1	I	I	PRON	_	Case=Nom|Number=Sing|Person=1|PronType=Prs	2	subj	_	AlignBegin=226776|AlignEnd=227174|Gloss=NOM.SG.1
2	finish	finish	VERB	_	_	5	parataxis:dislocated	_	AlignBegin=227174|AlignEnd=227572|Gloss=finish
3	<	<	PUNCT	_	_	2	punct	_	AlignBegin=227572|AlignEnd=227572|Gloss=PUNCT
4	she	she	PRON	_	Case=Nom|Gender=Fem|Number=Sing|Person=3|PronType=Prs	5	subj	_	AlignBegin=227572|AlignEnd=227970|Gloss=NOM.F.SG.3
5	con	con	AUX	_	Aspect=Cons	0	root	_	AlignBegin=227970|AlignEnd=228368|Gloss=CONS
6	post	post	VERB	_	_	5	comp:aux	_	AlignBegin=228368|AlignEnd=228766|Gloss=post
7	am	am	PRON	_	Case=Acc|Number=Sing|Person=3|PronType=Prs	6	comp:obj	_	AlignBegin=228766|AlignEnd=229164|Gloss=ACC.SG.3
8	out	out	ADP	_	_	6	compound:prt	_	AlignBegin=229164|AlignEnd=229562|Gloss=out
9	for	for	ADP	_	_	6	comp:obl	_	AlignBegin=229562|AlignEnd=229960|Gloss=for
10	{	{	PUNCT	_	_	11	punct	_	AlignBegin=229960|AlignEnd=229960|Gloss=PUNCT
11	Instagram	Instagram	PROPN	_	_	9	comp:obj	_	AlignBegin=229960|AlignEnd=230358|Gloss=Instagram
12	|c	|c	PUNCT	_	_	13	punct	_	AlignBegin=230358|AlignEnd=230358|Gloss=PUNCT
13	Facebook	Facebook	PROPN	_	_	11	conj:coord	_	AlignBegin=230358|AlignEnd=230756|Gloss=Facebook
14	|c	|c	PUNCT	_	_	15	punct	_	AlignBegin=230756|AlignEnd=230756|Gloss=PUNCT
15	Whatsapp	WhatsApp	PROPN	_	_	13	conj:coord	_	AlignBegin=230756|AlignEnd=231154|Gloss=WhatsApp
16	|c	|c	PUNCT	_	_	17	punct	_	AlignBegin=231154|AlignEnd=231154|Gloss=PUNCT
17	Everywhere	everywhere	ADV	_	_	15	conj:coord	_	AlignBegin=231154|AlignEnd=231552|Gloss=everywhere
18	}	}	PUNCT	_	_	11	punct	_	AlignBegin=231552|AlignEnd=231552|Gloss=PUNCT
19	//	//	PUNCT	_	_	5	punct	_	AlignBegin=231552|AlignEnd=231552|Gloss=PUNCT
{{< /conll >}}

The relation can be used with the deep extension `emb`, see [coordination construction page](../../Universal_construction/coordination.md#embedded-coordination).
