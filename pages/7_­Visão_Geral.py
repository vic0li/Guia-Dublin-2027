import streamlit as st
from datetime import date, datetime
import pandas as pd
from utils import load_css, page_header, checklist, step_card

st.set_page_config(page_title="Visão Geral", page_icon="🏠", layout="wide")
load_css()
page_header("Visão Geral", "Painel geral do intercâmbio — datas, orçamento, clima e checklist rápido", icon="🏠")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["⏳ Contagem Regressiva", "📅 Datas da Viagem", "💰 Orçamento", "🌦️ Clima Esperado", "✅ Checklist Geral"]
)

# -------- Contagem regressiva --------
with tab1:
    st.subheader("Quanto falta para cada marco do intercâmbio")

    if "data_viagem" not in st.session_state:
        st.session_state.data_viagem = date(2027, 10, 1)
    if "data_inicio_curso" not in st.session_state:
        st.session_state.data_inicio_curso = date(2027, 10, 4)
    if "data_volta" not in st.session_state:
        st.session_state.data_volta = None

    hoje = date.today()
    col1, col2, col3 = st.columns(3)
    with col1:
        dias_viagem = (st.session_state.data_viagem - hoje).days
        st.metric("Dias até embarcar", f"{dias_viagem} dias" if dias_viagem > 0 else "Já embarquei! ✈️")
    with col2:
        dias_curso = (st.session_state.data_inicio_curso - hoje).days
        st.metric("Dias até início do curso", f"{dias_curso} dias" if dias_curso > 0 else "Já começou! 🎓")
    with col3:
        if st.session_state.data_volta:
            dias_volta = (st.session_state.data_volta - hoje).days
            st.metric("Dias até a volta", f"{dias_volta} dias" if dias_volta > 0 else "Já voltei! 🏡")
        else:
            st.metric("Dias até a volta", "Defina na aba 'Datas da Viagem'")

# -------- Datas da viagem --------
with tab2:
    st.subheader("Configure as datas principais")
    st.caption("Essas datas alimentam a contagem regressiva acima e ficam salvas durante esta sessão.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.data_viagem = st.date_input("Data de embarque", value=st.session_state.get("data_viagem", date(2027, 10, 1)))
    with col2:
        st.session_state.data_inicio_curso = st.date_input(
            "Início das aulas (ILSC/Berlitz)", value=st.session_state.get("data_inicio_curso", date(2027, 10, 4))
        )
    with col3:
        volta = st.date_input("Data de volta (se já souber)", value=st.session_state.get("data_volta") or date(2028, 3, 1))
        st.session_state.data_volta = volta

    st.markdown("---")
    st.subheader("Linha do tempo")
    step_card(1, "Embarque", f"{st.session_state.data_viagem.strftime('%d/%m/%Y')} — saída do Brasil rumo a Dublin.")
    step_card(2, "Início das aulas", f"{st.session_state.data_inicio_curso.strftime('%d/%m/%Y')} — primeiro dia na ILSC/Berlitz.")
    step_card(3, "Volta prevista", f"{st.session_state.data_volta.strftime('%d/%m/%Y')} — data provisória, ajuste quando confirmar a passagem de volta.")

# -------- Orçamento resumo --------
with tab3:
    st.subheader("Resumo do orçamento")
    st.caption("O detalhamento completo por categoria fica na página 💰 Orçamento — aqui é só um resumo rápido.")

    if "orcamento_categorias" in st.session_state:
        df = st.session_state.orcamento_categorias
        planejado = df["Planejado (€)"].sum()
        gasto = df["Gasto (€)"].sum()
        saldo = planejado - gasto
        col1, col2, col3 = st.columns(3)
        col1.metric("Planejado", f"€ {planejado:,.2f}")
        col2.metric("Gasto até agora", f"€ {gasto:,.2f}")
        col3.metric("Saldo", f"€ {saldo:,.2f}", delta=f"{saldo:,.2f}")
    else:
        st.info("Você ainda não preencheu o orçamento. Vá até a página 💰 Orçamento para começar.")

# -------- Clima esperado --------
with tab4:
    st.subheader("Clima esperado em Dublin")
    st.caption("Médias históricas aproximadas — sempre confira a previsão real perto da data de embarque.")

    clima = pd.DataFrame(
        {
            "Mês": ["Out", "Nov", "Dez", "Jan", "Fev", "Mar"],
            "Mín (°C)": [8, 5, 3, 3, 3, 4],
            "Máx (°C)": [13, 9, 8, 8, 8, 11],
            "Chuva": ["Frequente", "Frequente", "Frequente", "Frequente", "Moderada", "Moderada"],
        }
    )
    st.dataframe(clima, use_container_width=True, hide_index=True)

    st.markdown(
        """
**Dica de vestuário:** Dublin no outono/inverno pede roupas em camadas, casaco corta-vento/impermeável
e calçado à prova d'água — chuva fina e vento são constantes mesmo quando não está muito frio.
"""
    )

# -------- Checklist geral --------
with tab5:
    st.subheader("Checklist geral rápido")
    st.caption("Uma visão rápida dos itens mais críticos. O checklist completo está na página ✅ Checklist.")
    checklist(
        [
            "Passagem aérea comprada",
            "Passaporte com validade suficiente",
            "Seguro viagem contratado",
            "Acomodação temporária reservada",
            "Escola confirmada (ILSC/Berlitz)",
            "Orçamento inicial definido",
        ],
        key_prefix="checklist_geral_visao",
    )
