import streamlit as st
import pandas as pd
from utils import load_css, page_header, step_card

st.set_page_config(page_title="Renda e Horas", page_icon="💶", layout="wide")
load_css()
page_header("Renda e Horas", "Quanto dá para ganhar, quanto sobra e como isso vira viagem", icon="💶")

SALARIO_HORA = 14.15

tab1, tab2, tab3, tab4 = st.tabs(
    ["🧮 Simulador de Renda", "📅 Regras de Horas", "🏦 Quanto Sobra", "🎯 Meta de Viagem"]
)

# ============ TAB 1: Simulador ============
with tab1:
    st.subheader("Simule sua renda mensal")

    col1, col2 = st.columns(2)
    with col1:
        horas = st.slider("Horas por semana", 0, 40, 20)
        valor_hora = st.number_input("Valor da hora (€)", value=SALARIO_HORA, step=0.25)
    with col2:
        semanas_mes = st.number_input("Semanas por mês", value=4.33, step=0.01, format="%.2f")
        st.caption("4,33 é a média usada oficialmente (52 semanas ÷ 12 meses).")

    bruto_semana = horas * valor_hora
    bruto_mes = bruto_semana * semanas_mes
    bruto_ano = bruto_semana * 52

    # Estimativa simplificada de descontos
    if horas <= 20:
        desconto_pct = 0.02
    elif horas <= 30:
        desconto_pct = 0.10
    else:
        desconto_pct = 0.13

    liquido_mes = bruto_mes * (1 - desconto_pct)

    c1, c2, c3 = st.columns(3)
    c1.metric("Bruto por semana", f"€ {bruto_semana:,.0f}")
    c2.metric("Bruto por mês", f"€ {bruto_mes:,.0f}")
    c3.metric("Líquido estimado/mês", f"€ {liquido_mes:,.0f}")

    st.markdown("---")
    st.markdown("### Comparativo de cenários")

    cenarios = []
    for h in [15, 20, 25, 30, 40]:
        b_sem = h * valor_hora
        b_mes = b_sem * semanas_mes
        d = 0.02 if h <= 20 else (0.10 if h <= 30 else 0.13)
        cenarios.append(
            {
                "Horas/semana": h,
                "Bruto/semana (€)": round(b_sem),
                "Bruto/mês (€)": round(b_mes),
                "Líquido aprox./mês (€)": round(b_mes * (1 - d)),
                "Permitido?": "✅ Sempre" if h <= 20 else ("⚠️ Só jun-set e 15dez-15jan" if h <= 40 else "❌"),
            }
        )
    st.dataframe(pd.DataFrame(cenarios), use_container_width=True, hide_index=True)

    st.warning(
        "⚠️ Os descontos (IRPF irlandês, USC e PRSI) são uma **estimativa simplificada** apenas para "
        "planejamento. O valor real depende dos seus créditos fiscais, do número de empregos e de como "
        "o empregador registra você no Revenue. Consulte o site do Revenue ou um contador para números precisos."
    )

