---
layout: default
---

# **@caus**

The `@caus` feature is used for the argument of causative auxiliaries.
{{< rawhtml >}}
    <reactive-dep-tree
      interactive="true"
      shown-metas="text_en"
      shown-features="UPOS,LEMMA,FEATS.Tense,FEATS.VerbForm,FEATS.Number,FEATS.Person,MISC.Gloss"
      hidden-features="XPOS"
      conll="
      # text_en = He makes his troops go faster.
      1	Il	il	PRON	_	_	2	subj@caus	_	Gloss=he
      2	fait	faire	AUX	_	_	0	root	_	Gloss=make
      3	accélérer	accélérer	VERB	_	_	2	comp:aux@caus	_	Gloss=accelerate
      4	ses	son	DET	_	_	5	det	_	Gloss=his
      5	troupes	troupe	NOUN	_	_	2	comp:obj@agent	_	Gloss=troops
      "
    ></reactive-dep-tree>
{{< /rawhtml >}}

