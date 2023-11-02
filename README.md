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

<p align = "center">This repository provides a <a href="some_cloud_link">dataset</a> and a neural machine translation model nicknamed <a href="https://github.com/IS2AI/KazParC/tree/main/scripts">Tilmash</a> for the paper <br><a href = "link_to_be_added"><b>KazParC: Kazakh Parallel Corpus for Machine Translation</b></a></p> 

<a name = "domains"><h2>Domains ℹ️</h2></a>

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
- communications from the <a href = "https://www.akorda.kz/">official website of the President of the Republic of Kazakhstan</a>
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

<h2>Data Collection 📅</h2>

<p align = "justify">We started the data collection process in July 2021, and it continued until September 2023. During this period, we collected a vast amount of text materials and their translations.<br><br>
Our team of linguists played a crucial role in ensuring the quality of the data. They carefully reviewed the collected data, screening it for inappropriate content. The next step involved segmenting the data into individual sentences, with each sentence labelled with a source identifier. We also paid close attention to grammar and spelling accuracy and removed any duplicate sentences.<br><br>
Kazakh-Russian <a href = "https://en.wikipedia.org/wiki/Code-switching">code-switching</a> is a common practice in Kazakhstan, so we took steps to maintain uniformity. For sentences containing both Kazakh and Russian words, we initiated a modification process. This process involved translating the Russian elements into Kazakh while preserving the intended meaning of the sentences.</p>

<h2>Data Pre-Processing 🧹</h2>


<p align = "justify">We organised the data into language pairs. We then carefully removed any unwanted characters and effectively replaced <a href = "https://en.wikipedia.org/wiki/Homoglyph">homoglyphs</a>.
We also took care of formatting issues by eliminating line breaks (\n) and carriage returns (\r).
We identified and removed duplicate entries, making sure to filter out rows with identical text in both language columns. 
However, to make our corpus more diverse and include a broader range of synonyms for different words and expressions, we decided to keep lines with duplicate text within a single language column.<br><br>
In the table below, you will find statistics regarding the language pairs present in our corpus.
The column labelled '# lines' shows the total number of rows for each language pair. 
In the columns labelled '# sents', '# tokens', and '# types', we provide counts of unique sentences, tokens, and <a href = "https://en.wikipedia.org/wiki/Type%E2%80%93token_distinction">word types</a> for each language pair. For these counts, the upper numbers correspond to the first language in the pair, and the lower numbers correspond to the second language. 
These token and type counts were determined after processing the data using <a href = "https://pypi.org/project/mosestokenizer/">Moses Tokenizer 1.2.1</a>.</p>

<table align = "center">
<thead align = "center">
  <tr>
    <th>Pair</th>
    <th># lines</th>
    <th># sents</th>
    <th># tokens</th>
    <th># types</th>
  </tr>
  <tr></tr>
</thead>
<tbody align = "center">
  <tr>
    <td>KK&harr;EN</td>
    <td>368,347</td>
    <td>362,234<br>361,043</td>
    <td>4,670,823<br>6,393,435</td>
    <td>184,398<br>59,030</td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK&harr;RU</td>
    <td>368,467</td>
    <td>362,234<br>362,529</td>
    <td>4,674,635<br>5,000,429</td>
    <td>184,398<br>182,915</td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK&harr;TR</td>
    <td>366,980</td>
    <td>362,234<br>360,590</td>
    <td>4,667,123<br>4,607,550</td>
    <td>184,398<br>175,621</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN&harr;RU</td>
    <td>368,429</td>
    <td>361,043<br>362,529</td>
    <td>6,397,249<br>4,998,732</td>
    <td>59,030<br>182,915</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN&harr;TR</td>
    <td>366,064</td>
    <td>361,043<br>360,590</td>
    <td>6,352,770<br>4,578,751</td>
    <td>59,030<br>175,621</td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU&harr;TR</td>
    <td>368,545</td>
    <td>362,529<br>360,590</td>
    <td>5,000,364<br>4,615,551</td>
    <td>182,915<br>175,621</td>
  </tr>
</tbody>
</table>

<h2>Data Splitting ✂️</h2>

<p align = "justify">We began by creating a test set. To do this, we employed a random selection process, carefully choosing 250 unique and non-repeating rows from each of the sources outlined in <a href = "#domains">Domains</a>.
The remaining data were divided into pairs, following an 80/20 split, while ensuring that the distribution of domains was maintained within both the training and validation sets.</p>

<table align = "center">
<thead align = "center">
  <tr>
    <th rowspan="3">Pair</th>
    <th colspan="4">Train</th>
    <th colspan="4">Valid</th>
    <th colspan="4">Test</th>
  </tr>
  <tr></tr>
  <tr>
    <th>#<br>lines</th>
    <th>#<br>sents</th>
    <th>#<br>tokens</th>
    <th>#<br>types</th>
    <th>#<br>lines</th>
    <th>#<br>sents</th>
    <th>#<br>tokens</th>
    <th>#<br>types</th>
    <th>#<br>lines</th>
    <th>#<br>sents</th>
    <th>#<br>tokens</th>
    <th>#<br>types</th>
  </tr>
