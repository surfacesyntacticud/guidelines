---
title: ""
date: 2020-04-26T17:45:38+02:00
title: Surface Syntactic Universal Dependencies (SUD)

---

<center>⚠️ This website is in construction ⚠️</center>

![Surface Syntactic Universal Dependencies (SUD)](/images/sud.svg#floatleft)

SUD is an annotation scheme for syntactic dependency treebanks, and has a nearly perfect degree of two-way convertibility with the Universal Dependencies scheme (UD). Contrary to UD, it is based on syntactic criteria (favoring functional heads) and the relations are defined on distributional and functional bases.

## An Example:

{{< rawhtml >}}
    <reactive-dep-tree
      interactive="true"
      shown-metas="text_en"
      shown-features="UPOS,LEMMA,FEATS.Tense,FEATS.VerbForm,FEATS.Number,FEATS.Person,MISC.Gloss"
      hidden-features="XPOS"
      conll="
      # sent_id = email-enronsent19_01-0071
      # text = I'm happy about this.
      1	I	I	PRON	PRP	Case=Nom|Number=Sing|Person=1|PronType=Prs	2	subj	_	SpaceAfter=No
      2	'm	be	AUX	VBP	Mood=Ind|Tense=Pres|VerbForm=Fin	0	root	_	_
      3	happy	happy	ADJ	JJ	Degree=Pos	2	comp:pred	_	_
      4	about	about	ADP	IN	_	3	mod	_	_
      5	SUD	SUD	PROPN	DT	Number=Sing	4	comp:obj	_	SpaceAfter=No
      6	.	.	PUNCT	.	_	2	punct	_	_
      "
    ></reactive-dep-tree>
{{< /rawhtml >}}



To see more examples, head over to the [universal SUD guidelines](guidelines/u/), or to the dedicated [French](guidelines/french/) and [Naija](guidelines/pcm/) pages.


## Data
Automatic conversion to the SUD format is available [here](data).

## Publications
The SUD annotation scheme is described in the publications below:

  * Kim Gerdes, Bruno Guillaume, Sylvain Kahane, Guy Perrier. [Improving Surface-syntactic Universal Dependencies (SUD): surface-syntactic relations and deep syntactic features](https://hal.inria.fr/hal-02266003v1) presented at [TLT 2019](https://syntaxfest.github.io/syntaxfest19/tlt2019/tlt2019.html).
  * Kim Gerdes, Bruno Guillaume, Sylvain Kahane, Guy Perrier. [SUD or Surface-Syntactic Universal Dependencies: An annotation scheme near-isomorphic to UD](https://hal.inria.fr/hal-01930614v1) presented at [UDW 2018](https://universaldependencies.org/udw18/).
  * Some linguistic arguments in favor of SUD can be found in the Glossa article: Timothy Osborne, Kim Gerdes [The status of function words in dependency grammar: A critique of Universal Dependencies (UD)](https://www.glossa-journal.org/article/10.5334/gjgl.537/)
  * Comparing syntactic complexity and cognitive constraint of SUD and UD: Yan, Jianwei, and Haitao Liu. [Which annotation scheme is more expedient to measure syntactic difficulty and cognitive demand?.](https://www.aclweb.org/anthology/W19-7903.pdf) Presented at [Quasy](https://quasy-2019.webnode.com/), SyntaxFest 2019.

## SUD relations overview

The picture below describes:
  * in blue: the hierarchy of relations specific to SUD
  * in green: the relations shared with UD
  * in orange: the UD relations not used in SUD

The light-blue boxes at the bottom correspond to the deep syntactic features.

<img class="logo" src="http://localhost:51181/images/taxo.svg" width="100%">

![taxonomy](/images/taxo.svg)
