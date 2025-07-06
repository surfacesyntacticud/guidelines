---
title: "ctxt"
weight: 10
---

# `ctxt`

## Universal
In French, adjectives agree with nouns in gender and number. Gender on adjectives functions as an agreement morpheme, marking their relationship with the noun.

Although French adjectives generally agree in gender, many share the same form for masculine and feminine. This raises questions about whether such adjectives should be assigned a `Gender` feature. This phenomenon, already frequent in written French, is even more prevalent in spoken French.

The ctxt suffix (e.g., Gender[ctxt], Number[ctxt]) is used when a morphological feature cannot be retrieved directly from the surface form but must be inferred from syntactic or semantic context.
This situation arises both in written and spoken French, but is especially frequent in oral corpora, where final inflectional endings are often not pronounced.

### __Written corpora__
The `ctxt` feature was introduced in French to specify when the Gender or Number of adjectives, participles, pronouns, or common nouns can only be inferred from context. In written French, some adjectives maintain the same form regardless of gender or number, as illustrated in the example below:

{{< conll >}}
# sent_id = fr-ud-train_01762
# text = Les sandwichs sont relativement variés et pas mauvais.
# text_en = The sandwiches are relatively varied and not bad.
# timestamp = 1749489420114.754
1	Les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	2	det	_	_
2	sandwichs	sandwich	NOUN	_	Number=Plur	3	subj	_	Gender[lex]=Masc
3	sont	être	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	relativement	relativement	ADV	_	Shared=No	5	mod	_	_
5	variés	varié	ADJ	_	Gender=Masc|Number=Plur	3	comp:pred	_	_
6	et	et	CCONJ	_	_	8	cc	_	_
7	pas	pas	ADV	_	Polarity=Neg	8	mod	_	_
8	mauvais	mauvais	ADJ	_	Gender=Masc	5	conj:coord	_	Number[ctxt]=Plur|SpaceAfter=No
9	.	.	PUNCT	_	_	3	punct	_	_
{{< /conll >}}


### __Oral corpora__

This phenomenon becomes even more pronounced in spoken French. In oral corpora, we annotate what is actually pronounced, not the standard written transcription. In many cases, the *-s* marking plural nouns or adjectives is not pronounced, which makes the `Number` feature dependent on context.

{{< conll >}}
# macrosyntax = la compagne de l'un des détenus est toujours en garde à vue //
# sent_id = Rhap_M2006-55
# text = la compagne de l'un des détenus est toujours en garde à vue.
# text_en = the partner of one of the detainees is still in custody.
# timestamp = 1749235252573.8699
1	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	_	_
2	compagne	compagne	NOUN	_	_	9	subj	_	Gender[lex]=Fem|Number[ctxt]=Sing
3	de	de	ADP	_	_	2	udep	_	_
4	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	5	det	_	Gender[ctxt]=Masc|SpaceAfter=No
5	un	un	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Ind	3	comp:obj	_	_
6-7	des	_	_	_	_	_	_	_	_
6	de	de	ADP	_	_	5	comp:obl	_	_
7	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	8	det	_	_
8	détenus	détenu	NOUN	_	_	6	comp:obj	_	Gender[lex]=Masc|Number[ctxt]=Plur
9	est	être	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
10	toujours	toujours	ADV	_	_	11	mod	_	_
11	en	en	ADP	_	_	9	comp:obl	_	_
12	garde	garde	NOUN	_	_	11	comp:obj	_	Gender[lex]=Fem|Number[ctxt]=Sing
13	à	à	ADP	_	_	12	udep	_	_
14	vue	vue	NOUN	_	_	13	comp:obj	_	Gender[lex]=Fem|Number[ctxt]=Sing|SpaceAfter=No
15	.	.	PUNCT	_	_	9	punct	_	_

{{< /conll >}}

#### Liaison
There is additional complexity due to liaison in French. Adjectives ending in consonants are sometimes pronounced differently when followed by vowel-initial words. We identified several main rules for when `Number[ctxt]` and `Gender[ctxt]` features apply.

> __Number[ctxt]__

When an adjective precedes a vowel-initial noun, only adjectives ending in *-s* or *-x* in the masculine form take the feature `Number[ctxt]`, since number is not phonologically recoverable through liaison.

{{< grew >}}
pattern { X [upos=ADJ, Number=Plur]; X<Y; Y[upos=NOUN, form=re"[a|e|i|o|u|é|è].*"] }
{{< /grew >}}

{{< conll >}}
# macrosyntax = il y a plein d'autres itinéraires possibles //
# sent_id = Rhap_D0020-2
# speaker = L1
# text = il y a plein d'autres itinéraires possibles.
# text_en = there are plenty of other possible routes.
# timestamp = 1750072418889
1	il	lui	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@expl	_	_
2	y	y	PRON	_	Person=3|PronType=Prs	3	comp@expl	_	_
3	a	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	plein	plein	ADV	_	_	3	comp:obj	_	_
5	d'	de	ADP	_	_	4	comp:obl	_	SpaceAfter=No
6	autres	autre	ADJ	_	Number=Plur	7	mod	_	Gender[ctxt]=Masc
7	itinéraires	itinéraire	NOUN	_	_	5	comp:obj	_	Gender[lex]=Masc|Number[ctxt]=Plur
8	possibles	possible	ADJ	_	_	7	mod	_	Gender[ctxt]=Masc|Number[ctxt]=Plur|SpaceAfter=No
9	.	.	PUNCT	_	_	3	punct	_	_

{{< /conll >}}

> __Gender[ctxt]__

Adjectives ending in *-t*, *-s*, *-x*, or *-n* are often pronounced identically in masculine and feminine forms when followed by a vowel-initial noun. In such cases, they are marked with `Gender[ctxt]`.

{{< grew corpus="SUD_French-Rhapsodie@latest" >}}
pattern { 
	X [upos=ADJ, Gender__ctxt, Number__ctxt=Sing];
	Y[upos=NOUN, form=re"[a|e|i|o|u|é|è].*"];
	X<Y
}
{{< /grew >}}

{{< conll >}}
# macrosyntax = ^et j'étais pas un très bon élève //
# sent_id = Rhap_D2005-49
# speaker = L2
# text = et j'étais pas un très bon élève.
# text_en = and i wasn't a very good student.
# timestamp = 1750087111947
1	et	et	CCONJ	_	_	3	cc	_	_
2	j'	moi	PRON	_	Number=Sing|Person=1|PronType=Prs	3	subj	_	SpaceAfter=No
3	étais	être	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin	0	root	_	_
4	pas	pas	ADV	_	Polarity=Neg	3	mod	_	_
5	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	8	det	_	_
6	très	très	ADV	_	_	7	mod	_	_
7	bon	bon	ADJ	_	_	8	mod	_	Gender[ctxt]=Masc|Number[ctxt]=Sing
8	élève	élève	NOUN	_	_	3	comp:pred	_	Gender[lex]=Masc|Number[ctxt]=Sing|SpaceAfter=No
9	.	.	PUNCT	_	_	3	punct	_	_

{{< /conll >}}
