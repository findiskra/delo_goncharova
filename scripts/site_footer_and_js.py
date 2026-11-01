# -*- coding: utf-8 -*-
"""
Footer and JavaScript logic for the Iskra Goncharov investigation website.
Features:
- Loads rich catalog from docs_rich_catalog.json
- Executive Document Summary Modal (structured, clean brief)
- Open clean .TXT document in new tab with authentic official styling
- Direct .TXT download
- Section 7 Dossier filter without emoji circles
- Real-time Election Simulator
"""

def get_footer_and_js(docs_json_str):
    return f"""
  </div> <!-- /main-wrapper -->

  <!-- MODAL DOCUMENT SUMMARY VIEWER -->
  <div class="modal-overlay" id="modalOverlay" onclick="handleOverlayClick(event)">
    <div class="modal-container">
      <div class="modal-header">
        <div>
          <span class="badge-red" id="modalBadge">ДОКУМЕНТ</span>
          <h3 id="modalTitle" style="margin-top:6px;">НАЗВАНИЕ ДОКУМЕНТА</h3>
          <div class="doc-meta" id="modalMeta">МЕТАДАННЫЕ</div>
        </div>
        <button class="modal-close" onclick="closeDocModal()">&times;</button>
      </div>

      <div class="modal-content-area" id="modalContent"></div>

      <div class="modal-toolbar">
        <button class="btn-file red-btn" onclick="openTxtTab(currentDocId)">ОТКРЫТЬ В НОВОЙ ВКЛАДКЕ (.TXT)</button>
        <button class="btn-file" onclick="downloadCurrentModalPdf()">СКАЧАТЬ .PDF</button>
        <button class="btn-file" onclick="downloadCurrentModalDoc()">СКАЧАТЬ .TXT</button>
        <button class="btn-file" onclick="copyCurrentModalSummary()">СКОПИРОВАТЬ СВОДКУ</button>
        <button class="btn-file" onclick="closeDocModal()">ЗАКРЫТЬ (ESC)</button>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast" id="toast">ДОКУМЕНТ СКОПИРОВАН В БУФЕР</div>

  <!-- FOOTER -->
  <footer>
    <div class="logo">ИСКРА // АНТИКОРРУПЦИОННЫЙ И ПОЛИТИЧЕСКИЙ ФОРЕНЗИК</div>
    <p>Специальное журналистское расследование. Документальная база: ФНС России, Росприроднадзор, ЕИС Закупки, ГАС «Правосудие», Мосгоризбирком.</p>
    <p style="margin-top:6px; color:#555;">2019–2026 // Все материалы верифицированы и готовы к передаче в следственные органы.</p>
  </footer>

  <script>
    // Embedded authentic documents rich catalog
    const docsCatalog = {docs_json_str};

    let currentDocId = null;

    function escapeHtml(text) {{
      return (text || '')
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }}

    // Tab Switching
    function switchTab(tabId) {{
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));

      const targetPane = document.getElementById(tabId);
      if (targetPane) {{
        targetPane.classList.add('active');
      }}

      // Find button by onclick
      document.querySelectorAll('.nav-btn').forEach(btn => {{
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(tabId)) {{
          btn.classList.add('active');
        }}
      }});

      window.location.hash = tabId;
      window.scrollTo({{ top: 380, behavior: 'smooth' }});
    }}

    // Render documents in Tab 8
    function renderDocs() {{
      const grid = document.getElementById('docCardsGrid');
      if (!grid) return;

      grid.innerHTML = docsCatalog.map(doc => `
        <div class="file-card red">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="badge-red">${{doc.code}}</span>
              <span style="font-size:10px; color:#888; font-weight:800;">${{doc.date}}</span>
            </div>
            <div class="file-title">${{doc.title}}</div>
            <div class="file-meta">${{doc.meta}}</div>
            <div class="file-desc">${{doc.desc || 'Официальный материальный документ форензик-расследования.'}}</div>
          </div>
          <div class="file-actions">
            <button class="btn-file red-btn" onclick="openDocSummaryModal('${{doc.id}}')">СВОДКА ДОКУМЕНТА</button>
            <a class="btn-file" href="${{doc.pdf_file}}" download target="_blank" style="background:#20202a; border-color:#3c3c4f; color:#fff;">СКАЧАТЬ .PDF</a>
            <button class="btn-file" onclick="openTxtTab('${{doc.id}}')">ОТКРЫТЬ .TXT</button>
            <button class="btn-file" onclick="downloadDoc('${{doc.id}}')">СКАЧАТЬ .TXT</button>
            ${{doc.word_file ? `<a class="btn-file" href="${{doc.word_file}}" download target="_blank" style="background:#1b2533; border-color:#2e4466; color:#70a5ff;">СКАЧАТЬ .DOC</a>` : ''}}
          </div>
        </div>
      `).join('');
    }}

    // Open Executive Summary Modal
    function openDocSummaryModal(docId) {{
      const doc = docsCatalog.find(d => d.id === docId);
      if (!doc) return;

      currentDocId = docId;
      document.getElementById('modalBadge').innerText = doc.code;
      document.getElementById('modalTitle').innerText = doc.title;
      document.getElementById('modalMeta').innerText = (doc.org || '') + ' | ' + (doc.date || '');
      document.getElementById('modalContent').innerHTML = doc.summary || '<p>Сводка документа временно недоступна.</p>';

      document.getElementById('modalOverlay').classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    // Open clean .TXT document in new tab with authentic styling
    function openTxtTab(docId) {{
      const doc = docsCatalog.find(d => d.id === docId);
      if (!doc) return;

      const textContent = doc.clean_txt || doc.content || '';
      const safeTitle = escapeHtml(doc.title);
      const safeCode = escapeHtml(doc.code);
      const safeOrg = escapeHtml(doc.org || '');
      const safeDate = escapeHtml(doc.date || '');
      const safeTxt = escapeHtml(textContent);

      const htmlContent = `<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>${{safeCode}} — ${{safeTitle}}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #0d0d12;
      color: #e2e2ec;
      font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
      padding: 30px 20px 80px;
      line-height: 1.6;
    }}
    .top-bar {{
      max-width: 980px;
      margin: 0 auto 20px;
      background: #16161f;
      border: 1px solid #282838;
      border-left: 5px solid #E30613;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      font-family: 'Montserrat', sans-serif;
    }}
    .top-left h1 {{
      font-size: 15px;
      font-weight: 900;
      text-transform: uppercase;
      color: #fff;
    }}
    .top-left .meta {{
      font-size: 11px;
      font-weight: 600;
      color: #888899;
      margin-top: 3px;
    }}
    .actions {{
      display: flex;
      gap: 8px;
    }}
    .btn {{
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      padding: 8px 14px;
      background: #252533;
      color: #fff;
      border: 1px solid #3a3a4d;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.15s;
    }}
    .btn:hover {{ background: #fff; color: #000; }}
    .btn-red {{ background: #E30613; border-color: #E30613; color: #fff; }}
    .btn-red:hover {{ background: #ff2233; color: #fff; }}
    .doc-paper {{
      max-width: 980px;
      margin: 0 auto;
      background: #08080c;
      border: 1px solid #252535;
      padding: 40px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.85);
      white-space: pre-wrap;
      font-size: 13px;
      line-height: 1.65;
      color: #d8d8e8;
      word-break: break-word;
    }}
    @media print {{
      body {{ background: #fff; color: #000; }}
      .top-bar {{ display: none; }}
      .doc-paper {{ border: none; box-shadow: none; padding: 0; background: #fff; color: #000; }}
    }}
  </style>
</head>
<body>
  <div class="top-bar">
    <div class="top-left">
      <h1>[${{safeCode}}] ${{safeTitle}}</h1>
      <div class="meta">${{safeOrg}} &nbsp;|&nbsp; ${{safeDate}} &nbsp;|&nbsp; ОФИЦИАЛЬНЫЙ АУТЕНТИЧНЫЙ ДОКУМЕНТ</div>
    </div>
    <div class="actions">
      <button class="btn btn-red" onclick="window.print()">ПЕЧАТЬ</button>
      <button class="btn" onclick="navigator.clipboard.writeText(document.getElementById('txtBody').innerText); alert('Текст документа скопирован!');">СКОПИРОВАТЬ</button>
      <button class="btn" onclick="window.close()">ЗАКРЫТЬ ВКЛАДКУ</button>
    </div>
  </div>

  <div class="doc-paper" id="txtBody">${{safeTxt}}</div>
</body>
</html>`;

      const blob = new Blob([htmlContent], {{ type: 'text/html;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      window.open(url, '_blank');
    }}

    // Close Modal
    function closeDocModal() {{
      document.getElementById('modalOverlay').classList.remove('active');
      document.body.style.overflow = '';
      currentDocId = null;
    }}

    function handleOverlayClick(e) {{
      if (e.target.id === 'modalOverlay') {{
        closeDocModal();
      }}
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeDocModal();
    }});

    // Toast Notification
    function showToast(text) {{
      const t = document.getElementById('toast');
      t.innerText = text;
      t.style.display = 'block';
      setTimeout(() => {{ t.style.display = 'none'; }}, 2500);
    }}

    // Copy Content
    function copyCurrentModalSummary() {{
      if (!currentDocId) return;
      const doc = docsCatalog.find(d => d.id === currentDocId);
      if (!doc) return;

      const temp = document.createElement('div');
      temp.innerHTML = doc.summary;
      const plainText = temp.innerText || temp.textContent;

      navigator.clipboard.writeText(plainText).then(() => {{
        showToast('СВОДКА [' + doc.code + '] СКОПИРОВАНА В БУФЕР');
      }}).catch(() => {{
        showToast('ОШИБКА ПРИ КОПИРОВАНИИ');
      }});
    }}

    // Download Doc
    function downloadDoc(docId) {{
      const doc = docsCatalog.find(d => d.id === docId);
      if (!doc) return;

      const blob = new Blob([doc.clean_txt || doc.content || ''], {{ type: 'text/plain;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = doc.code + '_' + doc.id + '.txt';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast('СКАЧИВАНИЕ ФАЙЛА НАЧАТО: ' + doc.code);
    }}

    function downloadCurrentModalDoc() {{
      if (currentDocId) {{
        downloadDoc(currentDocId);
      }}
    }}

    function downloadCurrentModalPdf() {{
      if (!currentDocId) return;
      const doc = docsCatalog.find(d => d.id === currentDocId);
      if (!doc || !doc.pdf_file) return;

      const a = document.createElement('a');
      a.href = doc.pdf_file;
      a.download = doc.pdf_file.split('/').pop();
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      showToast('СКАЧИВАНИЕ PDF НАЧАТО: ' + doc.code);
    }}

    // Real-time Election Simulator
    function updateSim() {{
      const slider = document.getElementById('simSlider');
      const valDisplay = document.getElementById('simVal');
      const lobanovDisplay = document.getElementById('simLobanov');
      const resultDisplay = document.getElementById('simResult');

      if (!slider) return;
      const pct = parseInt(slider.value, 10);
      valDisplay.innerText = pct + '%';

      const baseLobanov = 72805;
      const goncharovVotes = 19425;
      const popovVotes = 80894;

      const transferred = Math.round(goncharovVotes * (pct / 100));
      const totalLobanov = baseLobanov + transferred;

      lobanovDisplay.innerText = totalLobanov.toLocaleString('ru-RU') + ' голосов';

      const diff = totalLobanov - popovVotes;
      if (diff > 0) {{
        resultDisplay.innerText = 'ПОБЕДА ЛОБАНОВА (+' + diff.toLocaleString('ru-RU') + ' голосов)';
        resultDisplay.style.color = '#2ecc71';
      }} else if (diff === 0) {{
        resultDisplay.innerText = 'НИЧЬЯ С ПОПОВЫМ';
        resultDisplay.style.color = '#f1c40f';
      }} else {{
        resultDisplay.innerText = 'ПОПОВ ВПЕРЕДИ НА ' + Math.abs(diff).toLocaleString('ru-RU') + ' голосов';
        resultDisplay.style.color = 'var(--iskra-red)';
      }}
    }}

    // Filter Evidence Matrix
    function filterMatrix() {{
      const q = document.getElementById('matrixSearch').value.toLowerCase();
      const rows = document.querySelectorAll('#evidenceTable tbody tr');

      rows.forEach(row => {{
        const text = row.innerText.toLowerCase();
        if (text.includes(q)) {{
          row.style.display = '';
        }} else {{
          row.style.display = 'none';
        }}
      }});
    }}

    // Filter Dossier (Section 7)
    function filterDossier(group, btnEl) {{
      document.querySelectorAll('.dossier-filter-btn').forEach(btn => btn.classList.remove('active'));
      if (btnEl) {{
        btnEl.classList.add('active');
      }}

      const cards = document.querySelectorAll('#dossierGrid .persona-card');
      cards.forEach(card => {{
        if (group === 'all' || card.getAttribute('data-group') === group) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // Initialization
    window.addEventListener('DOMContentLoaded', () => {{
      renderDocs();
      updateSim();

      if (window.location.hash) {{
        const tab = window.location.hash.replace('#', '');
        switchTab(tab);
      }}
    }});
  </script>
</body>
</html>
"""

if __name__ == '__main__':
    print("site_footer_and_js.py updated successfully.")
