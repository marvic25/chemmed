# ChemMed — Editor Molecular Web

Aplicativo web para ensino de **Química Médica — Farmácia (UNINASSAU)**, desenvolvido por **Msc. Marcos Gregório**.

Inspirado no ChemDraw, combina um editor gráfico de moléculas com análise farmacoquímica completa.

## Funcionalidades

- **Editor molecular interativo** — desenho de estruturas com undo/redo, atalhos de teclado e paleta de elementos
- **Input SMILES bidirecional** — editor gráfico ↔ campo de texto sincronizados
- **Lipinski Ro5** — Peso Molecular, LogP, HBD, HBA, PSA com dados do PubChem
- **pKa / Ionização** — previsão de grupos ionizáveis, % ionizado, LogD em pH 7.4
- **ADME** — absorção GI, permeabilidade BBB, substrato P-gp, solubilidade
- **Nome IUPAC** — nomenclatura via PubChem NIH/NLM
- **Análise Estrutural** — grupos funcionais, sistemas de anéis, centros estereogênicos

## Fontes de dados

- [PubChem (NIH/NLM)](https://pubchem.ncbi.nlm.nih.gov) — dados oficiais com retry automático e cache
- Estimativas locais (Crippen LogP, Henderson–Hasselbalch) como fallback

## Como gerar o HTML

```bash
pip install --break-system-packages # nenhuma dependência externa de Python
npm install smiles-drawer            # instala a biblioteca de renderização
python3 build5.py                    # gera chemmed5.html (~267 KB, self-contained)
```

## Créditos

Desenvolvido por **Msc. Marcos Gregório** · UNINASSAU — Farmácia  
Uso restrito aos estudantes de Farmácia em aulas com Msc. Marcos Gregório  
Biblioteca de estruturas: [SmilesDrawer](https://github.com/reymond-group/smilesDrawer)
