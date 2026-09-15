import streamlit as st
import pandas as pd
from utils import load_css, page_header

st.set_page_config(page_title="Orçamento", page_icon="💰", layout="wide")
load_css()
page_header("Orçamento", "Planejado vs. gasto por categoria, com saldo automático", icon="💰")

st.caption(
    "Preencha os valores planejados e vá atualizando o gasto conforme a viagem avança. "
    "O saldo é calculado automaticamente. Fica salvo durante esta sessão do navegador."
)

if "orcamento_categorias" not in st.session_state:
    st.session_state.orcamento_categorias = pd.DataFrame(
        [
            {"Categoria": "Passagem aérea", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Acomodação temporária", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Acomodação definitiva (mês)", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Curso (ILSC/Berlitz)", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Seguro viagem", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Transporte (Leap Card)", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Alimentação", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Chip/eSIM e internet", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Lazer e passeios", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
            {"Categoria": "Emergência/reserva", "Planejado (€)": 0.0, "Gasto (€)": 0.0},
        ]
    )

edited = st.data_editor(
    st.session_state.orcamento_categorias,
    num_rows="dynamic",
    use_container_width=True,
    key="tabela_orcamento",
)
st.session_state.orcamento_categorias = edited

df = st.session_state.orcamento_categorias.copy()
df["Saldo (€)"] = df["Planejado (€)"] - df["Gasto (€)"]

st.markdown("---")
st.subheader("Resumo")

planejado_total = df["Planejado (€)"].sum()
gasto_total = df["Gasto (€)"].sum()
saldo_total = planejado_total - gasto_total

col1, col2, col3 = st.columns(3)
col1.metric("Total planejado", f"€ {planejado_total:,.2f}")
col2.metric("Total gasto", f"€ {gasto_total:,.2f}")
col3.metric("Saldo", f"€ {saldo_total:,.2f}")

st.markdown("### Saldo por categoria")
st.dataframe(df[["Categoria", "Planejado (€)", "Gasto (€)", "Saldo (€)"]], use_container_width=True, hide_index=True)

st.markdown("### Gasto por categoria")
chart_df = df.set_index("Categoria")[["Planejado (€)", "Gasto (€)"]]
st.bar_chart(chart_df)

st.info(
    "⚠️ Esta tabela fica salva apenas durante a sessão atual do navegador (não há banco de dados). "
    "Para persistência entre sessões, dá para evoluir depois com Google Sheets ou um banco simples."
)
