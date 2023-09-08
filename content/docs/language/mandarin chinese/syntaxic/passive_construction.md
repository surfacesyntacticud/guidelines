# Passive construction in Mandarin Chinese

“Passive construction”, also known as “passive voice”, is a grammatical structure that shifts the focus from the agent of the action to the recipient. In passive voice, the subject of the sentence becomes the entity affected by the action, while the doer is often omitted or indicated by the passive marker (typically auxiliary verbs) in Madarin Chinese.

Here are the most commun three auxiliary verbs used as the passive voice indicator :
1) 被 (bèi)
2) 叫 (jiào)
3) 让 (ràng)
4) 给 (gěi)

This linguistic construction allows for the emphasis on the result or effect of the action rather than on the performer of the action. The passive voice is frequently employed to convey a sense of objectivity, formality, or to place emphasis on the affected entity.

## How to annotate
The root of the sentence will be the passive marker (the auxiliary verb).

The relation between the auxiliary and the verb is marked comp:aux@pass. The subject of the auxiliary bears the subj@pass feature, and the object of the auxiliary carries the comp:obj@pass feature.

## Structures

### - Subj + 被 + (Doer) + V

{{< conll_interactive >}}
# sent_id = 2586
# text = 我 被 他 骗 了 。
# pinyin = Wǒ bèi tā piàn le.
# text_en = I was deceived by him.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGHF9F1
1	我	我	PRON	_	Person=1	2	subj@pass	_	Gloss=1SG|Tone=3|Translit=wǒ
2	被	被	AUX	_	_	0	root	_	Grammar_Target=Yes|Tone=4|Translit=bèi|highlight=red
3	他	他	PRON	_	Person=3	2	comp:obj@pass	_	Tone=1|Translit=tā
4	骗	骗	VERB	_	_	2	comp:aux@pass	_	Tone=4|Translit=piàn
5	了	了	PART	_	_	2	aspect	_	Gloss=PRF|Tone=5|Translit=le
6	。	。	PUNCT	_	_	2	punct	_	Translit=。
{{< /conll_interactive >}}

{{< conll_interactive >}}
# sent_id = 3018
# text = 我 差点儿 没 被 发现。
# pinyin = Wǒ chàdiǎnr méi bèi fāxiàn.
# text_en = I was almost discovered.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGGOUJB
1	我	我	PRON	_	Person=1	6	subj@pass	_	Gloss=1SG|Tone=3|Translit=wǒ
2	差	差	ADV	_	_	6	mod	_	Grammar_Target=Yes|Tone=4|Translit=chà
3	点	点	ADV	_	_	2	@m	_	Grammar_Target=Yes|Tone=3|Translit=diǎn
4	儿	儿	PART	_	_	3	@m	_	Grammar_Target=Yes|Tone=2|Translit=ér
5	没	没	ADV	_	Polarity=Neg	6	mod	_	Grammar_Target=Yes|Tone=2|Translit=méi
6	被	被	AUX	_	_	0	root	_	Tone=4|Translit=bèi|highlight=red
7	发	发	VERB	_	_	6	comp:aux@pass	_	Tone=1|Translit=fā
8	现	现	NOUN	_	_	7	@m	_	Tone=4|Translit=xiàn
9	。	。	PUNCT	_	_	6	punct	_	Translit=。
{{< /conll_interactive >}}

### - Subj + 叫/让/给 + Doer + V
When the passive marker is "叫", "让" or "给", the doer of the action cannot be omitted.

{{< conll_interactive >}}
# sent_id = 3502
# text = 菜 都 给 你们 吃 完了 吗？
# pinyin = Cài dōu gěi nǐmen chī wán le ma?
# text_en = All the food has been finished off by you guys?
# url = https://resources.allsetlearning.com/chinese/grammar/ASGEZ2HN
1	菜	菜	NOUN	_	_	3	subj@pass	_	Tone=4|Translit=cài
2	都	都	ADV	_	_	3	mod	_	Tone=1|Translit=dū
3	给	给	AUX	_	_	0	root	_	Grammar_Target=Yes|Tone=3|Translit=gěi|highlight=red
4	你	你	PRON	_	Number=Plur|Person=2	3	comp:obj@pass	_	Gloss=2SG|Tone=3|Translit=nǐ
5	们	们	PART	_	Number=Plur|Person=2	4	@m	_	Tone=5|Translit=men
6	吃	吃	VERB	_	_	3	comp:aux@pass	_	Tone=1|Translit=chī
7	完	完	VERB	_	_	6	comp:res	_	Tone=2|Translit=wán
8	了	了	PART	_	_	3	aspect	_	Gloss=PRF|Tone=5|Translit=le
9	吗	吗	PART	_	Mood=Inter	3	discourse	_	Tone=5|Translit=ma
10	？	？	PUNCT	_	_	3	punct	_	Translit=？
{{< /conll_interactive >}}
