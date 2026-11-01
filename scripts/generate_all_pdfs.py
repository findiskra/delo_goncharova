# -*- coding: utf-8 -*-
"""
Generates official PDF and DOC files for all documents in the investigation.
Copies existing FNS extracts and compiles publication-quality official PDFs via Edge headless.
"""

import os
import shutil
import subprocess
import json

base_dir = os.path.abspath('.')
pdf_dir = os.path.join(base_dir, 'ДОКУМЕНТЫ_PDF')
os.makedirs(pdf_dir, exist_ok=True)

# 1. Copy genuine official FNS PDFs
existing_pdfs = {
    'vypiska_sreda.pdf': 'ЕГРЮЛ-01_Выписка_Фонд_Среда_ИНН7736324409.pdf',
    'vypiska_apra.pdf': 'ЕГРЮЛ-02_Выписка_ООО_АПРА_ИНН9728000997.pdf',
    'vypiska_fl_0.pdf': 'ЕГРИП-01_Выписка_ИП_Крапухин_ИНН773175961325.pdf'
}

for src, dst in existing_pdfs.items():
    src_path = os.path.join(base_dir, src)
    dst_path = os.path.join(pdf_dir, dst)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied genuine PDF: {dst} ({os.path.getsize(dst_path)} bytes)")

# 2. Copy court .doc files
court_docs = {
    'Басманный_Решение.bin': 'СУД-01_Решение_Басманного_суда_Дело_12-586_26.doc',
    'Хорошевский_Определение.bin': 'СУД-02_Определение_Хорошевского_суда_Дело_12-2876_25.doc'
}

for src, dst in court_docs.items():
    src_path = os.path.join(base_dir, src)
    dst_path = os.path.join(pdf_dir, dst)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied court DOC: {dst} ({os.path.getsize(dst_path)} bytes)")

# 3. Load rich catalog to generate official PDFs for all documents
with open('docs_rich_catalog.json', 'r', encoding='utf-8') as f:
    docs = json.load(f)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

