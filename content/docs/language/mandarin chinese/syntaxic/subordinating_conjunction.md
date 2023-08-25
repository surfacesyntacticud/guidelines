# Subordinating conjunction in Mandarin Chinese

Subordinating conjunction is a conjunction that links two clauses within a sentence, creating a hierarchy where one clause relies on the other. It introduces the dependent clause, which cannot exist independently as a sentence and instead depends on the main clause for meaning. In Madarin Chinese, the subordinating conjunction can mark both the main clause and the subordinate clause. Subordinating conjunction indicates various relationships between the clauses, here are the most commun relations :

1) Cause and effect 
	- 因为...所以 (yīn wèi...suǒ yǐ) - "because"
2) Condition 
	- 如果...就 (rú guǒ...jiù) - "if"
	- 除非...否则 (chú fēi...fǒu zé) - "unless"
3) Concession 
	- 虽然...但是 (suī rán...dàn shì) - "although"
4) Time 
	- 当 (dāng) - "when"
	- 一...就 (yī...jiù) - "as soon as"
5) Purpose
	- 来 (lái) - "so as to" - It is inserted between two verbs to indicate the purpose.
	
In a pair of subordinating conjunction, like 因为...所以 (yīn wèi...suǒ yǐ), either of them can be used independently to indicate the relationship between two clauses.

## How to annotate
The subordinating conjunction of the main clause is the head of the phrase, with a mod relation to the other subordinating conjunction in the subordinate clause.
For SCONJ 来, it is attached by a mod relation with the first verb, and has a comp:obj relation to the second verb. 
VERB1-[mod]->来-[comp:obj]->VERB2

## Structures

### - 但是
{{< conll_interactive >}}
# sent_id = 777
# text = 这 个 地方 很 漂亮，但是 人 太 多 了。
# pinyin = Zhège dìfang hěn piàoliang, dànshì rén tài duō le.
# text_en = This place is beautiful, but there are too many people.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGUD81S
1	这	这	DET	_	_	2	det	_	Tone=4|Translit=zhè
2	个	个	NOUN	_	_	3	clf	_	Gloss=CLF|Tone=4|Translit=gè
3	地	地	NOUN	_	_	6	subj	_	Tone=4|Translit=dì
4	方	方	NOUN	_	_	3	@m	_	Tone=1|Translit=fāng
5	很	很	ADV	_	_	6	mod	_	Tone=3|Translit=hěn
6	漂	漂	ADJ	_	_	9	mod	_	Tone=1|Translit=piāo
7	亮	亮	ADJ	_	_	6	@m	_	Tone=4|Translit=liàng
8	，	，	PUNCT	_	_	9	punct	_	Translit=，
9	但	但	SCONJ	_	_	0	root	highlight=red	Grammar_Target=Yes|Tone=4|Translit=dàn
10	是	是	SCONJ	_	_	9	@m	highlight=red	Grammar_Target=Yes|Tone=4|Translit=shì
11	人	人	NOUN	_	_	13	subj	_	Tone=2|Translit=rén
12	太	太	ADV	_	_	13	mod	_	Tone=4|Translit=tài
13	多	多	ADJ	_	_	9	comp:obj	_	Tone=1|Translit=duō
14	了	了	PART	_	_	13	discourse	_	Gloss=PRF|Tone=5|Translit=le
15	。	。	PUNCT	_	_	9	punct	_	Translit=。
{{< /conll_interactive >}}

The terms "但是" (dànshì), is not invariably categorized as the subordinating conjunction (SCONJ), here is an counter example :
{{< conll_interactive >}}
# sent_id = 20
# text = 我 哥哥 不 高，但是 很 帅。
# pinyin = Wǒ gēge bù gāo , dànshì hěn shuài.
# text_en = My older brother is not tall, but he is very handsome.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGIPYFV
1	我	我	PRON	_	Person=1	2	mod	_	Gloss=1SG|Tone=3|Translit=wǒ
2	哥	哥	NOUN	_	_	5	subj	_	Tone=1|Translit=gē
3	哥	哥	NOUN	_	_	2	conj:redup@m	_	Tone=1|Translit=gē
4	不	不	ADV	_	Polarity=Neg	5	mod	_	Grammar_Target=Yes|Tone=4|Translit=bù
5	高	高	ADJ	_	_	0	root	_	Gloss=tall|Tone=1|Translit=gāo
6	，	，	PUNCT	_	_	10	punct	_	Translit=，
7	但	但	CCONJ	_	_	10	cc	highlight=#3eaa0c	Tone=4|Translit=dàn
8	是	是	CCONJ	_	_	7	@m	highlight=#3eaa0c	Tone=4|Translit=shì
9	很	很	ADV	_	_	10	mod	_	Tone=3|Translit=hěn
10	帅	帅	ADJ	_	_	5	conj	_	Tone=4|Translit=shuài
11	。	。	PUNCT	_	_	5	punct	_	Translit=。
{{< /conll_interactive >}}

