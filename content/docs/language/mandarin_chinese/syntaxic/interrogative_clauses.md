# Interrogative Clauses

## Direct Interrogative Clauses
### yes/no questions 
#### Using 吗


By using 吗 (ma) at the end of the sentence, we can turn any sentence in a yes/no question. This form is straightforward and neutral in tone, making it suitable for a wide range of contexts without implying urgency.


{{< conll_interactive >}}
# text_en = Would you like to eat a stuffed steamed bun?
# translit = Nǐ xiǎng chī gè bāozi ma?
1	你	你	PRON	_	Person=2	2	subj	_	Gloss=2SG|Tone=3|Translit=nǐ
2	想	想	AUX	_	_	0	root	_	Tone=3|Translit=xiǎng
3	吃	吃	VERB	_	_	2	comp:aux	_	Tone=1|Translit=chī
4	个	个	NOUN	_	_	5	clf	_	Gloss=CLF|Grammar_Target=Yes|Tone=4|Translit=gè
5	包	包	NOUN	_	_	3	comp:obj	_	Tone=1|Translit=bāo
6	子	子	NOUN	_	_	5	@m	_	Tone=5|Translit=zi
7	吗	吗	PART	_	Mood=Inter	2	discourse	_	Tone=5|Translit=ma|highlight=red
8	？	？	PUNCT	_	_	2	punct	_	Translit=？
{{< / conll_interactive >}}

#### Using the positive/negative/positive pattern VERB/ADJ + 不/没 + VERB/ADJ
For indicating a choice between doing and not doing an action (or being and not being in the case of some adjectives), the positive/negative/positive structure can be used. It emphasizes the dichotomy, almost as if saying "or not" in English. In some contexts, especially when spoken with particular intonations, this form can sound a bit more pressing or urgent, as if seeking an immediate answer or confirmation.

{{< conll_interactive >}}
# text_en = Are they going to come or not?
# translit = Tāmen lái bu lái?
1	他	他	PRON	_	Number=Plur|Person=3	3	subj	_	Tone=1|Translit=tā
2	们	们	PART	_	Number=Plur|Person=3	1	@m	_	Tone=5|Translit=men
3	来	来	VERB	_	_	0	root	_	Grammar_Target=Yes|Tone=2|Translit=lái|highlight=red
4	不	不	ADV	_	Polarity=Neg	5	mod	_	Grammar_Target=Yes|Tone=4|Translit=bù|highlight=blue
5	来	来	VERB	_	_	3	conj	_	Grammar_Target=Yes|Tone=2|Translit=lái|highlight=red
6	？	？	PUNCT	_	_	3	punct	_	Translit=？
{{< / conll_interactive >}}


{{< conll_interactive >}}
# text_en = Does your dad drink alcohol or not?
# translit = Nǐ bàba ​hē bu hējiǔ?
1	你	你	PRON	_	Person=2	2	mod	_	Gloss=2SG|Tone=3|Translit=nǐ
2	爸	爸	NOUN	_	_	4	subj	_	Tone=4|Translit=bà
3	爸	爸	NOUN	_	_	2	conj:redup@m	_	Tone=4|Translit=bà
4	喝	喝	VERB	_	_	0	root	_	Grammar_Target=Yes|Tone=1|Translit=hē|highlight=red
5	不	不	ADV	_	Polarity=Neg	6	mod	_	Grammar_Target=Yes|Tone=4|Translit=bù|highlight=blue
6	喝	喝	VERB	_	_	4	conj	_	Grammar_Target=Yes|Tone=1|Translit=hē|highlight=red
7	酒	酒	NOUN	_	_	4	comp:obj	_	Tone=3|Translit=jǐu
8	？	？	PUNCT	_	_	4	punct	_	Translit=？
{{< / conll_interactive >}}

### Content questions

Content questions in Chinese, similar to "wh-questions" in English, are constructed using specific interrogative pronouns (疑问词 yíwèncí, or also commonly called "questions words"). 

Here are the most common questions words : 
- 什么 (shénme) - What - 你学习什么？
    (Nǐ xuéxí shénme?)
    "What are you studying?"
- 谁 (shuí) - Who - 谁是你的老师？ (Shuí shì nǐ de lǎoshī?) "Who is your teacher?"
- 哪 (nǎ) or 哪儿 (nǎr) - Where: 你住在哪？ (Nǐ zhù zài nǎ?) "Where do you live?"
- 为什么 (wèishénme) - Why: 你为什么迟到？(Nǐ wèishénme chídào?)"Why are you late?"
- 怎么 (zěnme) - How:  你怎么去学校？ (Nǐ zěnme qù xuéxiào?) "How do you go to school?"
- 哪一个 (nǎ yīgè) - Which one: 你喜欢哪一个颜色？ (Nǐ xǐhuān nǎ yīgè yánsè?) "Which color do you like?"
- 多少 (duōshǎo) - How much/How many: 这个苹果多少钱？ (Zhège píngguǒ duōshǎo qián?) "How much is this apple?"
- 什么时候 (shénme shíhòu) - When: 你什么时候来？ (Nǐ shénme shíhòu lái?) "When are you coming?"
- 为何 (wèihé) - Why (a more formal version of 为什么): 他为何离开？ (Tā wèihé líkāi?) "Why did he leave?"
- 怎么样 (zěnmeyàng) - How is it/How about: 这本书怎么样？ (Zhè běn shū zěnmeyàng?) "How is this book?"

