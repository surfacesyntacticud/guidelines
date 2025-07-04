---
title: "subj"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# The `subj` relation

## Universal

The `subj` relation is used for all subjects, regardless of their form, nominal or clausal.

> __English__
{{<conll>}}
1	A	a	DET	_	_	2	det	_	_
2	man	man	NOUN	_	_	3	subj	_	_
3	walks	walk	VERB	_	_	0	root	_	_
{{</conll>}}

> English
{{< conll >}}
# sent_id = GUM_whow_joke-55
# text = Practicing your joke is crucial.
# s_type=decl
1	Practicing	practice	VERB	VBG	VerbForm=Ger	4	subj	_	_
2	your	your	PRON	PRP$	Person=2|Poss=Yes|PronType=Prs	3	mod@poss	_	_
3	joke	joke	NOUN	NN	Number=Sing	1	comp:obj	_	_
4	is	be	AUX	VBZ	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
5	crucial	crucial	ADJ	JJ	Degree=Pos	4	comp:pred	_	SpaceAfter=No
{{< /conll >}}


### Deep syntactic features

The `subj` relation can be used with two deep syntactic features.

#### `subj@expl`
The `subj@expl` relation indicates that the subject is present to fill in an obligatory syntactic position bit it has no semantic value (see [`@expl`](../../Deep/expl.md)).

> __French__
{{<conll>}}
# sent_fr = Il pleut dans ma maison
# text_en = It's raining in my house
1	Il	il	PRON	_	_	2	subj@expl	_	Gloss=it
2	pleut	pleuvoir	VERB	_	_	0	root	_	Gloss=rains
3	dans	dans	ADP	_	_	2	mod	_	Gloss=in
4	ma	son	DET	_	_	5	det	_	Gloss=my
5	maison	maison	NOUN	_	_	3	comp:obj	_	Gloss=house
{{</conll>}}


#### `subj@pass`

The relation `subj@pass` is used to indicate a passive construction.
This can be used for both standard passive constructions, and for mediopassive constructions (see [`@pass`](../../Deep/pass.md)).

> __English__
{{<conll>}}
# text = This shall be applauded
1	This	this	PRON	DT	Number=Sing|PronType=Dem	2	subj@pass	_	Entity=(event-70)
2	shall	shall	AUX	MD	VerbForm=Fin	0	root	_	_
3	be	be	AUX	VB	VerbForm=Inf	2	comp:aux	_	_
4	applauded	applaud	VERB	VBD	Mood=Ind|Tense=Past|VerbForm=Fin	3	comp:aux@pass	_	_
{{</conll>}}


> __French__
{{<conll>}}
# text = Il fut bâti en 1998.
# text_en = It was build in 1998.
1	Il	il	PRON	_	_	2	subj@pass	_	Gloss=It
2	fut	être	AUX	_	_	0	root	_	Gloss=was
3	bâti	bâtir	VERB	_	_	2	comp:aux@pass	_	Gloss=built
4	en	en	ADP	_	_	2	mod	_	Gloss=in
5	1998	1998	NUM	_	_	4	comp:obj	_	Gloss=1998
{{</conll>}}

The `subj@pass` is also used for subject in mediopassive constructions.

> __Czech__
{{<conll>}}
# text_en = the number of employees decreased
# text_cs = počet zaměstnanců se snížil
1	počet	počet	NOUN	_	_	4	subj@pass	_	Gloss=number
2	zaměstnanců	zaměstnanec	NOUN	_	_	1	mod	_	Gloss=employees.PL.GEN
3	se	se	PRON	_	_	4	comp@pass	_	Gloss=itself
4	snížil	snížit	VERB	_	_	0	root	_	Gloss=decrease
{{</conll>}}

> __French__
{{<conll>}}
# text_en = the book is selling well
# text_cs = le livre se vend bien
1	le	le	DET	_	_	2	det	_	Gloss=the
2	livre	livre	NOUN	_	_	4	subj@pass	_	Gloss=book
3	se	se	PRON	_	_	4	comp@pass	_	Gloss=itself
4	vend	vendre	VERB	_	_	0	root	_	Gloss=sell
5	bien	bien	ADV	_	_	4	mod	_	Gloss=well
{{</conll>}}

> __Russian__
{{<conll>}}
# text_en = the book is selling well
# text_ru = книга хорошо продаётся
1	книга	книга	NOUN	_	_	3	subj@pass	_	Gloss=book
2	хорошо	хорошо	ADV	_	_	3	mod	_	Gloss=well
3	продаётся	продаваться	VERB	_	_	0	root	_	Gloss=is selling
{{</conll>}}






