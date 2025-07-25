---
title: "Idioms and Titles"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Idioms and Titles

## Universal

SUD offers several features which allow annotators to mark idiomatic expressions and titles while still preserving the internal syntactic structure between their various components. We have decided to distinguish these two categories from Multi-Word Expressions (MWEs), which represent a broader category which also includes named entities.

For our purposes, "title" refer to any title given to a film, book, painting, or other work of art, such as *Planet of the Apes*, *Dark Side of the Moon*, *American Gothic*, or *Super Mario Bros*. However, this excludes other named entities like events, holidays or locations, such as *The Gulf War*, *Good Friday*, or *The Eiffel Tower*.

Idioms, meanwhile, refer to any figurative expression ranging from classic examples like *kick the bucket* to extremely common phrases like *in general* whose precise meaning cannot directly be deduced from its constituents. Pronominal verbs, such as those common in Romance languages, are also treated as idioms.

Idioms and titles are annotated in the following way:
 - The **head** of the idiom or title contains the feature `Idiom=Yes` or `Title=Yes`
 - The **head** also contains an "external part of speech" feature (`ExtPos`) which denotes the element's function within the wider sentence. For title, the `ExtPos` value is always `PROPN`.
- The **remaining components** of the element contain the feature `InIdiom=Yes` or `InTitle=Yes`.

By marking these categories with features rather than a `fixed` relation, we are able to preserve their internal syntactic structure.

{{< grew >}}
pattern { X[Idiom] }
{{< /grew >}}

{{< grew >}}
pattern { X[Title] }
{{< /grew >}}


{{< hint warning >}}
Until SUD version 2.8, the feature `PhraseType=Idiom` was used for the head of idioms (now replaced by `Idiom=Yes`) and the feature `PhraseType=Title` was used for the head of titles (now replaced by `Title=Yes`)
{{< /hint >}}

### With internal syntactic relations

> English 
{{< conll >}}
1	Karen	Karen	PROPN	_	_	2	subj	_	_
2	loved	love	VERB	_	_	0	root	_	_
3	One	one	PRON	_	_	4	subj	_	InTitle=Yes|highlight=red
4	Flew	fly	VERB	_	ExtPos=PROPN	2	comp:obj	_	Title=Yes|highlight=red
5	Over	over	ADP	_	_	4	comp:obl	_	InTitle=Yes|highlight=red
6	the	the	DET	_	_	7	det	_	InTitle=Yes|highlight=red
7	Cuckoo	cuckoo	NOUN	_	_	8	comp:obj	_	InTitle=Yes|highlight=red
8	's	's	PART	_	_	9	mod@poss	_	InTitle=Yes|highlight=red
9	Nest	nest	VERB	_	_	5	comp:obj	_	InTitle=Yes|highlight=red
{{< /conll >}}

> English
{{< conll >}}
1	That	that	PRON	_	_	2	subj@pass	_	InIdiom=Yes|highlight=red
2	said	say	VERB	_	ExtPos=ADV	5	mod	_	Idiom=Yes|highlight=red
3	,	,	PUNCT	_	_	2	punct	_	_
4	it	it	PRON	_	_	5	subj	_	_
5	was	be	AUX	_	_	0	root	_	_
6	not	not	ADV	_	_	5	mod	_	_
7	my	my	DET	_	_	8	det	_	_
8	favorite	favorite	NOUN	_	_	5	comp:pred	_	_
{{< /conll >}}

> English
{{< conll >}}
1	Finance	finance	NOUN	_	_	4	subj	_	_
2	and	and	CCONJ	_	_	3	cc	_	_
3	mentorship	mentorship	NOUN	_	_	1	conj	_	_
4	should	shall	AUX	_	_	0	root	_	_
5	go	go	VERB	_	_	4	comp:aux	_	_
6	hand	hand	NOUN	_	ExtPos=ADV|Idiom=Yes	5	mod	_	highlight=red
7	in	in	ADP	_	InIdiom=Yes	6	udep	_	highlight=red
8	hand	hand	NOUN	_	InIdiom=Yes	7	comp:obj	_	highlight=red
{{< /conll >}}

> Spanish
{{< conll >}}
# text_en = His name is Alejandro.
1	Se	se	PRON	_	_	2	comp	_	Gloss=himself|InIdiom=Yes|highlight=red
2	llama	llamar	VERB	_	ExtPos=VERB	0	root	_	Gloss=calls|Idiom=Yes|highlight=red
3	Alejandro	Alejandro	PROPN	_	_	2	comp:pred	_	Gloss=Alejandro
{{< /conll >}}


### Without internal syntactic relations 
When there is no clear internal syntactic structure, the relation `unk` is used.

> English
{{< conll >}}
1	Let	let	VERB	_	_	0	root	_	_
2	me	I	PRON	_	_	1	comp:obj	_	_
3	know	know	VERB	_	_	1	comp:pred	_	_
4	what	what	PRON	_	_	5	subj	_	_
5	's	be	AUX	_	_	3	comp:obj	_	_
6	happening	happen	VERB	_	_	5	comp:aux	_	_
7	as	as	SCONJ	_	ExtPos=SCONJ	5	mod	_	Idiom=Yes|highlight=red
8	soon	soon	ADV	_	_	7	unk	_	InIdiom=Yes|highlight=red
9	as	as	SCONJ	_	_	8	unk	_	InIdiom=Yes|highlight=red
10	you	you	PRON	_	_	11	subj	_	_
11	can	can	AUX	_	_	7	comp:obj	_	_
{{< /conll >}}

> French
{{< conll >}}
# sent_id = fr-ud-train_10134__shorten
# text_en = I found the rates applied here to be quite correct.
# text = j'ai trouvé tout à fait correct les tarifs appliqués ici.
1	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	Gloss=I
2	ai	avoir	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=--
3	trouvé	trouver	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	2	comp:aux@tense	_	Gloss=found
4	tout	tout	ADV	_	ExtPos=ADV	7	mod	_	Gloss=quite|Idiom=Yes|highlight=red
5	à	à	ADP	_	_	4	unk	_	Gloss=--|InIdiom=Yes|highlight=red
6	fait	fait	NOUN	_	Gender=Masc|Number=Sing	5	unk	_	Gloss=--|InIdiom=Yes|highlight=red
7	correct	correct	ADJ	_	Gender=Masc|Number=Sing|Typo=Yes	3	comp:pred	_	Gloss=correct
8	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	9	det	_	Gloss=the
9	tarifs	tarif	NOUN	_	Gender=Masc|Number=Plur	3	comp:obj	_	Gloss=rates
10	appliqués	appliquer	VERB	_	Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part	9	mod	_	Gloss=applied
11	ici	ici	ADV	_	_	10	mod	_	Gloss=here
{{< /conll >}}