</thead>
<tbody align = "center">
  <tr>
    <td>KK&harr;EN</td>
    <td>290,877</td>
    <td>286,864<br>286,130</td>
    <td>3,690,674<br>5,054,426</td>
    <td>164,986<br>54,321</td>
    <td>72,720 </td>
    <td>72,445 <br>72,385</td>
    <td>923,105<br>1,263,142</td>
    <td>82,915<br>31,840</td>
    <td>4,750</td>
    <td>4,750 <br>4,750</td>
    <td>57,044<br>75,867</td>
    <td>17,483<br>9,722 </td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK&harr;RU</td>
    <td>290,973</td>
    <td>286,961 <br>287,085</td>
    <td>3,697,962<br>3,953,907</td>
    <td>164,943<br>165,618</td>
    <td>72,744 </td>
    <td>72,452<br>72,453</td>
    <td>919,629<br>984,583</td>
    <td>83,173<br>87,698</td>
    <td>4,750</td>
    <td>4,750 <br>4,750</td>
    <td>57,044<br>61,939</td>
    <td>17,483<br>18,801</td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK&harr;TR</td>
    <td>289,784 </td>
    <td>286,715 <br>285,650</td>
    <td>3,691,291<br>3,644,221</td>
    <td>164,744<br>157,820</td>
    <td>72,446</td>
    <td>72,231 <br>72,161</td>
    <td>918,788<br>907,080</td>
    <td>82,799<br>81,201</td>
    <td>4,750</td>
    <td>4,750 <br>4,750</td>
    <td>57,044<br>56,249</td>
    <td>17,483<br>17,399</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN&harr;RU</td>
    <td>290,943 </td>
    <td>286,161 <br>287,137</td>
    <td>5,060,961<br>3,952,614</td>
    <td>54,355<br>165,619</td>
    <td>72,736 </td>
    <td>72,378 <br>72,470</td>
    <td>1,260,421<br>984,179</td>
    <td>31,951<br>87,435</td>
    <td>4,750</td>
    <td>4,750 <br>4,750</td>
    <td>75,867<br>61,939</td>
    <td>9,722<br>18,801</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN&harr;TR</td>
    <td>289,051 </td>
    <td>285,907<br>285,528</td>
    <td>5,024,415<br>3,619,889</td>
    <td>54,271<br>157,806</td>
    <td>72,263 </td>
    <td>72,029 <br>72,009</td>
    <td>1,252,488<br>902,613</td>
    <td>31,830<br>80,908</td>
    <td>4,750</td>
    <td>4,750 <br>4,750</td>
    <td>75,867<br>56,249</td>
    <td>9,722<br>17,399</td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU&harr;TR</td>
    <td>291,036 </td>
    <td>287,123 <br>285,818</td>
    <td>3,956,995<br>3,653,913</td>
    <td>165,396<br>158,004</td>
    <td>72,759</td>
    <td>72,471<br>72,409</td>
    <td>981,430<br>905,389</td>
    <td>87,625<br>81,352</td>
    <td>4,750</td>
    <td>4,750 <br>4,750</td>
    <td>61,939<br>56,249</td>
    <td>18,801<br>17,399</td>
  </tr>
</tbody>
</table>

<h2>Synthetic Corpus 🧪</h2>
<p align = "justify">To make our parallel corpus more extensive and diverse and to explore how well our translation models perform when dealing with a combination of human-translated and machine-translated content, we carried out web crawling to gather a total of 1,797,066 sentences from English-language websites. These sentences were then automatically translated into Kazakh, Russian, and Turkish using the <a href = "https://translate.google.com/">Google Translate</a> service. In the context of our research, we refer to this collection of data as 'SynC' (Synthetic Corpus).</p>

<table align = "center">
<thead  align = "center">
  <tr>
    <th>Pair</th>
    <th>#<br>lines</th>
    <th>#<br>sents</th>
    <th>#<br>tokens</th>
    <th>#<br>types</th>
  </tr>
</thead>
<tr></tr>
<tbody align = "center">
  <tr>
    <td>KK&harr;EN</td>
    <td>1,787,050</td>
    <td>1,782,192<br>1,781,019</td>
    <td>26,630,960<br>35,291,705</td>
    <td>685,135<br>300,556</td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK&harr;RU</td>
    <td>1,787,448</td>
    <td>1,782,192<br>1,777,500</td>
    <td>26,654,195<br>30,241,895</td>
    <td>685,135<br>672,146</td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK&harr;TR</td>
    <td>1,791,425</td>
    <td>1,782,192<br>1,782,257</td>
    <td>26,726,439<br>27,865,860</td>
    <td>685,135<br>656,294</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN&harr;RU</td>
    <td>1,784,513</td>
    <td>1,781,019<br>362,529</td>
    <td>35,244,800<br>30,175,611</td>
    <td>300,556<br>672,146</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN&harr;TR</td>
    <td>1,788,564</td>
    <td>1,781,019<br>1,782,257</td>
    <td>35,344,188<br>27,806,708</td>
    <td>300,556<br>656,294</td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU&harr;TR</td>
    <td>1,788,027</td>
    <td>1,777,500<br>1,782,257</td>
    <td>30,269,083<br>27,816,210</td>
    <td>672,146<br>656,294</td>
  </tr>
</tbody>
</table>

<p align = "justify">We further divided the synthetic corpus into training and validation sets with a 90/10 ratio.</p>

<table align = "center">
<thead align = "center">
  <tr>
    <th rowspan="3">Pair</th>
    <th colspan="4">Train</th>
    <th colspan="4">Valid</th>
  </tr>
  <tr></tr>
  <tr>
    <th># lines</th>
    <th># sents</th>
    <th># tokens</th>
    <th># types</th>
    <th># lines</th>
    <th># sents</th>
    <th># tokens</th>
    <th># types</th>
  </tr>
</thead>
<tr></tr>
<tbody align = "center">
  <tr>
    <td>KK&harr;EN</td>
    <td>1,608,345</td>
    <td>1,604,414<br>1,603,426</td>
    <td>23,970,260<br>31,767,617</td>
    <td>650,144<br>286,372</td>
    <td>178,705</td>
    <td>178,654<br>178,639</td>
    <td>2,660,700<br>3,524,088</td>
    <td>208,838<br>105,517</td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK&harr;RU</td>
    <td>1,608,703</td>
    <td>1,604,468<br>1,600,643</td>
    <td>23,992,148<br>27,221,583</td>
    <td>650,170<br>642,604</td>
    <td>178,745</td>
    <td>178,691<br>178,642</td>
    <td>2,662,047<br>3,020,312</td>
    <td>209,188<br>235,642</td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK&harr;TR</td>
    <td>1,612,282</td>
    <td>1,604,793<br>1,604,822</td>
    <td>24,053,671<br>25,078,688</td>
    <td>650,384<br>626,724</td>
    <td>179,143</td>
    <td>179,057<br>179,057</td>
    <td>2,672,768<br>2,787,172</td>
    <td>209,549<br>221,773</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN&harr;RU</td>
    <td>1,606,061</td>
    <td>1,603,199<br>1,600,372</td>
    <td>31,719,781<br>27,158,101</td>
    <td>286,645<br>642,686</td>
    <td>178,452</td>
    <td>178,419<br>178,379</td>
    <td>3,525,019<br>3,017,510</td>
    <td>104,834<br>235,069</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN&harr;TR</td>
    <td>1,609,707</td>
    <td>1,603,636<br>1,604,545</td>
    <td>31,805,393<br>25,022,782</td>
    <td>286,387<br>626,740</td>
    <td>178,857</td>
    <td>178,775<br>178,796</td>
    <td>3,538,795<br>2,783,926</td>
    <td>105,641<br>221,372</td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU&harr;TR</td>
    <td>1,609,224</td>
    <td>1,600,605<br>1,604,521</td>
    <td>27,243,278<br>25,035,274</td>
    <td>642,797<br>626,587</td>
    <td>178,803</td>
    <td>178,695<br>178,750</td>
    <td>3,025,805<br>2,780,936</td>
    <td>235,970<br>221,792</td>
  </tr>
