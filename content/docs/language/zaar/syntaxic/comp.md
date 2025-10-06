# `comp` deprel


{{< grew key1="e.label" corpus="SUD_Zaar-Autogramm@latest">}}
pattern { e:X -[1=comp]-> Y }
{{< /grew >}}

## `comp:obj@R`

{{< conll >}}
# sent_id = SAY_BC_narr_01_056-056
# speaker_id = SP1
# sound_url = https://corporan.huma-num.fr/Archives/media/SAY/WAV/SAY_BC_NARR_01.WAV
# sent_timecode = 68270, 68932
# text = tə́ gə̀mtə̀ mə́nɗi //
# text_ortho = tə́ gə̀mtə̀ mə́nɗi //
# text_en = They gave it to him.
1	tə́	á	AUX	_	Aspect=Aor|Number=Plur|Person=3	0	root	_	AlignBegin=68270|AlignEnd=68436|Gloss=3Plur.Aor
2-3	gə̀mtə̀	_	_	_	_	_	_	_	_
2	gə̀m	gəm	VERB	_	_	1	comp:aux	_	AlignBegin=68436|AlignEnd=68519|Gloss=put|highlight=red
3	=tə᷅	=tə	PRON	_	Case=Acc|Number=Sing|Person=3|PronType=Prs	2	comp:obj@R	_	AlignBegin=68519|AlignEnd=68602|Gloss=3Sing.Obj|highlight=red
4-5	mə́nɗi	_	_	_	_	_	_	_	_
4	mə́n	mə́n	PART	_	Case=Ben|PartType=Adv	2	compound:prt	_	AlignBegin=68602|AlignEnd=68685|Gloss=BEN
5	ɗi	ɗi	PART	_	PartType=Adv	2	compound:prt	_	AlignBegin=68685|AlignEnd=68768|Gloss=Ctp|wordform==ɗi
6	//	//	PUNCT	_	_	1	punct	_	AlignBegin=68768|AlignEnd=68932|Gloss=PUNCT
{{< /conll >}}


## `comp:obj@T`

{{< conll >}}
# sent_id = SAY_BC_INT_02_Burial_132-132
# speaker_id = SP1
# sound_url = https://corporan.huma-num.fr/Archives/media/SAY/WAV/SAY_BC_INT_02_BURIAL.WAV
# sent_timecode = 171151, 171749
# text = tá gìːʃí ɗân //
# text_ortho = tá gìːʃí ɗân //
# text_en = They would bury them there.
1	tá	a	AUX	_	Number=Plur|Person=3|Tense=Fut	0	root	_	AlignBegin=171151|AlignEnd=171301|Gloss=3Plur.Fut
2-3	gìːʃí	_	_	_	_	_	_	_	_
2	gìː	giː	VERB	_	_	1	comp:aux	_	AlignBegin=171301|AlignEnd=171376|Gloss=bury|highlight=red
3	=ʃí	=ʃí	PRON	_	Case=Acc|Number=Plur|Person=3|PronType=Prs	2	comp:obj@T	_	AlignBegin=171376|AlignEnd=171451|Gloss=3Plur.Obj|highlight=red
4	ɗân	ɗáni	ADV	_	_	2	comp:obl	_	AlignBegin=171451|AlignEnd=171601|Gloss=there
5	//	//	PUNCT	_	_	1	punct	_	AlignBegin=171601|AlignEnd=171749|Gloss=PUNCT
{{< /conll >}}



## `comp:obj`


{{% hint info %}}

@Bernard: un seul `comp:obj` verbal avec le dépendant à gauche:
{{< grew corpus="SUD_Zaar-Autogramm@latest">}}
pattern { N1 -[comp:obj]-> N2 ; N1[upos=VERB]; N2 << N1 }
{{< /grew >}}

{{% /hint %}}


# ============ Old guidelines ============

`comp:ben`, `comp:goal`, `comp:loc`, `comp:source` are specific relations used in Zaar.

## comp:ben

For example, the `comp:ben` relation is used when the complement is the beneficiary of the action, which is different from the `comp:obl` relation, because the complement is not syntactically nor morphologically marked. Another reason is based on the order : the dependant of a `comp:obj` relation can not stand before the dependant of a `comp:obl` relation in SUD.

  

