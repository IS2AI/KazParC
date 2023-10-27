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
- language learning materials, including the SCoRE corpus by <a href = "https://www.torrossa.com/en/resources/an/5000845#page=118">Chujo et al. (2015)</a>
- educational video subtitle collections, such as QED by <a href = "http://www.lrec-conf.org/proceedings/lrec2014/pdf/877_Paper.pdf">Abdelali et al. (2014)</a>
- news items, such as KazNERD (<a href = "https://aclanthology.org/2022.lrec-1.44.pdf">Yeshpanov et al., 2022</a>) and WMT (<a href = "http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf">Tiedemann, 2012</a>)
- <a href = "https://www.ted.com/">TED</a> talks
- <a href = "https://adilet.zan.kz/">governmental and regulatory legal documents from Kazakhstan</a>
- communications from <a href = "https://www.akorda.kz/">the official website of the President of the Republic of Kazakhstan</a>
- <a href = "https://www.un.org/">United Nations</a> publications
- image captions from sources like <a href = "https://arxiv.org/pdf/1405.0312.pdf%090.949.pdf">COCO</a>

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

## Data Collection 📅

<p align = "justify">We started the data collection process in July 2021, and it continued until September 2023. During this period, we collected a vast amount of text materials and their translations.<br><br>
Our team of linguists played a crucial role in ensuring the quality of the data. They carefully reviewed the collected data, screening it for inappropriate content. The next step involved segmenting the data into individual sentences, with each sentence labelled with a source identifier. We also paid close attention to grammar and spelling accuracy and removed any duplicate sentences.<br><br>
Kazakh-Russian <a href = "https://en.wikipedia.org/wiki/Code-switching">code-switching</a> is a common practice in Kazakhstan, so we took steps to maintain uniformity. For sentences containing both Kazakh and Russian words, we initiated a modification process. This process involved translating the Russian elements into Kazakh while preserving the intended meaning of the sentences.</p>

## Data Pre-Processing 🧹

<p align = "justify">We organised the data into language pairs. We then carefully removed any unwanted characters and effectively replaced <a href = "https://en.wikipedia.org/wiki/Homoglyph">homoglyphs</a>.
We also took care of formatting issues by eliminating line breaks (\n) and carriage returns (\r).
We identified and removed duplicate entries, making sure to filter out rows with identical text in both language columns. 
However, to make our corpus more diverse and include a broader range of synonyms for different words and expressions, we decided to keep lines with duplicate text within a single language column.</p>

## Acknowledgements 🙏

<p align = "justify">We wish to convey our deep appreciation to the diligent group of translators whose exceptional contributions have been crucial to the successful realisation of this study. Their tireless efforts to ensure the accuracy and faithful rendition of the source materials have indeed proved invaluable. Our sincerest thanks go to the following esteemed individuals: Aigerim Baidauletova, Aigerim Boranbayeva, Ainagul Akmuldina, Aizhan Seipanova, Askhat Kenzhegulov, Assel Kospabayeva, Assel Mukhanova, Elmira Nikiforova, Gaukhar Rayanova, Gulim Kabidolda, Gulzhanat Abduldinova, Indira Yerkimbekova, Moldir Orazalinova, Saltanat Kemaliyeva, and Venera Spanbayeva.</p>