</tbody>
</table>

<h2>Corpus Structure 🗂️</h2>

<p align = "justify">The <a href="some_cloud_link">corpus</a> is organized into two distinct groups based on their file prefixes. Files "01" through "14" have the "kazparc" prefix, while Files "15" to "27" have the "sync" prefix.</p>

```
├── kazparc
   ├── 01_kazparc_all_entries.csv
   ├── 02_kazparc_train_en_kk.csv
   ├── 03_kazparc_train_en_ru.csv
   ├── 04_kazparc_train_en_tr.csv
   ├── 05_kazparc_train_kk_ru.csv
   ├── 06_kazparc_train_kk_tr.csv
   ├── 07_kazparc_train_ru_tr.csv
   ├── 08_kazparc_valid_en_kk.csv
   ├── 09_kazparc_valid_en_ru.csv
   ├── 10_kazparc_valid_en_tr.csv
   ├── 11_kazparc_valid_kk_ru.csv
   ├── 12_kazparc_valid_kk_tr.csv
   ├── 13_kazparc_valid_ru_tr.csv
   ├── 14_kazparc_test.csv
├── sync
   ├── 15_sync_all_entries.csv
   ├── 16_sync_train_en_kk.csv
   ├── 17_sync_train_en_ru.csv
   ├── 18_sync_train_en_tr.csv
   ├── 19_sync_train_kk_ru.csv
   ├── 20_sync_train_kk_tr.csv
   ├── 21_sync_train_ru_tr.csv
   ├── 22_sync_valid_en_kk.csv
   ├── 23_sync_valid_en_ru.csv
   ├── 24_sync_valid_en_tr.csv
   ├── 25_sync_valid_kk_ru.csv
   ├── 26_sync_valid_kk_tr.csv
   ├── 27_sync_valid_ru_tr.csv
```

<b>KazParC files:</b>
<ul>
<li>File "01" contains the original, unprocessed text data for the four languages considered within KazParC.
<li>Files "02" through "13" represent pre-processed texts divided into language pairs for training (Files "02" to "07") and validation (Files "08" to "13"). Language pairs are indicated within the filenames using two-letter language codes (e.g., en_kk).
<li>File "14" is dedicated to pre-processed texts for use as the test set for the four languages in KazParC.
</ul>

<b>SynC files:</b>
<ul>
<li>File "15" contains raw, unprocessed text data for the four languages.</li>
<li>Files "16" to "27" contain pre-processed text divided into language pairs for training (Files "16" to "21") and validation (Files "22" to "27") purposes.</li>
</ul>

<p align = "justify">In both "01" and "15," each line consists of specific components: a unique line identifier (<tt>id</tt>), texts in Kazakh (<tt>kk</tt>), English (<tt>en</tt>), Russian (<tt>ru</tt>), and Turkish (<tt>tr</tt>), along with accompanying domain information (<tt>domain</tt>). For the other files, the metadata includes <tt>id</tt>, the source language code (e.g., <tt>kk</tt>), the target language code (e.g., <tt>en</tt>), and <tt>domain</tt>.</p>

<h2>Experimental Setup 🔬</h2>

<p align = "justify">In our study, we used Facebook's NLLB model, which supports translation for a wide range of languages, including Kazakh, English, Russian, and Turkish. To assess the performance of the model, we initially tested two versions: the <a href = "https://huggingface.co/facebook/nllb-200-1.3B">baseline</a> and the <a href = "https://huggingface.co/facebook/nllb-200-distilled-1.3B">distilled</a> models. We fine-tuned these versions on KazParC data. After comparing their results, we found that the distilled model consistently outperformed the baseline, though the difference was relatively small, with an improvement of just 0.01 BLEU score. Consequently, we focused our subsequent experiments exclusively on fine-tuning the distilled model.</p>

<p align = "justify">We trained a total of four models:</p>
<ol>
<li>'base', the off-the-shelf model.</li>
<li>'parc', fine-tuned on KazParC data.</li>
<li>'sync', fine-tuned on SynC data.</li>
<li>'parsync', fine-tuned on both KazParC and SynC data.</li>
</ol>

<p align = "justify">We fine-tuned these models using hyperparameters tuned with validation sets. We included synthetic data in the validation sets only when assessing the performance of the 'sync' and 'parsync' models. The best-performing models were then evaluated on the test sets.<br><br>
In addition to the KazParC test set, we used the FLoRes dataset. We merged the <tt>dev</tt> and <tt>devtest</tt> sets from FLoRes into one set for our evaluation. We also explored language pairs, such as German-French, German-Ukrainian, and French-Uzbek, to assess how fine-tuning the model affected translation quality for different language pairs.<br><br>
All the models were fine-tuned using eight GPUs on an NVIDIA DGX A100 machine. We initially set a learning rate of 2 &times; 10<sup>-5</sup> and used the AdaFactor optimization algorithm. The training process spanned three epochs, with both the training and evaluation batch sizes set to 8. In order to start training the model, you need to run the train.py script using the following command:
  
<code>python3 -m torch.distributed.launch --nproc_per_node 8 --nnodes 1 train.py</code>
</p>

