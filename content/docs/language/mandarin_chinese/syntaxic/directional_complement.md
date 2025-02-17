# Directional Complement in Mandarin Chinese (comp:dir)

A "directional complement" (known as "directional verb compound” in UD) consists of a series of at least two verbs where the second verb is one of the directional or deitic motion verbs (or a combination of the two) in the below exhaustive list : 

## VERB + A : Directional motion
Eight verbs expressing directional motion:
- 上 (shàng) - "我爬上山" (wǒ pá shàng shān) - "I climb up the mountain"
- 下 (xià) - "他跑下楼" (tā pǎo xià lóu) - "He runs down the stairs"
- 出 (chū) - "我走出房间" (wǒ zǒu chū fángjiān) - "I walk out of the room"
- 进 (jìn) - "我们走进电影院" (wǒmen zǒu jìn diànyǐngyuàn) - "We walk into the movie theater"
- 回 (huí) - "他跑回家" (tā pǎo huí jiā) - "He runs back home"
- 过 (guò) - "他跳过河" (tā tiào guò hé) - "He jumps over the river"
- 开 (kāi) - "她拉开门" (tā lā kāi mén) - "She pulls open the door"
- 起 (qǐ) - "他拿起书" (tā ná qǐ shū) - "He picks up the book"

The main verb is the head of it's directional complement : 
VERB<-[comp:dir]- A

{{< conll_interactive >}}
# text_en = My leg was injured, so I had no choice but to drop out of the competition.
# translit = Wǒ de tuǐ shòushāng le, wǒ bùdébù tuìchū bǐsài.
1	我	我	PRON	_	Person=1	2	comp:obj	_	Gloss=1SG|Tone=3|Translit=wǒ
2	的	的	PART	_	Case=Gen	3	mod	_	Tone=5|Translit=de
3	腿	腿	NOUN	_	_	4	subj	_	Tone=3|Translit=tǔi
4	受	受	VERB	_	_	0	root	_	Tone=4|Translit=shòu
5	伤	伤	NOUN	_	_	4	comp:obj	_	Tone=1|Translit=shāng
6	了	了	PART	_	_	4	discourse	_	Gloss=PRF|Tone=5|Translit=le
7	，	，	PUNCT	_	_	4	punct	_	Translit=，
8	我	我	PRON	_	Person=1	10	subj	_	Gloss=1SG|Tone=3|Translit=wǒ
9	不	不	ADV	_	_	10	@m	_	Grammar_Target=Yes|Tone=4|Translit=bù
10	得	得	AUX	_	_	4	parataxis:new	_	Grammar_Target=Yes|Tone=2|Translit=dé
11	不	不	ADV	_	Polarity=Neg	10	@m	_	Grammar_Target=Yes|Tone=4|Translit=bù
12	退	退	VERB	_	_	10	comp:aux	_	Tone=4|Translit=tùi|highlight=green
13	出	出	VERB	_	_	12	comp:dir	_	Tone=1|Translit=chū|highlight=red
14	比	比	NOUN	_	_	13	comp:obj	_	Tone=3|Translit=bǐ
15	赛	赛	NOUN	_	_	14	@m	_	Tone=4|Translit=sài
16	。	。	PUNCT	_	_	10	punct	_	Translit=。
{{< / conll_interactive >}}


## VERB + B : Diectic motion 
Two verbs expressing deictic motion:
- 来 (lái) - "老师正向我们走来" (Lǎoshī zhèng xiàng wǒmen zǒu lái) - "The teacher is currently walking towards us."
- 去 (qù) - "我天天走路去公司" (Wǒ tiān tiān zǒulù qù gōngsī.) - "I walk to work everyday"

The main verb is the head of it's directional complement : 
VERB<-[comp:dir]- B

{{< conll_interactive >}}

# text_en = The teacher is currently walking towards us.
# translit = Lǎoshī zhèng xiàng wǒmen zǒu lái.
1	老	老	NOUN	_	_	7	subj	_	Tone=3|Translit=lǎo
2	师	师	NOUN	_	_	1	@m	_	Tone=1|Translit=shī
3	正	正	ADV	_	_	7	mod	_	Tone=4|Translit=zhèng
4	向	向	ADP	_	_	7	comp:obl	_	Grammar_Target=Yes|Tone=4|Translit=xiàng
5	我	我	PRON	_	Number=Plur|Person=1	4	comp:obj	_	Gloss=1SG|Tone=3|Translit=wǒ
6	们	们	PART	_	Number=Plur|Person=1	5	@m	_	Tone=5|Translit=men
7	走	走	VERB	_	_	0	root	_	Tone=3|Translit=zǒu|highlight=green
8	来	来	VERB	_	_	7	comp:dir	_	Tone=2|Translit=lái||highlight=blue
9	。	。	PUNCT	_	_	7	punct	_	Translit=。
{{< / conll_interactive >}}


{{< conll_interactive >}}

# text_en = I walk to work everyday
# translit = Wǒ tiān tiān zǒulù qù gōngsī.
1	我	我	PRON	_	Person=1	4	subj	_	Gloss=1SG|Tone=3|Translit=wǒ
2	天	天	NOUN	_	_	4	mod@freq	_	Grammar_Target=Yes|Tone=1|Translit=tiān
3	天	天	NOUN	_	_	2	conj:redup@m	_	Grammar_Target=Yes|Tone=1|Translit=tiān
4	走	走	VERB	_	_	0	root	_	Tone=3|Translit=zǒu|highlight=green
5	路	路	NOUN	_	_	4	comp:obj	_	Tone=4|Translit=lù
6	去	去	VERB	_	_	4	comp:dir	_	Tone=4|Translit=qù|highlight=blue
7	公	公	NOUN	_	_	6	comp:obj	_	Tone=1|Translit=gōng
8	司	司	NOUN	_	_	7	@m	_	Tone=1|Translit=sī
9	。	。	PUNCT	_	_	4	punct	_	Translit=。
{{< / conll_interactive >}}


## VERB + AB : Directional and diectic motion
The combination of directional verbs (上/下/进/出/回/过/开/起) with deictic motion verbs (来/去) can result in more specific expressions of motion or direction. Here are the combinations:
- 上来 (shànglái) - "他把箱子提上来" (tā bǎ xiāngzi tí shànglái) - "He lifts the box up"
- 上去 (shàngqù) - "他爬上去" (tā pá shàngqù) - "He climbs up"
- 下来 (xiàlái) - "他滑下来" (tā huá xiàlái) - "He slides down"
- 下去 (xiàqù) - "我跳下去" (wǒ tiào xiàqù) - "I jump down"
- 进来 (jìnlái) - "请进来" (qǐng jìnlái) - "Please come in"
- 进去 (jìnqù) - "我走进去" (wǒ zǒu jìnqù) - "I walk in"
- 出来 (chūlái) - "他走出来" (tā zǒu chūlái) - "He walks out"
- 出去 (chūqù) - ""我带他们出去" (Wǒ dài tāmen chūqù) - "I take them out"
- 回来 (huílái) - "他会回来" (tā huì huílái) - "He will come back"
- 回去 (huíqù) - "我要回去" (wǒ yào huíqù) - "I need to go back"
- 过来 (guòlái) - "请过来" (qǐng guòlái) - "Please come over"
- 过去 (guòqù) - "我走过去" (wǒ zǒu guòqù) - "I walk over there"
- 开来 (kāilái) - "花儿开来了" (huā er kāilái le) - "The flowers have blossomed" (Note: 开来 in this sense is less common and has a more metaphorical usage)
- 开去 (kāiqù) - Not commonly used, as it doesn't make much sense in most contexts
- 起来 (qǐlái) - "他站起来" (tā zhàn qǐlái) - "He stands up"
- 起去 (qǐqù) - Not commonly used, as it doesn't make much sense in most contexts

This construction is annotated as a comp:dir relation both between the main verb and the directional complement group, and between each element of the directional complement group :
VERB <-[comp:dir]- A <-[comp:dir]- B

{{< conll_interactive >}}

# text_en = Don't let it run out.
# translit = Bùyào ràng tā pǎo chūqù.
1	不	不	ADV	_	_	2	mod	_	Tone=4|Translit=bù
2	要	要	AUX	_	_	0	root	_	Tone=4|Translit=yào
3	让	让	VERB	_	_	2	comp:aux	_	Tone=4|Translit=ràng
4	它	它	NOUN	_	_	3	comp:obj	_	Tone=1|Translit=tā
5	跑	跑	VERB	_	_	3	comp:obj	_	Tone=3|Translit=pǎo|highlight=green
6	出	出	VERB	_	_	5	comp:dir	_	Grammar_Target=Yes|Tone=1|Translit=chū|highlight=red
7	去	去	VERB	_	_	6	comp:dir	_	Grammar_Target=Yes|Tone=4|Translit=qù||highlight=blue
8	。	。	PUNCT	_	_	2	punct	_	Translit=。
{{< / conll_interactive >}}

## A + B
A+B directional construction can occur by itself without complementing a verb (it's in fact the most frequent form of this construction).

{{< conll_interactive >}}
# text_en = May I come in?
# translit = Wǒ kěyǐ jìnlái ma?
1	我	我	PRON	_	Person=1	2	subj	_	Gloss=1SG|Tone=3|Translit=wǒ
2	可	可	AUX	_	_	0	root	_	Grammar_Target=Yes|Tone=3|Translit=kě
3	以	以	AUX	_	_	2	@m	_	Grammar_Target=Yes|Tone=3|Translit=yǐ
4	进	进	VERB	_	_	2	comp:aux	_	Tone=4|Translit=jìn|highlight=red
5	来	来	VERB	_	_	4	comp:dir	_	Tone=2|Translit=lái|highlight=blue
6	吗	吗	PART	_	Mood=Inter	2	discourse	_	Tone=5|Translit=ma
7	？	？	PUNCT	_	_	2	punct	_	Translit=？
{{< / conll_interactive >}}

## Remarks
- You can find a SVC (see [SVC in mandarin](./serial_verbs_construction)) construction at the end of directional complement verbs chain (我出去玩). The head of this word is the last verb of the directional complement verb chain (here 去) and the label is `compound:svc`.

- For V + 出/起 (+ 来), we annotate this as comp:dir. It serves as an (imagé). 

## Other schemas and litterature
### UD : 
See page about compound:dir for mandarin in UD : https://universaldependencies.org/zh/dep/compound-dir.html

### Chinese grammar wiki :
For a more didactic explanation towards language learners, this ressource is really helpful : https://resources.allsetlearning.com/chinese/grammar/Direction_complement


