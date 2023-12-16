# New Sentence 
In case a sentence is made of two seperated sentence, we encode this as a `parataxis:new` relation between the root of the second sentence to the root of the first sentence. The final punctuation of each sentence is attached to its corresponding root.

{{< conll_interactive >}}
# sent_id = 1718
# structure = Subj. + 都 + Predicate + 了
# text = 我都说了三遍了。别烦我！
# level = B1
# structure_verbose = Expressing "already" with "dou"
# url = https://resources.allsetlearning.com/chinese/grammar/ASGT1CIR
# text_en = I've said it three times already. Leave me alone!
# translit = Wǒ dōu shuō le sān biàn le. Bié fán wǒ!
1	我	我	PRON	_	Person=1	3	subj	_	Gloss=1SG|SpaceAfter=No|Tone=3|Translit=wǒ
2	都	都	ADV	_	_	3	mod	_	Grammar_Target=Yes|SpaceAfter=No|Tone=1|Translit=dū
3	说	说	VERB	_	_	0	root	_	SpaceAfter=No|Tone=1|Translit=shuō
4	了	了	PART	_	_	3	aspect	_	Gloss=PFV|SpaceAfter=No|Tone=5|Translit=le
5	三	三	NUM	_	NumType=Card	6	mod	_	Gloss=three|SpaceAfter=No|Tone=1|Translit=sān
6	遍	遍	NOUN	_	_	3	mod	_	SpaceAfter=No|Tone=4|Translit=biàn
7	了	了	PART	_	_	3	discourse	_	Gloss=PRF|SpaceAfter=No|Tone=5|Translit=le
8	。	。	PUNCT	_	_	3	punct	_	SpaceAfter=No|Translit=。
9	别	别	AUX	_	_	3	parataxis:new	_	SpaceAfter=No|Tone=2|Translit=bié
10	烦	烦	VERB	_	_	9	comp:aux	_	SpaceAfter=No|Tone=2|Translit=fán
11	我	我	PRON	_	Person=1	10	comp:obj	_	Gloss=1SG|SpaceAfter=No|Tone=3|Translit=wǒ
12	！	！	PUNCT	_	_	9	punct	_	SpaceAfter=No|Translit=！
{{< /conll_interactive >}}