<h2>Evaluation Metrics 📏</h2>

<p align = "justify">In our evaluation of machine translation models, we used two widely recognised metrics:</p> 
<ol>
<li>BLEU, based on precision in 4-grams, measures how closely machine-produced translations match human references.</li>
<li>chrF evaluates translation quality by considering character n-grams, making it well-suited for languages with complex morphologies (e.g., Kazakh and Turkish). chrF calculates the harmonic mean of character-based precision and recall, offering a robust evaluation of translation performance.</li>
</ol>
Both BLEU and chrF scores range from 0 to 1, where higher scores indicate better translation quality.


<h2>Experiment Results 📈</h2>

<p align = "justify">We translated the test dataset using the <code>translating_testset.py</code> script. To obtain the BLEU and ChrF metrics we used <code>Evaluation.ipynb</code>. Below are the results we obtained from evaluating the Tilmash model on the KazParC and FLoRes test datasets.</p>

<table align = "center">
<thead align = "center">
  <tr>
    <th rowspan="3">Pair</th>
    <th colspan="6">FLoRes Test Set</th>
  </tr>
  <tr></tr>
  <tr>
    <th>base</th>
    <th>parc</th>
    <th>sync</th>
    <th>parsync</th>
    <th>Yandex</th>
    <th>Google</th>
  </tr>
</thead>
<tbody align = "center">
  <tr>
    <td>EN↔KK</td>
    <td>0.11 | 0.49</td>
    <td>0.14 | 0.56</td>
    <td><b>0.20</b> | <b>0.60</b></td>
    <td><b>0.20</b> | <b>0.60</b></td>
    <td>0.18 | 0.58</td>
    <td><b>0.20</b> | <b>0.60</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN↔RU</td>
    <td>0.25 | 0.56</td>
    <td>0.26 | 0.58</td>
    <td>0.28 | 0.60</td>
    <td>0.28 | 0.60</td>
    <td><b>0.32</b> | <b>0.63</b></td>
    <td>0.31 | 0.62</td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN↔TR</td>
    <td>0.19 | 0.58</td>
    <td>0.22 | 0.61</td>
    <td>0.27 | 0.65</td>
    <td>0.27 | 0.65</td>
    <td>0.29 | <b>0.66</b></td>
    <td><b>0.30</b> | <b>0.66</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK↔EN</td>
    <td>0.28 | 0.59</td>
    <td>0.32 | 0.62</td>
    <td>0.31 | 0.62</td>
    <td>0.32 | 0.63</td>
    <td>0.30 | 0.62</td>
    <td><b>0.36</b> | <b>0.65</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK↔RU</td>
    <td>0.15 | 0.49</td>
    <td>0.17 | 0.51</td>
    <td>0.18 | 0.52</td>
    <td>0.18 | 0.52</td>
    <td>0.18 | 0.52</td>
    <td><b>0.20</b> | <b>0.53</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK↔TR</td>
    <td>0.09 | 0.48</td>
    <td>0.13 | 0.52</td>
    <td>0.14 | 0.54</td>
    <td>0.14 | 0.54</td>
    <td>0.12 | 0.52</td>
    <td><b>0.17</b> | <b>0.56</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU↔EN</td>
    <td>0.31 | 0.62</td>
    <td>0.32 | 0.63</td>
    <td>0.32 | 0.63</td>
    <td>0.32 | 0.63</td>
    <td>0.33 | 0.64</td>
    <td><b>0.35</b> | <b>0.65</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU↔KK</td>
    <td>0.08 | 0.49</td>
    <td>0.10 | 0.52</td>
    <td><b>0.13</b> | 0.53</td>
    <td><b>0.13</b> | <b>0.54</b></td>
    <td>0.12 | <b>0.54</b></td>
    <td><b>0.13</b> | <b>0.54</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU↔TR</td>
    <td>0.10 | 0.49</td>
    <td>0.12 | 0.52</td>
    <td>0.14 | 0.54</td>
    <td>0.14 | 0.54</td>
    <td>0.13 | 0.54</td>
    <td><b>0.17</b> | <b>0.56</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>TR↔EN</td>
    <td>0.34 | 0.64</td>
    <td>0.35 | 0.65</td>
    <td>0.36 | 0.66</td>
    <td>0.36 | 0.66</td>
    <td>0.38 | <b>0.67</b></td>
    <td><b>0.39</b> | <b>0.67</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>TR↔KK</td>
    <td>0.07 | 0.45</td>
    <td>0.10 | 0.51</td>
    <td><b>0.13</b> | <b>0.54</b></td>
    <td><b>0.13</b> | <b>0.54</b></td>
    <td>0.12 | 0.53</td>
    <td><b>0.13</b> | <b>0.54</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>TR↔RU</td>
    <td>0.15 | 0.48</td>
    <td>0.17 | 0.51</td>
    <td>0.18 | 0.52</td>
    <td>0.19 | 0.53</td>
    <td>0.20 | <b>0.54</b></td>
    <td><b>0.21</b> | <b>0.54</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td><b>Average</b></td>
    <td>0.18 | 0.53</td>
    <td>0.20 | 0.56</td>
    <td>0.22 | 0.58</td>
    <td>0.22 | 0.58</td>
    <td>0.23 | 0.58</td>
    <td><b>0.25</b> | <b>0.59</b></td>
  </tr>
</tbody>
</table>
<p align = "center">BLEU | chrF scores for models on the FLoRes test</p>

<table align = "center">
<thead align = "center">
  <tr>
    <th rowspan="3">Pair</th>
    <th colspan="6">KazParC Test Set</th>
  </tr>
  <tr></tr>
  <tr>
    <th>base</th>
    <th>parc</th>
    <th>sync</th>
    <th>parsync</th>
    <th>Yandex</th>
    <th>Google</th>
  </tr>