## French

### Overview

The `subj` in French is usualy between a [VERB](docs/general_guideline/Upos/VERB.md) or an [AUX](docs/general_guideline/Upos/AUX.md) and a nominal ([NOUN](docs/general_guideline/Upos/NOUN.md), [PROPN](docs/general_guideline/Upos/PROPN.md) or [PRON](docs/general_guideline/Upos/PRON.md)).

{{<conll>}} 
# text = L'œuvre est située dans la galerie des batailles, dans le château de Versailles.
1	L'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	2	det	_	SpaceAfter=No|wordform=l'
2	œuvre	œuvre	NOUN	_	Gender=Fem|Number=Sing	3	subj	_	_
3	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	située	situer	VERB	_	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	3	comp:pred	_	_
5	dans	dans	ADP	_	_	4	comp:obl	_	_
6	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	_	_
7	galerie	galerie	NOUN	_	Gender=Fem|Number=Sing	5	comp:obj	_	_
8-9	des	_	_	_	_	_	_	_	_
8	de	de	ADP	_	_	7	udep	_	_
9	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	10	det	_	_
10	batailles	bataille	NOUN	_	Gender=Fem|Number=Plur	8	comp:obj	_	SpaceAfter=No
11	,	,	PUNCT	_	_	12	punct	_	_
12	dans	dans	ADP	_	_	4	comp:obl	_	_
13	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	14	det	_	_
14	château	château	NOUN	_	Gender=Masc|Number=Sing	12	comp:obj	_	_
15	de	de	ADP	_	_	14	udep	_	_
16	Versailles	Versailles	PROPN	_	_	15	comp:obj	_	SpaceAfter=No
17	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}



### Deep features

In French, three deep syntactic features are used:
 - [`@pass`](docs/general_guideline/Deep/pass.md) for passive subject
 - [`@expl`](docs/general_guideline/Deep/expl.md): for expletive subject
 - [`@caus`](docs/general_guideline/Deep/caus.md): for subject in causative construction

#### passive subject 

{{<grew>}}
pattern { GOV -[subj@pass]-> DEP } 
{{</grew>}}

{{<conll>}}
1	Le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	wordform=le
2	château	château	NOUN	_	Gender=Masc|Number=Sing	3	subj@pass	_	_
3	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	ensuite	ensuite	ADV	_	_	3	mod	_	_
5	vendu	vendre	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	3	comp:aux@pass	_	_
6	plusieurs	plusieurs	DET	_	Number=Plur|PronType=Ind	7	det	_	_
7	fois	fois	NOUN	_	Gender=Fem|Number=Plur	3	mod	_	_
8	;	;	PUNCT	_	_	3	punct	_	_
{{</conll>}}

#### causativ subject 

{{<grew>}}
pattern { GOV -[subj@caus]-> DEP } 
{{</grew>}}

{{<conll>}}
# text = et donc, je le fais même rentrer dans la maison.
1	et	et	CCONJ	_	_	6	cc	_	AlignBegin=60484|AlignEnd=60615
2	donc	donc	ADV	_	_	6	mod	_	AlignBegin=60615|AlignEnd=60745|SpaceAfter=No
3	,	,	PUNCT	_	_	2	punct	_	AlignBegin=60745|AlignEnd=60745
4	je	moi	PRON	_	Number=Sing|Person=1|PronType=Prs	6	subj@caus	_	AlignBegin=61067|AlignEnd=61234
5	le	lui	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	6	comp:obj@agent	_	AlignBegin=61234|AlignEnd=61402
6	fais	faire	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=61402|AlignEnd=61569
7	même	même	ADV	_	_	6	mod	_	AlignBegin=61569|AlignEnd=61737
8	rentrer	rentrer	VERB	_	VerbForm=Inf	6	comp:aux@caus	_	AlignBegin=61737|AlignEnd=61904|Subject=ObjRaising
9	dans	dans	ADP	_	_	8	comp:obl	_	AlignBegin=61904|AlignEnd=62071
10	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	11	det	_	AlignBegin=62071|AlignEnd=62239
11	maison	maison	NOUN	_	Gender=Fem|Number=Sing	9	comp:obj	_	AlignBegin=62239|AlignEnd=62406|SpaceAfter=No
12	.	.	PUNCT	_	_	6	punct	_	AlignBegin=62406|AlignEnd=62406
{{</conll>}}

#### expletive subject 

{{<grew>}}
pattern { GOV -[subj@expl]-> DEP } 
{{</grew>}}