### Choices questions with 还是
When you want to present a choice between two or more options in a question, you use the word "还是 (háishì)." It can be likened to the English word "or" when used in questions.

{{< conll_interactive >}}
# text_en = Do you want to eat Chinese food or French food?
# translit = Nǐmen xiǎng chī Zhōngguó cài  háishì Fǎguó cài?
1	你	你	PRON	_	Number=Plur|Person=2	3	subj	_	Gloss=2SG|Tone=3|Translit=nǐ
2	们	们	PART	_	Number=Plur|Person=2	1	@m	_	Tone=5|Translit=men
3	想	想	AUX	_	_	0	root	_	Tone=3|Translit=xiǎng
4	吃	吃	VERB	_	_	3	comp:aux	_	Tone=1|Translit=chī
5	中	中	PROPN	_	_	7	mod	_	Tone=1|Translit=zhōng|highlight=blue
6	国	国	PROPN	_	_	5	@m	_	Tone=2|Translit=guó|highlight=blue
7	菜	菜	NOUN	_	_	4	comp:obj	_	Tone=4|Translit=cài|highlight=blue
8	还	还	CCONJ	_	_	12	cc	_	Grammar_Target=Yes|Tone=2|Translit=huán|highlight=red
9	是	是	CCONJ	_	_	8	@m	_	Grammar_Target=Yes|Tone=4|Translit=shì|highlight=red
10	法	法	PROPN	_	_	12	mod	_	Tone=3|Translit=fǎ|highlight=blue
11	国	国	PROPN	_	_	10	@m	_	Tone=2|Translit=guó|highlight=blue
12	菜	菜	NOUN	_	_	7	conj	_	Tone=4|Translit=cài|highlight=blue
13	？	？	PUNCT	_	_	3	punct	_	Translit=？
{{< / conll_interactive >}}



## Embedded intterogative clauses
Embedded interrogative clauses (also known as embedded or indirect questions) in Chinese function somewhat similarly to their counterparts in English. They are questions that are embedded within another sentence, often introduced by a verb like "know," "wonder," "ask," etc.

In Mandarin Chinese, when transforming direct questions into embedded questions, the word order typically remains the same as in direct questions. However, the question marker "吗" (ma) can be ommited in some embedded structures.


##### Direct Question:
    他在哪里？
    (Tā zài nǎlǐ?)
    "Where is he?"

##### Embedded Questions:

    你知道他在哪里吗？
    (Nǐ zhīdào tā zài nǎlǐ ma?)
    "Do you know where he is?"

    我知道他在哪里。
    (Wǒ zhīdào tā zài nǎlǐ)
    "I know where he is."

{{< conll_interactive >}}
# text_en = Say what you want to say, just don't spill secrets.
# translit = Shuō dōu shuō le, jiù bié shuō zhè shì shénme mìmì le.
1	说	说	VERB	_	_	0	root	_	Tone=1|Translit=shuō
2	都	都	ADV	_	_	3	mod	_	Grammar_Target=Yes|Tone=1|Translit=dū
3	说	说	VERB	_	_	1	parataxis	_	Tone=1|Translit=shuō
4	了	了	PART	_	_	3	discourse	_	Gloss=PRF|Tone=5|Translit=le
5	，	，	PUNCT	_	_	7	punct	_	Translit=，
6	就	就	SCONJ	_	_	7	cc	_	Tone=4|Translit=jìu
7	别	别	AUX	_	_	3	parataxis	_	Tone=2|Translit=bié
8	说	说	VERB	_	_	7	comp:aux	_	Tone=1|Translit=shuō
9	这	这	DET	_	_	10	subj	_	Tone=4|Translit=zhè
10	是	是	AUX	_	_	8	comp:obj	_	Tone=4|Translit=shì
11	什	什	PRON	_	PronType=Int	13	mod	_	Tone=2|Translit=shén|highlight=red
12	么	么	PRON	_	_	11	@m	_	Tone=5|Translit=me|highlight=red
13	秘	秘	NOUN	_	_	10	comp:pred	_	Tone=4|Translit=mì
14	密	密	NOUN	_	_	13	@m	_	Tone=4|Translit=mì
15	了	了	PART	_	_	7	discourse	_	Gloss=PRF|Tone=5|Translit=le
16	。	。	PUNCT	_	_	1	punct	_	Translit=。
{{< /conll_interactive >}}
## Miscallaneous
##### /!\ Expressing "every" with question words + 都/也
When used with 都 (dou) or 也(ye), the questions words take the sense of "every"/"any" (where, thing, people). They then act as indefinite references.
In these cases, we annotated the pronoun as an ADV modifying either the referenced noun (他什么菜都喜欢吃) or the verb is a referenced noun is not in the same close (他什么都喜欢吃).

- "Everyone"/"Anywhere" with 谁 + 都/也
- "Everywhere"/"Anywhere" with 哪儿/哪里/哪一个地方 + 都/也
- "Whenever"/"Anytime" with 什么时候 + 都/也
- "However Much" with 多少 + 都/也
- "However" with 怎么 + 都/也

[Reference to allsetlearning page](https://resources.allsetlearning.com/chinese/grammar/Expressing_%22every%22_with_question_words)


### Questions
- is 干吗 an interogative pronoun ? (eg : 你 老 是 这 么 凶 干 吗 ？ )