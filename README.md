<h1 align="center">KazParC</h1>

<p align="center">
  <a href="https://github.com/IS2AI/KazParC/stargazers">
    <img src="https://img.shields.io/github/stars/IS2AI/KazParC.svg?colorA=orange&colorB=orange&logo=github"
         alt="GitHub stars">
  </a>
  <a href="https://github.com/IS2AI/KazParC/issues">
    <img src="https://img.shields.io/github/issues/IS2AI/KazParC.svg"
         alt="GitHub issues">
  </a>
  <a href="https://issai.nu.edu.kz">
    <img src="https://img.shields.io/static/v1?label=ISSAI&amp;message=official site&amp;color=blue&amp"
         alt="ISSAI Official Website">
  </a> 
</p>

<p align = "center">This repository provides a <a href="https://github.com/IS2AI/KazParC/tree/main/dataset">dataset</a> and a neural machine translation model nicknamed <a href="https://github.com/IS2AI/KazParC/tree/main/scripts">Tilmash</a> for the paper <br><a href = "link_to_be_added"><b>KazParC: Kazakh Parallel Corpus for Machine Translation</b></a></p> 

## Domains ℹ️

<p align = "justify">We collected data for our Kazakh Parallel Corpus (referred to as KazParC) from a diverse range of textual sources. These sources include</p> 

- proverbs and sayings
- terminology glossaries
- phrasebooks
- literary works
- periodicals
- language learning materials, including the SCoRE corpus by Chujo et al. (2015)[^1]
- educational video subtitle collections, such as QED by Abdelali et al. (2014)[^2]
- news items, such as KazNERD (Yeshpanov et al., 2022)[^3] and WMT (Tiedemann, 2012)[^4]
- TED talks[^5]
- governmental and regulatory legal documents from Kazakhstan[^6]
- communications from the official website of the President of the Republic of Kazakhstan[^7]
- United Nations publications[^8]
- image captions from sources like COCO[^9]

We categorized the data acquired from these sources into five broad domains:

1. Education and science
2. Fiction
3. General
4. Legal documents
5. Mass media

<table align = "justify">
<thead>
  <tr align = "center">
    <th rowspan="3">Domain</th>
    <th colspan="2">lines</th>
  </tr>
  <tr></tr>
  <tr>
    <th>#</th>
    <th>%</th>
  </tr>
</thead>
<tbody align = "right">
  <tr>
    <td align = "center">Mass media</td>
    <td>120,692</td>
    <td>32</td>
  </tr>
  <tr></tr>
  <tr>
    <td align = "center">General</td>
    <td>95,085</td>
    <td>26</td>
  </tr>
  <tr></tr>
  <tr>
    <td align = "center">Legal documents</td>
    <td>77,186</td>
    <td>21</td>
  </tr>
  <tr></tr>
  <tr>
    <td align = "center">Education and science</td>
    <td>46,269</td>
    <td>12</td>
  </tr>
  <tr></tr>
  <tr>
    <td align = "center">Fiction</td>
    <td>32,932</td>
    <td>9</td>
  </tr>
  <tr></tr>
  <tr>
    <td align = "center"><b>Total</b></td>
    <td><b>372,164</b></td>
    <td><b>100</b></td>
  </tr>
</tbody>
</table>

---

**References:**

[^1]: [SCoRE](https://www.torrossa.com/en/resources/an/5000845#page=118)
[^2]: [QED](http://www.lrec-conf.org/proceedings/lrec2014/pdf/877_Paper.pdf)
[^3]: [KazNERD](https://aclanthology.org/2022.lrec-1.44.pdf)
[^4]: [WMT](http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf)
[^5]: [TED Talks](https://www.ted.com/)
[^6]: [Kazakhstan Legal Documents](https://adilet.zan.kz/)
[^7]: [Official Website of the President of the Republic of Kazakhstan](https://www.akorda.kz/)
[^8]: [United Nations](https://www.un.org/)
[^9]: [COCO](https://arxiv.org/pdf/1405.0312.pdf%090.949.pdf)

## Data Collection 📅

<p align = "justify">We started the data collection process in July 2021, and it continued until September 2023. During this period, we collected a vast amount of text materials and their translations.<br><br>
Our team of linguists played a crucial role in ensuring the quality of the data. They carefully reviewed the collected data, screening it for inappropriate content. The next step involved segmenting the data into individual sentences, with each sentence labelled with a source identifier. We also paid close attention to grammar and spelling accuracy and removed any duplicate sentences.<br><br>
Kazakh-Russian <a href = "https://en.wikipedia.org/wiki/Code-switching">code-switching</a> is a common practice in Kazakhstan, so we took steps to maintain uniformity. For sentences containing both Kazakh and Russian words, we initiated a modification process. This process involved translating the Russian elements into Kazakh while preserving the intended meaning of the sentences.</p>