{{<conll>}}
# text = il y avait Maxime aussi, pas mal.
1	il	lui	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@expl	_	AlignBegin=12306|AlignEnd=12621
2	y	y	PRON	_	Person=3|PronType=Prs	3	comp@expl	_	AlignBegin=12621|AlignEnd=12935
3	avait	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	AlignBegin=12935|AlignEnd=13249
4	Maxime	Maxime	PROPN	_	_	3	comp:obj	_	AlignBegin=13249|AlignEnd=13563
5	aussi	aussi	ADV	_	_	4	mod	_	AlignBegin=13563|AlignEnd=13878|SpaceAfter=No
6	,	,	PUNCT	_	_	8	punct	_	AlignBegin=13878|AlignEnd=13878
7	pas	pas	ADV	_	_	8	mod	_	AlignBegin=13878|AlignEnd=14192
8	mal	mal	ADV	_	Gender=Masc|Number=Sing	4	mod	_	AlignBegin=14192|AlignEnd=14506|SpaceAfter=No
9	.	.	PUNCT	_	_	3	punct	_	AlignBegin=14506|AlignEnd=14506
{{</conll>}}

### Table

{{< agg table_output_french_subj >}}
 




## Haitian Creole

### Overview

In Haitian Creole, the `subj` relation is used for all subjects, regardless of their form.
The `subj` dependency in Haitian Creole is usually used between a [VERB](docs/general_guideline/Upos/VERB.md) and a nominal ([NOUN](docs/general_guideline/Upos/NOUN.md), [PROPN](docs/general_guideline/Upos/PROPN.md) or [PRON](docs/general_guideline/Upos/PRON.md)).

{{<conll>}} 
# text = Yon pòt pawòl Depatman d Eta deklare Samdi, gouvènman Ameriken an o kouran de rapò ki di kòm kwa gen 2 sitwayen Ameriken ki disparèt an Ayiti, apre laprès nan eta Florid rapòte yo kidnape yon koup.
# text_fr = Un porte-parole du département d'Etat américain déclare samedi, que le gouvernement est au courant du rapport qui dit comme quoi qu'il y a deux citoyens américains qui sont disparus en Haïti , après que la presse dans l'Etat Floride rapporte qu'ils ont kidnappé un couple.
1	Yon	Yon 	DET	_	Definite=Ind|Number=Sing	2	det	_	Gloss=Un
2	pòt	pòt 	NOUN	_	_	7	subj	_	Gloss=porte
3	pawòl	pawòl 	NOUN	_	_	2	compound	_	Gloss=parole
4	Depatman	Depatman	NOUN	_	_	3	comp:obj	_	Gloss=département
5	d	d	X	_	_	4	udep	_	Gloss=d'
6	Eta	Eta	NOUN	_	_	5	goeswith	_	Gloss=Eta
7	deklare	deklare 	VERB	_	Number=Sing|Person=3|Tense=Pres	0	root	_	Gloss=déclarer
8	Samdi	Samdi	NOUN	_	_	7	mod	_	Gloss=samedi|SpaceAfter=No
9	,	,	PUNCT	_	_	7	punct	_	_
10	gouvènman	gouvènman 	NOUN	_	_	13	subj	_	Gloss=gouvernement
11	Ameriken	ameriken 	ADJ	_	_	10	mod	_	Gloss=américain
12	an	an	DET	_	Definite=Def|Number=Sing	11	det	_	Gloss=le
13	o	o	X	_	_	7	comp:obj	_	Gloss=au
14	kouran	kouran	NOUN	_	VerbForm=Vnoun	13	goeswith	_	Gloss=être au courant
15	de	de 	ADP	_	_	14	udep	_	Gloss=de
16	rapò	rapò 	NOUN	_	_	15	comp:obj	_	Gloss=rapport
17	ki	ki	PRON	_	_	18	subj	_	Gloss=qui
18	di	di	VERB	_	Number=Sing|Person=3|Tense=Pres	16	mod@relcl	_	Gloss=dire
19	kòm	kòm	SCONJ	_	_	18	comp:obj	_	Gloss=comme
20	kwa	kwa	PRON	_	_	19	unk	_	Gloss=quoi
21	gen	gen 	VERB	_	_	19	comp:obj	_	Gloss=avoir
22	2	2	NUM	_	_	23	det:num	_	Gloss=deux
23	sitwayen	sitwayen 	NOUN	_	_	21	comp:obj	_	Gloss=citoyen
24	Ameriken	amirekèn	ADJ	_	_	23	mod	_	Gloss=américain
25	ki	ki	PRON	_	_	26	subj	_	Gloss=qui
26	disparèt	disparèt	VERB	_	Number=Plur|Person=3|Tense=Pres	24	mod@relcl	_	Gloss=disparaître
27	an	an	ADP	_	_	26	mod	_	Gloss=en
28	Ayiti	Aiti	PROPN	_	_	27	comp:obj	_	Gloss=Haïti|SpaceAfter=No
29	,	,	PUNCT	_	_	26	punct	_	_
30	apre	apre	ADP	_	_	31	mod	_	Gloss=après
31	laprès	laprès 	NOUN	_	_	35	subj	_	Gloss=la presse
32	nan	nan	ADP	_	_	31	mod	_	Gloss=dans
33	eta	eta	NOUN	_	_	32	comp:obj	_	Gloss=eta
34	Florid	Florid 	PROPN	_	_	33	comp:obj	_	Gloss=Floride
35	rapòte	rapòte 	VERB	_	Number=Sing|Person=3|Tense=Pres	7	conj	_	Gloss=rapporter
36	yo	yo	PRON	_	Number=Plur|Person=3|PronType=Prs	37	subj	_	Gloss=PRON
37	kidnape	kidnape	VERB	_	_	35	comp:obj	_	Gloss=kidnapper
38	yon	yon	DET	_	Definite=Ind|Number=Sing	39	det	_	Gloss=une
39	koup	koup 	NOUN	_	_	37	comp:obj	_	Gloss=coupe|SpaceAfter=No
40	.	.	PUNCT	_	_	7	punct	_	_
{{</conll>}}