# ============ TAB 2: Regras de horas ============
with tab2:
    st.subheader("O que a lei permite (Stamp 2)")

    st.error(
        "**Ponto crítico:** o limite de 20h/semana é o total somado de TODOS os empregos, não por emprego. "
        "Ter dois trabalhos de 15h cada resulta em 30h — acima do permitido. O limite é um máximo semanal "
        "absoluto, não uma média. Descumprir pode levar à revogação da permissão de estudante, o que afeta "
        "diretamente a renovação do IRP."
    )

    st.markdown(
        """
**Períodos em que 40h/semana são permitidas** (datas fixas definidas pela imigração, independentes
do calendário da sua escola):

- **1º de junho a 30 de setembro** (4 meses)
- **15 de dezembro a 15 de janeiro** (1 mês)

Em todo o resto do ano: **máximo de 20h por semana**.
"""
    )

    calendario = pd.DataFrame(
        [
            {"Período": "Outubro a 14 de dezembro", "Limite": "20h/semana", "Foco sugerido": "Adaptação, burocracia, bate-voltas baratos"},
            {"Período": "15 dez a 15 jan", "Limite": "40h/semana", "Foco sugerido": "Trabalhar forte (alta temporada encarece viagem)"},
            {"Período": "16 jan a 31 maio", "Limite": "20h/semana", "Foco sugerido": "Melhor época para viajar (baixa temporada)"},
            {"Período": "1 jun a 30 set", "Limite": "40h/semana", "Foco sugerido": "Maior geração de caixa do ano + 1 viagem longa"},
        ]
    )
    st.dataframe(calendario, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown(
        """
**Outras restrições do Stamp 2:**
- Não é permitido trabalhar como autônomo/self-employed.
- Não é permitido trabalhar como motorista de táxi.
- A permissão de trabalhar termina junto com a validade do Stamp 2.
- É necessário ter **IRP válido e PPS Number** para trabalhar legalmente.

**Sobre férias remuneradas:** trabalhadores na Irlanda têm direito a férias proporcionais às horas
trabalhadas (annual leave), inclusive em meio período. Vale confirmar com o empregador como isso
funciona no seu contrato — são esses dias que podem financiar as viagens curtas.
"""
    )
    st.info(
        "⚠️ Regras de imigração mudam com frequência. Confirme sempre em irishimmigration.ie e "
        "citizensinformation.ie antes de assumir qualquer compromisso de trabalho."
    )

# ============ TAB 3: Quanto sobra ============
with tab3:
    st.subheader("Renda menos custo de vida = dinheiro para viajar")
    st.caption("Ajuste os custos mensais conforme sua realidade em Dublin.")

    col1, col2 = st.columns(2)
    with col1:
        horas_v = st.slider("Horas/semana trabalhadas", 0, 40, 20, key="horas_sobra")
        bruto_m = horas_v * SALARIO_HORA * 4.33
        d = 0.02 if horas_v <= 20 else (0.10 if horas_v <= 30 else 0.13)
        liquido_m = bruto_m * (1 - d)
        st.metric("Renda líquida estimada/mês", f"€ {liquido_m:,.0f}")

    with col2:
        aluguel = st.number_input("Aluguel/quarto (€)", value=800.0, step=50.0)
        comida = st.number_input("Alimentação (€)", value=250.0, step=25.0)
        transporte = st.number_input("Transporte (€)", value=60.0, step=10.0)
        celular = st.number_input("Celular/internet (€)", value=20.0, step=5.0)
        outros = st.number_input("Outros (lazer, higiene, etc.) (€)", value=150.0, step=25.0)

    custo_total = aluguel + comida + transporte + celular + outros
    sobra = liquido_m - custo_total

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Custo de vida/mês", f"€ {custo_total:,.0f}")
    c2.metric("Sobra por mês", f"€ {sobra:,.0f}", delta=f"{sobra:,.0f}")
    c3.metric("Sobra em 6 meses", f"€ {sobra*6:,.0f}")

    if sobra < 0:
        st.error(
            "Com essa configuração o orçamento fica negativo. Considere: dividir quarto para reduzir "
            "aluguel, aumentar horas nos períodos permitidos (jun-set, 15dez-15jan), ou buscar funções "
            "com valor/hora acima do mínimo (homecare costuma pagar mais que o mínimo)."
        )
    elif sobra < 200:
        st.warning("Sobra apertada — as viagens vão depender muito dos períodos de 40h/semana.")
    else:
        st.success(f"Com €{sobra:,.0f}/mês sobrando, dá para fazer cerca de uma viagem média a cada 2 meses.")

# ============ TAB 4: Meta de viagem ============
with tab4:
    st.subheader("Quanto tempo para juntar o valor de uma viagem")

    col1, col2 = st.columns(2)
    with col1:
        meta = st.number_input("Custo da viagem (€)", value=600.0, step=50.0)
        st.caption("Use a calculadora da página 🌍 Viagens Europa para estimar esse valor.")
    with col2:
        poupanca_mes = st.number_input("Quanto consigo poupar por mês (€)", value=300.0, step=50.0)

    if poupanca_mes > 0:
        meses = meta / poupanca_mes
        horas_necessarias = meta / SALARIO_HORA
        c1, c2 = st.columns(2)
        c1.metric("Tempo para juntar", f"{meses:,.1f} meses")
        c2.metric("Horas de trabalho equivalentes", f"{horas_necessarias:,.0f}h")
    else:
        st.info("Informe um valor de poupança mensal maior que zero.")

    st.markdown("---")
    st.markdown("### Plano sugerido de viagens ao longo do ano")
    step_card(1, "Out-Dez", "Bate-voltas baratos na Irlanda (€60-150 cada). Foco em se estabelecer.")
    step_card(2, "Jan-Maio", "2 a 4 viagens curtas na baixa temporada — Portugal, Espanha, leste europeu são os melhores custo-benefício.")
    step_card(3, "Jun-Set", "Trabalhar 40h para capitalizar + 1 viagem maior de 7 a 14 dias.")
    st.caption(
        "Esse plano é um ponto de partida — ajuste conforme sua renda real, o valor do aluguel que "
        "conseguir e as oportunidades de trabalho que aparecerem."
    )
