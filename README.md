# hk_school

## 簡介

是咁的，唔少家長可能都會為快將入讀 K1 或 N 班嘅子女做定資料搜集功課。教育局既「幼稚園及幼稚園暨幼兒中心概覽」係其中一個必用網站( http://kgp2015.highlight.hk/website/school.php ) 。但係用落其實個 website 真係唔係幾 user friendly。睇一間就 click 一間，想同其他學校做比較就更麻煩。

有人可能會將資料慢慢 copy & paste 咁抄落個 excel 度方便之後再參考返。呢個小 program 主要係想減省呢啲咁嘅 copy & paste work，佢會自動將所有幼稚園同埋 N 班嘅資料 download 哂落個 csv file 度。

## 原理

其實都係起下面果兩條 URL 做 web scrapping 。節一條 link 係拎哂條 full list 同埋個 ID，而第二條 link 就係用返個 ID 去 extract 啲學校資料。

http://kgp2015.highlight.hk/website/school.php

http://kgp2015.highlight.hk/website/schoolinfo.php?schid=6440

## 用法