### Specific Pattern

#### Construction with [ADP](docs/general_guideline/Upos/ADP.md) governor 

In Haitian Creole, the `subj` relation can be used with an [ADP](docs/general_guideline/Upos/ADP.md) governor.

{{<grew corpus="SUD_Haitian_Creole-Autogramm@latest">}}
pattern { GOV -[subj]-> DEP; GOV[upos=ADP] }
{{</grew>}}

{{<conll>}}
# text = Batay ant gang yo pou kontwòl teritwa lakoz anpil san koule epi plizyè santèn milye moun oblije kouri kite kay yo.
# text_fr = La lutte entre les gangs pour le contrôle des territoires  a fait couler beaucoup de sang et plusieurs centaines de gens sont obligés de courir en laissant leur maison.
1	Batay	Batay 	NOUN	_	_	8	subj	_	Gloss=Lutte
2	ant	ant 	ADP	_	_	1	udep	_	Gloss=entre
3	gang	gang	NOUN	_	_	2	comp:obj	_	Gloss=gangs
4	yo	yo	DET	_	Definite=Def|Number=Plur	3	det	_	Gloss=les
5	pou	pou	ADP	_	_	1	udep	_	Gloss=pour
6	kontwòl	kontwòl	NOUN	_	_	5	comp:obj	_	Gloss=contrôle
7	teritwa	teritwa 	NOUN	_	_	6	comp:obj	_	Gloss=territoire
8	lakoz	lakoz	ADP	_	_	0	root	_	Gloss=à cause
9	anpil	anpil	ADJ	_	_	10	mod	_	Gloss=beacoup
10	san	san	NOUN	_	_	8	comp:obj	_	Gloss=sang
11	koule	koule	VERB	_	Number=Sing|Person=3|Tense=Pres	8	comp:pred	_	Gloss=coulé
12	epi	epi	CCONJ	_	_	17	cc	_	Gloss=et
13	plizyè	plizyè	ADV	_	_	14	det	_	Gloss=plusieurs
14	santèn	santèn	NUM	_	_	17	subj	_	Gloss=centaine
15	milye	milye	NUM	_	_	14	comp:obj	_	Gloss=milliers
16	moun	moun	NOUN	_	_	15	comp:obj	_	Gloss=gens
17	oblije	oblije	VERB	_	Number=Plur|Person=3|Tense=Pres	8	conj:coord	_	Gloss=obliger
18	kouri	kouri	VERB	_	VerbForm=Inf	17	comp:obl	_	Gloss=courir
19	kite	kite 	VERB	_	VerbForm=Inf	18	compound:svc	_	Gloss=quitter
20	kay	kay	NOUN	_	_	19	comp:obj	_	Gloss=maisons
21	yo	yo	DET	_	Number=Plur|Person=3|Poss=Yes	20	det	_	Gloss=PRON|SpaceAfter=No
22	.	.	PUNCT	_	_	8	punct	_	_
{{</conll>}}

#### Tables

{{< agg table_output_haitian_creole_subj >}}
