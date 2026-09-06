import os
import webbrowser

smiles_drawer_path = os.path.join(
  os.path.dirname(os.path.abspath(__file__)),
  'node_modules', 'smiles-drawer', 'dist', 'smiles-drawer.min.js'
)
with open(smiles_drawer_path, 'r') as f:
    sd_js = f.read()

html = r'''<!doctype html>
<title>ChemMed</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@400;500;600;700&display=swap">
<style>
:root{
  --bg:#f2f3fb;--sf:#fff;--sf2:#f0f2f9;--bd:#dde0ef;
  --tx:#1a1c2e;--mu:#6b7280;
  --ac:#4f5fd4;--ac-d:#eef0fd;--ac-s:rgba(79,95,212,.12);
  --ok:#16a34a;--ok-bg:#dcfce7;--ok-br:#86efac;
  --wa:#d97706;--wa-bg:#fef3c7;--wa-br:#fcd34d;
  --er:#dc2626;--er-bg:#fee2e2;--er-br:#fca5a5;
  --cv:#fafbff;--gr:rgba(79,95,212,.05);--bn:#1a1c2e;
  --an:#3b82f6;--ao:#dc2626;--as:#ca8a04;--ah:#7c3aed;--ap:#ea580c;
  --pc:#0369a1;--pc-bg:#e0f2fe;--pc-br:#7dd3fc;
}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#0c0d1a;--sf:#161728;--sf2:#1b1d32;--bd:#272a48;
  --tx:#e2e6f8;--mu:#757d9e;
  --ac:#7080f0;--ac-d:#1e2245;--ac-s:rgba(112,128,240,.15);
  --ok:#22c55e;--ok-bg:#052e16;--ok-br:#166534;
  --wa:#f59e0b;--wa-bg:#1c1200;--wa-br:#713f12;
  --er:#f87171;--er-bg:#2a0808;--er-br:#7f1d1d;
  --cv:#0f1020;--gr:rgba(112,128,240,.06);--bn:#c8cde8;
  --an:#60a5fa;--ao:#f87171;--as:#fbbf24;--ah:#a78bfa;--ap:#fb923c;
  --pc:#38bdf8;--pc-bg:#082f49;--pc-br:#0c4a6e;
}}
:root[data-theme="dark"]{
  --bg:#0c0d1a;--sf:#161728;--sf2:#1b1d32;--bd:#272a48;
  --tx:#e2e6f8;--mu:#757d9e;
  --ac:#7080f0;--ac-d:#1e2245;--ac-s:rgba(112,128,240,.15);
  --ok:#22c55e;--ok-bg:#052e16;--ok-br:#166534;
  --wa:#f59e0b;--wa-bg:#1c1200;--wa-br:#713f12;
  --er:#f87171;--er-bg:#2a0808;--er-br:#7f1d1d;
  --cv:#0f1020;--gr:rgba(112,128,240,.06);--bn:#c8cde8;
  --an:#60a5fa;--ao:#f87171;--as:#fbbf24;--ah:#a78bfa;--ap:#fb923c;
  --pc:#38bdf8;--pc-bg:#082f49;--pc-br:#0c4a6e;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;font-family:'Inter',system-ui,sans-serif;font-size:14px;background:var(--bg);color:var(--tx);overflow:hidden}
.app{display:grid;grid-template-rows:50px 1fr 24px;height:100vh}
/* HEADER */
.hdr{background:var(--ac);color:#fff;display:flex;align-items:center;gap:10px;padding:0 18px;box-shadow:0 2px 14px rgba(79,95,212,.45);z-index:10}
.hl{font-family:'Space Mono',monospace;font-size:1.05rem;font-weight:700;letter-spacing:-.5px}
.hl span{opacity:.55;font-weight:400}
.hs{font-size:.65rem;opacity:.65;font-family:'Space Mono',monospace;margin-top:1px}
.hpills{margin-left:auto;display:flex;gap:6px;align-items:center}
.hpill{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);border-radius:100px;padding:3px 9px;font-size:.65rem;font-family:'Space Mono',monospace}
.hpill.pc-pill{background:rgba(3,105,161,.3);border-color:rgba(125,211,252,.4);display:flex;align-items:center;gap:4px;transition:background .3s}
.hpill.pc-ok{background:rgba(22,163,74,.25);border-color:rgba(134,239,172,.4)}
.hpill.pc-fail{background:rgba(220,38,38,.2);border-color:rgba(252,165,165,.3)}
.hpill.ch-pill{background:rgba(124,58,237,.25);border-color:rgba(167,139,250,.35);display:flex;align-items:center;gap:4px;transition:background .3s}
.hpill.ch-ok{background:rgba(22,163,74,.25);border-color:rgba(134,239,172,.4)}
.hpill.ch-fail{background:rgba(220,38,38,.2);border-color:rgba(252,165,165,.3)}
.pc-dot{width:6px;height:6px;border-radius:50%;background:currentColor;opacity:.8}
.thm{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#fff;font-size:.85rem;transition:background .2s}
.thm:hover{background:rgba(255,255,255,.25)}
/* MAIN */
.main{display:grid;grid-template-columns:388px 1fr;gap:9px;padding:9px;overflow:hidden}
/* PANEL */
.pnl{background:var(--sf);border:1px solid var(--bd);border-radius:11px;display:flex;flex-direction:column;overflow:hidden}
/* TOOLBAR */
.tb{display:flex;align-items:center;gap:3px;padding:5px 7px;background:var(--sf2);border-bottom:1px solid var(--bd);overflow-x:auto;flex-shrink:0}
.tbs{width:1px;background:var(--bd);height:18px;flex-shrink:0;margin:0 2px}
.tbl{font-size:.58rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.4px;flex-shrink:0;white-space:nowrap}
.btn{height:26px;padding:0 8px;border:1px solid var(--bd);border-radius:5px;background:var(--sf);color:var(--tx);font-family:'Inter',sans-serif;font-size:.68rem;font-weight:500;cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:3px;transition:all .15s;flex-shrink:0;position:relative}
.btn:hover{background:var(--ac-d);border-color:var(--ac);color:var(--ac)}
.btn.act{background:var(--ac);color:#fff;border-color:var(--ac)}
.btn.d:hover{background:var(--er-bg);border-color:var(--er);color:var(--er)}
.btn:disabled{opacity:.4;cursor:not-allowed}
/* Tooltip */
.btn[data-tip]:hover::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);background:#1a1c2e;color:#e2e6f8;font-size:.6rem;line-height:1.35;text-align:center;white-space:normal;width:max-content;max-width:180px;padding:6px 8px;border-radius:5px;box-shadow:0 4px 12px rgba(0,0,0,.22);pointer-events:none;z-index:100;font-family:'Inter',sans-serif;font-weight:400}
.btn[data-tip]:hover::before{content:'';position:absolute;bottom:calc(100% + 1px);left:50%;transform:translateX(-50%);border:4px solid transparent;border-top-color:#1a1c2e;pointer-events:none;z-index:100}
.asel{height:26px;padding:0 5px;border:1px solid var(--bd);border-radius:5px;background:var(--sf);color:var(--tx);font-size:.68rem;cursor:pointer;flex-shrink:0}
/* Element palette */
.elpal{display:flex;gap:2px;flex-shrink:0}
.elb{width:26px;height:26px;border:1px solid var(--bd);border-radius:5px;background:var(--sf);color:var(--tx);font-size:.7rem;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s;font-family:'Space Mono',monospace}
.elb:hover{background:var(--ac-d);border-color:var(--ac);color:var(--ac)}
.elb[data-tip]{position:relative}
.elb[data-tip]:hover::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);background:#1a1c2e;color:#e2e6f8;font-size:.6rem;line-height:1.35;text-align:center;white-space:normal;width:max-content;max-width:150px;padding:6px 8px;border-radius:5px;box-shadow:0 4px 12px rgba(0,0,0,.22);pointer-events:none;z-index:100;font-family:'Inter',sans-serif;font-weight:400}
.elb.act{background:var(--ac);color:#fff;border-color:var(--ac)}
.elb[data-el="N"].act{background:#3b82f6;border-color:#3b82f6}
.elb[data-el="O"].act{background:#dc2626;border-color:#dc2626}
.elb[data-el="S"].act{background:#ca8a04;border-color:#ca8a04}
.elb[data-el="F"].act,.elb[data-el="Cl"].act,.elb[data-el="Br"].act,.elb[data-el="I"].act{background:#7c3aed;border-color:#7c3aed}
/* CANVAS */
#mol-cv{flex:1;display:block;cursor:crosshair;min-height:0;background:var(--cv)}
/* Hint bar */
.hint{padding:3px 9px;background:var(--sf2);border-top:1px solid var(--bd);font-size:.6rem;color:var(--mu);flex-shrink:0;display:flex;align-items:center;gap:8px}
#editor-status{margin-left:auto;color:var(--ac);font-family:'Space Mono',monospace;white-space:nowrap}
.hint kbd{background:var(--bd);border-radius:3px;padding:0 4px;font-family:'Space Mono',monospace;font-size:.58rem;color:var(--tx)}
/* SMILES */
.sb{display:flex;align-items:center;gap:5px;padding:5px 7px;background:var(--sf2);border-top:1px solid var(--bd);flex-shrink:0}
.sl{font-family:'Space Mono',monospace;font-size:.6rem;font-weight:700;color:var(--ac);text-transform:uppercase;letter-spacing:.4px;flex-shrink:0}
.si{flex:1;height:27px;padding:0 8px;border:1px solid var(--bd);border-radius:5px;background:var(--sf);color:var(--tx);font-family:'Space Mono',monospace;font-size:.7rem;min-width:0}
.si:focus{outline:none;border-color:var(--ac);box-shadow:0 0 0 3px var(--ac-s)}
.ab{height:27px;padding:0 12px;background:var(--ac);color:#fff;border:none;border-radius:5px;font-size:.7rem;font-weight:600;cursor:pointer;flex-shrink:0;font-family:'Inter',sans-serif;transition:background .15s;display:flex;align-items:center;gap:5px}
.ab:hover:not(:disabled){background:#3d4ebe}
.ab:disabled{opacity:.6;cursor:not-allowed}
/* TEMPLATES */
.tpb{display:flex;align-items:center;gap:5px;padding:4px 7px;border-top:1px solid var(--bd);flex-shrink:0}
.tplbl{font-size:.63rem;color:var(--mu);flex-shrink:0;white-space:nowrap}
.tpsel{flex:1;height:26px;padding:0 5px;border:1px solid var(--bd);border-radius:5px;background:var(--sf);color:var(--tx);font-size:.68rem;cursor:pointer;min-width:0}
/* TABS */
.tabs{display:flex;background:var(--sf2);border-bottom:1px solid var(--bd);flex-shrink:0}
.tab{flex:1;height:38px;display:flex;align-items:center;justify-content:center;gap:5px;font-size:.72rem;font-weight:600;color:var(--mu);cursor:pointer;border-bottom:2px solid transparent;transition:all .15s}
.tab:hover{color:var(--ac)}
.tab.act{color:var(--ac);border-bottom-color:var(--ac);background:var(--sf)}
.tcon{flex:1;overflow-y:auto;padding:12px;min-height:0}
.tpn{display:none;flex-direction:column;gap:10px}
.tpn.act{display:flex}
/* Stereochemistry / lead design */
.st-hero{padding:12px;border:1px solid var(--ac-s);border-radius:9px;background:var(--ac-d)}
.st-hero h3{margin:0 0 5px;font-size:.88rem;color:var(--tx)}
.st-hero p,.st-note{margin:0;color:var(--mu);font-size:.72rem;line-height:1.5}
.st-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.st-card{padding:10px;border:1px solid var(--bd);border-radius:8px;background:var(--sf2);display:flex;flex-direction:column;gap:7px}
.st-card h4{margin:0;font-size:.78rem;color:var(--tx)}
.st-metric{font-family:'Space Mono',monospace;font-size:.69rem;color:var(--ac)}
.st-actions{display:flex;gap:5px;flex-wrap:wrap}
.st-action{border:1px solid var(--ac);border-radius:5px;background:var(--sf);color:var(--ac);padding:4px 7px;font-size:.65rem;font-weight:700;cursor:pointer}
.st-action:hover{background:var(--ac);color:#fff}
.st-warn{padding:9px 10px;border-radius:7px;background:var(--wa-bg);border:1px solid var(--wa-br);color:#854d0e;font-size:.7rem;line-height:1.45}
.st-lead{padding:10px;border:1px solid var(--bd);border-radius:8px;background:var(--sf2);font-size:.72rem;line-height:1.55;color:var(--tx)}
.st-lead ul{margin:6px 0 0;padding-left:17px}.st-lead li+li{margin-top:3px}
@media(max-width:900px){.st-grid{grid-template-columns:1fr}}
/* Structure */
#svc{width:100%;height:255px;display:block;border-radius:8px;border:1px solid var(--bd);background:var(--cv)}
.chips{display:flex;gap:6px;flex-wrap:wrap}
.chip{background:var(--ac-d);color:var(--ac);border:1px solid var(--ac-s);padding:3px 9px;border-radius:100px;font-size:.68rem;font-family:'Space Mono',monospace;font-weight:700}
.chip.pcc{background:var(--pc-bg);color:var(--pc);border-color:var(--pc-br)}
/* IUPAC box */
.iupac-box{padding:10px 12px;border-radius:8px;border:1px solid var(--bd);background:var(--sf2);display:flex;flex-direction:column;gap:4px}
.iupac-label{font-size:.6rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.4px;display:flex;align-items:center;gap:6px}
.iupac-name{font-family:'Space Mono',monospace;font-size:.85rem;color:var(--tx);word-break:break-all;line-height:1.45}
/* Properties */
.sec{font-size:.62rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px;display:flex;align-items:center;gap:6px}
.sec::after{content:'';flex:1;height:1px;background:var(--bd)}
.pg{display:grid;grid-template-columns:1fr 1fr 1fr;gap:7px}
.pcard{border-radius:8px;padding:11px 12px;border:1px solid var(--bd);background:var(--sf2)}
.pcard.ok{background:var(--ok-bg);border-color:var(--ok-br)}
.pcard.fail{background:var(--er-bg);border-color:var(--er-br)}
.pcard.warn{background:var(--wa-bg);border-color:var(--wa-br)}
.pn{font-size:.6rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.3px;margin-bottom:4px}
.pv{font-family:'Space Mono',monospace;font-size:1.25rem;font-weight:700;font-variant-numeric:tabular-nums;line-height:1}
.ok .pv{color:var(--ok)}.fail .pv{color:var(--er)}.warn .pv{color:var(--wa)}
.pu{font-size:.6rem;color:var(--mu);margin-top:1px}
.pb{display:inline-block;font-size:.6rem;font-weight:700;padding:2px 7px;border-radius:100px;margin-top:5px}
.ok .pb{background:var(--ok);color:#fff}.fail .pb{background:var(--er);color:#fff}.warn .pb{background:var(--wa);color:#fff}
.plain .pb{background:var(--ac);color:#fff}
.src-tag{display:inline-block;font-size:.55rem;font-weight:700;padding:1px 5px;border-radius:3px;margin-left:4px;vertical-align:middle;letter-spacing:.3px;text-transform:uppercase}
.src-pc{background:var(--pc-bg);color:var(--pc);border:1px solid var(--pc-br)}
.src-est{background:var(--wa-bg);color:var(--wa);border:1px solid var(--wa-br)}
.vrd{padding:10px 14px;border-radius:8px;font-size:.82rem;font-weight:700;text-align:center}
.vrd.ok{background:var(--ok-bg);color:var(--ok);border:1px solid var(--ok-br)}
.vrd.fail{background:var(--er-bg);color:var(--er);border:1px solid var(--er-br)}
.note{font-size:.68rem;color:var(--mu);line-height:1.55;padding:8px 12px;background:var(--sf2);border-radius:8px;border-left:3px solid var(--ac)}
.term{position:relative;border-bottom:1px dotted currentColor;cursor:help}
.term::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 7px);left:50%;transform:translateX(-50%);width:220px;padding:7px 9px;border-radius:5px;background:#1a1c2e;color:#e2e6f8;font-size:.62rem;font-weight:400;line-height:1.4;text-align:center;white-space:normal;box-shadow:0 4px 14px rgba(0,0,0,.24);opacity:0;visibility:hidden;pointer-events:none;transition:opacity .15s;z-index:120}
.term:hover::after{opacity:1;visibility:visible}
.note.pc-note{border-left-color:var(--pc)}
/* pKa */
.pka-list{display:flex;flex-direction:column;gap:6px}
.pka-row{display:grid;grid-template-columns:110px 80px 1fr 90px;align-items:center;gap:8px;padding:10px 12px;border-radius:8px;border:1px solid var(--bd);background:var(--sf2);font-size:.75rem}
.pka-grp{font-family:'Space Mono',monospace;font-size:.7rem;font-weight:700;color:var(--ac)}
.pka-val{font-family:'Space Mono',monospace;font-weight:700;font-size:1rem;font-variant-numeric:tabular-nums;color:var(--tx)}
.pka-desc{font-size:.68rem;color:var(--mu)}
.ionized-bar{height:10px;border-radius:5px;background:var(--bd);overflow:hidden}
.ionized-fill{height:100%;border-radius:5px;background:var(--ac);transition:width .4s}
.ionized-pct{font-size:.65rem;font-family:'Space Mono',monospace;font-weight:700;color:var(--ac)}
.logd-box{padding:12px;border-radius:8px;border:1px solid var(--bd);background:var(--sf2)}
.logd-title{font-size:.62rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.3px;margin-bottom:8px}
.logd-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}
.logd-lbl{font-size:.7rem;color:var(--mu)}
.logd-val{font-family:'Space Mono',monospace;font-size:.85rem;font-weight:700;color:var(--ac)}
.adme-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.adme-row{display:flex;justify-content:space-between;align-items:center;padding:8px 10px;border-radius:7px;border:1px solid var(--bd);background:var(--sf2);font-size:.7rem}
.adme-lbl{color:var(--mu);font-weight:500}
.adme-val{font-weight:700;padding:2px 8px;border-radius:100px;font-size:.65rem}
.av-hi{background:var(--ok-bg);color:var(--ok)}
.av-lo{background:var(--er-bg);color:var(--er)}
.av-md{background:var(--wa-bg);color:var(--wa)}
.empty{text-align:center;padding:30px 20px;color:var(--mu);font-size:.78rem}
.ico{font-size:2rem;margin-bottom:6px}
.spin{display:inline-block;width:13px;height:13px;border:2px solid rgba(255,255,255,.35);border-top-color:#fff;border-radius:50%;animation:spin .7s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.pc-link{display:inline-flex;align-items:center;gap:4px;font-size:.65rem;color:var(--pc);text-decoration:none;font-weight:700;padding:3px 8px;border-radius:100px;background:var(--pc-bg);border:1px solid var(--pc-br);transition:opacity .15s}
.pc-link:hover{opacity:.8}
/* Análise tab */
.fg-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.fg-card{border-radius:8px;padding:10px 12px;border:1px solid var(--bd);background:var(--sf2);display:flex;flex-direction:column;gap:3px}
.fg-header{display:flex;align-items:center;justify-content:space-between}
.fg-name{font-weight:700;font-size:.75rem;color:var(--tx)}
.fg-cnt{font-size:.65rem;font-weight:700;padding:2px 8px;border-radius:100px;background:var(--ac);color:#fff}
.fg-desc{font-size:.65rem;color:var(--mu);line-height:1.4}
.stat-row{display:flex;justify-content:space-between;align-items:center;padding:8px 10px;border-radius:7px;border:1px solid var(--bd);background:var(--sf2);margin-bottom:5px}
.stat-lbl{font-size:.7rem;color:var(--mu);font-weight:500}
.stat-val{font-family:'Space Mono',monospace;font-size:.85rem;font-weight:700;color:var(--ac)}
/* FOOTER */
.ftr{display:flex;align-items:center;justify-content:center;gap:8px;font-size:.6rem;color:var(--mu);background:var(--sf2);border-top:1px solid var(--bd);padding:0 18px;font-family:'Space Mono',monospace}
.ftr a{color:var(--ac);text-decoration:none}
.ftr a:hover{text-decoration:underline}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--bd);border-radius:99px}
</style>

<div class="app">
  <header class="hdr">
    <span style="font-size:1.4rem">⚗️</span>
    <div>
      <div class="hl">Chem<span>Med</span></div>
      <div class="hs">Editor Molecular · Química Medicinal</div>
    </div>
    <div class="hpills">
      <span class="hpill">Lipinski Ro5</span>
      <span class="hpill">pKa / LogD</span>
      <span class="hpill">ADME</span>
      <span class="hpill pc-pill" id="pc-status"><span class="pc-dot"></span>PubChem</span>
      <span class="hpill ch-pill" id="ch-status"><span class="pc-dot"></span>ChEMBL</span>
      <button class="thm" onclick="toggleTheme()" title="Alternar tema">☀</button>
    </div>
  </header>

  <div class="main">
    <!-- EDITOR -->
    <div class="pnl">
      <div class="tb">
        <span class="tbl">Modo</span>
        <button class="btn act" id="t-draw" onclick="setTool('draw')" data-tip="Desenhar átomos e ligações (D)">✏ Desenhar</button>
        <button class="btn" id="t-sel" onclick="setTool('sel')" data-tip="Mover átomos no canvas (M)">↖ Mover</button>
        <button class="btn" id="t-era" onclick="setTool('era')" data-tip="Apagar átomos ou ligações (Del)">⌫ Apagar</button>
        <div class="tbs"></div>
        <button class="btn" id="undo-btn" onclick="undo()" data-tip="Desfazer última alteração (Ctrl+Z)" disabled>↩</button>
        <button class="btn" id="redo-btn" onclick="redo()" data-tip="Refazer alteração (Ctrl+Y)" disabled>↪</button>
        <button class="btn" onclick="centerMol()" data-tip="Centralizar a molécula no canvas">⊕</button>
        <button class="btn" onclick="editor.optimize2D()" data-tip="Organizar 2D - otimizar geometria">↔</button>
        <button class="btn" onclick="copySmiles()" data-tip="Copiar o SMILES atual">⧉ SMILES</button>
        <button class="btn" onclick="editor.exportPng()" data-tip="Baixar a estrutura desenhada como PNG">▣ PNG</button>
        <div class="tbs"></div>
        <span class="tbl">Ligação</span>
        <button class="btn act" id="b1" onclick="setBo(1)" data-tip="Selecionar ligação simples">─</button>
        <button class="btn" id="b2" onclick="setBo(2)" data-tip="Selecionar ligação dupla">═</button>
        <button class="btn" id="b3" onclick="setBo(3)" data-tip="Selecionar ligação tripla">≡</button>
        <div class="tbs"></div>
        <select class="asel" id="funcGroupSel" onchange="setFuncGroup(this.value)" data-tip="Adicionar grupo funcional">
          <option value="">Grupos funcionais</option>
          <option value="O">-OH (Hidroxila)</option>
          <option value="N">-NH₂ (Amina)</option>
          <option value="C(=O)O">-COOH (Ácido)</option>
          <option value="C(=O)">-C=O (Carbonila)</option>
          <option value="Cl">-Cl (Cloro)</option>
          <option value="Br">-Br (Bromo)</option>
          <option value="F">-F (Flúor)</option>
          <option value="I">-I (Iodo)</option>
        </select>
        <div class="tbs"></div>
        <span class="tbl">Anéis</span>
        <button class="btn ring-btn" onclick="startRing(6,true)" data-tip="Inserir anel benzênico aromático">⬡</button>
        <button class="btn ring-btn" onclick="startRing(6,false)" data-tip="Inserir anel alifático de 6 átomos">○6</button>
        <button class="btn ring-btn" onclick="startRing(5,false)" data-tip="Inserir anel alifático de 5 átomos">○5</button>
        <div class="tbs"></div>
        <button class="btn d" onclick="clearAll()" data-tip="Limpar tudo">✕</button>
      </div>
      <!-- Element palette -->
      <div class="tb" style="border-bottom:none;border-top:1px solid var(--bd);padding:4px 7px;gap:3px">
        <span class="tbl">Átomo</span>
        <div class="elpal" id="elpal">
          <button class="elb act" data-el="C" onclick="setEl('C')" title="Carbono (C)" data-tip="Adicionar ou editar como carbono">C</button>
          <button class="elb" data-el="N" onclick="setEl('N')" title="Nitrogênio (N)" data-tip="Adicionar ou editar como nitrogênio">N</button>
          <button class="elb" data-el="O" onclick="setEl('O')" title="Oxigênio (O)" data-tip="Adicionar ou editar como oxigênio">O</button>
          <button class="elb" data-el="S" onclick="setEl('S')" title="Enxofre (S)" data-tip="Adicionar ou editar como enxofre">S</button>
          <button class="elb" data-el="P" onclick="setEl('P')" title="Fósforo (P)" data-tip="Adicionar ou editar como fósforo">P</button>
          <button class="elb" data-el="F" onclick="setEl('F')" title="Flúor (F)" data-tip="Adicionar ou editar como flúor">F</button>
          <button class="elb" data-el="Cl" onclick="setEl('Cl')" title="Cloro (Cl)" data-tip="Adicionar ou editar como cloro">Cl</button>
          <button class="elb" data-el="Br" onclick="setEl('Br')" title="Bromo (Br)" data-tip="Adicionar ou editar como bromo">Br</button>
          <button class="elb" data-el="I" onclick="setEl('I')" title="Iodo (I)" data-tip="Adicionar ou editar como iodo">I</button>
        </div>
        <div class="tbs"></div>
        <span style="font-size:.6rem;color:var(--mu);white-space:nowrap">Clique duplo no átomo para editar</span>
      </div>
      <canvas id="mol-cv"></canvas>
      <div class="hint">
        <span>✏ Arrastar = nova ligação · Clique vazio = novo átomo · Clique duplo = editar elemento</span>
        <span>|</span>
        <span><kbd>D</kbd> Desenhar · <kbd>M</kbd> Selecionar/mover · <kbd>Del</kbd> exclui seleção · <kbd>Esc</kbd> cancela · <kbd>Ctrl+Z</kbd> Desfazer · <kbd>1/2/3</kbd> Ordem</span>
        <span id="editor-status" aria-live="polite"></span>
      </div>
      <div class="sb">
        <span class="sl">SMILES</span>
        <input class="si" id="si" type="text" value="CC(=O)Oc1ccccc1C(=O)O" placeholder="SMILES ou nome IUPAC — ex: aspirin"
               onkeydown="if(event.key==='Enter')analyze()">
        <button class="ab" id="import-btn" onclick="importSmilesToEditor()" title="Importar o SMILES no canvas sem consultar bases externas">↳ Importar</button>
        <button class="ab" id="analyze-btn" onclick="analyze()">▶ Analisar</button>
      </div>
      <div class="tpb">
        <span class="tplbl">Exemplos:</span>
        <select class="tpsel" id="tpsel" onchange="loadTpl()">
          <option value="">— Selecione molécula —</option>
          <optgroup label="Fármacos">
            <option value="CC(=O)Oc1ccccc1C(=O)O">Aspirina</option>
            <option value="CC(=O)Nc1ccc(O)cc1">Paracetamol</option>
            <option value="CC(C)Cc1ccc(cc1)C(C)C(=O)O">Ibuprofeno</option>
            <option value="Cn1cnc2c1c(=O)n(c(=O)n2C)C">Cafeína</option>
            <option value="CN1C(=O)CN=C(c2ccccc2)c3cc(Cl)ccc13">Diazepam</option>
            <option value="OC(=O)Cc1c[nH]c2ccc(O)cc12">5-Hidroxitriptofano</option>
            <option value="CC(=O)Nc1ccc(cc1)S(N)(=O)=O">Sulfanilamida</option>
            <option value="CCC(C)(C)C(=O)O[C@H]1C[C@H](C=C2[C@H]1[C@H]([C@H](C=C2)C)CC[C@@H]3C[C@H](CC(=O)O3)O)C">Sinvastatina</option>
            <option value="CC(C)C1=NC(=NC(=C1/C=C/[C@H](C[C@H](CC(=O)O)O)O)C2=CC=C(C=C2)F)N(C)S(=O)(=O)C">Rosuvastatina</option>
          </optgroup>
          <optgroup label="Neurotransmissores">
            <option value="NCCc1ccc(O)c(O)c1">Dopamina</option>
            <option value="NCCc1c[nH]c2ccc(O)cc12">Serotonina</option>
            <option value="CNC[C@@H](O)c1ccc(O)c(O)c1">Adrenalina</option>
            <option value="NCCCC(=O)O">GABA</option>
          </optgroup>
          <optgroup label="Referência">
            <option value="c1ccccc1">Benzeno</option>
            <option value="c1ccncc1">Piridina</option>
            <option value="CC(=O)O">Ác. Acético</option>
            <option value="Oc1ccccc1">Fenol</option>
            <option value="CN">Metilamina</option>
            <option value="OC(=O)c1ccccc1">Ác. Benzóico</option>
            <option value="NC1=CC=CC=C1">Anilina</option>
            <option value="OC(=O)CC(O)=O">Ác. Malônico</option>
          </optgroup>
        </select>
      </div>
    </div>

    <!-- ANALYSIS -->
    <div class="pnl">
      <div class="tabs">
        <div class="tab act" onclick="showTab('str',this)">🔬 Estrutura</div>
        <div class="tab" onclick="showTab('lip',this)">⚖️ Lipinski + Prop.</div>
        <div class="tab" onclick="showTab('pka',this)">🧪 pKa / Ionização</div>
        <div class="tab" onclick="showTab('ana',this)">🔎 Análise</div>
        <div class="tab" onclick="showTab('stereo',this)">◈ Estereo</div>
        <div class="tab" onclick="showTab('che',this)">💊 ChEMBL</div>
      </div>
      <div class="tcon">
        <div class="tpn act" id="tp-str">
          <canvas id="svc"></canvas>
          <div id="iupac-box-container"></div>
          <div class="chips" id="chips"></div>
          <div class="empty" id="str-empty"><div class="ico">🔬</div>Selecione um exemplo ou escreva um SMILES e clique ▶ Analisar</div>
        </div>
        <div class="tpn" id="tp-lip">
          <div id="lip-out"><div class="empty"><div class="ico">⚖️</div>Carregue uma molécula</div></div>
        </div>
        <div class="tpn" id="tp-pka">
          <div id="pka-out"><div class="empty"><div class="ico">🧪</div>Carregue uma molécula</div></div>
        </div>
        <div class="tpn" id="tp-ana">
          <div id="ana-out"><div class="empty"><div class="ico">🔎</div>Carregue uma molécula para análise estrutural</div></div>
        </div>
        <div class="tpn" id="tp-stereo">
          <div id="stereo-out"></div>
        </div>
        <div class="tpn" id="tp-che">
          <div id="che-out"><div class="empty"><div class="ico">💊</div>Carregue uma molécula para buscar no ChEMBL</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="ftr">
    <span>⚗️ ChemMed · Desenvolvido por <strong>Msc. Marcos Gregório</strong></span>
    <span>·</span>
    <span>UFPE — Química Medicinal</span>
    <span>·</span>
    <span>Dados: <a href="https://pubchem.ncbi.nlm.nih.gov" target="_blank">PubChem NIH/NLM</a></span>
  </footer>
</div>

<script>
''' + sd_js + r'''
</script>
<script>
// ─── THEME ────────────────────────────────────────────────
function toggleTheme(){
  const r=document.documentElement,t=r.dataset.theme;
  if(!t)r.dataset.theme=window.matchMedia('(prefers-color-scheme:dark)').matches?'light':'dark';
  else if(t==='dark')r.dataset.theme='light';
  else delete r.dataset.theme;
  editor.draw();
}

// ─── PUBCHEM STATUS ───────────────────────────────────────
function setPCStatus(state){
  // state: 'idle'|'loading'|'ok'|'fail'
  const el=document.getElementById('pc-status');
  el.className='hpill pc-pill';
  if(state==='ok'){el.classList.add('pc-ok');el.innerHTML='<span class="pc-dot"></span>PubChem ✓';}
  else if(state==='fail'){el.classList.add('pc-fail');el.innerHTML='<span class="pc-dot"></span>PubChem ✗';}
  else if(state==='loading'){el.innerHTML='<span class="spin" style="width:8px;height:8px;border-width:1.5px"></span> PubChem...';}
  else{el.innerHTML='<span class="pc-dot"></span>PubChem';}
}

// ─── ELEMENT PALETTE ─────────────────────────────────────
function setEl(el){
  editor.el=el;
  document.querySelectorAll('.elb').forEach(b=>b.classList.toggle('act',b.dataset.el===el));
}
function setEditorStatus(message){
  document.getElementById('editor-status').textContent=message;
}

// ─── MOLECULAR EDITOR ─────────────────────────────────────
const ATOM_COLORS={C:'--bn',N:'--an',O:'--ao',S:'--as',P:'--ap',F:'--ah',Cl:'--ah',Br:'--ah',I:'--ah'};
const ATOM_R={C:12,N:13,O:13,S:14,P:14,F:11,Cl:14,Br:14,I:14};
const BOND_LEN=58;
function getValence(element){
  const valenceTable={
    C:{maxBonds:4,lonePairs:0,hybrid:'sp3',naturalCharge:0},
    N:{maxBonds:3,lonePairs:1,hybrid:'sp3',naturalCharge:0},
    O:{maxBonds:2,lonePairs:2,hybrid:'sp3',naturalCharge:0},
    S:{maxBonds:2,lonePairs:2,hybrid:'sp3',naturalCharge:0},
    P:{maxBonds:3,lonePairs:1,hybrid:'sp3',naturalCharge:0},
    F:{maxBonds:1,lonePairs:3,hybrid:'sp3',naturalCharge:0},
    Cl:{maxBonds:1,lonePairs:3,hybrid:'sp3',naturalCharge:0},
    Br:{maxBonds:1,lonePairs:3,hybrid:'sp3',naturalCharge:0},
    I:{maxBonds:1,lonePairs:3,hybrid:'sp3',naturalCharge:0},
    B:{maxBonds:3,lonePairs:0,hybrid:'sp2',naturalCharge:0},
    H:{maxBonds:1,lonePairs:0,hybrid:'s',naturalCharge:0}
  };
  return valenceTable[element]||{maxBonds:2,lonePairs:2,hybrid:'sp3',naturalCharge:0};
}
function validateBondCreation(editor,fromAtomId,toAtomId,order){
  const fa=editor.atoms.find(a=>a.id===fromAtomId);
  const ta=editor.atoms.find(a=>a.id===toAtomId);
  if(!fa||!ta)return{valid:false,msg:'Átomo inválido'};
  const fv=getValence(fa.el),tv=getValence(ta.el);
  const fBonds=(editor.adj[fromAtomId]||[]).reduce((sum,nb)=>{
    const b=editor.bonds.find(b=>(b.from===fromAtomId&&b.to===nb.nb)||(b.from===nb.nb&&b.to===fromAtomId));
    return sum+(b?.order||1);
  },0);
  const tBonds=(editor.adj[toAtomId]||[]).reduce((sum,nb)=>{
    const b=editor.bonds.find(b=>(b.from===toAtomId&&b.to===nb.nb)||(b.from===nb.nb&&b.to===toAtomId));
    return sum+(b?.order||1);
  },0);
  if(fBonds+order>fv.maxBonds)return{valid:false,msg:`${fa.el} excede valência (máx ${fv.maxBonds})`};
  if(tBonds+order>tv.maxBonds)return{valid:false,msg:`${ta.el} excede valência (máx ${tv.maxBonds})`};
  return{valid:true,msg:`Ligação válida`};
}
const MAX_HIST=20;

class MolEditor{
  constructor(cv){
    this.cv=cv;this.cx=cv.getContext('2d');
    this.atoms=[];this.bonds=[];this.adj={};
    this.nA=0;this.nB=0;this.sel=-1;this.selBond=-1;
    this.tool='draw';this.el='C';this.bo=1;
    this.drag=null;this.ringMode=false;this.ringN=6;this.ringAro=true;
    this.mx=0;this.my=0; // mouse position for cursor preview
    this._hist=[];this._hIdx=-1;
    this._rsz();
    new ResizeObserver(()=>this._rsz()).observe(cv);
    cv.addEventListener('mousedown',e=>this._md(e));
    cv.addEventListener('mousemove',e=>this._mm(e));
    cv.addEventListener('mouseup',e=>this._mu(e));
    cv.addEventListener('dblclick',e=>this._db(e));
    cv.addEventListener('contextmenu',e=>{e.preventDefault();this._rc(e);});
    cv.addEventListener('mouseleave',()=>{this.drag=null;this.mx=-999;this.my=-999;this.draw();});
    this.draw();
  }
  _rsz(){
    const r=this.cv.getBoundingClientRect(),d=devicePixelRatio||1;
    this.cv.width=r.width*d;this.cv.height=r.height*d;
    this.cx.scale(d,d);this._w=r.width;this._h=r.height;this.draw();
  }
  _pos(e){const r=this.cv.getBoundingClientRect();return{x:e.clientX-r.left,y:e.clientY-r.top};}
  _atomAt(x,y){for(const a of this.atoms){if(Math.hypot(x-a.x,y-a.y)<=(ATOM_R[a.el]||12)+6)return a.id;}return -1;}
  _bondNear(x,y){
    for(const b of this.bonds){
      const a1=this.atoms.find(a=>a.id===b.from),a2=this.atoms.find(a=>a.id===b.to);
      if(!a1||!a2)continue;
      const dx=a2.x-a1.x,dy=a2.y-a1.y,l2=dx*dx+dy*dy;
      if(!l2)continue;
      const t=Math.max(0,Math.min(1,((x-a1.x)*dx+(y-a1.y)*dy)/l2));
      if(Math.hypot(x-(a1.x+t*dx),y-(a1.y+t*dy))<9)return b.id;
    }return -1;
  }
  _snap(x,y,fromX,fromY){
    const ang=Math.atan2(y-fromY,x-fromX);
    return Math.round(ang/(Math.PI/6))*(Math.PI/6);
  }
  _snapContextual(x,y,fromAtomId){
    const fa=this.atoms.find(a=>a.id===fromAtomId);
    if(!fa)return this._snap(x,y,0,0);
    const targetAng=Math.atan2(y-fa.y,x-fa.x);
    const neighbors=(this.adj[fromAtomId]||[]).map(nb=>{
      const na=this.atoms.find(a=>a.id===nb.nb);
      return na?Math.atan2(na.y-fa.y,na.x-fa.x):null;
    }).filter(a=>a!==null);
    const candidates=[0,Math.PI/3,2*Math.PI/3,Math.PI,-Math.PI/3,-2*Math.PI/3];
    let bestAng=candidates[0],minConflict=Infinity;
    for(const candidate of candidates){
      let conflict=0;
      for(const nAng of neighbors){
        const diff=Math.abs(candidate-nAng);
        const normalizedDiff=Math.min(diff,2*Math.PI-diff);
        if(normalizedDiff<Math.PI/3)conflict+=Math.PI/3-normalizedDiff;
      }
      if(conflict<minConflict){minConflict=conflict;bestAng=candidate;}
    }
    return bestAng;
  }
  _getImplicitH(atomId){
    const a=this.atoms.find(a=>a.id===atomId);
    if(!a)return 0;
    const reactiveElements={N:true,O:true,S:true,P:true};
    if(!reactiveElements[a.el])return 0;
    const valenceMap={N:3,O:2,S:2,P:3,F:1,Cl:1,Br:1,I:1};
    const maxBonds=valenceMap[a.el]||2;
    const bondCount=(this.adj[a.id]||[]).reduce((sum,nb)=>{
      const bond=this.bonds.find(b=>(b.from===a.id&&b.to===nb.nb)||(b.from===nb.nb&&b.to===a.id));
      return sum+(bond?.order||1);
    },0);
    const h=Math.max(0,maxBonds-bondCount-a.ch);
    return h;
  }
  _addFuncGroup(targetAtomId,groupSmiles){
    const ta=this.atoms.find(a=>a.id===targetAtomId);
    if(!ta)return;
    const groupMol=parseSMILES(groupSmiles);
    if(!groupMol.atoms.length)return;
    const gAtomId=this._addA(ta.x+BOND_LEN,ta.y,groupMol.atoms[0].el);
    this._addB(targetAtomId,gAtomId,1);
    for(let i=1;i<groupMol.atoms.length;i++){
      const pa=groupMol.atoms[i-1],ga=groupMol.atoms[i];
      const gb=groupMol.bonds.find(b=>(b.from===pa.id&&b.to===ga.id)||(b.from===ga.id&&b.to===pa.id));
      const off=Math.PI/3*i;
      const newId=this._addA(gAtomId.x+BOND_LEN*Math.cos(off),gAtomId.y+BOND_LEN*Math.sin(off),ga.el);
      this._addB(gAtomId,newId,gb?.order||1);
    }
  }
  _saveHist(){
    const snap={atoms:JSON.parse(JSON.stringify(this.atoms)),bonds:JSON.parse(JSON.stringify(this.bonds)),adj:JSON.parse(JSON.stringify(this.adj)),nA:this.nA,nB:this.nB};
    this._hist=this._hist.slice(0,this._hIdx+1);
    this._hist.push(snap);
    if(this._hist.length>MAX_HIST)this._hist.shift();
    this._hIdx=this._hist.length-1;
    this._updHist();
  }
  _updHist(){
    document.getElementById('undo-btn').disabled=this._hIdx<=0;
    document.getElementById('redo-btn').disabled=this._hIdx>=this._hist.length-1;
  }
  _load(snap){
    this.atoms=JSON.parse(JSON.stringify(snap.atoms));
    this.bonds=JSON.parse(JSON.stringify(snap.bonds));
    this.adj=JSON.parse(JSON.stringify(snap.adj));
    this.nA=snap.nA;this.nB=snap.nB;
    this.sel=-1;this.selBond=-1;
    this._upd();this.draw();
  }
  undo(){if(this._hIdx>0){this._hIdx--;this._load(this._hist[this._hIdx]);this._updHist();}}
  redo(){if(this._hIdx<this._hist.length-1){this._hIdx++;this._load(this._hist[this._hIdx]);this._updHist();}}
  _md(e){
    if(e.button!==0)return;
    const{x,y}=this._pos(e);
    if(this.funcGroupMode){
      const ai=this._atomAt(x,y);
      if(ai>=0){this._addFuncGroup(ai,this.funcGroupMode);this.funcGroupMode=null;document.getElementById('funcGroupSel').value='';document.getElementById('funcGroupSel').classList.remove('act');this._saveHist();this._upd();this.draw();setEditorStatus('Grupo funcional adicionado');}
      else{setEditorStatus('Selecione um átomo');}
      return;
    }
    if(this.ringMode){this._placeRing(x,y);this._saveHist();return;}
    const ai=this._atomAt(x,y);
    if(this.tool==='era'){
      let changed=false;
      if(ai>=0){this._delA(ai);changed=true;}else{const bi=this._bondNear(x,y);if(bi>=0){this._delB(bi);changed=true;}}
      if(changed)this._saveHist();
      this._upd();this.draw();return;
    }
    if(this.tool==='sel'){
      this.sel=ai;
      this.selBond=ai>=0?-1:this._bondNear(x,y);
      if(ai>=0){
        this.drag={t:'mv',id:ai,ox:this.atoms.find(a=>a.id===ai).x,oy:this.atoms.find(a=>a.id===ai).y};
        setEditorStatus(`Átomo ${this.atoms.find(a=>a.id===ai).el} selecionado`);
      }else if(this.selBond>=0)setEditorStatus('Ligação selecionada');
      else setEditorStatus('Seleção limpa');
      this.draw();return;
    }
    // draw tool
    if(ai>=0){this.drag={t:'bd',from:ai,cx:x,cy:y};}
    else{const ni=this._addA(x,y,this.el);this.drag={t:'bd',from:ni,cx:x,cy:y,newAtom:true};this._upd();this.draw();}
  }
  _mm(e){
    const{x,y}=this._pos(e);this.mx=x;this.my=y;
    if(!this.drag){this.draw();return;}
    if(this.drag.t==='mv'){const a=this.atoms.find(a=>a.id===this.drag.id);if(a){a.x=x;a.y=y;}}
    else if(this.drag.t==='bd'){this.drag.cx=x;this.drag.cy=y;}
    this.draw();
  }
  _mu(e){
    if(!this.drag)return;
    const{x,y}=this._pos(e);
    if(this.drag.t==='mv'){
      const a=this.atoms.find(a=>a.id===this.drag.id);
      if(a&&(Math.abs(a.x-this.drag.ox)>2||Math.abs(a.y-this.drag.oy)>2))this._saveHist();
      this.drag=null;this._upd();return;
    }
    if(this.drag.t==='bd'){
      const tgt=this._atomAt(x,y),from=this.drag.from;
      let changed=!!this.drag.newAtom;
      if(tgt>=0&&tgt!==from){
        const ex=this.bonds.find(b=>(b.from===from&&b.to===tgt)||(b.from===tgt&&b.to===from));
        if(ex){ex.order=ex.order===3?1:ex.order+1;}
        else{this._addB(from,tgt,this.bo);}
        changed=true;
      }else if(tgt<0){
        const fa=this.atoms.find(a=>a.id===from);
        if(fa&&Math.hypot(x-fa.x,y-fa.y)>22){
          const ang=this._snapContextual(x,y,from);
          const ni=this._addA(fa.x+Math.cos(ang)*BOND_LEN,fa.y+Math.sin(ang)*BOND_LEN,this.el);
          this._addB(from,ni,this.bo);
          changed=true;
        }
      }
      if(changed)this._saveHist();
    }
    this.drag=null;this._upd();this.draw();
  }
  _db(e){
    const{x,y}=this._pos(e);const ai=this._atomAt(x,y);
    if(ai>=0){
      const a=this.atoms.find(a=>a.id===ai);
      const el=prompt('Elemento (ex: N, O, Cl, Se…):',a.el);
      if(el&&/^[A-Z][a-z]?$/.test(el.trim())){a.el=el.trim();this._saveHist();this._upd();this.draw();}
    }
  }
  _rc(e){
    const{x,y}=this._pos(e);const ai=this._atomAt(x,y);
    let changed=false;
    if(ai>=0){this._delA(ai);changed=true;}else{const bi=this._bondNear(x,y);if(bi>=0){this._delB(bi);changed=true;}}
    if(changed)this._saveHist();
    this._upd();this.draw();
  }
  _addA(x,y,el,aro=false,stereo=null,hx=-1,ch=0){const id=this.nA++;this.atoms.push({id,x,y,el,aro,stereo,hx,ch});this.adj[id]=[];return id;}
  _addB(f,t,order){
    const id=this.nB++;this.bonds.push({id,from:f,to:t,order});
    this.adj[f]=this.adj[f]||[];this.adj[t]=this.adj[t]||[];
    this.adj[f].push({nb:t,bid:id});this.adj[t].push({nb:f,bid:id});
    return id;
  }
  _delA(ai){
    this.bonds.filter(b=>b.from===ai||b.to===ai).forEach(b=>this._delB(b.id));
    this.atoms=this.atoms.filter(a=>a.id!==ai);delete this.adj[ai];
    if(this.sel===ai)this.sel=-1;
  }
  _delB(bi){
    const b=this.bonds.find(b=>b.id===bi);if(!b)return;
    this.bonds=this.bonds.filter(b=>b.id!==bi);
    if(this.adj[b.from])this.adj[b.from]=this.adj[b.from].filter(n=>n.bid!==bi);
    if(this.adj[b.to])this.adj[b.to]=this.adj[b.to].filter(n=>n.bid!==bi);
    if(this.selBond===bi)this.selBond=-1;
  }
  _placeRing(cx,cy){
    const n=this.ringN,r=50;
    const off=-Math.PI/2+(n%2===0?Math.PI/n:0);
    const ids=[];
    for(let i=0;i<n;i++)ids.push(this._addA(cx+r*Math.cos(off+2*Math.PI*i/n),cy+r*Math.sin(off+2*Math.PI*i/n),this.el,this.ringAro));
    for(let i=0;i<n;i++)this._addB(ids[i],ids[(i+1)%n],this.ringAro&&i%2===0?2:1);
    this.ringMode=false;
    document.querySelectorAll('.ring-btn').forEach(b=>b.classList.remove('act'));
    this._upd();setEditorStatus(`${n}-anel ${this.ringAro?'aromático':'alifático'} inserido`);this.draw();
  }
  center(){
    if(!this.atoms.length)return;
    const xs=this.atoms.map(a=>a.x),ys=this.atoms.map(a=>a.y);
    const cx=(Math.min(...xs)+Math.max(...xs))/2,cy=(Math.min(...ys)+Math.max(...ys))/2;
    const dx=this._w/2-cx,dy=this._h/2-cy;
    this.atoms.forEach(a=>{a.x+=dx;a.y+=dy;});
    this._saveHist();setEditorStatus('Molécula centralizada');this.draw();
  }
  _cv(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim();}
  draw(){
    const cx=this.cx,w=this._w||300,h=this._h||300;
    cx.clearRect(0,0,w,h);
    // grid
    const gc=this._cv('--gr');cx.strokeStyle=gc;cx.lineWidth=1;
    for(let x=0;x<=w;x+=22){cx.beginPath();cx.moveTo(x,0);cx.lineTo(x,h);cx.stroke();}
    for(let y=0;y<=h;y+=22){cx.beginPath();cx.moveTo(0,y);cx.lineTo(w,y);cx.stroke();}
    // bonds
    for(const b of this.bonds){
      const a1=this.atoms.find(a=>a.id===b.from),a2=this.atoms.find(a=>a.id===b.to);
      if(a1&&a2)this._drawB(cx,a1,a2,b.order,b.id===this.selBond);
    }
    // ghost bond preview
    if(this.drag&&this.drag.t==='bd'){
      const fa=this.atoms.find(a=>a.id===this.drag.from);
      if(fa){
        const ang=this._snapContextual(this.drag.cx,this.drag.cy,this.drag.from);
        const ex=Math.hypot(this.drag.cx-fa.x,this.drag.cy-fa.y)>22;
        const tx=ex?fa.x+Math.cos(ang)*BOND_LEN:this.drag.cx;
        const ty=ex?fa.y+Math.sin(ang)*BOND_LEN:this.drag.cy;
        // snap target preview
        const tgt=this._atomAt(this.drag.cx,this.drag.cy);
        cx.save();cx.strokeStyle=this._cv('--ac');cx.lineWidth=2;cx.setLineDash([4,4]);cx.globalAlpha=.65;
        cx.beginPath();cx.moveTo(fa.x,fa.y);cx.lineTo(tgt>=0&&tgt!==fa.id?this.atoms.find(a=>a.id===tgt).x:tx,tgt>=0&&tgt!==fa.id?this.atoms.find(a=>a.id===tgt).y:ty);cx.stroke();
        // new atom preview
        if(tgt<0&&ex){
          cx.fillStyle=this._cv('--ac');cx.globalAlpha=.4;cx.beginPath();cx.arc(tx,ty,ATOM_R[this.el]||12,0,2*Math.PI);cx.fill();
          cx.globalAlpha=.8;cx.font=`bold 11px 'Space Mono',monospace`;cx.textAlign='center';cx.textBaseline='middle';
          cx.fillStyle='#fff';cx.fillText(this.el,tx,ty);
        }
        cx.restore();
      }
    }
    // cursor element label (draw mode, no drag)
    if(this.tool==='draw'&&!this.drag&&!this.ringMode&&this.mx>0){
      const hover=this._atomAt(this.mx,this.my);
      if(hover<0){
        cx.save();cx.font=`bold 11px 'Space Mono',monospace`;cx.textAlign='center';cx.textBaseline='middle';
        cx.fillStyle=this._cv('--ac');cx.globalAlpha=.5;
        cx.fillText(this.el,this.mx,this.my-18);
        cx.restore();
      }
    }
    // atoms
    for(const a of this.atoms)this._drawA(cx,a);
  }
  _drawB(cx,a1,a2,order,selected=false){
    const dx=a2.x-a1.x,dy=a2.y-a1.y,len=Math.hypot(dx,dy);
    const nx=-dy/len,ny=dx/len;
    if(selected){
      cx.save();cx.strokeStyle=this._cv('--ac');cx.lineWidth=9;cx.globalAlpha=.18;cx.lineCap='round';
      cx.beginPath();cx.moveTo(a1.x,a1.y);cx.lineTo(a2.x,a2.y);cx.stroke();cx.restore();
    }
    const c=this._cv('--bn');cx.strokeStyle=c;cx.lineWidth=2;cx.lineCap='round';cx.setLineDash([]);
    const g=3;
    if(order===1){cx.beginPath();cx.moveTo(a1.x,a1.y);cx.lineTo(a2.x,a2.y);cx.stroke();}
    else if(order===1.5){
      cx.beginPath();cx.moveTo(a1.x,a1.y);cx.lineTo(a2.x,a2.y);cx.stroke();
      const inset=Math.min(7,len*.18);
      cx.beginPath();cx.moveTo(a1.x+dx/len*inset+nx*g,a1.y+dy/len*inset+ny*g);cx.lineTo(a2.x-dx/len*inset+nx*g,a2.y-dy/len*inset+ny*g);cx.stroke();
    }else if(order===2){
      for(const o of[g,-g]){cx.beginPath();cx.moveTo(a1.x+nx*o,a1.y+ny*o);cx.lineTo(a2.x+nx*o,a2.y+ny*o);cx.stroke();}
    }else{
      for(const o of[0,g*1.6,-g*1.6]){cx.beginPath();cx.moveTo(a1.x+nx*o,a1.y+ny*o);cx.lineTo(a2.x+nx*o,a2.y+ny*o);cx.stroke();}
    }
  }
  _drawA(cx,a){
    const isSel=this.sel===a.id,isC=a.el==='C';
    const r=ATOM_R[a.el]||12,acolor=this._cv(ATOM_COLORS[a.el]||'--bn');
    cx.save();
    if(isSel){cx.strokeStyle=this._cv('--ac');cx.lineWidth=2;cx.setLineDash([3,3]);cx.beginPath();cx.arc(a.x,a.y,r+5,0,2*Math.PI);cx.stroke();}
    cx.setLineDash([]);
    // hover highlight
    const hov=Math.hypot(a.x-this.mx,a.y-this.my)<(r+6);
    if(hov&&!this.drag){cx.strokeStyle=this._cv('--ac');cx.lineWidth=1.5;cx.globalAlpha=.4;cx.beginPath();cx.arc(a.x,a.y,r+4,0,2*Math.PI);cx.stroke();cx.globalAlpha=1;}
    cx.fillStyle=this._cv('--cv');cx.beginPath();cx.arc(a.x,a.y,r+1,0,2*Math.PI);cx.fill();
    cx.font=`bold 12px 'Space Mono',monospace`;cx.textAlign='center';cx.textBaseline='middle';
    cx.fillStyle=acolor;
    const h=this._getImplicitH(a.id);
    const label=h>0?a.el+('₀₁₂₃₄₅₆₇₈₉'[h]):a.el;
    cx.fillText(label,a.x,a.y);
    if(a.stereo){
      cx.fillStyle=this._cv('--ac');cx.font=`bold 9px 'Space Mono',monospace`;cx.textAlign='left';cx.textBaseline='bottom';
      cx.fillText(a.stereo,a.x+r+3,a.y-2);
    }
    cx.restore();
  }
  toSMILES(){
    if(!this.atoms.length)return'';
    const vis=new Set(),rbs=new Map();let rn=1;
    const fr=(id,pb)=>{vis.add(id);for(const nb of(this.adj[id]||[])){if(nb.bid===pb)continue;if(vis.has(nb.nb)){if(!rbs.has(nb.bid))rbs.set(nb.bid,rn++);}else fr(nb.nb,nb.bid);}};
    for(const a of this.atoms)if(!vis.has(a.id))fr(a.id,-1);
    const sv=new Set();
    const dfs=(id,pb)=>{
      sv.add(id);const a=this.atoms.find(a=>a.id===id);
      const aromaticSymbol={C:'c',N:'n',O:'o',P:'p',S:'s'}[a.el];
      const symbol=a.aro&&aromaticSymbol?aromaticSymbol:(['B','C','N','O','P','S','F','Cl','Br','I'].includes(a.el)?a.el:`[${a.el}]`);
      const h=a.hx>0?`H${a.hx>1?a.hx:''}`:'';
      const charge=a.ch?`${a.ch>0?'+':'-'}${Math.abs(a.ch)>1?Math.abs(a.ch):''}`:'';
      let s=a.stereo?`[${symbol}${a.stereo}${h}${charge}]`:symbol;
      for(const nb of(this.adj[id]||[])){
        if(nb.bid===pb)continue;
        if(sv.has(nb.nb)&&rbs.has(nb.bid)){const num=rbs.get(nb.bid);const b=this.bonds.find(b=>b.id===nb.bid);s+=(b.order===2?'=':b.order===3?'#':'')+(num>9?`%${num}`:String(num));}
      }
      const ch=(this.adj[id]||[]).filter(nb=>nb.bid!==pb&&!sv.has(nb.nb));
      ch.forEach((nb,i)=>{const b=this.bonds.find(b=>b.id===nb.bid);const bc=b.order===2?'=':b.order===3?'#':'';const sub=dfs(nb.nb,nb.bid);s+=i<ch.length-1?`(${bc}${sub})`:bc+sub;});
      return s;
    };
    const sv2=new Set(),parts=[];
    for(const a of this.atoms){if(!sv2.has(a.id)){sv.clear();parts.push(dfs(a.id,-1));sv.forEach(id=>sv2.add(id));}}
    return parts.join('.');
  }
  _upd(){document.getElementById('si').value=this.toSMILES();}
  correctLinearity(){
    if(!this.atoms.length)return;
    const currentInput=document.getElementById('si').value;
    try{
      const parsed={
        atoms:this.atoms.map(a=>({id:a.id,el:a.el,aro:!!a.aro,hI:a.hI||0,ch:a.ch||0})),
        bonds:this.bonds.map(b=>({id:b.id,from:b.from,to:b.to,o:b.order,ar:b.order===1.5})),
        adj:JSON.parse(JSON.stringify(this.adj))
      };
      this.loadFromParsed(parsed);
      document.getElementById('si').value=currentInput;
      setEditorStatus('Geometria 2D corrigida');
    }catch(e){console.warn('Não foi possível corrigir a geometria:',e.message);}
  }
  clear(){this.atoms=[];this.bonds=[];this.adj={};this.nA=0;this.nB=0;this.sel=-1;this.selBond=-1;this.drag=null;this._saveHist();this._upd();setEditorStatus('Canvas limpo');this.draw();}
  deleteSelection(){
    let changed=false;
    if(this.sel>=0){this._delA(this.sel);this.sel=-1;changed=true;}
    else if(this.selBond>=0){this._delB(this.selBond);changed=true;}
    if(!changed){setEditorStatus('Selecione um átomo ou ligação primeiro');return;}
    this._saveHist();this._upd();setEditorStatus('Seleção removida');this.draw();
  }
  exportPng(){
    if(!this.atoms.length){setEditorStatus('Desenhe ou importe uma molécula primeiro');return;}
    const link=document.createElement('a');
    link.download='chemmed-estrutura.png';
    link.href=this.cv.toDataURL('image/png');
    link.click();
    setEditorStatus('PNG exportado');
  }

  // ── Load a parsed mol into the editor with auto-layout ──────────
  loadFromParsed(parsedMol){
    if(!parsedMol||!parsedMol.atoms.length)return;
    this.atoms=[];this.bonds=[];this.adj={};this.nA=0;this.nB=0;this.sel=-1;this.selBond=-1;this.drag=null;
    const W=this._w||400,H=this._h||300,STEP=BOND_LEN;
    const snap=a=>Math.round(a/(Math.PI/6))*(Math.PI/6);
    const pos={},placed=new Set();

    // DFS 2-D layout
    const dfs=(id,px,py,inAng,depth)=>{
      placed.add(id);pos[id]={x:px,y:py};
      const nbs=(parsedMol.adj[id]||[]).filter(n=>!placed.has(n.nb));
      if(!nbs.length)return;
      const base=inAng+Math.PI; // direction away from parent
      let angs;
      if(nbs.length===1){
        // Zigzag: alternate ±60° from forward direction
        angs=[snap(base+(depth%2===0?Math.PI/3:-Math.PI/3))];
      }else if(nbs.length===2){
        angs=[snap(base-Math.PI/3),snap(base+Math.PI/3)];
      }else if(nbs.length===3){
        angs=[snap(base-2*Math.PI/3),snap(base),snap(base+2*Math.PI/3)];
      }else{
        const stp=(2*Math.PI)/nbs.length;
        angs=nbs.map((_,i)=>snap(base+(i-(nbs.length-1)/2)*stp));
      }
      for(let i=0;i<nbs.length;i++){
        const a=angs[i];
        dfs(nbs[i].nb,px+Math.cos(a)*STEP,py+Math.sin(a)*STEP,a-Math.PI,depth+1);
      }
    };

    // Layout connected components
    let sx=W/2,sy=H/2;
    for(const a of parsedMol.atoms){
      if(!placed.has(a.id)){dfs(a.id,sx,sy,0,0);sx+=STEP*3;}
    }

    // Regularize simple aromatic rings instead of leaving them as DFS zigzags.
    const aromaticSeen=new Set();
    for(const start of parsedMol.atoms.filter(a=>a.aro)){
      if(aromaticSeen.has(start.id))continue;
      const component=[],queue=[start.id];aromaticSeen.add(start.id);
      while(queue.length){
        const id=queue.shift();component.push(id);
        for(const nb of(parsedMol.adj[id]||[])){
          if(parsedMol.atoms[nb.nb]?.aro&&!aromaticSeen.has(nb.nb)){aromaticSeen.add(nb.nb);queue.push(nb.nb);}
        }
      }
      if(component.length!==6||component.some(id=>(parsedMol.adj[id]||[]).filter(nb=>parsedMol.atoms[nb.nb]?.aro).length!==2))continue;
      const order=[component[0]],used=new Set(order);
      while(order.length<component.length){
        const current=order[order.length-1];
        const next=(parsedMol.adj[current]||[]).find(nb=>parsedMol.atoms[nb.nb]?.aro&&!used.has(nb.nb));
        if(!next)break;
        order.push(next.nb);used.add(next.nb);
      }
      if(order.length!==6)continue;
      const center=order.reduce((sum,id)=>({x:sum.x+pos[id].x/6,y:sum.y+pos[id].y/6}),{x:0,y:0});
      const radius=STEP;
      order.forEach((id,i)=>{const angle=i*Math.PI/3;pos[id]={x:center.x+radius*Math.cos(angle),y:center.y+radius*Math.sin(angle)};});
      const moved=new Set(order);
      for(const ringId of order){
        for(const nb of(parsedMol.adj[ringId]||[])){
          if(parsedMol.atoms[nb.nb]?.aro||moved.has(nb.nb))continue;
          const oldPos=pos[nb.nb],ringPos=pos[ringId];
          if(!oldPos)continue;
          const angle=Math.atan2(ringPos.y-center.y,ringPos.x-center.x);
          const target={x:ringPos.x+Math.cos(angle)*STEP,y:ringPos.y+Math.sin(angle)*STEP};
          const shift={x:target.x-oldPos.x,y:target.y-oldPos.y};
          const queue=[nb.nb];moved.add(nb.nb);
          while(queue.length){
            const id=queue.shift();pos[id]={x:pos[id].x+shift.x,y:pos[id].y+shift.y};
            for(const next of(parsedMol.adj[id]||[])){
              if(!parsedMol.atoms[next.nb]?.aro&&!moved.has(next.nb)){moved.add(next.nb);queue.push(next.nb);}
            }
          }
        }
      }
    }

    // Center result
    const xs=parsedMol.atoms.map(a=>(pos[a.id]||{x:sx}).x);
    const ys=parsedMol.atoms.map(a=>(pos[a.id]||{y:sy}).y);
    const dx=W/2-(Math.min(...xs)+Math.max(...xs))/2;
    const dy=H/2-(Math.min(...ys)+Math.max(...ys))/2;
    const fitted=parsedMol.atoms.map(a=>({x:(pos[a.id]||{x:sx}).x+dx,y:(pos[a.id]||{y:sy}).y+dy}));
    const minFitX=Math.min(...fitted.map(p=>p.x)),maxFitX=Math.max(...fitted.map(p=>p.x));
    const minFitY=Math.min(...fitted.map(p=>p.y)),maxFitY=Math.max(...fitted.map(p=>p.y));
    const scale=Math.min(1,(W-32)/(maxFitX-minFitX||1),(H-32)/(maxFitY-minFitY||1));
    const fitX=W/2-(minFitX+maxFitX)*scale/2,fitY=H/2-(minFitY+maxFitY)*scale/2;

    // Add atoms to editor
    const idMap={};
    for(const a of parsedMol.atoms){
      const p=pos[a.id]||{x:W/2,y:H/2};
      idMap[a.id]=this._addA(p.x*scale+fitX+dx*scale,p.y*scale+fitY+dy*scale,a.el,a.aro,a.stereo||null,a.hx??-1,a.ch||0);
    }

    // Add bonds (aromatic 1.5 → display as 1 single; round others)
    const seen=new Set();
    for(const b of parsedMol.bonds){
      const k=Math.min(b.from,b.to)+','+Math.max(b.from,b.to);
      if(seen.has(k))continue;seen.add(k);
      const ord=b.o===1.5?1.5:(Math.round(b.o)||1);
      this._addB(idMap[b.from],idMap[b.to],Math.max(1,Math.min(3,ord)));
    }

    this._saveHist();this._upd();this.draw();
  }
  detectComponents(){
    const visited=new Set(),components=[];
    const dfs=(id,comp)=>{
      if(visited.has(id))return;
      visited.add(id);comp.push(id);
      for(const nb of(this.adj[id]||[]))if(!visited.has(nb.nb))dfs(nb.nb,comp);
    };
    for(const a of this.atoms){
      if(!visited.has(a.id)){const comp=[];dfs(a.id,comp);components.push(comp);}
    }
    return components;
  }
  detectCycles(){
    const cycles=[],visited=new Set(),rec=new Set();
    const dfs=(id,parent,path)=>{
      visited.add(id);rec.add(id);path.push(id);
      for(const nb of(this.adj[id]||[])){
        if(nb.nb===parent)continue;
        if(!visited.has(nb.nb)){dfs(nb.nb,id,path);}
        else if(rec.has(nb.nb)){
          const cycleStart=path.indexOf(nb.nb);
          if(cycleStart>=0){const cycle=path.slice(cycleStart);if(cycle.length>2&&!cycles.some(c=>c.sort().join(',')===cycle.sort().join(','))){cycles.push(cycle);}}
        }
      }
      rec.delete(id);path.pop();
    };
    for(const a of this.atoms)if(!visited.has(a.id))dfs(a.id,-1,[]);
    return cycles;
  }
  optimize2D(){
    if(!this.atoms.length)return;
    const cycles=this.detectCycles();
    const pos={};
    for(const a of this.atoms)pos[a.id]={x:a.x,y:a.y};
    cycles.forEach(cycle=>{
      if(cycle.length===6){
        const cx=cycle.reduce((s,id)=>s+(pos[id]?.x||0),0)/6;
        const cy=cycle.reduce((s,id)=>s+(pos[id]?.y||0),0)/6;
        const r=BOND_LEN;
        cycle.forEach((id,i)=>{
          const ang=i*Math.PI/3;
          pos[id]={x:cx+r*Math.cos(ang),y:cy+r*Math.sin(ang)};
        });
      }
    });
    for(let iter=0;iter<3;iter++){
      for(const a of this.atoms){
        let fx=0,fy=0;
        for(const nb of(this.adj[a.id]||[])){
          const nb_pos=pos[nb.nb],a_pos=pos[a.id];
          const dx=nb_pos.x-a_pos.x,dy=nb_pos.y-a_pos.y;
          const len=Math.hypot(dx,dy);
          const target=BOND_LEN,fac=(len-target)/(len||1)*0.1;
          fx-=fac*dx;fy-=fac*dy;
        }
        pos[a.id].x+=fx*0.5;pos[a.id].y+=fy*0.5;
      }
    }
    const xs=Object.values(pos).map(p=>p.x),ys=Object.values(pos).map(p=>p.y);
    const ox=this._w/2-(Math.min(...xs)+Math.max(...xs))/2;
    const oy=this._h/2-(Math.min(...ys)+Math.max(...ys))/2;
    for(const a of this.atoms){const p=pos[a.id];a.x=p.x+ox;a.y=p.y+oy;}
    this._saveHist();this._upd();setEditorStatus('Geometria 2D otimizada');this.draw();
  }
}

const editor=new MolEditor(document.getElementById('mol-cv'));
// Save initial empty state
editor._saveHist();

function setTool(t){
  editor.tool=t;editor.ringMode=false;editor.sel=-1;editor.selBond=-1;
  ['draw','sel','era'].forEach(id=>document.getElementById('t-'+id).classList.toggle('act',id===t));
  document.getElementById('mol-cv').style.cursor=t==='era'?'not-allowed':t==='sel'?'default':'crosshair';
  editor.draw();
}
function setBo(n){
  editor.bo=n;
  [1,2,3].forEach(i=>document.getElementById('b'+i).classList.toggle('act',i===n));
  if(editor.selBond>=0){
    const bond=editor.bonds.find(b=>b.id===editor.selBond);
    if(bond&&bond.order!==n){bond.order=n;editor._saveHist();editor._upd();editor.draw();setEditorStatus(`Ligação alterada para ordem ${n}`);}
  }
}
function setFuncGroup(group){
  if(!group){editor.funcGroupMode=null;setEditorStatus('Modo grupo funcional cancelado');return;}
  editor.funcGroupMode=group;
  editor.tool='sel';
  setEditorStatus(`Selecione um átomo para conectar -${group}`);
  document.getElementById('funcGroupSel').classList.add('act');
}
function startRing(n,aro){
  editor.ringN=n;editor.ringAro=aro;editor.ringMode=!editor.ringMode;editor.tool='draw';
  document.querySelectorAll('.ring-btn').forEach(b=>b.classList.remove('act'));
  if(editor.ringMode)event.currentTarget.classList.add('act');
}
function centerMol(){editor.center();}
function clearAll(){if(editor.atoms.length===0)return;editor.clear();document.getElementById('si').value='';}
function undo(){editor.undo();}
function redo(){editor.redo();}
async function copySmiles(){
  const smiles=editor.toSMILES();
  if(!smiles){setEditorStatus('Desenhe ou importe uma molécula primeiro');return;}
  try{
    await navigator.clipboard.writeText(smiles);
    setEditorStatus('SMILES copiado');
  }catch(err){
    const field=document.getElementById('si');field.focus();field.select();
    setEditorStatus('SMILES selecionado — use Ctrl+C para copiar');
  }
}
function importSmilesToEditor(){
  const input=document.getElementById('si').value.trim();
  if(!input){setEditorStatus('Informe um SMILES para importar');return;}
  try{
    const mol=parseSMILES(input);
    if(!mol.atoms.length)throw new Error('nenhum átomo reconhecido');
    editor.loadFromParsed(mol);
    setEditorStatus(`${mol.atoms.length} átomo${mol.atoms.length===1?'':'s'} importado${mol.atoms.length===1?'':'s'}`);
  }catch(err){
    setEditorStatus('SMILES inválido — revise a estrutura');
  }
}

// ─── KEYBOARD SHORTCUTS ───────────────────────────────────
document.addEventListener('keydown',e=>{
  const tag=document.activeElement.tagName;
  if(tag==='INPUT'||tag==='SELECT'||tag==='TEXTAREA')return;
  if(e.ctrlKey||e.metaKey){
    if(e.key==='z'){e.preventDefault();editor.undo();}
    else if(e.key==='y'||(e.key==='z'&&e.shiftKey)){e.preventDefault();editor.redo();}
    return;
  }
  if(e.key==='Escape'){
    if(editor.ringMode){editor.ringMode=false;document.querySelectorAll('.ring-btn').forEach(b=>b.classList.remove('act'));setEditorStatus('Inserção de anel cancelada');editor.draw();}
    else if(editor.sel>=0||editor.selBond>=0){editor.sel=-1;editor.selBond=-1;setEditorStatus('Seleção limpa');editor.draw();}
    return;
  }
  if(e.key==='Delete'||e.key==='Backspace'){
    if(editor.sel>=0||editor.selBond>=0)editor.deleteSelection();
    else setTool('era');
    return;
  }
  const kmap={d:'draw',m:'sel'};
  if(kmap[e.key]){setTool(kmap[e.key]);return;}
  if(e.key==='1')setBo(1);
  else if(e.key==='2')setBo(2);
  else if(e.key==='3')setBo(3);
  // Element shortcuts
  const emap={c:'C',n:'N',o:'O',s:'S',p:'P',f:'F',l:'Cl',b:'Br',i:'I'};
  if(emap[e.key.toLowerCase()]){setEl(emap[e.key.toLowerCase()]);}
});

// ─── SMILES PARSER ────────────────────────────────────────
function parseSMILES(smi){
  const mol={atoms:[],bonds:[],adj:{}};
  let i=0,pA=-1,pB=null;
  const stk=[],rings={};
  const addA=(el,aro,hx,ch)=>{const id=mol.atoms.length;mol.atoms.push({id,el,aro,hx,hI:0,ch});mol.adj[id]=[];return id;};
  const addB=(f,t,o,ar)=>{if(f<0||t<0)return;const id=mol.bonds.length;mol.bonds.push({id,from:f,to:t,o,ar});mol.adj[f].push({nb:t,bid:id});mol.adj[t].push({nb:f,bid:id});};
  while(i<smi.length){
    const c=smi[i];
    if(c==='('){stk.push(pA);i++;continue;}
    if(c===')'){pA=stk.pop();pB=null;i++;continue;}
    if(c==='='){pB={o:2};i++;continue;}if(c==='#'){pB={o:3};i++;continue;}
    if(c===':'){pB={o:1.5,ar:true};i++;continue;}if(c==='-'){pB={o:1};i++;continue;}
    if(c==='.'){pA=-1;pB=null;i++;continue;}if(c==='/'||c==='\\'){i++;continue;}
    if(c>='0'&&c<='9'||c==='%'){
      let num;if(c==='%'){i++;num=parseInt(smi.substring(i,i+2));i+=2;}else{num=parseInt(c);i++;}
      if(rings[num]!==undefined){
        const ro=rings[num];const b=pB||ro.b||{o:1};
        const ar=pA>=0&&ro.a>=0&&mol.atoms[pA]?.aro&&mol.atoms[ro.a]?.aro;
        addB(ro.a,pA,ar?1.5:b.o,ar||b.ar||false);delete rings[num];
      }else rings[num]={a:pA,b:pB};
      pB=null;continue;
    }
    if(c==='['){
      i++;while(i<smi.length&&smi[i]>='0'&&smi[i]<='9')i++;
      let aro=false;if(smi[i]>='a'&&smi[i]<='z')aro=true;
      let el=smi[i].toUpperCase();i++;
      if(i<smi.length&&smi[i]>='a'&&smi[i]<='z'){el+=smi[i];i++;}
      while(i<smi.length&&(smi[i]==='@'||smi[i]==='/'||smi[i]==='\\'))i++;
      let hx=-1;if(i<smi.length&&smi[i]==='H'){i++;hx=i<smi.length&&smi[i]>='0'&&smi[i]<='9'?(()=>{const v=parseInt(smi[i]);i++;return v;})():1;}
      let ch=0;if(i<smi.length&&(smi[i]==='+'||smi[i]==='-')){const sg=smi[i]==='+'?1:-1;i++;ch=i<smi.length&&smi[i]>='0'&&smi[i]<='9'?(sg*(()=>{const v=parseInt(smi[i]);i++;return v;})()):sg;}
      while(i<smi.length&&smi[i]!==']')i++;i++;
      const aid=addA(el,aro,hx,ch);
      if(pA>=0){const b=pB||(aro&&mol.atoms[pA]?.aro?{o:1.5,ar:true}:{o:1});addB(pA,aid,b.o,b.ar||false);}
      pA=aid;pB=null;continue;
    }
    const tw=smi.substring(i,i+2);let el,aro=false;
    if(tw==='Cl'||tw==='Br'){el=tw;i+=2;}
    else if('cnosp'.includes(c)){el=c.toUpperCase();aro=true;i++;}
    else if('BCNOPSFIB'.includes(c)||c==='I'){el=c;i++;}
    else{i++;continue;}
    const aid=addA(el,aro,-1,0);
    if(pA>=0){const b=pB||(aro&&mol.atoms[pA]?.aro?{o:1.5,ar:true}:{o:1});addB(pA,aid,b.o,b.ar||false);}
    pA=aid;pB=null;
  }
  const MV={C:4,N:3,O:2,S:2,P:3,F:1,Cl:1,Br:1,I:1,B:3};
  for(const a of mol.atoms){
    if(a.hx>=0){a.hI=a.hx;continue;}
    const mv=MV[a.el];if(mv===undefined){a.hI=0;continue;}
    let bs=0;for(const nb of mol.adj[a.id]){const b=mol.bonds[nb.bid];bs+=b.o;}
    if(a.aro)bs=Math.ceil(bs);
    a.hI=Math.max(0,Math.round(mv-bs-a.ch));
  }
  return mol;
}

// ─── LOCAL PROPERTY CALCULATOR ───────────────────────────
const AM={H:1.008,C:12.011,N:14.007,O:15.999,F:18.998,P:30.974,S:32.06,Cl:35.45,Br:79.904,I:126.904,B:10.811};
const LP_C={Caro:0.13,Csp2:0.10,Csp3:0.53,Naro:-0.70,Nam:-1.08,Namine:-1.03,Oether:0.23,Oalc:-0.67,Ocar:-0.55,S:0.03,F:0.14,Cl:0.60,Br:0.88,I:1.35,P:0.50};
function hasCarbonylAdj(mol,aid){return(mol.adj[aid]||[]).some(nb=>{const c=mol.atoms[nb.nb];if(c.el!=='C')return false;return(mol.adj[nb.nb]||[]).some(n2=>{const b=mol.bonds[n2.bid];return b.o===2&&mol.atoms[n2.nb].el==='O';});});}
function hasCarbonylDirect(mol,aid){return(mol.adj[aid]||[]).some(nb=>{const b=mol.bonds[nb.bid];return b.o===2&&mol.atoms[nb.nb].el==='O';});}
function calcProps(mol){
  let mw=0,hbd=0,hba=0,psa=0,lp=0,rb=0,sp3=0,spTot=0;
  for(const a of mol.atoms){
    mw+=(AM[a.el]||12)+a.hI*1.008;
    if((a.el==='N'||a.el==='O')&&a.hI>0)hbd+=a.hI;
    if(a.el==='N'||a.el==='O')hba++;
    if(a.el==='O'){psa+=a.hI>0?20.23:17.07;}
    if(a.el==='N'){const inR=(mol.adj[a.id]||[]).length>=2;psa+=a.hI>0?(inR?13.97:26.02):(inR?12.89:3.24);}
    if(a.el==='F')lp+=LP_C.F;else if(a.el==='Cl')lp+=LP_C.Cl;else if(a.el==='Br')lp+=LP_C.Br;
    else if(a.el==='I')lp+=LP_C.I;else if(a.el==='S')lp+=LP_C.S;else if(a.el==='P')lp+=LP_C.P;
    else if(a.el==='N'){const isAm=hasCarbonylAdj(mol,a.id);if(a.aro)lp+=LP_C.Naro;else if(isAm)lp+=LP_C.Nam;else lp+=LP_C.Namine;}
    else if(a.el==='O'){const dbl=(mol.adj[a.id]||[]).some(nb=>mol.bonds[nb.bid].o===2);if(dbl)lp+=LP_C.Ocar;else if(a.hI>0)lp+=LP_C.Oalc;else lp+=LP_C.Oether;}
    else if(a.el==='C'){
      if(a.aro){lp+=LP_C.Caro;}
      else{const dbl=(mol.adj[a.id]||[]).some(nb=>mol.bonds[nb.bid].o>=2);if(dbl)lp+=LP_C.Csp2;else{lp+=LP_C.Csp3;sp3++;}spTot++;}
    }
  }
  for(const b of mol.bonds){
    if(b.o!==1&&b.o!==1.5)continue;
    const d1=(mol.adj[b.from]||[]).length,d2=(mol.adj[b.to]||[]).length;
    const a1=mol.atoms[b.from],a2=mol.atoms[b.to];
    if(d1===1||d2===1)continue;
    if(!a1.aro&&!a2.aro)rb++;
  }
  const fsp3=spTot>0?sp3/spTot:0;
  const cnt={};
  for(const a of mol.atoms){cnt[a.el]=(cnt[a.el]||0)+1;if(a.hI>0)cnt.H=(cnt.H||0)+a.hI;}
  const ord=['C','H','N','O','S','P','F','Cl','Br','I'];
  let formula='';for(const el of ord)if(cnt[el])formula+=el+(cnt[el]>1?cnt[el]:'');
  for(const el in cnt)if(!ord.includes(el))formula+=el+(cnt[el]>1?cnt[el]:'');
  return{mw:Math.round(mw*100)/100,lp:Math.round(lp*100)/100,hbd,hba,psa:Math.round(psa*10)/10,rb,fsp3:Math.round(fsp3*100)/100,formula};
}

// ─── PUBCHEM (with retry) ────────────────────────────────
const _pcCache=new Map();

async function _fetchWithRetry(url,retries=2,timeout=12000){
  for(let attempt=0;attempt<=retries;attempt++){
    try{
      const controller=new AbortController();
      const tid=setTimeout(()=>controller.abort(),timeout);
      try{
        const r=await fetch(url,{signal:controller.signal});
        clearTimeout(tid);
        if(r.ok)return r;
        if(r.status===404||r.status===400)return null; // compound not found — don't retry
        if(r.status>=500){if(attempt<retries)throw new Error(`Server error ${r.status}`);return null;} // retry on 5xx
        return null; // other non-2xx errors
      }catch(e){
        clearTimeout(tid);
        throw e;
      }
    }catch(e){
      if(attempt===retries)throw e;
      const delay=Math.min(1000*(attempt+1)*Math.pow(2,attempt),8000); // exponential backoff, max 8s
      await new Promise(res=>setTimeout(res,delay));
    }
  }
  return null;
}

async function fetchPubChem(smiles){
  const key=smiles.trim();
  if(_pcCache.has(key))return _pcCache.get(key);
  const enc=encodeURIComponent(key);
  // Core properties — IUPACName kept separate to avoid 404 breaking the whole request
  const props='MolecularWeight,XLogP,HBondDonorCount,HBondAcceptorCount,TPSA,MolecularFormula,RotatableBondCount';
  const url=`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/${enc}/property/${props}/JSON`;
  try{
    const r=await _fetchWithRetry(url,2,12000); // 2 retries, 12s timeout
    if(!r)return null;
    const j=await r.json();
    const p=j?.PropertyTable?.Properties?.[0];
    if(!p)return null;
    // CID lookup
    let cid=null;
    try{
      const cidUrl=`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/${enc}/cids/JSON`;
      const cr=await _fetchWithRetry(cidUrl,2,8000); // 2 retries, 8s timeout
      if(cr){const cj=await cr.json();cid=cj?.IdentifierList?.CID?.[0]||null;}
    }catch(e){console.warn('CID lookup failed:',e.message);}
    // IUPACName fetched separately via CID (more stable than SMILES-based)
    let iupac=null;
    if(cid){
      try{
        const ir=await _fetchWithRetry(`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/${cid}/property/IUPACName/JSON`,2,8000); // 2 retries, 8s timeout
        if(ir){const ij=await ir.json();iupac=ij?.PropertyTable?.Properties?.[0]?.IUPACName||null;}
      }catch(e){console.warn('IUPAC lookup failed:',e.message);}
    }
    const result={mw:parseFloat(p.MolecularWeight),lp:p.XLogP!=null?parseFloat(p.XLogP):null,hbd:p.HBondDonorCount,hba:p.HBondAcceptorCount,psa:p.TPSA!=null?parseFloat(p.TPSA):null,rb:p.RotatableBondCount,formula:p.MolecularFormula,iupac,cid,source:'pubchem'};
    _pcCache.set(key,result);
    return result;
  }catch(e){console.warn('PubChem unavailable:',e.message);return null;}
}

// ─── CHEMBL ──────────────────────────────────────────────
const _chemblCache=new Map();
async function fetchChEMBL(smiles){
  const key=smiles.trim();
  if(_chemblCache.has(key))return _chemblCache.get(key);
  const enc=encodeURIComponent(key);
  try{
    const r=await _fetchWithRetry(
      `https://www.ebi.ac.uk/chembl/api/data/molecule.json?molecule_structures__canonical_smiles__flexmatch=${enc}&limit=1`,
      1,9000
    );
    if(!r)return null;
    const j=await r.json();
    const mol=j?.molecules?.[0];
    if(!mol)return null;
    const chemblId=mol.molecule_chembl_id;
    const mp=mol.molecule_properties||{};
    // Mechanisms of action
    let mechs=[];
    try{
      const mr=await _fetchWithRetry(`https://www.ebi.ac.uk/chembl/api/data/mechanism.json?molecule_chembl_id=${chemblId}&limit=5`,1,6000);
      if(mr){const mj=await mr.json();mechs=(mj?.mechanisms||[]).map(m=>({target:m.target_name||m.mechanism_of_action,action:m.action_type,moa:m.mechanism_of_action}));}
    }catch(e){}
    // Drug indications
    let indics=[];
    try{
      const di=await _fetchWithRetry(`https://www.ebi.ac.uk/chembl/api/data/drug_indication.json?molecule_chembl_id=${chemblId}&limit=6`,1,6000);
      if(di){const dij=await di.json();indics=(dij?.drug_indications||[]).map(i=>i.indication_refs?.[0]?.ref_type==='MeSH'?i.mesh_heading:i.efo_term).filter(Boolean);}
    }catch(e){}
    const result={
      chemblId,
      prefName:mol.pref_name||null,
      type:mol.molecule_type||null,
      maxPhase:mol.max_phase,
      oral:mol.oral,
      topical:mol.topical,
      blackBox:mol.black_box_warning,
      alogp:mp.alogp!=null?parseFloat(mp.alogp):null,
      psa:mp.psa!=null?parseFloat(mp.psa):null,
      hba:mp.hba,hbd:mp.hbd,rtb:mp.rtb,
      ro3:mp.ro3_pass==='Y',
      mechs,indics
    };
    _chemblCache.set(key,result);
    return result;
  }catch(e){console.warn('ChEMBL unavailable:',e.message);return null;}
}
function setCHStatus(state){
  const el=document.getElementById('ch-status');
  el.className='hpill ch-pill';
  if(state==='ok'){el.classList.add('ch-ok');el.innerHTML='<span class="pc-dot"></span>ChEMBL ✓';}
  else if(state==='fail'){el.classList.add('ch-fail');el.innerHTML='<span class="pc-dot"></span>ChEMBL ✗';}
  else if(state==='loading'){el.innerHTML='<span class="spin" style="width:8px;height:8px;border-width:1.5px"></span> ChEMBL...';}
  else{el.innerHTML='<span class="pc-dot"></span>ChEMBL';}
}

// ─── pKa PREDICTOR ────────────────────────────────────────
function predictPKa(mol){
  const ionizable=[];
  const isAro=(aid)=>mol.atoms[aid]?.aro;
  const nbrs=(aid)=>(mol.adj[aid]||[]).map(n=>({a:mol.atoms[n.nb],b:mol.bonds[n.bid],id:n.nb}));
  for(const a of mol.atoms){
    if(a.el==='C'&&hasCarbonylDirect(mol,a.id)){
      const ohs=nbrs(a.id).filter(n=>n.a.el==='O'&&n.b.o===1&&n.a.hI>0);
      for(const oh of ohs){
        let pka=4.75;
        for(const nc of nbrs(a.id).filter(n=>n.a.el==='C'&&n.id!==oh.id)){if(isAro(nc.id))pka-=0.3;if(['F','Cl','Br','I'].includes(nc.a.el))pka-=1.2;}
        pka-=nbrs(a.id).filter(n=>['F','Cl','Br'].includes(n.a.el)).length*1.2;
        ionizable.push({group:'—COOH',type:'Ácido carboxílico',pka:Math.round(pka*100)/100,nature:'acid',atom:a.id});
      }
    }
    if(a.el==='O'&&a.hI>0){
      const nbC=nbrs(a.id).filter(n=>n.a.el==='C');
      if(nbC.some(n=>isAro(n.id))){
        let pka=9.95;
        for(const c of nbrs(a.id).filter(n=>isAro(n.id))){for(const rn of nbrs(c.id).filter(n=>n.id!==a.id&&isAro(n.id))){const rnEl=mol.atoms[rn.id].el;if(['F','Cl','Br','I'].includes(rnEl))pka-=1.0;if(rnEl==='N'&&mol.atoms[rn.id].hI===0)pka-=3.0;}}
        ionizable.push({group:'Ar—OH',type:'Fenol',pka:Math.round(pka*100)/100,nature:'acid',atom:a.id});
      }else ionizable.push({group:'R—OH',type:'Álcool',pka:16.0,nature:'acid',atom:a.id});
    }
    if(a.el==='N'&&!a.aro&&a.hI>0&&!hasCarbonylAdj(mol,a.id)){
      let pka=10.6;const adjAro=nbrs(a.id).some(n=>isAro(n.id));
      if(adjAro)pka=4.6;else{for(const an of nbrs(a.id).filter(n=>n.a.el==='C')){if(hasCarbonylDirect(mol,an.id))pka-=2.0;pka-=nbrs(an.id).filter(n=>['F','Cl','Br'].includes(n.a.el)).length*0.8;}}
      ionizable.push({group:'R—NH',type:adjAro?'Amina aromática':'Amina alifática',pka:Math.round(pka*100)/100,nature:'base',atom:a.id});
    }
    if(a.el==='N'&&!a.aro&&a.hI>0&&hasCarbonylAdj(mol,a.id))ionizable.push({group:'—NHCO—',type:'Amida (N-H)',pka:14.5,nature:'acid',atom:a.id});
    if(a.el==='N'&&a.aro&&a.hI===0)ionizable.push({group:'Ar—N',type:'Piridina/Imidazol',pka:5.2,nature:'base',atom:a.id});
    if(a.el==='N'&&a.aro&&a.hI>0)ionizable.push({group:'Ar—N—H',type:'Pirrol / Indol N-H',pka:17.0,nature:'acid',atom:a.id});
    if(a.el==='S'&&a.hI>0)ionizable.push({group:'R—SH',type:'Tiol',pka:10.5,nature:'acid',atom:a.id});
    if(a.el==='N'&&!a.aro&&a.hI>0){
      const adjS=nbrs(a.id).some(n=>{if(n.a.el!=='S')return false;return(mol.adj[n.id]||[]).filter(n2=>mol.bonds[n2.bid].o===2&&mol.atoms[n2.nb].el==='O').length>=2;});
      if(adjS){const idx=ionizable.findIndex(io=>io.atom===a.id);if(idx>=0)ionizable.splice(idx,1);ionizable.push({group:'—SO₂NH',type:'Sulfonamida',pka:10.1,nature:'acid',atom:a.id});}
    }
  }
  const seen=new Set();
  return ionizable.filter(io=>{if(seen.has(io.atom))return false;seen.add(io.atom);return true;});
}
function calcLogD(lp,ionizable,pH){
  if(!ionizable.length)return lp;
  let logd=lp;
  for(const a of ionizable.filter(i=>i.nature==='acid'&&i.pka<16))logd-=Math.log10(1+Math.pow(10,pH-a.pka));
  for(const b of ionizable.filter(i=>i.nature==='base'))logd-=Math.log10(1+Math.pow(10,b.pka-pH));
  return Math.round(logd*100)/100;
}

// ─── LOCAL STRUCTURAL ANALYSIS ───────────────────────────
function analyzeStructure(mol, smiles){
  const atoms=mol.atoms, bonds=mol.bonds, adj=mol.adj;

  // Helper: get neighbors of atom id
  const nbrs=(aid)=>(adj[aid]||[])
    .map(n=>({a:atoms[n.nb],b:bonds[n.bid],id:n.nb,bid:n.bid}))
    .filter(n=>n.a&&n.b);

  // Helper: does atom have carbonyl directly (C=O)?
  const hasCO=(aid)=>(adj[aid]||[]).some(n=>{const b=bonds[n.bid],a=atoms[n.nb];return b?.o===2&&a?.el==='O';});

  // Detect functional groups
  const fg={
    'Ácido carboxílico':0,
    'Éster':0,
    'Amida':0,
    'Aldeído':0,
    'Cetona':0,
    'Álcool':0,
    'Éter':0,
    'Amina primária':0,
    'Amina secundária':0,
    'Amina terciária':0,
    'Flúor':0,
    'Cloro':0,
    'Bromo':0,
    'Iodo':0,
    'Nitro':0,
    'Sulfonamida':0,
    'Tiol':0,
  };

  for(const a of atoms){
    // Carbonyl-containing groups: find C with C=O
    if(a.el==='C'&&hasCO(a.id)){
      const oxyDbl=nbrs(a.id).filter(n=>n.b.o===2&&n.a.el==='O');
      const oxySgl=nbrs(a.id).filter(n=>n.b.o===1&&n.a.el==='O');
      const nitNb=nbrs(a.id).filter(n=>n.b.o===1&&n.a.el==='N');
      const cNb=nbrs(a.id).filter(n=>n.a.el==='C');
      // Check for OH neighbor (acid) — O with hI>0 singly bonded
      const ohNb=oxySgl.filter(n=>n.a.hI>0);
      // Check for O bonded to C (ester)
      const oCNb=oxySgl.filter(n=>n.a.hI===0&&nbrs(n.id).some(n2=>n2.id!==a.id&&n2.a.el==='C'));
      if(ohNb.length>0){
        fg['Ácido carboxílico']++;
      } else if(oCNb.length>0&&nitNb.length===0){
        fg['Éster']++;
      } else if(nitNb.length>0){
        fg['Amida']++;
      } else {
        // Aldehyde: carbonyl C with hI>0 on C itself, or only 1 C neighbor
        const nonONonDblNb=nbrs(a.id).filter(n=>n.b.o!==2&&n.a.el!=='O');
        const isAldehyde=a.hI>0||(nonONonDblNb.length===0&&oxyDbl.length===1);
        // Also detect terminal carbonyl = aldehyde (only one heavy neighbor besides =O)
        const heavyNonODbl=nbrs(a.id).filter(n=>bonds[n.bid].o!==2);
        if(isAldehyde||(heavyNonODbl.length===0)){
          fg['Aldeído']++;
        } else {
          // Ketone: C bonded to two Cs (via single bonds) and one =O
          const cSglNb=nbrs(a.id).filter(n=>n.b.o===1&&n.a.el==='C');
          if(cSglNb.length>=2){
            fg['Cetona']++;
          } else if(cSglNb.length===1){
            // Could still be aldehyde (one C, one implicit H)
            fg['Aldeído']++;
          }
        }
      }
    }

    // Alcohol: O with hI>0, not adjacent to C=O
    if(a.el==='O'&&a.hI>0){
      const adjCO=nbrs(a.id).some(n=>n.a.el==='C'&&hasCO(n.id));
      if(!adjCO) fg['Álcool']++;
    }

    // Ether: O with hI==0, bonded to two Cs (not carbonyl)
    if(a.el==='O'&&a.hI===0){
      const isDbl=(adj[a.id]||[]).some(n=>bonds[n.bid].o===2);
      if(!isDbl){
        const cNb=nbrs(a.id).filter(n=>n.a.el==='C');
        if(cNb.length>=2) fg['Éter']++;
      }
    }

    // Amines: N non-aromatic, not adjacent to carbonyl
    if(a.el==='N'&&!a.aro){
      const adjCO=hasCarbonylAdj(mol,a.id);
      if(!adjCO){
        if(a.hI>=2) fg['Amina primária']++;
        else if(a.hI===1) fg['Amina secundária']++;
        else if(a.hI===0) fg['Amina terciária']++;
      }
    }

    // Halogens
    if(a.el==='F') fg['Flúor']++;
    if(a.el==='Cl') fg['Cloro']++;
    if(a.el==='Br') fg['Bromo']++;
    if(a.el==='I') fg['Iodo']++;

    // Nitro: N bonded to 2 oxygens, at least one with bond order 2
    if(a.el==='N'){
      const oNb=nbrs(a.id).filter(n=>n.a.el==='O');
      const dblO=oNb.filter(n=>bonds[n.bid].o===2);
      if(oNb.length>=2&&dblO.length>=1) fg['Nitro']++;
    }

    // Sulfonamide: S with 2 double-bond O AND bonded to N
    if(a.el==='S'){
      const dblO=nbrs(a.id).filter(n=>n.b.o===2&&n.a.el==='O');
      const nNb=nbrs(a.id).filter(n=>n.a.el==='N');
      if(dblO.length>=2&&nNb.length>=1) fg['Sulfonamida']++;
    }

    // Thiol: S with hI>0
    if(a.el==='S'&&a.hI>0) fg['Tiol']++;
  }

  // Build funcGroups array (descriptions)
  const fgDesc={
    'Ácido carboxílico':'C(=O)OH — doador/aceptor de H, ácido fraco',
    'Éster':'C(=O)O—C — derivado acídico, metabolizável',
    'Amida':'C(=O)N — ligação resistente, presente em peptídeos',
    'Aldeído':'C(=O)H — eletrofílico, reativo',
    'Cetona':'C(=O)C — aceptor de H, polar',
    'Álcool':'R—OH — doador/aceptor de H, polar',
    'Éter':'R—O—R — aceptor de H, menos polar',
    'Amina primária':'—NH₂ — básico, doador de H',
    'Amina secundária':'—NHR — básico, menos polar',
    'Amina terciária':'—NR₃ — básico, lipossolúvel',
    'Flúor':'C—F — aumenta metabolismo, isostero de OH',
    'Cloro':'C—Cl — aumenta LogP, farmacóforo comum',
    'Bromo':'C—Br — interações halogen bond',
    'Iodo':'C—I — pesado, contraste em imagem',
    'Nitro':'—NO₂ — elétron-retirador, potencial tóxico',
    'Sulfonamida':'—SO₂NH — ionizável, farmacóforo de sulfa',
    'Tiol':'—SH — nucleofílico, oxidável',
  };

  const funcGroups=Object.entries(fg)
    .filter(([,count])=>count>0)
    .map(([name,count])=>({name,count,desc:fgDesc[name]||''}));

  // Ring detection
  // Aromatic: count connected components among aromatic atoms
  const aroAtoms=atoms.filter(a=>a.aro);
  let aromaticRings=0;
  if(aroAtoms.length>0){
    const visited=new Set();
    for(const a of aroAtoms){
      if(!visited.has(a.id)){
        // BFS over aromatic atoms
        const queue=[a.id];visited.add(a.id);
        let compSize=0;
        while(queue.length){
          const cur=queue.shift();compSize++;
          for(const nb of(adj[cur]||[])){
            if(!visited.has(nb.nb)&&atoms[nb.nb]?.aro){visited.add(nb.nb);queue.push(nb.nb);}
          }
        }
        // Each aromatic component ~6 atoms = 1 ring; fused systems: size/6 rounded
        aromaticRings+=Math.max(1,Math.round(compSize/6));
      }
    }
  }

  // Aliphatic rings: DFS back-edge detection on non-aromatic atoms
  let aliphaticRings=0;
  {
    const visited=new Set();
    const dfsRing=(id,parentBid)=>{
      visited.add(id);
      for(const nb of(adj[id]||[])){
        if(nb.bid===parentBid)continue;
        const na=atoms[nb.nb];
        if(!na||na.aro)continue; // skip aromatic
        if(visited.has(nb.nb)){aliphaticRings++;}
        else{dfsRing(nb.nb,nb.bid);}
      }
    };
    for(const a of atoms){
      if(!a.aro&&!visited.has(a.id))dfsRing(a.id,-1);
    }
    // DFS counts each ring edge twice (back and forth), divide by 2
    aliphaticRings=Math.floor(aliphaticRings/2);
  }

  const ringInfo={aromatic:aromaticRings,aliphatic:aliphaticRings};

  // Stereocenters: simplified — C, non-aromatic, degree 4, varied neighbors
  // Also check if smiles contains '@'
  const smilesHasStereo=smiles.includes('@');
  let stereoCenters=0;
  if(smilesHasStereo){
    // Count '@' occurrences as rough stereo center count
    stereoCenters=(smiles.match(/@/g)||[]).length;
    // But also count from structure
  } else {
    for(const a of atoms){
      if(a.el==='C'&&!a.aro){
        const deg=(adj[a.id]||[]).length;
        if(deg===4){
          const nbEls=nbrs(a.id).map(n=>n.a.el);
          const uniqueEls=new Set(nbEls);
          if(uniqueEls.size>=3) stereoCenters++;
        }
      }
    }
  }

  const heavyAtomCount=atoms.length;
  const totalRings=aromaticRings+aliphaticRings;
  const complexity=heavyAtomCount*1+totalRings*10+stereoCenters*5+funcGroups.length*3;

  return{funcGroups,ringInfo,heavyAtomCount,stereoCenters,complexity};
}

// ─── RENDER ANALYSIS ────────────────────────────────────
function renderAnalysis(mol, smiles, pcData){
  const ana=analyzeStructure(mol,smiles);
  const p=calcProps(mol);
  const iupac=pcData?.iupac||null;
  const formula=pcData?.formula||p.formula;
  const mw=pcData?.mw||p.mw;

  // Nomenclatura section
  const nomenclaturaHtml=`
    <div class="sec">Nomenclatura</div>
    <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:2px">
      <div class="stat-row"><span class="stat-lbl">Nome IUPAC</span><span class="stat-val" style="font-size:.7rem;max-width:60%;text-align:right;word-break:break-all">${iupac?escHtml(iupac):'—'}</span></div>
      <div class="stat-row"><span class="stat-lbl">Fórmula Molecular</span><span class="stat-val">${formula}</span></div>
      <div class="stat-row"><span class="stat-lbl">Peso Molecular</span><span class="stat-val">${mw.toFixed(2)} Da</span></div>
    </div>
  `;

  // Functional groups section
  let fgHtml='';
  if(ana.funcGroups.length===0){
    fgHtml='<div class="empty" style="padding:16px 8px"><div class="ico" style="font-size:1.3rem">🔍</div>Nenhum grupo funcional identificado</div>';
  } else {
    fgHtml=`<div class="fg-grid">${ana.funcGroups.map(g=>`
      <div class="fg-card">
        <div class="fg-header">
          <span class="fg-name">${escHtml(g.name)}</span>
          <span class="fg-cnt">×${g.count}</span>
        </div>
        <div class="fg-desc">${escHtml(g.desc)}</div>
      </div>`).join('')}</div>`;
  }

  // Ring systems
  const ringsHtml=`
    <div class="stat-row"><span class="stat-lbl">Anéis aromáticos</span><span class="stat-val">${ana.ringInfo.aromatic}</span></div>
    <div class="stat-row"><span class="stat-lbl">Anéis alifáticos</span><span class="stat-val">${ana.ringInfo.aliphatic}</span></div>
  `;

  // Complexity stats
  const fsp3=p.fsp3;
  const complexHtml=`
    <div class="stat-row"><span class="stat-lbl">Átomos pesados</span><span class="stat-val">${ana.heavyAtomCount}</span></div>
    <div class="stat-row"><span class="stat-lbl">Centros estereogênicos</span><span class="stat-val">${ana.stereoCenters}</span></div>
    <div class="stat-row"><span class="stat-lbl">Escore de complexidade</span><span class="stat-val">${ana.complexity}</span></div>
    <div class="stat-row"><span class="stat-lbl">Fração Csp³ (Fsp³)</span><span class="stat-val">${fsp3.toFixed(2)}</span></div>
  `;

  document.getElementById('ana-out').innerHTML=`
    ${nomenclaturaHtml}
    <div class="sec">Grupos Funcionais</div>
    ${fgHtml}
    <div class="sec">Sistemas de Anéis</div>
    ${ringsHtml}
    <div class="sec">Complexidade Molecular</div>
    ${complexHtml}
    <div class="note">Análise estrutural local — grupos funcionais identificados por padrões de conectividade.</div>
  `;
}

function escHtml(s){
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

// ─── RENDER ───────────────────────────────────────────────
function renderStructure(sm,mol,pcData){
  const cv=document.getElementById('svc'),emp=document.getElementById('str-empty'),ch=document.getElementById('chips');
  const iupacBox=document.getElementById('iupac-box-container');
  if(!sm){cv.style.display='none';emp.style.display='';ch.innerHTML='';iupacBox.innerHTML='';return;}
  cv.style.display='block';emp.style.display='none';
  try{
    const drw=new SmilesDrawer.Drawer({width:cv.offsetWidth||500,height:255,bondThickness:1.5,fontSizeLarge:11,fontSizeSmall:8,themes:{
      light:{C:'#1a1c2e',N:'#3b82f6',O:'#dc2626',S:'#ca8a04',P:'#ea580c',F:'#7c3aed',Cl:'#7c3aed',Br:'#7c3aed',I:'#7c3aed',BACKGROUND:'#fafbff'},
      dark:{C:'#e2e6f8',N:'#60a5fa',O:'#f87171',S:'#fbbf24',P:'#fb923c',F:'#a78bfa',Cl:'#a78bfa',Br:'#a78bfa',I:'#a78bfa',BACKGROUND:'#0f1020'}
    }});
    SmilesDrawer.parse(sm,(tree)=>{
      const th=document.documentElement.dataset.theme||(window.matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');
      drw.draw(tree,'svc',th,false);
    },()=>{cv.style.display='none';emp.innerHTML='<div class="ico">⚠️</div>SMILES inválido';emp.style.display='';});
  }catch(e){console.error(e);}
  // IUPAC box
  const iupacName=pcData?.iupac||null;
  iupacBox.innerHTML=`<div class="iupac-box">
    <div class="iupac-label">Nome IUPAC <span class="src-tag src-pc">PubChem</span></div>
    <div class="iupac-name">${iupacName?escHtml(iupacName):'—'}</div>
  </div>`;
  const p=calcProps(mol);
  const formula=pcData?.formula||p.formula;
  let chipsHtml=`<span class="chip ${pcData?'pcc':''}">Fórmula: ${formula}</span><span class="chip">Átomos pesados: ${mol.atoms.length}</span><span class="chip">Ligações: ${mol.bonds.length}</span>`;
  if(pcData?.cid)chipsHtml+=`<a class="pc-link" href="https://pubchem.ncbi.nlm.nih.gov/compound/${pcData.cid}" target="_blank">PubChem CID ${pcData.cid} ↗</a>`;
  ch.innerHTML=chipsHtml;
}

function srcTag(src){return src==='pc'?'<span class="src-tag src-pc">PubChem</span>':'<span class="src-tag src-est">Estimado</span>';}

function renderLipinski(p,pcData){
  const mw=pcData?.mw??p.mw,lp=pcData?.lp??p.lp,hbd=pcData?.hbd??p.hbd,hba=pcData?.hba??p.hba,psa=pcData?.psa??p.psa,rb=pcData?.rb??p.rb,fsp3=p.fsp3,formula=pcData?.formula??p.formula;
  const hasPc=!!pcData,ms=hasPc?'pc':'est',lps=pcData&&pcData.lp!=null?'pc':'est',ps=pcData&&pcData.psa!=null?'pc':'est';
  const mwOk=mw<=500,lpOk=lp<=5,hbdOk=hbd<=5,hbaOk=hba<=10,psaOk=psa<=140;
  const viol=[!mwOk,!lpOk,!hbdOk,!hbaOk].filter(Boolean).length;
  const card=(nm,val,lim,ok,unit,src)=>{const cl=ok?'ok':'fail',badge=ok?'✓ OK':'✗ FAIL';return`<div class="pcard ${cl}"><div class="pn">${nm} ${srcTag(src)}</div><div class="pv">${val}<span style="font-size:.6rem;font-weight:400">${unit?' '+unit:''}</span></div><div class="pu">Limite: ${lim}</div><span class="pb">${badge}</span></div>`;};
  const cardN=(nm,val,unit,src)=>`<div class="pcard plain"><div class="pn">${nm} ${srcTag(src)}</div><div class="pv">${val}<span style="font-size:.6rem;font-weight:400">${unit?' '+unit:''}</span></div><span class="pb">INFO</span></div>`;
  const giHi=psa<90&&mw<500&&lp<5,bbb=lp>0&&lp<=3&&psa<70&&mw<450,pgp=mw>400&&psa>100,sol=lp<3?'Alta':lp<5?'Moderada':'Baixa';
  const adme=[{l:'Absorção GI',v:giHi?'Alta':'Baixa',c:giHi?'av-hi':'av-lo'},{l:'Permeab. BBB',v:bbb?'Provável':'Improvável',c:bbb?'av-hi':'av-lo'},{l:'Substrato P-gp',v:pgp?'Provável':'Improvável',c:pgp?'av-md':'av-hi'},{l:'Solubilidade aq.',v:sol,c:lp<3?'av-hi':lp<5?'av-md':'av-lo'},{l:'Fsp³',v:fsp3.toFixed(2),c:fsp3>0.3?'av-hi':'av-md'},{l:'Lig. Rotacionáveis',v:rb,c:rb<=10?'av-hi':'av-md'}];
  const srcNote=hasPc?`<div class="note pc-note">📡 <strong>PubChem (NIH/NLM):</strong> MW, XLogP, HBD, HBA, TPSA e ligações rotacionáveis são dados oficiais.${pcData.cid?` <a href="https://pubchem.ncbi.nlm.nih.gov/compound/${pcData.cid}" target="_blank" style="color:var(--pc)">Ver composto ↗</a>`:''} Fsp³ calculado localmente.</div>`:`<div class="note">⚠️ <strong>PubChem indisponível</strong> — valores estimados pelo método de Crippen. Fins didáticos.</div>`;
  document.getElementById('lip-out').innerHTML=`
    <div class="sec">Regra dos 5 de Lipinski</div>
    <div class="pg">
      ${card('Peso Molecular',mw.toFixed(1),'≤ 500 Da',mwOk,'Da',ms)}
      ${card('<span class="term" data-tip="LogP — Octanol-water partition coefficient / Coeficiente de partição octanol-água">LogP</span> (XLogP)',lp!=null?lp.toFixed(2):'—','≤ 5',lpOk,'',lps)}
      ${card('<span class="term" data-tip="HBD — Hydrogen Bond Donor / Doador de ligação de hidrogênio">HBD</span> — Doadores H',hbd,'≤ 5',hbdOk,'',ms)}
      ${card('<span class="term" data-tip="HBA — Hydrogen Bond Acceptor / Aceitador de ligação de hidrogênio">HBA</span> — Aceitadores H',hba,'≤ 10',hbaOk,'',ms)}
      <div class="pcard ${psaOk?'ok':'warn'}"><div class="pn"><span class="term" data-tip="PSA — Polar Surface Area / Área de superfície polar">PSA</span> ${srcTag(ps)}</div><div class="pv">${psa!=null?psa.toFixed(1):'—'}<span style="font-size:.6rem;font-weight:400"> Å²</span></div><div class="pu">Limite: ≤ 140 Å²</div><span class="pb">${psaOk?'✓ OK':'⚠ ALTO'}</span></div>
      ${cardN('Fórmula Molecular',formula,'',ms)}
    </div>
    <div class="vrd ${viol===0?'ok':'fail'}" style="margin-top:2px">${viol===0?'✓ Boa biodisponibilidade oral prevista':'✗ '+viol+' violação(ões) da Ro5 — biodisponibilidade comprometida'}</div>
    <div class="sec">Perfil ADME Estimado</div>
    <div class="adme-grid">${adme.map(r=>`<div class="adme-row"><span class="adme-lbl">${r.l==='Fsp³'?'<span class="term" data-tip="Fsp³ — Fraction of sp³-hybridized carbons / Fração de carbonos hibridizados sp³">Fsp³</span>':r.l}</span><span class="adme-val ${r.c}">${r.v}</span></div>`).join('')}</div>
    ${srcNote}
    <div class="note">📚 <strong>Lipinski Ro5:</strong> MW≤500, LogP≤5, HBD≤5, HBA≤10. PSA≤140 Å². Fsp³>0.3 associado a melhor solubilidade e seletividade.</div>`;
}

function renderPKa(mol,props,pcData){
  const logpForLogD=pcData?.lp??props.lp,formula=pcData?.formula??props.formula;
  const ioniz=predictPKa(mol),pH=7.4,logd=calcLogD(logpForLogD,ioniz,pH);
  let rows='';
  if(!ioniz.length)rows='<div class="empty"><div class="ico">🔬</div>Nenhum grupo ionizável encontrado</div>';
  else{
    rows='<div class="pka-list">';
    for(const io of ioniz){
      const acid=io.nature==='acid';
      let fi=0,fiLabel='';
      if(acid&&io.pka<14){fi=100/(1+Math.pow(10,io.pka-pH));fiLabel=`${fi.toFixed(1)}% ionizado (pH 7.4)`;}
      else if(!acid){fi=100/(1+Math.pow(10,pH-io.pka));fiLabel=`${fi.toFixed(1)}% protonado (pH 7.4)`;}
      rows+=`<div class="pka-row">
        <span class="pka-grp">${io.group}</span>
        <div><div style="font-size:.58rem;color:var(--mu);text-transform:uppercase;letter-spacing:.3px">${acid?'pKₐ':'pKₐ (conj.)'}</div><div class="pka-val">${io.pka.toFixed(2)}</div></div>
        <div><div class="pka-desc" style="margin-bottom:4px">${io.type} · ${acid?'Ácido':'Base'}</div>
          ${io.pka<14?`<div class="ionized-bar" style="width:140px"><div class="ionized-fill" style="width:${fi.toFixed(0)}%"></div></div><div class="ionized-pct" style="margin-top:3px">${fiLabel}</div>`:'<div class="ionized-pct" style="opacity:.5">fora da faixa fisiológica</div>'}
        </div>
        <div style="text-align:right"><span style="font-size:.6rem;color:var(--mu)">pKb (base conj.)</span><br><span style="font-family:\'Space Mono\',monospace;font-weight:700;color:var(--tx)">${(14-io.pka).toFixed(2)}</span></div>
      </div>`;
    }
    rows+='</div>';
  }
  const acids=ioniz.filter(i=>i.nature==='acid'&&i.pka<14),bases=ioniz.filter(i=>i.nature==='base');
  let charge=0;
  for(const a of acids)charge-=1/(1+Math.pow(10,a.pka-pH));
  for(const b of bases)charge+=1/(1+Math.pow(10,pH-b.pka));
  const lps=pcData?.lp!=null?'<span class="src-tag src-pc" style="margin-left:6px">PubChem XLogP</span>':'<span class="src-tag src-est" style="margin-left:6px">Estimado</span>';
  const mws=pcData?.mw!=null?'<span class="src-tag src-pc" style="margin-left:4px">PubChem</span>':'';
  document.getElementById('pka-out').innerHTML=`
    <div class="sec">Grupos Ionizáveis <span class="src-tag src-est" style="margin-left:6px">Previsão local</span></div>
    ${rows}
    <div class="sec">Parâmetros em pH 7.4 (Fisiológico)</div>
    <div class="logd-box">
      <div class="logd-title">Parâmetros Calculados</div>
      <div class="logd-row"><span class="logd-lbl"><span class="term" data-tip="LogP — Octanol-water partition coefficient / Coeficiente de partição octanol-água">LogP</span> (neutro) ${lps}</span><span class="logd-val">${logpForLogD.toFixed(2)}</span></div>
      <div class="logd-row"><span class="logd-lbl">LogD (pH 7.4, corrigido)</span><span class="logd-val">${logd.toFixed(2)}</span></div>
      <div class="logd-row"><span class="logd-lbl">Carga média em pH 7.4</span><span class="logd-val">${charge.toFixed(2)}</span></div>
      <div class="logd-row"><span class="logd-lbl">Peso Molecular ${mws}</span><span class="logd-val">${(pcData?.mw??props.mw).toFixed(3)} Da</span></div>
      <div class="logd-row"><span class="logd-lbl">Fórmula Molecular</span><span class="logd-val">${formula}</span></div>
    </div>
    <div class="note"><strong>Henderson-Hasselbalch:</strong> ácidos: % ion = 100/(1+10^(pKₐ−pH)); bases: % prot = 100/(1+10^(pH−pKₐ)). LogD = LogP − Σlog(1+10^(pH−pKₐ)). pKₐ calculados por análise de grupos funcionais — estimativas para fins didáticos.</div>`;
}

// ─── RENDER CHEMBL ────────────────────────────────────────
const PHASE_LABEL={0:'Pré-clínico',1:'Fase I',2:'Fase II',3:'Fase III',4:'Aprovado'};
const PHASE_COLOR={0:'av-lo',1:'av-md',2:'av-md',3:'av-hi',4:'av-hi'};
function renderChEMBL(chData){
  const el=document.getElementById('che-out');
  if(!chData){
    el.innerHTML=`<div class="note" style="border-left-color:var(--ah)">⚠️ Composto não encontrado no ChEMBL — pode ser inédito ou sem correspondência exata por SMILES. O ChEMBL usa correspondência flexível de estrutura.</div>
    <div class="note" style="margin-top:8px">📚 <strong>ChEMBL (EMBL-EBI):</strong> banco de dados de moléculas bioativas com propriedades drug-like, dados de bioatividade e mecanismo de ação de fármacos aprovados e em desenvolvimento.</div>`;
    return;
  }
  const phase=chData.maxPhase??0;
  const idLink=`<a href="https://www.ebi.ac.uk/chembl/compound_report_card/${chData.chemblId}/" target="_blank" style="color:var(--ah);font-weight:700">${chData.chemblId} ↗</a>`;
  // Mechanisms
  let mechHtml='<div class="empty" style="padding:14px"><div class="ico" style="font-size:1.2rem">—</div>Sem mecanismo registrado</div>';
  if(chData.mechs?.length){
    mechHtml='<div class="pka-list">'+chData.mechs.map(m=>`
      <div class="stat-row" style="flex-direction:column;align-items:flex-start;gap:4px">
        <span style="font-size:.65rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.3px">${m.action||'—'}</span>
        <span style="font-size:.75rem;color:var(--tx)">${m.moa||m.target||'—'}</span>
      </div>`).join('')+'</div>';
  }
  // Indications
  let indicHtml='<span style="color:var(--mu);font-size:.72rem">Não listadas</span>';
  if(chData.indics?.length){
    indicHtml='<div class="chips" style="margin-top:4px">'+chData.indics.map(i=>`<span class="chip" style="background:var(--ah);background:rgba(124,58,237,.12);color:var(--ah);border-color:rgba(124,58,237,.2)">${i}</span>`).join('')+'</div>';
  }
  el.innerHTML=`
    <div class="sec">Identificação ChEMBL</div>
    <div class="logd-box">
      <div class="logd-row"><span class="logd-lbl">ChEMBL ID</span><span class="logd-val">${idLink}</span></div>
      <div class="logd-row"><span class="logd-lbl">Nome preferencial</span><span class="logd-val" style="font-size:.78rem">${chData.prefName||'—'}</span></div>
      <div class="logd-row"><span class="logd-lbl">Tipo de molécula</span><span class="logd-val" style="font-size:.78rem">${chData.type||'—'}</span></div>
      <div class="logd-row"><span class="logd-lbl">Fase de desenvolvimento</span><span class="adme-val ${PHASE_COLOR[phase]}" style="font-size:.72rem">${PHASE_LABEL[phase]||phase}</span></div>
      <div class="logd-row"><span class="logd-lbl">Via oral</span><span class="adme-val ${chData.oral?'av-hi':'av-lo'}">${chData.oral?'Sim':'Não'}</span></div>
      <div class="logd-row"><span class="logd-lbl">Alerta caixa preta (FDA)</span><span class="adme-val ${chData.blackBox?'av-lo':'av-hi'}">${chData.blackBox?'⚠ Sim':'Não'}</span></div>
    </div>
    <div class="sec">Mecanismo de Ação</div>
    ${mechHtml}
    <div class="sec">Indicações Terapêuticas</div>
    ${indicHtml}
    ${chData.alogp!=null?`<div class="sec">Propriedades ChEMBL</div>
    <div class="logd-box">
      <div class="logd-row"><span class="logd-lbl"><span class="term" data-tip="AlogP — Calculated octanol-water partition coefficient / Coeficiente de partição octanol-água calculado">AlogP</span></span><span class="logd-val">${chData.alogp.toFixed(2)}</span></div>
      <div class="logd-row"><span class="logd-lbl"><span class="term" data-tip="PSA — Polar Surface Area / Área de superfície polar">PSA</span> (Å²)</span><span class="logd-val">${chData.psa?.toFixed(1)||'—'}</span></div>
      <div class="logd-row"><span class="logd-lbl"><span class="term" data-tip="HBD — Hydrogen Bond Donor / Doador de ligação de hidrogênio">HBD</span> / <span class="term" data-tip="HBA — Hydrogen Bond Acceptor / Aceitador de ligação de hidrogênio">HBA</span></span><span class="logd-val">${chData.hbd??'—'} / ${chData.hba??'—'}</span></div>
      <div class="logd-row"><span class="logd-lbl">Lig. Rotacionáveis</span><span class="logd-val">${chData.rtb??'—'}</span></div>
      <div class="logd-row"><span class="logd-lbl">Regra dos 3 (Ro3)</span><span class="adme-val ${chData.ro3?'av-hi':'av-lo'}">${chData.ro3?'Passa':'Não passa'}</span></div>
    </div>`:''}
    <div class="note" style="margin-top:4px;border-left-color:var(--ah)">📡 <strong>ChEMBL v34 (EMBL-EBI):</strong> banco de dados curado manualmente com dados de bioatividade de literatura médico-química. <a href="https://www.ebi.ac.uk/chembl/compound_report_card/${chData.chemblId}/" target="_blank" style="color:var(--ah)">Ver ficha completa ↗</a></div>`;
}

// ─── UI ───────────────────────────────────────────────────
function showTab(id,el){
  document.querySelectorAll('.tpn').forEach(p=>p.classList.remove('act'));
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('act'));
  document.getElementById('tp-'+id).classList.add('act');
  if(el)el.classList.add('act');
}

function looksLikeSmiles(value){
  return /^[0-9BCNOPSFIHbcnopsilr@+\-\[\]()=#$.\\/:]+$/.test(value);
}

async function resolveMoleculeInput(input){
  if(looksLikeSmiles(input))return{smiles:input,mol:parseSMILES(input)};
  const enc=encodeURIComponent(input);
  const r=await _fetchWithRetry(`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/${enc}/property/IsomericSMILES/JSON`,1,9000);
  if(!r)throw new Error('Nome IUPAC não encontrado no PubChem');
  const p=(await r.json())?.PropertyTable?.Properties?.[0];
  const smiles=p?.SMILES||p?.IsomericSMILES||p?.ConnectivitySMILES;
  if(!smiles)throw new Error('PubChem não retornou um SMILES');
  return{smiles,mol:parseSMILES(smiles)};
}

let _analyzing=false;
async function analyze(){
  if(_analyzing)return;
  const input=document.getElementById('si').value.trim();
  if(!input)return;
  let sm,mol;
  try{
    ({smiles:sm,mol}=await resolveMoleculeInput(input));
  }catch(e){alert('SMILES ou nome IUPAC não encontrado.');return;}

  // Load into editor for modification
  editor.loadFromParsed(mol);
  document.getElementById('si').value=input;

  // Render structure immediately
  renderStructure(sm,mol,null);
  showTab('lip',document.querySelectorAll('.tab')[1]);

  // Button loading state
  _analyzing=true;
  const btn=document.getElementById('analyze-btn');
  btn.disabled=true;btn.innerHTML='<span class="spin"></span> Consultando...';
  setPCStatus('loading');setCHStatus('loading');

  // Fetch PubChem + ChEMBL in parallel
  const [pcData,chData]=await Promise.all([
    fetchPubChem(sm).catch(()=>null),
    fetchChEMBL(sm).catch(()=>null)
  ]);

  setPCStatus(pcData?'ok':'fail');
  setCHStatus(chData?'ok':'fail');

  const p=calcProps(mol);
  renderStructure(sm,mol,pcData);
  renderLipinski(p,pcData);
  renderPKa(mol,p,pcData);
  renderAnalysis(mol,sm,pcData);
  renderChEMBL(chData);

  btn.disabled=false;btn.innerHTML='▶ Analisar';
  _analyzing=false;
}

function loadTpl(){const s=document.getElementById('tpsel');if(!s.value)return;document.getElementById('si').value=s.value;s.value='';analyze();}

window.addEventListener('resize',()=>editor._rsz());

// Default molecule: AAS (acetylsalicylic acid)
setTimeout(()=>{document.getElementById('si').value='CC(=O)Oc1ccccc1C(=O)O';analyze();},400);
</script>
'''

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chemmed5.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Done: {os.path.getsize(output_path):,} bytes")
webbrowser.open(output_path)
