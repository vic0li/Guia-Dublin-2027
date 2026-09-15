import streamlit as st
from utils import load_css, page_header, checklist

st.set_page_config(page_title="Acomodação", page_icon="🏠", layout="wide")
load_css()
page_header("Acomodação", "Onde ficar nas primeiras semanas e como procurar moradia definitiva", icon="🏠")

st.markdown("### ✅ Checklist")
checklist(
    [
        "Alertas ativados no Daft.ie",
        "Contato com letting agents feito",
        "Acomodação temporária (2 a 4 semanas) reservada",
        "Disponibilidade e preço da acomodação da escola (ILSC) verificados",
    ],
    key_prefix="acomodacao",
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔎 Buscando moradia definitiva")
    st.markdown(
        """
- **Daft.ie**: principal site de aluguel na Irlanda — ative alertas por região e faixa de preço.
- **Letting agents**: além dos anúncios, procure agências de locação (letting agents) na área desejada e mande e-mail direto perguntando por vagas que ainda não foram anunciadas.
- Ao contatar um anúncio, seja rápido e objetivo: apresente-se, diga que é estudante da ILSC/Berlitz, período de estadia e se pode ir ver o imóvel pessoalmente.
- Desconfie de anúncios que pedem depósito antes de qualquer visita ou contrato.
"""
    )

with col2:
    st.subheader("🛏️ Acomodação temporária (primeiras semanas)")
    st.markdown(
        """
Hostels sugeridos para ficar enquanto procura algo definitivo:

- **Leevin Hostel**
- **Abbey Court Hostel**
- **Abigail's Hostel**
- **Jacobs Inn**

Também vale checar a **disponibilidade e preço da acomodação temporária oferecida pela própria ILSC**, que costuma ser mais prática para os primeiros dias.
"""
    )

st.markdown("---")
st.subheader("📍 Referência: endereço da escola")
st.markdown("**ILSC English Language School / Berlitz Language Centre Dublin**\n\n4 Swift's Alley, The Liberties, Dublin, D08 WRK6, Irlanda")
st.caption("Dica: ao procurar acomodação, priorize bairros com boa conexão de ônibus/Luas até The Liberties.")