</thead>
<tbody align = "center">
  <tr>
    <td>EN↔KK</td>
    <td>0.12 | 0.51</td>
    <td>0.18 | 0.58</td>
    <td>0.18 | 0.58</td>
    <td>0.21 | 0.60</td>
    <td>0.18 | 0.58</td>
    <td><b>0.30</b> | <b>0.65</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN↔RU</td>
    <td>0.31 | 0.64</td>
    <td>0.38 | 0.68</td>
    <td>0.35 | 0.66</td>
    <td>0.38 | 0.68</td>
    <td>0.39 | 0.70</td>
    <td><b>0.41</b> | <b>0.71</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>EN↔TR</td>
    <td>0.19 | 0.59</td>
    <td>0.22 | 0.62</td>
    <td>0.25 | 0.63</td>
    <td>0.25 | 0.64</td>
    <td>0.27 | 0.64</td>
    <td><b>0.34</b> | <b>0.68</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK↔EN</td>
    <td>0.24 | 0.55</td>
    <td><b>0.33</b> | <b>0.62</b></td>
    <td>0.24 | 0.57</td>
    <td>0.32 | <b>0.62</b></td>
    <td>0.28 | 0.60</td>
    <td>0.31 | <b>0.62</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK↔RU</td>
    <td>0.22 | 0.56</td>
    <td><b>0.29</b> | <b>0.63</b></td>
    <td>0.24 | 0.59</td>
    <td><b>0.29</b> | <b>0.63</b></td>
    <td><b>0.29</b> | <b>0.63</b></td>
    <td><b>0.29</b> | 0.61</td>
  </tr>
  <tr></tr>
  <tr>
    <td>KK↔TR</td>
    <td>0.10 | 0.47</td>
    <td>0.15 | 0.54</td>
    <td>0.14 | 0.52</td>
    <td>0.16 | 0.55</td>
    <td>0.13 | 0.52</td>
    <td><b>0.23</b> | <b>0.59</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU↔EN</td>
    <td>0.34 | 0.63</td>
    <td><b>0.43</b> | <b>0.71</b></td>
    <td>0.34 | 0.65</td>
    <td>0.42 | 0.70</td>
    <td><b>0.43</b> | <b>0.71</b></td>
    <td>0.42 | <b>0.71</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU↔KK</td>
    <td>0.15 | 0.55</td>
    <td>0.21 | 0.61</td>
    <td>0.18 | 0.58</td>
    <td>0.22 | <b>0.62</b></td>
    <td>0.23 | <b>0.62</b></td>
    <td><b>0.24</b> | <b>0.62</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>RU↔TR</td>
    <td>0.11 | 0.49</td>
    <td>0.16 | 0.56</td>
    <td>0.16 | 0.55</td>
    <td>0.18 | 0.57</td>
    <td>0.16 | 0.55</td>
    <td><b>0.22</b> | <b>0.60</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>TR↔EN</td>
    <td>0.31 | 0.61</td>
    <td><b>0.38</b> | <b>0.67</b></td>
    <td>0.32 | 0.63</td>
    <td><b>0.38</b> | 0.66</td>
    <td>0.36 | 0.66</td>
    <td>0.37 | 0.66</td>
  </tr>
  <tr></tr>
  <tr>
    <td>TR↔KK</td>
    <td>0.08 | 0.46</td>
    <td>0.14 | 0.53</td>
    <td>0.14 | 0.52</td>
    <td>0.16 | 0.55</td>
    <td>0.14 | 0.53</td>
    <td><b>0.19</b> | <b>0.57</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td>TR↔RU</td>
    <td>0.17 | 0.50</td>
    <td>0.23 | 0.56</td>
    <td>0.20 | 0.54</td>
    <td>0.24 | 0.57</td>
    <td>0.23 | 0.57</td>
    <td><b>0.26</b> | <b>0.58</b></td>
  </tr>
  <tr></tr>
  <tr>
    <td><b>Average</b></td>
    <td>0.20 | 0.55</td>
    <td>0.27 | 0.61</td>
    <td>0.23 | 0.59</td>
    <td>0.27 | 0.62</td>
    <td>0.26 | 0.61</td>
    <td><b>0.30</b> | <b>0.63</b></td>
  </tr>
</tbody>
</table>
<p align = "center">BLEU | chrF scores for models on the KazParC test</p>

<p align = "justify">After a comprehensive analysis of both qualitative and quantitative outcomes, we have found that the 'parsync' model, which was fine-tuned on a mix of the KazParC corpus and synthetic data, emerged as the top-performing model. Let us simply call this model <i>Tilmash</i>, a Kazakh term that means 'interpreter' or 'translator'.</p>

<table align = "center">
<thead align = "center">
  <tr>
    <th rowspan="3">Pair</th>
    <th colspan="2">BLEU</th>
    <th colspan="2">chrF</th>
  </tr>
  <tr></tr>
  <tr>
    <th>base</th>
    <th>Tilmash</th>
    <th>base</th>
    <th>Tilmash</th>
  </tr>
</thead>
<tbody align = "center">
  <tr>
    <td>DE&rarr;FR</td>
    <td>0.33</td>
    <td>0.28</td>
    <td>0.61</td>
    <td>0.58</td>
  </tr>
  <tr></tr>
  <tr>
    <td>FR&rarr;DE</td>
    <td>0.22</td>
    <td>0.19</td>
    <td>0.55</td>
    <td>0.53</td>
  </tr>
  <tr></tr>
  <tr>
    <td>DE&rarr;UK</td>
    <td>0.15</td>
    <td>0.04</td>
    <td>0.49</td>
    <td>0.36</td>
  </tr>
  <tr></tr>
  <tr>
    <td>UK&rarr;DE</td>
    <td>0.19</td>
    <td>0.16</td>
    <td>0.53</td>
    <td>0.50</td>
  </tr>
  <tr></tr>
  <tr>
    <td>FR&rarr;UZ</td>
    <td>0.06</td>
    <td>0.02</td>
    <td>0.48</td>
    <td>0.31</td>
  </tr>
  <tr></tr>
  <tr>
    <td>UZ&rarr;FR</td>
    <td>0.25</td>
    <td>0.22</td>
    <td>0.56</td>
    <td>0.53</td>
  </tr>
</tbody>
</table>
<p align = "center">Results of the base and Tilmash models on the control language pairs on the FLoRes test set</p>

