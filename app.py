"""
app.py — Página principal do sistema de rastreabilidade
Interface Streamlit para fine-tuning e inferência da Câmera 1
"""

import streamlit as st

# ── Configuração da página (DEVE ser o primeiro comando Streamlit) ─────────────
st.set_page_config(
    page_title="Câmera 1 — Rastreabilidade Industrial",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS customizado ────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 16px 20px;
        border: 1px solid #D0D7E2;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .status-ok    { color: #1A5C3A; background: #D6F0E4;
                    padding: 4px 12px; border-radius: 20px; font-weight: 600; }
    .status-warn  { color: #5C3A1A; background: #FFF3E0;
                    padding: 4px 12px; border-radius: 20px; font-weight: 600; }
    .status-erro  { color: #7A1F1F; background: #FDECEA;
                    padding: 4px 12px; border-radius: 20px; font-weight: 600; }
    .step-box {
        border-left: 4px solid #2E6DA4;
        padding: 10px 16px;
        background: #F4F6F9;
        border-radius: 0 8px 8px 0;
        margin-bottom: 10px;
    }
    section[data-testid="stSidebar"] { background-color: #1A3A5C !important; }
    section[data-testid="stSidebar"] * { color: white !important; }
    section[data-testid="stSidebar"] .stSelectbox label { color: #D6E4F0 !important; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/camera.png", width=64)
    st.title("Câmera 1")
    st.caption("Sistema de rastreabilidade industrial")
    st.divider()

    st.markdown("**Navegação**")
    st.page_link("app.py",                        label="🏠 Início",          icon="🏠")
    st.page_link("pages/1_Coletar_Imagens.py",    label="📷 Coletar imagens", icon="📷")
    st.page_link("pages/2_Preprocessar.py",       label="⚙️ Pré-processar",   icon="⚙️")
    st.page_link("pages/3_Treinar.py",            label="🧠 Treinar modelo",  icon="🧠")
    st.page_link("pages/4_Inferir.py",            label="🔍 Inferência ao vivo", icon="🔍")
    st.page_link("pages/5_Resultados.py",         label="📊 Resultados",      icon="📊")

    st.divider()
    st.caption("PET Engenharia de Produção\nBlumenau / SC · 2025")


# ── Conteúdo principal ─────────────────────────────────────────────────────────
st.title("🏭 Sistema de Rastreabilidade — Câmera 1")
st.subheader("Identificação automática de código de peças por visão computacional")
st.divider()

# Visão geral do pipeline
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="metric-card" style="border-top: 4px solid #0F6E56">
        <h4 style="color:#0F6E56; margin:0">1. Coletar</h4>
        <p style="margin:6px 0 0">Frames do vídeo ou câmera ao vivo</p>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="metric-card" style="border-top: 4px solid #2E6DA4">
        <h4 style="color:#2E6DA4; margin:0">2. Pré-processar</h4>
        <p style="margin:6px 0 0">Validar qualidade e augmentar</p>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-card" style="border-top: 4px solid #A46D2E">
        <h4 style="color:#A46D2E; margin:0">3. Treinar</h4>
        <p style="margin:6px 0 0">Fine-tuning YOLOv8 nas suas peças</p>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="metric-card" style="border-top: 4px solid #1A5C3A">
        <h4 style="color:#1A5C3A; margin:0">4. Inferir</h4>
        <p style="margin:6px 0 0">YOLO + OCR → código → ERP</p>
    </div>""", unsafe_allow_html=True)

st.divider()

# Como o pipeline funciona
st.markdown("### 🔄 Como o pipeline funciona")
col_a, col_b = st.columns([1, 1])

with col_a:
    st.markdown("""
    <div class="step-box"><b>Passo 1</b> — Frame capturado pela câmera do posto</div>
    <div class="step-box"><b>Passo 2</b> — YOLO detecta a região da peça (bbox)</div>
    <div class="step-box"><b>Passo 3</b> — OCR testa 4 pipelines de pré-processamento</div>
    <div class="step-box"><b>Passo 4</b> — Regex valida o padrão do código</div>
    <div class="step-box"><b>Passo 5A ✅</b> — Conf ≥ 85% → apontamento automático no ERP</div>
    <div class="step-box"><b>Passo 5B ⚠️</b> — Conf &lt; 85% → aciona S2 (seleção manual)</div>
    """, unsafe_allow_html=True)

with col_b:
    st.info("""
    **Por que YOLO + OCR em vez de só OCR?**

    Rodar OCR na imagem inteira captura textos irrelevantes
    (etiquetas de fundo, texto da bancada, sujeira).

    O YOLO localiza **primeiro a peça**, então o OCR roda
    apenas na área útil — muito mais preciso e rápido.
    """)
    st.success("""
    **Tecnologias utilizadas**
    - **YOLOv8** (Ultralytics) — detecção da peça
    - **EasyOCR** — leitura do código
    - **OpenCV** — pré-processamento anti-reflexo
    - **Streamlit** — interface web
    """)

# Status do sistema
st.divider()
st.markdown("### 📋 Status do sistema")

from pathlib import Path
from config import MODELOS_DIR, IMAGES_TRAIN, IMAGES_VAL

col1, col2, col3, col4 = st.columns(4)

modelo_existe = (MODELOS_DIR / "cam1_best.pt").exists()
imgs_train = len(list(IMAGES_TRAIN.glob("*.jpg")) + list(IMAGES_TRAIN.glob("*.png")))
imgs_val   = len(list(IMAGES_VAL.glob("*.jpg"))   + list(IMAGES_VAL.glob("*.png")))

with col1:
    st.metric("Imagens de treino", imgs_train,
              delta="OK" if imgs_train >= 80 else "mínimo: 80")
with col2:
    st.metric("Imagens de validação", imgs_val,
              delta="OK" if imgs_val >= 20 else "mínimo: 20")
with col3:
    st.metric("Modelo treinado",
              "✅ Sim" if modelo_existe else "❌ Não",
              delta="Pronto" if modelo_existe else "Execute o treino")
with col4:
    try:
        import ultralytics, easyocr
        st.metric("Dependências", "✅ OK", delta="Todas instaladas")
    except ImportError as e:
        st.metric("Dependências", "⚠️ Faltam", delta=str(e).split("'")[1])

st.divider()
st.markdown("""
<center><small>Projeto PET Engenharia de Produção — Blumenau/SC · 2025</small></center>
""", unsafe_allow_html=True)
