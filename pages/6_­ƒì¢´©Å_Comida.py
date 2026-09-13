import streamlit as st
import pandas as pd
from utils import load_css, page_header

st.set_page_config(page_title="Comida", page_icon="🍽️", layout="wide")
load_css()
page_header("Comida", "Onde comer barato e preços médios de mercado", icon="🍽️")

st.subheader("🥪 Lanches baratos")
st.markdown(
    """
- **Subway** e redes similares costumam ter promoções tipo *"Sub of the Day"* (~€5) em dias específicos da semana — confira no app/site local ao chegar.
- Redes de sanduíche e padarias (Centra, Spar, Circle K) também têm combos de almoço em torno de €5–7.
- **Too Good To Go**: ótimo para pegar sobras de padarias e restaurantes por uma fração do preço.
"""
)

st.markdown("---")
st.subheader("🛒 Preços médios de mercado (editável)")
st.caption(
    "Preencha esta tabela com os preços que você for encontrando no dia a dia em Dublin "
    "(Aldi, Lidl, Tesco, Dunnes). Os valores abaixo são apenas um ponto de partida a confirmar."
)

if "precos_mercado" not in st.session_state:
    st.session_state.precos_mercado = pd.DataFrame(
        [
            {"Item": "Leite (1L)", "Preço aproximado (€)": 1.30, "Loja mais barata": ""},
            {"Item": "Pão de forma", "Preço aproximado (€)": 1.50, "Loja mais barata": ""},
            {"Item": "Dúzia de ovos", "Preço aproximado (€)": 3.00, "Loja mais barata": ""},
            {"Item": "Arroz (1kg)", "Preço aproximado (€)": 1.80, "Loja mais barata": ""},
            {"Item": "Frango (peito, 1kg)", "Preço aproximado (€)": 6.50, "Loja mais barata": ""},
            {"Item": "Banana (1kg)", "Preço aproximado (€)": 1.20, "Loja mais barata": ""},
            {"Item": "Café", "Preço aproximado (€)": 3.50, "Loja mais barata": ""},
        ]
    )

edited = st.data_editor(
    st.session_state.precos_mercado,
    num_rows="dynamic",
    use_container_width=True,
    key="tabela_precos",
)
st.session_state.precos_mercado = edited

st.info(
    "⚠️ Os valores acima são apenas estimativas de referência — atualize-os assim que chegar "
    "com os preços reais observados nos mercados de Dublin. Esta tabela fica salva apenas durante "
    "a sessão atual do navegador."
)