<table align = "center">
<thead align = "center">
  <tr>
    <th>Pair</th>
    <th>Type</th>
    <th>Text</th>
    <th>BLEU</th>
    <th>chrF</th>
  </tr>
<tr></tr>
</thead>
<tbody align = "center">
  <tr>
    <td rowspan="9">KK&rarr;EN</td>
    <td>source</td>
    <td align = "left", colspan="3"><i>Ыстық және желді.<br>ystyq jane jeldi.</i></td>
  </tr>
  <tr></tr>
  <tr>
    <td>reference</td>
    <td align = "left"><i>It is hot and windy.</td>
    <td>1.00</td>
    <td>1.00</td>
  </tr>
  <tr></tr>
  <tr>
    <td>Tilmash</td>
    <td align = "left"><i>It's hot and windy.</td>
    <td>0.55</td>
    <td>0.81</td>
  </tr>
  <tr></tr>
  <tr>
    <td>Yandex</td>
    <td align = "left"><i>Hot and windy.</td>
    <td>0.00</td>
    <td>0.66</td>
  </tr>
  <tr></tr>
  <tr>
    <td>Google</td>
    <td align = "left"><i>Hot and windy.</td>
    <td>0.00</td>
    <td>0.66</td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="9">KK&rarr;EN</td>
    <td>source</td>
    <td align = "left", colspan="3"><i>1 қыркүйекте бесінші ана өлімі тіркелді.<br>1 qyrkuiekte besinshi ana olimi tirkeldi.</i></td>
  </tr>
  <tr></tr>
  <tr>
    <td>reference</td>
    <td align = "left"><i>On September 1, the fifth maternal death was registered.</td>
    <td>1.00</td>
    <td>1.00</td>
  </tr>
  <tr></tr>
  <tr>
    <td>Tilmash</td>
    <td align = "left"><i>A fifth maternal death was recorded on 1 September.</td>
    <td>0.27</td>
    <td>0.63</td>
  </tr>
  <tr></tr>
  <tr>
    <td>Yandex</td>
    <td align = "left"><i>On September 1, the fifth maternal death was registered.</td>
    <td>1.00</td>
    <td>1.00</td>
  </tr>
  <tr></tr>
  <tr>
    <td>Google</td>
    <td align = "left"><i>On September 1, the fifth maternal death was recorded.</td>
    <td>0.81</td>
    <td>0.86</td>
  </tr>
</tbody>
</table>
<p align = "center">A selection of translation outputs from Tilmash, Yandex, and Google</p>

<p align = "justify">Below are the detailed tables of Tilmash, Yandex, and Google results per domain.</p>

<table align = "center">
<thead align = "center">
  <tr>
    <th colspan="8">EDUCATION AND SCIENCE</th>
  </tr>
<tr></tr>
</thead>
<tbody align = "center">
  <tr>
    <td rowspan="3"><b>Pair</b></td>
    <td colspan="2"><b>Tilmash</b></td>
    <td colspan="2"><b>Yandex</b></td>
    <td colspan="2"><b>Google</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→KK</td>
    <td>0.23</td>
    <td>0.63</td>
    <td>0.19</td>
    <td>0.61</td>
    <td><b>0.44</b></td>
    <td><b>0.73</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→RU</td>
    <td>0.39</td>
    <td>0.74</td>
    <td>0.39</td>
    <td>0.76</td>
    <td><b>0.43</b></td>
    <td><b>0.78</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→TR</td>
    <td>0.33</td>
    <td>0.71</td>
    <td>0.37</td>
    <td>0.74</td>
    <td><b>0.47</b></td>
    <td><b>0.79</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→EN</td>
    <td>0.28</td>
    <td>0.64</td>
    <td>0.27</td>
    <td>0.63</td>
    <td><b>0.32</b></td>
    <td><b>0.66</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→RU</td>
    <td>0.26</td>
    <td><b>0.66</b></td>
    <td>0.26</td>
    <td><b>0.66</b></td>
    <td><b>0.32</b></td>
    <td><b>0.66</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→TR</td>
    <td>0.20</td>
    <td>0.60</td>
    <td>0.15</td>
    <td>0.57</td>
    <td><b>0.29</b></td>
    <td><b>0.66</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→EN</td>
    <td>0.38</td>
    <td>0.73</td>
    <td><b>0.40</b></td>
    <td>0.75</td>
    <td><b>0.40</b></td>
    <td><b>0.76</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→KK</td>
    <td>0.21</td>
    <td>0.64</td>
    <td>0.22</td>
    <td>0.65</td>
    <td><b>0.30</b></td>
    <td><b>0.67</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→TR</td>
    <td>0.24</td>
    <td>0.65</td>
    <td>0.22</td>
    <td>0.65</td>
    <td><b>0.33</b></td>
    <td><b>0.70</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→EN</td>
    <td>0.38</td>
    <td>0.70</td>
    <td>0.38</td>
    <td>0.70</td>
    <td><b>0.40</b></td>
    <td><b>0.71</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→KK</td>
    <td>0.19</td>
    <td>0.58</td>
    <td>0.17</td>
    <td>0.56</td>
    <td><b>0.29</b></td>
    <td><b>0.64</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→RU</td>
    <td>0.27</td>
    <td>0.63</td>
    <td>0.29</td>
    <td>0.65</td>
    <td><b>0.33</b></td>
    <td><b>0.68</b></td>
  </tr>
</tbody>
</table>

<table align = "center">
<thead align = "center">
  <tr>
    <th colspan="8">FICTION</th>
  </tr>
