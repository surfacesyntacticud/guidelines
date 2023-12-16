# Resultative Complement (comp:res)

This relationship applies to verb-verb and verb-adjective combinations in which the second verb or adjective encompasses what are termed "resultative complements" and "phase complements" in the study of Chinese linguistics.

Like directional complements, the affirmative potential 得 de and negative potential 不 bù can intervene between the compound. However, unlike directional complements, this is the only situation in which the resultative and phase resultative complements can be separated.

## Resultative complement
{{< conll_interactive >}}
# text_en = Have you finished washing the clothes?
# translit = Yīfu nǐ xǐ hǎo le ma?
1	衣	衣	NOUN	_	_	4	comp:obj	_	Tone=1|Translit=yī
2	服	服	NOUN	_	_	1	@m	_	Tone=2|Translit=fú
3	你	你	PRON	_	Person=2	4	subj	_	Gloss=2SG|Tone=3|Translit=nǐ
4	洗	洗	VERB	_	_	0	root	_	Tone=3|Translit=xǐ|highlight=green
5	好	好	ADJ	_	_	4	comp:res	_	Tone=3|Translit=hǎo|highlight=red
6	了	了	PART	_	_	4	aspect	_	Gloss=PFV|Grammar_Target=Yes|Tone=5|Translit=le
7	吗	吗	PART	_	Mood=Inter	4	discourse	_	Grammar_Target=Yes|Tone=5|Translit=ma
8	？	？	PUNCT	_	_	4	punct	_	Translit=？
{{< / conll_interactive >}}




## Phase resultative complement
[cf. UD explanation of "phase compound"](https://universaldependencies.org/zh/dep/compound-vv.html#phase-compounds)

Phase resultative complements contain a second verb that modifies the first verb by adding aspectual or telic features. However, these secondary verbs are not fully grammaticalized and their syntactic behavior resembles that of the second verb in resultative resultative complements. As such, they are not categorized the same way as postverbal aspect markers that are tagged as AUX.

The verbs in this category include (non-neutral-tone versions of): 着 / zháo, which means "touched, got at, successful after an attempt"; 到 dào, meaning "arrive, reach"; 見 jiàn, meaning "see"; 完 wán, meaning "be complete, be finished"; and 過 guò, meaning "pass, cross" (for more details, see Chao 1968:446-450).

{{< conll_interactive >}}
# translit = Tā méiyǒu kàndào nǐ.
# text_en = She didn't see you.
1	她	她	PRON	_	Person=3	3	subj	_	Tone=1|Translit=tā
2	没	没	ADV	_	_	3	mod	_	Grammar_Target=Yes|Tone=2|Translit=méi
3	有	有	AUX	_	_	0	root	_	Grammar_Target=Yes|Tone=3|Translit=yǒu
4	看	看	VERB	_	_	3	comp:aux	_	Tone=4|Translit=kàn|highlight=green
5	到	到	VERB	_	_	4	comp:res	_	Tone=4|Translit=dào|highlight=red
6	你	你	PRON	_	Person=2	4	comp:obj	_	Gloss=2SG|Tone=3|Translit=nǐ
7	。	。	PUNCT	_	_	3	punct	_	Translit=。
{{< / conll_interactive >}}


## affirmative/negative potentiallity
{{< conll_interactive >}}
# text_en = You're so smart. You can definitely learn this.
# translit = Nǐ zhème cōngming, kěndìng xué de huì.
1	你	你	PRON	_	Person=2	4	subj	_	Gloss=2SG|Tone=3|Translit=nǐ
2	这	这	DET	ADV	_	4	mod	_	Tone=4|Translit=zhè
3	么	么	PART	_	_	2	@m	_	Tone=5|Translit=me
4	聪	聪	ADJ	_	_	0	root	_	Tone=1|Translit=cōng
5	明	明	ADJ	_	_	4	@m	_	Tone=2|Translit=míng
6	，	，	PUNCT	_	_	9	punct	_	Translit=，
7	肯	肯	AUX	ADV	_	9	mod	_	Tone=3|Translit=kěn
8	定	定	VERB	_	_	7	@m	_	Tone=4|Translit=dìng
9	学	学	VERB	_	_	4	parataxis	_	Tone=2|Translit=xué|highlight=green
10	得	得	PART	_	_	11	mod	_	Grammar_Target=Yes|Tone=2|Translit=dé|highlight=blue
11	会	会	NOUN	_	_	9	comp:res	_	Tone=4|Translit=hùi|highlight=red
12	。	。	PUNCT	_	_	4	punct	_	Translit=。
{{< / conll_interactive >}}

{{< conll_interactive >}}
# text_en = I don't understand the book.
# translit = Wǒ kàn bu dǒng zhè běn shū.
1	我	我	PRON	_	Person=1	2	subj	_	Gloss=1SG|Tone=3|Translit=wǒ
2	看	看	VERB	_	_	0	root	_	Tone=4|Translit=kàn|highlight=green
3	不	不	ADV	_	Polarity=Neg	4	mod	_	Grammar_Target=Yes|Tone=4|Translit=bù|highlight=blue
4	懂	懂	VERB	_	_	2	comp:res	_	Grammar_Target=Yes|Tone=3|Translit=dǒng|highlight=red
5	这	这	DET	_	_	6	det	_	Tone=4|Translit=zhè
6	本	本	NOUN	_	_	7	clf	_	Gloss=CLF|Tone=3|Translit=běn
7	书	书	NOUN	_	_	2	comp:obj	_	Tone=1|Translit=shū
8	。	。	PUNCT	_	_	2	punct	_	Translit=。
{{< / conll_interactive >}}


## remarks 
It seems, in what we currently annotate comp:res, there are in fact different types of paradigm : 
- 我 打 碎 瓶子 I hit the bottle shatter (or is it 2 actions ?)
- 他 哭 类 了 he cried tired   (reflexif)
- 我 摔 破 了脚 I fall breaking my leg (looks more like compound:svc)
- 我 看 到 了他 (phase compound in UD guidelines)


In french : concomitance
