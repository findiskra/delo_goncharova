# -*- coding: utf-8 -*-
"""
Master Assembler for the Iskra Goncharov Site.
Updated:
- Montserrat everywhere
- Removed redundant badge [ДЕЛО ГОНЧАРОВА]
- Exact title line breaks as requested:
  АНАТОМИЯ СИСТЕМНОГО СПОЙЛЕРА: 24,2 МЛН РУБЛЕЙ
  ОТ МЭРИИ, АФЕРА С БАТАРЕЙКАМИ, СЛИВ ВЫБОРОВ
  В ГОСДУМУ И МАРОДЕРСТВО В «ЯБЛОКЕ»
- Visual schemes in Sections 2, 3, 4, 5, 6
- Strict Section 7 palette (Red, Green, Yellow, Gray)
- Section 4: Name 1st line, Party 2nd line, 'Единая Россия (Едро)'
"""

import sys
import os
import json

from site_template_parts import get_head_and_styles
from site_content_tab1 import get_tab1_html
from site_content_tabs2_to_8 import get_tabs2_to_8_html
from site_footer_and_js import get_footer_and_js
from typographer_engine import typograph_html

with open('docs_rich_catalog.json', 'r', encoding='utf-8') as f:
    docs_json_str = f.read()

hero_banner = """
  <!-- TOP BANNER (EXACT ISKRA ASYMMETRICAL POSTER) -->
  <div class="iskra-banner">
    <div class="iskra-top-strip">
      <div><span>СОВЕРШЕННО СЕКРЕТНО // OSINT-РАССЛЕДОВАНИЕ</span> &nbsp;|&nbsp; <span>СПЕЦВЫПУСК ИСКРЫ</span></div>
      <div>2019–2026 // КОРРУПЦИЯ, СПОЙЛЕРСТВО И ЧЕРНАЯ КАССА МЭРИИ</div>
    </div>

    <div class="header-content">
      <div class="header-grid">
        <div class="header-title-block">
          <div>
            <span class="badge-white">СПЕЦПРОЕКТ ИСКРЫ</span>
            <span class="badge-red">ФОРЕНЗИК И СУДЕБНЫЕ АКТЫ</span>
          </div>
          <h1 style="margin-top:14px; margin-bottom:6px;">ДЕЛО КИРИЛЛА <span class="accent">ГОНЧАРОВА</span></h1>
          <h1 style="font-size:23px; color:#e0e0e0; margin-top:6px; font-weight:800; line-height:1.35; text-transform:uppercase;">
            АНАТОМИЯ СИСТЕМНОГО СПОЙЛЕРА: 24,2 МЛН РУБЛЕЙ<br>
            ОТ МЭРИИ, АФЕРА С БАТАРЕЙКАМИ, СЛИВ ВЫБОРОВ<br>
            В ГОСДУМУ И МАРОДЕРСТВО В «ЯБЛОКЕ»
          </h1>
          <p class="header-lead">
            Полная анатомия политической коррупции в Москве: почему самый молодой «лидер либералов» не сидит в тюрьме вместе с оппозиционерами, как экологический фонд «Среда» с финансовым ОКВЭДом осваивал миллионы из кормушки «Мой район», через какую фирму соратника обналичивался кэш, и как в 2021 году были сожжены 19 425 голосов ради победы кремлевского пропагандиста Евгения Попова.
          </p>
        </div>

        <div class="stats-widget">
          <div class="stat-row">
            <span class="stat-val red">24,2 МЛН ₽</span>
            <span class="stat-lbl">Транши фонда «Среда» от АНО «Мой район» (мэрия Москвы)</span>
          </div>
          <div class="stat-row">
            <span class="stat-val">19 425 ГОЛОСОВ</span>
            <span class="stat-lbl">Сожжено в Кунцево (округ 197) в пользу Евгения Попова</span>
          </div>
          <div class="stat-row">
            <span class="stat-val red">0 УГОЛОВОК</span>
            <span class="stat-lbl">За 15 лет в политике (при сроках до 25 лет у соратников)</span>
          </div>
          <div class="stat-row">
            <span class="stat-val">100% КОНТРОЛЬ</span>
            <span class="stat-lbl">Единоличная подпись Гончарова на счетах фонда и партии</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- NAVIGATION TABS (EXACT 2 ROWS, 4 COLS PER ROW) -->
  <div class="nav-container">
    <div class="nav-tabs-grid" id="navTabs">
      <!-- ROW 1 -->
      <button class="nav-btn active" onclick="switchTab('tab-overview')">
        <span class="tab-num">РАЗДЕЛ 01</span>
        <span class="tab-title">Что случилось и почему</span>
      </button>

      <button class="nav-btn" onclick="switchTab('tab-fond')">
        <span class="tab-num">РАЗДЕЛ 02</span>
        <span class="tab-title">Кормушка мэрии (24,2 млн ₽)</span>
      </button>

      <button class="nav-btn" onclick="switchTab('tab-apra')">
        <span class="tab-num">РАЗДЕЛ 03</span>
        <span class="tab-title">Обнальный шлюз (ООО «Апра»)</span>
      </button>

      <button class="nav-btn" onclick="switchTab('tab-duma')">
        <span class="tab-num">РАЗДЕЛ 04</span>
        <span class="tab-title">Спойлер в Госдуму (округ 197)</span>
      </button>

      <!-- ROW 2 -->
      <button class="nav-btn" onclick="switchTab('tab-purge')">
        <span class="tab-num">РАЗДЕЛ 05</span>
        <span class="tab-title">Погром в партии (250 млн ₽)</span>
      </button>

      <button class="nav-btn" onclick="switchTab('tab-coup')">
        <span class="tab-num">РАЗДЕЛ 06</span>
        <span class="tab-title">Аппаратный перехват кассы</span>
      </button>

      <button class="nav-btn" onclick="switchTab('tab-dossier')">
        <span class="tab-num">РАЗДЕЛ 07 // ДОСЬЕ</span>
        <span class="tab-title">Кто с чем и как остался</span>
      </button>

      <button class="nav-btn" onclick="switchTab('tab-vault')">
        <span class="tab-num">РАЗДЕЛ 08 // РЕПОЗИТОРИЙ</span>
        <span class="tab-title">Хранилище улик и документы</span>
      </button>
    </div>
  </div>

  <!-- MAIN WRAPPER -->
  <div class="main-wrapper">
"""

raw_html = (
    get_head_and_styles()
    + hero_banner
    + get_tab1_html()
    + get_tabs2_to_8_html()
    + get_footer_and_js(docs_json_str)
)

full_html = typograph_html(raw_html)

targets = [
    '10_ИНТЕРАКТИВНОЕ_РАССЛЕДОВАНИЕ_ГОНЧАРОВ_ИСКРА.html',
    '10_ИНТЕРАКТИВНОЕ_РАССЛЕДОВАНИЕ_ГОНЧАРОВ_И_ФОНД_СРЕДА.html',
    'index.html'
]

for t in targets:
    with open(t, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Written {t} ({len(full_html)} chars)")

print("All targets assembled successfully.")
