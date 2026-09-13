import streamlit as st
from datetime import date
from utils import load_css, page_header, GREEN_DARK, ORANGE

st.set_page_config(
    page_title="Guia Dublin 🍀 — Intercâmbio 2027",
    page_icon="🍀",
    layout="wide",
)

load_css()

page_header(
    "Guia de Sobrevivência — Dublin",
    "Tudo o que preciso organizar antes e depois de embarcar para o intercâmbio",
    icon="🍀",
)

# ---------- Contagem regressiva ----------
viagem = date(2027, 10, 1)
hoje = date.today()
dias_restantes = (viagem - hoje).days

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Dias até a viagem", f"{dias_restantes} dias" if dias_restantes > 0 else "Já embarquei! 🎉")
with col2:
    st.metric("Escola", "ILSC / Berlitz Dublin")
with col3:
    st.metric("Endereço da escola", "4 Swift's Alley, D08 WRK6")

st.markdown("---")

st.markdown(
    """
### Como usar este guia

Use o menu na barra lateral para navegar entre as seções. Cada página tem
checklists interativos (o progresso fica salvo enquanto a aba estiver aberta)
e passo a passo dos processos burocráticos.
"""
)

st.markdown("### 📌 Seções do guia")

secoes = [
    ("📋", "Antes de Ir", "Mala, roupas, remédios, produtos de cabelo e o que já dá para adiantar no Brasil."),
    ("📄", "Documentos", "PPS, IRP, conta bancária, GP e Leap Card — passo a passo detalhado."),
    ("🏠", "Acomodação", "Hostels temporários, sites de aluguel e como abordar agentes."),
    ("💼", "Trabalho", "Currículo, empresas de homecare e o processo completo até o primeiro emprego."),
    ("💰", "Dicas do Dia a Dia", "Como viver mais barato em Dublin, apps e sites úteis."),
    ("🍽️", "Comida", "Onde comer barato e preços médios de mercado."),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(secoes):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="step-card">
                <h4>{icon} {title}</h4>
                <p style="margin:0;color:#333;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")
st.info(
    "⚠️ Regras de imigração, valores e sites do governo irlandês mudam com frequência. "
    "Sempre confirme as informações mais recentes nos sites oficiais (irishimmigration.ie, "
    "mywelfare.ie, citizensinformation.ie) antes de cada etapa."
)
