# Part of Speeches

| Short Name                                       | Full Name   | Example in Mandarin                |
|--------------------------------------------------|-------------|-------------------------------------|
| ADJ                                              | Adjective                            | 红 (hóng) 红苹果。                  |
| ADP                                              | Adposition (Preposition)             | 在 (zài) 他在家。                   |
| ADV                                              | Adverb                               | 真 (zhēn) 他真忙。                  |
| [`AUX`]({{< ref "AUX.md" >}})   | Auxiliary                            | 会 (huì) 他会说中文。                |
| CCONJ                                            | Coordinating Conjunction             | 和 (hé) 苹果和香蕉。                 |
| DET                                              | Determiner                           | 这 (zhè) 这是我的书。                |
| INTJ                                             | Interjection                         | 哎呀 (āi yā) 哎呀！我忘了。           |
| NOUN                                             | Noun                                 | 书 (shū) 这是一本书。                |
| NUM                                              | Numeral                              | 三 (sān) 他有三本书。                |
| PART                                             | Particle                             | 的 (de) 我的书。                    |
| PRON                                             | Pronoun                              | 他 (tā) 他是我的朋友。               |
| PROPN                                            | Proper Noun                          | 北京 (Běijīng) 我住在北京。          |
| PUNCT                                            | Punctuation                          | ， (, ) 我喜欢吃苹果，香蕉和葡萄。     |
| SCONJ                                            | Subordinating Conjunction            | 如果 (rúguǒ) 如果你走，我也走。       |
| SYM                                              | Symbol                               | ¥ (yuan) 这本书是¥50。              |
| VERB                                             | Verb                                 | 吃 (chī) 我吃饭。                   |
| X                                                | Other                                | 〇 (líng) 一〇〇一夜                 |

## Current discussion
### 听说 (tingshuo) 
What is the dependency ?
- It can't be a comp:svc as the doer is not the same in both verb (I heard (other people) said)
- It can't be a comp:res as SAY is not the result of LISTEN

It seems to me that it's either a normal comp:obj, or a /m relation. As we can insert a noun or a pronoun between both characters, I (KG) think it's a comp:obj