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
1	这	这	DET	_	_	2	det	_	_
2	个	个	NOUN	_	_	3	clf	_	_
3	地	地	NOUN	_	_	6	subj	_	_
4	方	方	NOUN	_	_	3	@m	_	_
5	很	很	ADV	_	_	6	mod	_	_
6	漂	漂	ADJ	_	_	9	mod	_	_
7	亮	亮	ADJ	_	_	6	@m	_	_
8	，	，	PUNCT	_	_	9	punct	_	_
9	但	但	SCONJ	_	_	0	root	_	highlight=red
10	是	是	SCONJ	_	_	9	@m	_	highlight=red
11	人	人	NOUN	_	_	13	subj	_	_
12	太	太	ADV	_	_	13	mod	_	_
13	多	多	ADJ	_	_	9	comp:obj	_	_
14	了	了	PART	_	_	13	discourse	_	_
15	。	。	PUNCT	_	_	9	punct	_	_
{{< /conll_interactive >}}

The terms "但是" (dànshì), is not invariably categorized as the subordinating conjunction (SCONJ), here is an counter example :
{{< conll_interactive >}}
# sent_id = 20
# text = 我 哥哥 不 高，但是 很 帅。
# pinyin = Wǒ gēge bù gāo , dànshì hěn shuài.
# text_en = My older brother is not tall, but he is very handsome.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGIPYFV
1	我	我	PRON	_	Person=1	2	mod	_	_
2	哥	哥	NOUN	_	_	5	subj	_	_
3	哥	哥	NOUN	_	_	2	conj:redup@m	_	_
4	不	不	ADV	_	Polarity=Neg	5	mod	_	_
5	高	高	ADJ	_	_	0	root	_	_
6	，	，	PUNCT	_	_	10	punct	_	_
7	但	但	CCONJ	_	_	10	cc	_	highlight=#3eaa0c
8	是	是	CCONJ	_	_	7	@m	_	highlight=#3eaa0c
9	很	很	ADV	_	_	10	mod	_	_
10	帅	帅	ADJ	_	_	5	conj	_	_
11	。	。	PUNCT	_	_	5	punct	_	_
{{< /conll_interactive >}}

When the term doesn't introduce an entire clause but gives supplementary information, it assumes the role of a coordinating conjunction (CCONJ).

### - 如果...就
{{< conll_interactive >}}
# sent_id = 2825
# text = 如果 有 困难 ，就 给 我 打 电话 。
# pinyin = Rúguǒ yǒu kùnnan, jiù gěi wǒ dǎ diànhuà.
# text_en = If there is any difficulty, give me a call.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGGIVT0
1	如	如	SCONJ	_	_	7	mod	_	highlight=red
2	果	果	SCONJ	_	_	1	@m	_	highlight=red
3	有	有	VERB	_	_	1	comp:obj	_	_
4	困	困	NOUN	_	_	3	comp:obj	_	_
5	难	难	NOUN	_	_	4	@m	_	_
6	，	，	PUNCT	_	_	7	punct	_	_
7	就	就	SCONJ	_	_	0	root	_	highlight=red
8	给	给	ADP	_	_	10	comp:obl	_	_
9	我	我	PRON	_	Person=1	8	comp:obj	_	_
10	打	打	VERB	_	_	7	comp:obj	_	_
11	电	电	NOUN	_	_	10	comp:obj	_	_
12	话	话	NOUN	_	_	11	@m	_	_
13	。	。	PUNCT	_	_	7	punct	_	_
{{< /conll_interactive >}}

The word "就" (jiù) takes on different linguistic roles based on its contextual interactions. It functions as a subordinating conjunction when paired with "如果" (rú guǒ), introducing a conditional clause and indicating conditional relationships. In other cases, it serves as an adverbial connector. 
{{< conll_interactive >}}
# sent_id = 1637
# text = 我 就 要 出国 了 。
# pinyin = Wǒ jiù yào chūguó le.
# text_en = I'm about to go abroad.
# url = https://resources.allsetlearning.com/chinese/grammar/ASG9B210
1	我	我	PRON	_	Person=1	3	subj	_	_
2	就	就	ADV	_	_	3	mod	_	highlight=#3eaa0c
3	要	要	AUX	_	_	0	root	_	_
4	出	出	VERB	_	_	3	comp:aux	_	_
5	国	国	NOUN	_	_	4	comp:obj	_	_
6	了	了	PART	_	_	3	discourse	_	_
7	。	。	PUNCT	_	_	3	punct	_	_
{{< /conll_interactive >}}

### - 来
{{< conll_interactive >}}
# sent_id = 2023
# text = 用 这个 APP 来 学 汉字 更 容易 。
# pinyin = Yòng zhège APP lái xué Hànzì gèng róngyì.
# text_en = It's easier to use this app to study Chinese characters.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGBZ578
1	用	用	VERB	_	_	12	subj	_	_
2	这	这	DET	_	_	3	det	_	_
3	个	个	NOUN	_	_	4	clf	_	_
4	A	a	PROPN	_	_	1	comp:obj	_	_
5	P	p	PROPN	_	_	4	flat:foreign@m	_	_
6	P	p	PROPN	_	_	5	flat:foreign@m	_	_
7	来	来	SCONJ	_	_	1	mod	_	highlight=red
8	学	学	VERB	_	_	7	comp:obj	_	_
9	汉	汉	NOUN	_	_	8	comp:obj	_	_
10	字	字	NOUN	_	_	9	@m	_	_
11	更	更	ADV	_	_	12	mod	_	_
12	容	容	ADJ	_	_	0	root	_	_
13	易	易	ADJ	_	_	12	@m	_	_
14	。	。	PUNCT	_	_	12	punct	_	_
{{< /conll_interactive >}}