When the term doesn't introduce an entire clause but gives supplementary information, it assumes the role of a coordinating conjunction (CCONJ).

### - 如果...就
{{< conll_interactive >}}
# sent_id = 2825
# text = 如果 有 困难 ，就 给 我 打 电话 。
# pinyin = Rúguǒ yǒu kùnnan, jiù gěi wǒ dǎ diànhuà.
# text_en = If there is any difficulty, give me a call.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGGIVT0
1	如	如	SCONJ	_	_	7	mod	highlight=red	Grammar_Target=Yes|Tone=2|Translit=rú
2	果	果	SCONJ	_	_	1	@m	highlight=red	Grammar_Target=Yes|Tone=3|Translit=guǒ
3	有	有	VERB	_	_	1	comp:obj	_	Tone=3|Translit=yǒu
4	困	困	NOUN	_	_	3	comp:obj	_	Tone=4|Translit=kùn
5	难	难	NOUN	_	_	4	@m	_	Tone=2|Translit=nán
6	，	，	PUNCT	_	_	7	punct	_	Translit=，
7	就	就	SCONJ	_	_	0	root	highlight=red	Grammar_Target=Yes|Tone=4|Translit=jìu
8	给	给	ADP	_	_	10	comp:obl	_	Tone=3|Translit=gěi
9	我	我	PRON	_	Person=1	8	comp:obj	_	Gloss=1SG|Tone=3|Translit=wǒ
10	打	打	VERB	_	_	7	comp:obj	_	Tone=3|Translit=dǎ
11	电	电	NOUN	_	_	10	comp:obj	_	Tone=4|Translit=diàn
12	话	话	NOUN	_	_	11	@m	_	Tone=4|Translit=huà
13	。	。	PUNCT	_	_	7	punct	_	Translit=。
{{< /conll_interactive >}}

The word "就" (jiù) takes on different linguistic roles based on its contextual interactions. It functions as a subordinating conjunction when paired with "如果" (rú guǒ), introducing a conditional clause and indicating conditional relationships. In other cases, it serves as an adverbial connector. 
{{< conll_interactive >}}
# sent_id = 1637
# text = 我 就 要 出国 了 。
# pinyin = Wǒ jiù yào chūguó le.
# text_en = I'm about to go abroad.
# url = https://resources.allsetlearning.com/chinese/grammar/ASG9B210
1	我	我	PRON	_	Person=1	3	subj	_	Gloss=1SG|Tone=3|Translit=wǒ
2	就	就	ADV	_	_	3	mod	highlight=#3eaa0c	Grammar_Target=Yes|Tone=4|Translit=jìu
3	要	要	AUX	_	_	0	root	_	Grammar_Target=Yes|Tone=4|Translit=yào
4	出	出	VERB	_	_	3	comp:aux	_	Tone=1|Translit=chū
5	国	国	NOUN	_	_	4	comp:obj	_	Tone=2|Translit=guó
6	了	了	PART	_	_	3	discourse	_	Gloss=PRF|Tone=5|Translit=le
7	。	。	PUNCT	_	_	3	punct	_	Translit=。
{{< /conll_interactive >}}

### - 来
{{< conll_interactive >}}
# sent_id = 2023
# text = 用 这个 APP 来 学 汉字 更 容易 。
# pinyin = Yòng zhège APP lái xué Hànzì gèng róngyì.
# text_en = It's easier to use this app to study Chinese characters.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGBZ578
1	用	用	VERB	_	_	12	subj	_	Tone=4|Translit=yòng
2	这	这	DET	_	_	3	det	_	Tone=4|Translit=zhè
3	个	个	NOUN	_	_	4	clf	_	Gloss=CLF|Tone=4|Translit=gè
4	A	a	PROPN	_	_	1	comp:obj	_	Translit=A
5	P	p	PROPN	_	_	4	flat:foreign@m	_	Translit=P
6	P	p	PROPN	_	_	5	flat:foreign@m	_	Translit=P
7	来	来	SCONJ	_	_	1	mod	highlight=red	Grammar_Target=Yes|Tone=2|Translit=lái
8	学	学	VERB	_	_	7	comp:obj	_	Tone=2|Translit=xué
9	汉	汉	NOUN	_	_	8	comp:obj	_	Tone=4|Translit=hàn
10	字	字	NOUN	_	_	9	@m	_	Tone=4|Translit=zì
11	更	更	ADV	_	_	12	mod	_	Tone=4|Translit=gèng
12	容	容	ADJ	_	_	0	root	_	Tone=2|Translit=róng
13	易	易	ADJ	_	_	12	@m	_	Tone=4|Translit=yì
14	。	。	PUNCT	_	_	12	punct	_	Translit=。
{{< /conll_interactive >}}