<tr></tr>
</thead>
<tbody align = "center">
  <tr>
    <td rowspan="3"><b>Pair</b></td>
    <td colspan="2"><b>Tilmash</b></td>
    <td colspan="2"><b>Yandex</b></td>
    <td colspan="2"><b>Google</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→KK</td>
    <td>0.13</td>
    <td>0.51</td>
    <td>0.15</td>
    <td>0.52</td>
    <td><b>0.19</b></td>
    <td><b>0.53</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→RU</td>
    <td>0.35</td>
    <td>0.64</td>
    <td>0.34</td>
    <td><b>0.66</b></td>
    <td><b>0.37</b></td>
    <td><b>0.66</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→TR</td>
    <td>0.28</td>
    <td>0.62</td>
    <td>0.29</td>
    <td>0.63</td>
    <td><b>0.53</b></td>
    <td><b>0.74</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→EN</td>
    <td><b>0.29</b></td>
    <td>0.57</td>
    <td>0.24</td>
    <td>0.54</td>
    <td><b>0.29</b></td>
    <td><b>0.58</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→RU</td>
    <td><b>0.25</b></td>
    <td>0.58</td>
    <td>0.23</td>
    <td>0.55</td>
    <td><b>0.25</b></td>
    <td>0.57</td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→TR</td>
    <td>0.26</td>
    <td>0.62</td>
    <td>0.18</td>
    <td>0.56</td>
    <td><b>0.50</b></td>
    <td><b>0.77</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→EN</td>
    <td>0.40</td>
    <td>0.66</td>
    <td>0.41</td>
    <td>0.67</td>
    <td><b>0.42</b></td>
    <td><b>0.68</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→KK</td>
    <td>0.17</td>
    <td>0.55</td>
    <td><b>0.19</b></td>
    <td><b>0.56</b></td>
    <td>0.16</td>
    <td>0.55</td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→TR</td>
    <td>0.22</td>
    <td>0.59</td>
    <td>0.17</td>
    <td>0.55</td>
    <td><b>0.36</b></td>
    <td><b>0.67</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→EN</td>
    <td>0.36</td>
    <td>0.63</td>
    <td>0.35</td>
    <td>0.62</td>
    <td><b>0.37</b></td>
    <td><b>0.64</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→KK</td>
    <td>0.15</td>
    <td>0.55</td>
    <td>0.16</td>
    <td>0.55</td>
    <td><b>0.19</b></td>
    <td><b>0.58</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→RU</td>
    <td>0.24</td>
    <td>0.56</td>
    <td>0.24</td>
    <td>0.56</td>
    <td><b>0.26</b></td>
    <td><b>0.58</b></td>
  </tr>
</tbody>
</table>

<table align = "center">
<thead align = "center">
  <tr>
    <th colspan="8">GENERAL</th>
  </tr>
<tr></tr>
</thead>
<tbody align = "center">
  <tr>
    <td rowspan="3"><b>Pair</b></td>
    <td colspan="2"><b>Tilmash</b></td>
    <td colspan="2"><b>Yandex</b></td>
    <td colspan="2"><b>Google</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→KK</td>
    <td>0.26</td>
    <td>0.68</td>
    <td>0.17</td>
    <td>0.62</td>
    <td><b>0.45</b></td>
    <td><b>0.77</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→RU</td>
    <td>0.46</td>
    <td>0.76</td>
    <td>0.44</td>
    <td>0.77</td>
    <td><b>0.48</b></td>
    <td><b>0.79</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→TR</td>
    <td><b>0.12</b></td>
    <td>0.54</td>
    <td><b>0.12</b></td>
    <td>0.54</td>
    <td><b>0.12</b></td>
    <td><b>0.55</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→EN</td>
    <td><b>0.39</b></td>
    <td><b>0.68</b></td>
    <td>0.29</td>
    <td>0.64</td>
    <td>0.33</td>
    <td>0.65</td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→RU</td>
    <td><b>0.32</b></td>
    <td><b>0.68</b></td>
    <td>0.29</td>
    <td>0.66</td>
    <td>0.30</td>
    <td>0.66</td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→TR</td>
    <td>0.10</td>
    <td><b>0.52</b></td>
    <td>0.08</td>
    <td>0.47</td>
    <td><b>0.11</b></td>
    <td>0.51</td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→EN</td>
    <td><b>0.45</b></td>
    <td><b>0.74</b></td>
    <td>0.39</td>
    <td>0.71</td>
    <td>0.38</td>
    <td>0.70</td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→KK</td>
    <td><b>0.22</b></td>
    <td><b>0.66</b></td>
    <td>0.18</td>
    <td>0.63</td>
    <td><b>0.22</b></td>
    <td>0.65</td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→TR</td>
    <td><b>0.11</b></td>
    <td><b>0.52</b></td>
    <td>0.09</td>
    <td>0.49</td>
    <td>0.09</td>
    <td>0.51</td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→EN</td>
    <td><b>0.32</b></td>
    <td><b>0.62</b></td>
    <td>0.27</td>
    <td>0.59</td>
    <td>0.28</td>
    <td>0.60</td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→KK</td>
    <td>0.14</td>
    <td>0.55</td>
    <td>0.10</td>
    <td>0.50</td>
    <td><b>0.16</b></td>
    <td><b>0.56</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→RU</td>
    <td><b>0.22</b></td>
    <td>0.57</td>
    <td>0.18</td>
    <td>0.57</td>
    <td>0.21</td>
    <td><b>0.58</b></td>
  </tr>
</tbody>
</table>

<table align = "center">
<thead align = "center">
  <tr>
    <th colspan="8">LEGAL DOCUMENTS</th>
  </tr>