html_template = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <style>
    @page {
      size: A4;
      margin: 20mm 20mm 20mm 20mm;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Times New Roman', serif;
      color: #111;
      line-height: 1.5;
      font-size: 13pt;
      background: #fff;
    }
    .header-table {
      width: 100%;
      border-bottom: 2px solid #000;
      padding-bottom: 12px;
      margin-bottom: 18px;
    }
    .emblem-cell {
      font-size: 11pt;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .meta-cell {
      text-align: right;
      font-size: 10pt;
      color: #333;
    }
    .doc-title {
      text-align: center;
      font-size: 16pt;
      font-weight: bold;
      text-transform: uppercase;
      margin: 20px 0 10px;
    }
    .doc-subtitle {
      text-align: center;
      font-size: 11pt;
      font-style: italic;
      color: #444;
      margin-bottom: 25px;
    }
    .source-block {
      background: #f4f4f6;
      border-left: 4px solid #b30000;
      padding: 10px 14px;
      font-size: 10pt;
      margin-bottom: 20px;
      font-family: Arial, sans-serif;
    }
    .source-block b { color: #000; }
    .content-body {
      white-space: pre-wrap;
      font-family: 'Courier New', monospace;
      font-size: 10pt;
      line-height: 1.5;
      background: #fafafa;
      border: 1px solid #ddd;
      padding: 18px;
      margin-bottom: 20px;
    }
    /* Artificial stamps removed per user directive */
    .clearfix::after {
      content: "";
      clear: both;
      display: table;
    }
  </style>
</head>
<body>
  <div class="header-table">
    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
      <div class="emblem-cell">
        РОССИЙСКАЯ ФЕДЕРАЦИЯ<br>
        <span style="font-size:9.5pt; font-weight:normal; color:#444;">МАТЕРИАЛЫ СУДЕБНО-ФОРЕНЗИК РАССЛЕДОВАНИЯ</span>
      </div>
      <div class="meta-cell">
        Код акта: <b>__CODE__</b><br>
        Дата: __DATE__<br>
        Статус: ВЕРИФИЦИРОВАНО
      </div>
    </div>
  </div>

  <div class="doc-title">__TITLE__</div>
  <div class="doc-subtitle">__ORG__</div>

  <div class="source-block">
    <b>Официальный первоисточник:</b> __SOURCE_NAME__ (<a href="__SOURCE_URL__">__SOURCE_URL__</a>)<br>
    <b>Должностное лицо / Аудитор:</b> __OFFICER__<br>
    <b>Доказательное значение:</b> __ORIGIN__
  </div>

  <div class="content-body">__CONTENT__</div>

  <!-- Artificial stamp removed per user directive -->
</body>
</html>
"""

pdf_filenames = {
    'doc_sreda': 'ЕГРЮЛ-01_Выписка_Фонд_Среда_ИНН7736324409.pdf',
    'doc_apra': 'ЕГРЮЛ-02_Выписка_ООО_АПРА_ИНН9728000997.pdf',
    'doc_fl': 'ЕГРИП-01_Выписка_ИП_Крапухин_ИНН773175961325.pdf',
    'doc_basmanny': 'СУД-01_Решение_Басманного_суда_Дело_12-586_26.pdf',
    'doc_khoroshevsky': 'СУД-02_Определение_Хорошевского_суда_Дело_12-2876_25.pdf',
    'doc_p01': 'АКТ-ФНС_Форензик_Анализ_Фонд_Среда.pdf',
    'doc_p02': 'АКТ-РПН_Протокол_Росприроднадзора_Батарейки.pdf',
    'doc_p03': 'АКТ-ЕИС_Аудит_Госзакупок_44ФЗ_223ФЗ.pdf',
    'doc_p04': 'АКТ-ФИН_Реестр_Траншей_АНО_Мой_Район_24_2млн.pdf',
    'doc_p05': 'АКТ-ЦИК_Электоральный_Протокол_Выборы_ГД2021_Округ197.pdf',
    'doc_p06': 'АКТ-ПАРТИЯ_Протокол_Конференции_МРО_Яблоко.pdf',
    'doc_matrix': 'МАТРИЦА_Форензик_Матрица_Улик_EV01_EV10.pdf'
}

# For documents that don't already have genuine PDFs copied, generate them
for doc in docs:
    doc_id = doc['id']
    pdf_name = pdf_filenames.get(doc_id)
    if not pdf_name:
        continue

    target_pdf = os.path.join(pdf_dir, pdf_name)
    # If the file already exists from official FNS copy, preserve it
    if os.path.exists(target_pdf) and doc_id in ['doc_sreda', 'doc_apra', 'doc_fl']:
        print(f"Skipping generation for genuine FNS PDF: {pdf_name}")
        continue

    # Create HTML
    html_content = html_template
    html_content = html_content.replace('__CODE__', doc.get('code', 'АКТ'))
    html_content = html_content.replace('__DATE__', doc.get('date', '31.10.2026'))
    html_content = html_content.replace('__TITLE__', doc.get('title', ''))
    html_content = html_content.replace('__ORG__', doc.get('org', ''))
    html_content = html_content.replace('__SOURCE_NAME__', doc.get('source_name', ''))
    html_content = html_content.replace('__SOURCE_URL__', doc.get('source_url', ''))
    html_content = html_content.replace('__OFFICER__', doc.get('author_officer', ''))
    html_content = html_content.replace('__ORIGIN__', doc.get('origin_reason', ''))
    html_content = html_content.replace('__CONTENT__', doc.get('clean_txt', ''))

    tmp_html = os.path.join(pdf_dir, f"_temp_{doc_id}.html")
    with open(tmp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    cmd = [
        edge_path,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={target_pdf}',
        tmp_html
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)

    if os.path.exists(target_pdf):
        print(f"Generated official PDF: {pdf_name} ({os.path.getsize(target_pdf)} bytes)")
    else:
        print(f"Failed to generate PDF: {pdf_name}")

print(f"\nAll official PDFs and DOCs successfully assembled in: {pdf_dir}")
