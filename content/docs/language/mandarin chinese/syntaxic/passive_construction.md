# Passive construction in Mandarin Chinese

“Passive construction”, also known as “passive voice”, is a grammatical structure that shifts the focus from the agent of the action to the recipient. In passive voice, the subject of the sentence becomes the entity affected by the action, while the doer is often omitted or indicated by the passive marker (typically auxiliary verbs) in Madarin Chinese.

Here are the most commun three auxiliary verbs used as the passive voice indicator :
1) 被 (bèi)
2) 叫 (jiào)
3) 让 (ràng)

This linguistic construction allows for the emphasis on the result or effect of the action rather than on the performer of the action. The passive voice is frequently employed to convey a sense of objectivity, formality, or to place emphasis on the affected entity.

## How to annotate
The root of the sentence will be the passive marker (the auxiliary verb).
The agent of the action will be its object and the recipient will be its subject (@pass).

## Structures

### - Subj + 被 + (Doer) + V

{{< conll_interactive >}}
# sent_id = 2586
# text = 我 被 他 骗 了 。
# pinyin = Wǒ bèi tā piàn le.
# text_en = I was deceived by him.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGHF9F1
1	我	我	PRON	_	Person=1	2	subj	_	_
2	被	被	AUX	_	_	0	root	_	hightlight=red
3	他	他	PRON	_	Person=3	2	comp:obj	_	_
4	骗	骗	VERB	_	_	2	comp:aux	_	_
5	了	了	PART	_	_	2	aspect	_	_
6	。	。	PUNCT	_	_	2	punct	_	_
{{< /conll_interactive >}}

{{< conll_interactive >}}
# sent_id = 3018
# text = 我 差点儿 没 被 发现。
# pinyin = Wǒ chàdiǎnr méi bèi fāxiàn.
# text_en = I was almost discovered.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGGOUJB
1	我	我	PRON	_	Person=1	6	subj	_	_
2	差	差	VERB	ADV	_	6	mod	_	_
3	点	点	NOUN	_	_	2	mod@m	_	_
4	儿	儿	PART	_	_	3	@m	_	_
5	没	没	ADV	_	Polarity=Neg	6	mod	_	_
6	被	被	VERB	_	_	0	root	_	hightlight=red
7	发	发	VERB	_	_	6	comp:obj	_	_
8	现	现	NOUN	_	_	7	@m	_	_
9	。	。	PUNCT	_	_	6	punct	_	_
{{< /conll_interactive >}}

### - Subj + 叫/让 + Doer + V
When the passive marker is "叫" or "让", the doer of the action cannot be omitted.

Example 1 : 衣服让洗衣机洗破了。(Yīfú ràng xǐyījī xǐ pò le.)

English translation :  The clothes were washed by the washing machine and got torn. 

Example 2 : 我的秘密叫他给听见了。(Wǒ de mìmì jiào tā gěi tīngjiàn le.)

English translation : My secret was let be heard by him.