<tr></tr>
</thead>
<tbody align = "center">
  <tr>
    <td rowspan="3"><b>Pair</b></td>
    <td colspan="2"><b>Tilmash</b></td>
    <td colspan="2"><b>Yandex</b></td>
    <td colspan="2"><b>Google</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→KK</td>
    <td>0.27</td>
    <td>0.67</td>
    <td>0.28</td>
    <td>0.67</td>
    <td><b>0.29</b></td>
    <td><b>0.68</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→RU</td>
    <td><b>0.48</b></td>
    <td>0.75</td>
    <td>0.46</td>
    <td><b>0.76</b></td>
    <td>0.47</td>
    <td><b>0.76</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→TR</td>
    <td>0.22</td>
    <td><b>0.64</b></td>
    <td>0.23</td>
    <td><b>0.64</b></td>
    <td><b>0.25</b></td>
    <td>0.55</td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→EN</td>
    <td><b>0.41</b></td>
    <td><b>0.69</b></td>
    <td>0.34</td>
    <td>0.65</td>
    <td>0.36</td>
    <td>0.66</td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→RU</td>
    <td><b>0.47</b></td>
    <td><b>0.77</b></td>
    <td>0.45</td>
    <td>0.76</td>
    <td>0.38</td>
    <td>0.71</td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→TR</td>
    <td>0.11</td>
    <td><b>0.54</b></td>
    <td>0.11</td>
    <td>0.53</td>
    <td><b>0.13</b></td>
    <td><b>0.54</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→EN</td>
    <td><b>0.52</b></td>
    <td><b>0.76</b></td>
    <td><b>0.52</b></td>
    <td><b>0.76</b></td>
    <td>0.51</td>
    <td><b>0.76</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→KK</td>
    <td>0.37</td>
    <td>0.74</td>
    <td><b>0.38</b></td>
    <td><b>0.75</b></td>
    <td>0.33</td>
    <td>0.71</td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→TR</td>
    <td>0.14</td>
    <td>0.57</td>
    <td>0.13</td>
    <td>0.56</td>
    <td><b>0.15</b></td>
    <td><b>0.58</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→EN</td>
    <td><b>0.46</b></td>
    <td><b>0.72</b></td>
    <td>0.39</td>
    <td>0.69</td>
    <td>0.43</td>
    <td>0.70</td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→KK</td>
    <td><b>0.18</b></td>
    <td><b>0.58</b></td>
    <td>0.15</td>
    <td>0.56</td>
    <td><b>0.18</b></td>
    <td><b>0.58</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→RU</td>
    <td><b>0.29</b></td>
    <td><b>0.63</b></td>
    <td>0.22</td>
    <td>0.59</td>
    <td>0.27</td>
    <td>0.61</td>
  </tr>
</tbody>
</table>

<table align = "center">
<thead align = "center">
  <tr>
    <th colspan="8">MASS MEDIA</th>
  </tr>
<tr></tr>
</thead>
<tbody align = "center">
  <tr>
    <td rowspan="3"><b>Pair</b></td>
    <td colspan="2"><b>Tilmash</b></td>
    <td colspan="2"><b>Yandex</b></td>
    <td colspan="2"><b>Google</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
    <td><b>BLEU</b></td>
    <td><b>chrF</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→KK</td>
    <td>0.18</td>
    <td>0.58</td>
    <td>0.17</td>
    <td>0.58</td>
    <td><b>0.19</b></td>
    <td><b>0.59</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→RU</td>
    <td>0.35</td>
    <td>0.67</td>
    <td>0.38</td>
    <td><b>0.70</b></td>
    <td><b>0.40</b></td>
    <td><b>0.70</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>EN→TR</td>
    <td>0.30</td>
    <td>0.66</td>
    <td>0.31</td>
    <td>0.67</td>
    <td><b>0.41</b></td>
    <td><b>0.72</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→EN</td>
    <td>0.32</td>
    <td><b>0.62</b></td>
    <td>0.32</td>
    <td><b>0.62</b></td>
    <td><b>0.33</b></td>
    <td><b>0.62</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→RU</td>
    <td>0.27</td>
    <td>0.61</td>
    <td><b>0.29</b></td>
    <td><b>0.62</b></td>
    <td>0.26</td>
    <td>0.59</td>
 </tr>
  <tr></tr>
  <tr>
    <td>KK→TR</td>
    <td>0.18</td>
    <td>0.57</td>
    <td>0.16</td>
    <td>0.55</td>
    <td><b>0.26</b></td>
    <td><b>0.62</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→EN</td>
    <td>0.48</td>
    <td>0.73</td>
    <td><b>0.53</b></td>
    <td><b>0.76</b></td>
    <td>0.50</td>
    <td>0.74</td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→KK</td>
    <td>0.21</td>
    <td>0.60</td>
    <td><b>0.22</b></td>
    <td><b>0.62</b></td>
    <td>0.20</td>
    <td>0.59</td>
 </tr>
  <tr></tr>
  <tr>
    <td>RU→TR</td>
    <td>0.22</td>
    <td>0.60</td>
    <td>0.18</td>
    <td>0.58</td>
    <td><b>0.26</b></td>
    <td><b>0.63</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→EN</td>
    <td>0.40</td>
    <td>0.68</td>
    <td>0.40</td>
    <td>0.68</td>
    <td><b>0.41</b></td>
    <td><b>0.69</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→KK</td>
    <td>0.15</td>
    <td>0.55</td>
    <td>0.14</td>
    <td>0.54</td>
    <td><b>0.17</b></td>
    <td><b>0.57</b></td>
 </tr>
  <tr></tr>
  <tr>
    <td>TR→RU</td>
    <td>0.22</td>
    <td>0.57</td>
    <td>0.24</td>
    <td>0.58</td>
    <td><b>0.25</b></td>
    <td><b>0.59</b></td>
  </tr>
</tbody>
</table>

<h2> Use of the model :rocket: </h2>

You can translate a text using <code>predict.py</code>. For this, you need to download the model from ISSAI Hugging Face repository. In the script you need to choose the source and target languages (<code>src</code> and <code>trg</code> variables). They could contain the following values:
* Kazakh: kaz_Cyrl
* Russian: rus_Cyrl
* English: eng_Latn
* Turkish: tur_Latn

After this, enter the text that you want to translate in the <code>text</code> variable.

<h2>Acknowledgements 🙏</h2>

<p align = "justify">We wish to convey our deep appreciation to the diligent group of translators whose exceptional contributions have been crucial to the successful realisation of this study. Their tireless efforts to ensure the accuracy and faithful rendition of the source materials have indeed proved invaluable. Our sincerest thanks go to the following esteemed individuals: Aigerim Baidauletova, Aigerim Boranbayeva, Ainagul Akmuldina, Aizhan Seipanova, Askhat Kenzhegulov, Assel Kospabayeva, Assel Mukhanova, Elmira Nikiforova, Gaukhar Rayanova, Gulim Kabidolda, Gulzhanat Abduldinova, Indira Yerkimbekova, Moldir Orazalinova, Saltanat Kemaliyeva, and Venera Spanbayeva.</p>
