# -*- coding: utf-8 -*-
"""
Helper that produces HTML head and CSS styles for the Iskra-style Goncharov site.
Ensures Montserrat is used everywhere with varying weights, and strict red/green/yellow/gray palette for Dossier.
"""

def get_head_and_styles():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ИСКРА // РАССЛЕДОВАНИЕ: ДЕЛО КИРИЛЛА ГОНЧАРОВА</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,700;1,900&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #070709;
      --bg-panel: #111115;
      --bg-card: #17171d;
      --bg-card-alt: #1f1f26;
      --iskra-red: #E30613;
      --iskra-red-dark: #b3040e;
      --text-white: #ffffff;
      --text-gray: #a2a2ad;
      --text-dim: #6d6d7a;
      --border-dark: #262630;
      --border-light: rgba(255, 255, 255, 0.12);
      --font-main: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: var(--font-main) !important;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-white);
      font-family: var(--font-main) !important;
      font-size: 15px;
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    button, input, select, textarea, table, th, td, pre, code {
      font-family: var(--font-main) !important;
    }

    /* BADGES */
    .badge-white {
      display: inline-block;
      background: #FFFFFF;
      color: #000000;
      font-weight: 900;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 4px 9px;
      vertical-align: middle;
    }

    .badge-red {
      display: inline-block;
      background: var(--iskra-red);
      color: #FFFFFF;
      font-weight: 900;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 4px 9px;
      vertical-align: middle;
    }

    .badge-outline {
      display: inline-block;
      border: 1px solid var(--text-white);
      color: var(--text-white);
      font-weight: 800;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 3px 8px;
      vertical-align: middle;
    }

    /* TOP BANNER */
    .iskra-banner {
      background: #000000;
      border-bottom: 3px solid var(--iskra-red);
      position: relative;
      overflow: hidden;
    }

    .iskra-top-strip {
      background: var(--iskra-red);
      color: #ffffff;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 7px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .header-content {
      max-width: 1400px;
      margin: 0 auto;
      padding: 35px 24px 28px;
    }

    .header-grid {
      display: grid;
      grid-template-columns: 1fr 370px;
      gap: 30px;
      align-items: center;
    }

    @media (max-width: 950px) {
      .header-grid { grid-template-columns: 1fr; }
    }

    .header-title-block h1 {
      font-size: 38px;
      font-weight: 900;
      line-height: 1.15;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      margin-bottom: 8px;
      color: #FFFFFF;
    }

    .header-title-block h1 span.accent {
      background: var(--iskra-red);
      color: #FFFFFF;
      padding: 0 8px;
      display: inline-block;
    }

    .header-lead {
      font-size: 15px;
      font-weight: 500;
      color: var(--text-gray);
      max-width: 940px;
      line-height: 1.55;
      margin-top: 14px;
    }

    .stats-widget {
      background: var(--bg-panel);
      border: 1px solid var(--border-dark);
      border-left: 6px solid var(--iskra-red);
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .stat-row {
      display: flex;
      flex-direction: column;
    }

    .stat-val {
      font-size: 24px;
      font-weight: 900;
      color: #FFFFFF;
      line-height: 1;
    }

    .stat-val.red { color: var(--iskra-red); }

    .stat-lbl {
      font-size: 10px;
      text-transform: uppercase;
      font-weight: 800;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      margin-top: 3px;
    }

    /* NAVIGATION TABS */
    .nav-container {
      background: #0d0d11;
      border-bottom: 2px solid var(--iskra-red);
      position: sticky;
      top: 0;
      z-index: 1000;
      padding: 10px 24px;
    }

    .nav-tabs-grid {
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
    }

    @media (max-width: 1100px) {
      .nav-tabs-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .nav-tabs-grid { grid-template-columns: 1fr; }
    }

    .nav-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-dark);
      border-bottom: 3px solid transparent;
      padding: 9px 12px;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .nav-btn .tab-num {
      font-size: 10px;
      color: var(--iskra-red);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    .nav-btn .tab-title {
      font-size: 11px;
      font-weight: 800;
      color: #FFFFFF;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      line-height: 1.25;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .nav-btn:hover {
      background: var(--bg-card-alt);
      border-color: #FFFFFF;
    }

    .nav-btn.active {
      background: var(--bg-panel);
      border-color: var(--iskra-red);
      border-bottom: 3px solid var(--iskra-red);
      box-shadow: 0 4px 15px rgba(227, 6, 19, 0.25);
    }

    /* MAIN WRAPPER */
    .main-wrapper {
      max-width: 1400px;
      margin: 30px auto;
      padding: 0 24px;
    }

    .tab-pane {
      display: none;
      animation: fadeIn 0.3s ease-in-out;
    }

    .tab-pane.active { display: block; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .section-head {
      margin-bottom: 25px;
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-dark);
      padding-bottom: 12px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .section-head h2 {
      font-size: 22px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .section-head .desc {
      font-size: 13px;
      font-weight: 500;
      color: var(--text-gray);
      margin-top: 4px;
    }

    /* CARDS */
    .card {
      background: var(--bg-panel);
      border: 1px solid var(--border-dark);
      padding: 24px;
      margin-bottom: 20px;
      position: relative;
    }

    .card.red-bar-left { border-left: 4px solid var(--iskra-red); }
    .card.white-bar-left { border-left: 4px solid #FFFFFF; }
    .card.green-bar-left { border-left: 4px solid #2ecc71; }
    .card.yellow-bar-left { border-left: 4px solid #f1c40f; }

    .card-title {
      font-size: 14px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 15px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-dark);
      padding-bottom: 8px;
      flex-wrap: wrap;
      gap: 6px;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
    }

    @media (max-width: 1000px) {
      .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
    }

    /* LONGREAD CHAPTER BOXES */
    .chapter-box {
      background: #0d0d12;
      border: 1px solid #202029;
      border-left: 4px solid var(--iskra-red);
      padding: 28px;
      margin-bottom: 28px;
    }

    .chapter-tag {
      font-size: 11px;
      font-weight: 900;
      text-transform: uppercase;
      color: var(--iskra-red);
      letter-spacing: 0.1em;
      margin-bottom: 6px;
    }

    .chapter-title {
      font-size: 22px;
      font-weight: 900;
      text-transform: uppercase;
      color: #FFFFFF;
      margin-bottom: 16px;
      line-height: 1.25;
    }

    .chapter-body {
      font-size: 14.5px;
      font-weight: 400;
      color: #c9c9d4;
      line-height: 1.7;
    }

    .chapter-body p { margin-bottom: 14px; }
    .chapter-body p:last-child { margin-bottom: 0; }

    .callout-box {
      background: #14141c;
      border-left: 3px solid #FFFFFF;
      padding: 14px 18px;
      margin: 16px 0;
      font-size: 13.5px;
      color: #e5e5ed;
      font-weight: 500;
    }

    .callout-box.red {
      border-left-color: var(--iskra-red);
      background: rgba(227, 6, 19, 0.08);
    }

    /* CHAPTER QUICK NAV PILLS */
    .chapter-nav-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      background: var(--bg-panel);
      padding: 12px;
      border: 1px solid var(--border-dark);
      margin-bottom: 25px;
    }

    .chapter-pill {
      background: #1c1c24;
      color: #bbb;
      text-decoration: none;
      font-size: 11px;
      font-weight: 800;
      padding: 6px 12px;
      border: 1px solid #2a2a38;
      transition: all 0.15s;
    }
    .chapter-pill:hover {
      background: var(--iskra-red);
      color: #fff;
      border-color: var(--iskra-red);
    }

    /* DATA TABLES */
    .data-table-wrapper {
      overflow-x: auto;
      margin: 15px 0;
    }

    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }

    .data-table th {
      background: #1c1c24;
      color: #fff;
      font-weight: 800;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.05em;
      padding: 10px 14px;
      border: 1px solid var(--border-dark);
    }

    .data-table td {
      padding: 10px 14px;
      border: 1px solid var(--border-dark);
      color: #c0c0cc;
      vertical-align: top;
      font-weight: 500;
    }

    .data-table tr:nth-child(even) { background: rgba(255, 255, 255, 0.02); }
    .data-table tr:hover { background: rgba(227, 6, 19, 0.05); }

    /* SCHEMES & DIAGRAMS (HIGH CONTRAST ISKRA SYSTEM) */
    .scheme-container {
      background: #09090d;
      border: 1px solid var(--border-dark);
      border-left: 4px solid var(--iskra-red);
      padding: 24px;
      margin: 20px 0;
    }

    .scheme-title {
      font-size: 13px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #fff;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .scheme-desc {
      font-size: 12px;
      color: var(--text-gray);
      margin-bottom: 20px;
    }

    .scheme-flow {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .scheme-node {
      display: flex;
      align-items: stretch;
      gap: 16px;
      transition: transform 0.15s ease;
    }

    .scheme-node:hover {
      transform: translateX(4px);
    }

    .node-badge {
      width: 36px;
      background: var(--iskra-red);
      color: #fff;
      font-weight: 900;
      font-size: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .node-badge.green { background: #2ecc71; color: #000; }
    .node-badge.yellow { background: #f1c40f; color: #000; }
    .node-badge.gray { background: #555566; color: #fff; }

    .node-card {
      background: var(--bg-card);
      border: 1px solid var(--border-dark);
      padding: 14px 18px;
      flex-grow: 1;
    }

    .node-title {
      font-size: 13px;
      font-weight: 900;
      text-transform: uppercase;
      color: #fff;
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .node-body {
      font-size: 12.5px;
      color: #b5b5c2;
      line-height: 1.5;
    }

    .node-arrow {
      text-align: center;
      color: var(--iskra-red);
      font-size: 16px;
      font-weight: 900;
      line-height: 1;
      margin: -4px 0 -4px 18px;
    }

    /* SECTION 07 DOSSIER PERSONA CARDS (STRICT PALETTE: RED, GREEN, YELLOW, GRAY) */
    .dossier-filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 20px;
    }

    .dossier-filter-btn {
      background: #15151c;
      border: 1px solid var(--border-dark);
      color: #aaa;
      padding: 7px 14px;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      cursor: pointer;
      transition: all 0.15s;
    }

    .dossier-filter-btn:hover, .dossier-filter-btn.active {
      background: #fff;
      color: #000;
      border-color: #fff;
    }

    .persona-card {
      background: var(--bg-panel);
      border: 1px solid var(--border-dark);
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border-top: 5px solid #fff;
      transition: transform 0.2s;
    }

    .persona-card:hover {
      transform: translateY(-2px);
    }

    /* STRICT 4 COLORS ONLY */
    .persona-card.p-red { border-top-color: var(--iskra-red); }
    .persona-card.p-green { border-top-color: #2ecc71; }
    .persona-card.p-yellow { border-top-color: #f1c40f; }
    .persona-card.p-gray { border-top-color: #777788; }

    .persona-top-tag {
      font-size: 10px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 3px 8px;
      display: inline-block;
      margin-bottom: 12px;
    }

    .tag-red { background: var(--iskra-red); color: #fff; }
    .tag-green { background: #2ecc71; color: #000; }
    .tag-yellow { background: #f1c40f; color: #000; }
    .tag-gray { background: #333342; color: #ddd; border: 1px solid #555566; }

    .persona-name-row {
      font-size: 16px;
      font-weight: 900;
      color: #fff;
      text-transform: uppercase;
      line-height: 1.2;
      margin-bottom: 4px;
    }

    .persona-party-row {
      font-size: 11px;
      font-weight: 800;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border-dark);
    }

    .persona-outcome-box {
      background: #09090d;
      border: 1px solid var(--border-dark);
      padding: 10px 12px;
      margin-bottom: 12px;
      font-size: 12px;
    }

    .persona-outcome-lbl {
      font-size: 9px;
      font-weight: 900;
      text-transform: uppercase;
      color: var(--text-dim);
      letter-spacing: 0.06em;
      margin-bottom: 3px;
    }

    .persona-outcome-val {
      font-weight: 800;
      color: #fff;
      line-height: 1.35;
    }

    .persona-body-desc {
      font-size: 12px;
      font-weight: 500;
      color: var(--text-gray);
      line-height: 1.5;
    }

    .persona-footer-status {
      margin-top: 15px;
      padding-top: 8px;
      border-top: 1px solid var(--border-dark);
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* REPOSITORY FILE CARDS */
    .file-card {
      background: var(--bg-panel);
      border: 1px solid var(--border-dark);
      padding: 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 12px;
      transition: border-color 0.2s;
    }

    .file-card:hover { border-color: #fff; }
    .file-card.red { border-left: 4px solid var(--iskra-red); }

    .file-title {
      font-size: 13px;
      font-weight: 900;
      text-transform: uppercase;
      color: #fff;
      margin-bottom: 4px;
    }

    .file-meta {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-dim);
      margin-bottom: 8px;
    }

    .file-desc {
      font-size: 12px;
      font-weight: 500;
      color: var(--text-gray);
      line-height: 1.45;
    }

    .file-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 10px;
    }

    .btn-file {
      display: inline-block;
      background: #22222b;
      color: #fff;
      text-decoration: none;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 8px 14px;
      border: 1px solid var(--border-dark);
      cursor: pointer;
      transition: all 0.15s;
    }

    .btn-file:hover { background: #fff; color: #000; }

    .btn-file.red-btn {
      background: var(--iskra-red);
      border-color: var(--iskra-red);
      color: #fff;
    }

    .btn-file.red-btn:hover {
      background: #fff;
      color: #000;
      border-color: #fff;
    }

    /* MODAL OVERLAY */
    .modal-overlay {
      display: none;
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      background: rgba(0, 0, 0, 0.88);
      z-index: 9999;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }

    .modal-overlay.active { display: flex; }

    .modal-container {
      background: var(--bg-panel);
      border: 2px solid var(--iskra-red);
      width: 100%;
      max-width: 950px;
      max-height: 88vh;
      display: flex;
      flex-direction: column;
      position: relative;
      box-shadow: 0 10px 40px rgba(0,0,0,0.9);
      padding: 25px;
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid var(--border-dark);
      padding-bottom: 12px;
      gap: 15px;
    }

    .modal-header h3 {
      font-size: 16px;
      font-weight: 900;
      text-transform: uppercase;
      color: #fff;
    }

    .modal-header .doc-meta {
      font-size: 11px;
      font-weight: 600;
      color: var(--text-dim);
      margin-top: 4px;
    }

    .modal-close {
      background: none;
      border: none;
      color: #fff;
      font-size: 26px;
      font-weight: 900;
      cursor: pointer;
      line-height: 1;
    }

    .modal-close:hover { color: var(--iskra-red); }

    .modal-content-area {
      overflow-y: auto;
      margin-top: 15px;
      font-size: 13.5px;
      font-weight: 500;
      color: #dcdce8;
      line-height: 1.65;
      background: #07070a;
      padding: 24px;
      border: 1px solid var(--border-dark);
      flex-grow: 1;
    }

    .modal-toolbar {
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      margin-top: 14px;
      flex-wrap: wrap;
    }

    /* SEARCH BOX */
    .search-box {
      background: #111117;
      border: 1px solid var(--border-dark);
      padding: 10px 14px;
      color: #fff;
      font-size: 13px;
      font-weight: 600;
      width: 100%;
      max-width: 400px;
    }
    .search-box:focus {
      outline: none;
      border-color: var(--iskra-red);
    }

    /* INTERACTIVE SIMULATOR */
    .sim-panel {
      background: #0d0d12;
      border: 1px solid var(--border-dark);
      border-left: 4px solid var(--iskra-red);
      padding: 24px;
      margin: 20px 0;
    }

    .sim-slider-row {
      display: flex;
      align-items: center;
      gap: 20px;
      margin: 18px 0;
    }

    .sim-slider {
      flex-grow: 1;
      height: 8px;
      accent-color: var(--iskra-red);
      cursor: pointer;
    }

    .sim-slider-val {
      font-size: 20px;
      font-weight: 900;
      color: var(--iskra-red);
      width: 60px;
      text-align: right;
    }


    /* TOAST */
    .toast {
      position: fixed;
      bottom: 25px;
      right: 25px;
      background: var(--iskra-red);
      color: #fff;
      padding: 10px 20px;
      font-weight: 900;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
      display: none;
      z-index: 10000;
    }

    /* FOOTER */
    footer {
      background: #000;
      border-top: 2px solid var(--iskra-red);
      padding: 35px 24px;
      text-align: center;
      font-size: 12px;
      color: #777;
      margin-top: 60px;
    }

    footer .logo {
      font-weight: 900;
      font-size: 16px;
      color: #fff;
      letter-spacing: 0.1em;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
"""

print("Updated site_template_parts.py with Montserrat and strict Section 7 colors.")
