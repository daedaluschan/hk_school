# hk_school

## 簡介

是咁的，唔少家長可能都會為快將入讀 K1 或 N 班嘅子女做定資料搜集功課。教育局既「幼稚園及幼稚園暨幼兒中心概覽」係其中一個必用網站( http://kgp2015.highlight.hk/website/school.php ) 。但係用落其實個 website 真係唔係幾 user friendly。睇一間就 click 一間，想同其他學校做比較就更麻煩。所以有人可能會將資料慢慢 copy & paste 咁抄落個 excel 度 save 低方便之後再參考返。我亦都試過起政府嘅「資料一線通網站」( [data.gov.hk](https://data.gov.hk/tc-data/category/education) )，可借發覺果度資料好唔齊，無學費、收唔收學卷等重要資訊。

呢個小 program 主要係想減省呢啲咁嘅 copy & paste work，佢會自動將*所有*幼稚園同埋 N 班嘅資料 download 哂落個 csv file 度。

## 原理

其實都係起下面果兩條 URL 做 web scrapping 。節一條 link 係拎哂條 full list 同埋個 ID，而第二條 link 就係用返個 ID 去 extract 啲學校資料。

http://kgp2015.highlight.hk/website/school.php

http://kgp2015.highlight.hk/website/schoolinfo.php?schid=6440

## 用法

* 我未試過起 Python 2.X environment 上面 run 過，但係我都 99% sure 係唔會 work 嘅(因為冇做中文 UTF-8 嘅轉換)，所以請用 Python 3.X version。
* 跟住照住 requirement.txt 裝返所有 depending module。如果用 pip 的話： > pip install -r requirements.txt
* 如果用 jupyther notebook 的話只要行哂 school_web_scrap.ipynb 裡面啲 cell 就得；如果用 command prompt： > python school_web_scrap.py
* 應該 5 分鐘內可以行完，個 csv file 會 save 咗起同一個 directory 度。留意返  csv 嘅 deliminator 係「|」 ，唔係「，」。