### Example of a `comp:ben` relation

{{< conll >}}
# text_en =  He said that if it became (a game) he would ask you.
1	wéy	wéy	PART	_	Mood=Qot	4	discourse	_	AlignBegin=185007|AlignEnd=185162|Gloss=EVD
2	yáː	yáː	AUX	_	Mood=Cnd|Number=Sing|Person=3	4	parataxis@mod	_	AlignBegin=185162|AlignEnd=185317|Gloss=3SG.COND
3	nǎː	naː	VERB	_	VerbForm=Fin	2	comp:aux	_	AlignBegin=185317|AlignEnd=185473|Gloss=become
4	wò	wò	AUX	_	Number=Sing|Person=3|Tense=Fut	0	root	_	AlignBegin=185473|AlignEnd=185621|Gloss=3SG.FUT
5-6	ʧetkə	_	_	_	_	_	_	_	_
5	ʧet	ʧet	VERB	_	VerbForm=Fin	4	comp:aux	_	AlignBegin=185621|AlignEnd=185695|Gloss=ask
6	=kə	=kə	PRON	_	Case=Acc|Number=Sing|Person=2|PronType=Prs	5	comp:ben	_	AlignBegin=185695|AlignEnd=185769|Gloss=2SG.OBJ
7	//	//	PUNCT	_	_	4	punct	_	AlignBegin=185769|AlignEnd=185918|Gloss=PUNCT
{{< /conll >}}


## comp:goal

In the same way, the `comp:goal` relation is used when the complement is the goal of the action, and will also be different from the `comp:obj` relation.

  

### Example of a comp:goal relation

{{< conll >}}
# text_en =  If you enter the room, they will enter and follow you into the room.
1	kyáː	yáː	AUX	_	Mood=Cnd|Number=Sing|Person=2	5	parataxis@mod	_	AlignBegin=251131|AlignEnd=251297|Gloss=2SG.COND
2	ndá	nda	VERB	_	VerbForm=Fin	1	comp:aux	_	AlignBegin=251297|AlignEnd=251463|Gloss=enter
3	vìːn	vìːn	NOUN	_	_	2	comp:goal	_	AlignBegin=251463|AlignEnd=251629|Gloss=room
4	<	<	PUNCT	_	_	1	punct	_	AlignBegin=251629|AlignEnd=251795|Gloss=PUNCT
5	tə́	á	AUX	_	Aspect=Aor|Number=Plur|Person=3	0	root	_	AlignBegin=251795|AlignEnd=251978|Gloss=3PL.AOR
6	ʃîː	ʃiː	VERB	_	VerbForm=Fin	5	comp:aux	_	AlignBegin=251978|AlignEnd=252161|Gloss=get_down
7	tə́	á	AUX	_	Aspect=Aor|Number=Plur|Person=3	5	parataxis@conj	_	AlignBegin=252161|AlignEnd=252344|Gloss=3PL.AOR
8-9	lǎːpkə	_	_	_	_	_	_	_	_
8	lǎːp	láːp	VERB	_	VerbForm=Fin	7	comp:obj	_	AlignBegin=252344|AlignEnd=252436|Gloss=follow
9	=kə	=kə	PRON	_	Case=Acc|Number=Sing|Person=2|PronType=Prs	8	comp:obj	_	AlignBegin=252436|AlignEnd=252527|Gloss=2SG.OBJ
10	ɗa	ɗa	ADP	_	ExtPos=ADP	8	comp:obl	_	AlignBegin=252527|AlignEnd=252710|Gloss=at|Idiom=Yes
11	gìp	gìp	ADP	_	_	10	unk	_	AlignBegin=252710|AlignEnd=252893|Gloss=inside|InIdiom=Yes
12	vìːnì	vìːn	NOUN	_	Definite=Ind	10	comp:obj	_	AlignBegin=252893|AlignEnd=252985|Gloss=room.INDF
13	//	//	PUNCT	_	_	5	punct	_	AlignBegin=253076|AlignEnd=253260|Gloss=PUNCT
{{< /conll >}}

