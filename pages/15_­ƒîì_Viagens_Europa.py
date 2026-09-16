import streamlit as st
import pandas as pd
from utils import load_css, page_header, step_card

st.set_page_config(page_title="Viagens pela Europa", page_icon="🌍", layout="wide")
load_css()
page_header("Viagens pela Europa", "Destinos, estimativas de custo e melhor época para viajar", icon="🌍")

tab1, tab2, tab3, tab4 = st.tabs(
    ["🧮 Calculadora de Viagem", "💶 Estimativas por Destino", "📆 Quando Viajar", "✈️ Dicas de Passagem"]
)

# ============ Estimativas base ============
DESTINOS = {
    "Londres 🇬🇧": {"voo": 90, "hosp": 55, "alim": 35, "trans": 12, "passeios": 25, "dias": 4},
    "Paris 🇫🇷": {"voo": 100, "hosp": 50, "alim": 35, "trans": 10, "passeios": 25, "dias": 4},
    "Lisboa 🇵🇹": {"voo": 90, "hosp": 35, "alim": 25, "trans": 8, "passeios": 15, "dias": 4},
    "Porto 🇵🇹": {"voo": 85, "hosp": 32, "alim": 22, "trans": 7, "passeios": 15, "dias": 3},
    "Madri 🇪🇸": {"voo": 95, "hosp": 38, "alim": 28, "trans": 9, "passeios": 18, "dias": 4},
    "Barcelona 🇪🇸": {"voo": 100, "hosp": 45, "alim": 30, "trans": 10, "passeios": 20, "dias": 4},
    "Edimburgo 🏴": {"voo": 60, "hosp": 45, "alim": 30, "trans": 8, "passeios": 20, "dias": 3},
    "Amsterdã 🇳🇱": {"voo": 85, "hosp": 55, "alim": 35, "trans": 10, "passeios": 22, "dias": 3},
    "Roma 🇮🇹": {"voo": 100, "hosp": 42, "alim": 30, "trans": 9, "passeios": 22, "dias": 4},
    "Milão 🇮🇹": {"voo": 90, "hosp": 45, "alim": 30, "trans": 9, "passeios": 18, "dias": 3},
    "Budapeste 🇭🇺": {"voo": 95, "hosp": 28, "alim": 20, "trans": 6, "passeios": 15, "dias": 4},
    "Praga 🇨🇿": {"voo": 95, "hosp": 30, "alim": 22, "trans": 6, "passeios": 15, "dias": 4},
    "Cracóvia 🇵🇱": {"voo": 80, "hosp": 25, "alim": 18, "trans": 5, "passeios": 14, "dias": 3},
    "Berlim 🇩🇪": {"voo": 85, "hosp": 40, "alim": 28, "trans": 9, "passeios": 18, "dias": 3},
    "Belfast 🇬🇧 (ônibus)": {"voo": 30, "hosp": 40, "alim": 28, "trans": 6, "passeios": 18, "dias": 2},
    "Galway / Cliffs 🇮🇪": {"voo": 35, "hosp": 38, "alim": 25, "trans": 5, "passeios": 15, "dias": 2},
}

# ============ TAB 1: Calculadora ============
with tab1:
    st.subheader("Simule o custo de uma viagem")
    st.caption(
        "Valores-base são estimativas de mochileiro/estudante (hostel em quarto compartilhado, "
        "voo low cost com bagagem de mão). Ajuste os sliders conforme seu estilo."
    )

    col_a, col_b = st.columns([1, 1])
    with col_a:
        destino = st.selectbox("Destino", list(DESTINOS.keys()))
        base = DESTINOS[destino]
        dias = st.slider("Dias de viagem", 2, 14, base["dias"])
        estilo = st.radio(
            "Estilo de viagem",
            ["Econômico (hostel)", "Intermediário", "Confortável (hotel)"],
            horizontal=False,
        )

    mult = {"Econômico (hostel)": 0.85, "Intermediário": 1.0, "Confortável (hotel)": 1.6}[estilo]

    with col_b:
        voo = st.number_input("Voo ida e volta (€)", value=float(base["voo"]), step=10.0)
        hosp_dia = st.number_input("Hospedagem por noite (€)", value=float(base["hosp"] * mult), step=5.0)
        alim_dia = st.number_input("Alimentação por dia (€)", value=float(base["alim"] * mult), step=5.0)
        trans_dia = st.number_input("Transporte local por dia (€)", value=float(base["trans"]), step=1.0)
        passeios_dia = st.number_input("Passeios/atrações por dia (€)", value=float(base["passeios"]), step=5.0)

    noites = max(dias - 1, 1)
    total_hosp = hosp_dia * noites
    total_alim = alim_dia * dias
    total_trans = trans_dia * dias
    total_passeios = passeios_dia * dias
    subtotal = voo + total_hosp + total_alim + total_trans + total_passeios
    reserva = subtotal * 0.15
    total = subtotal + reserva

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Custo total estimado", f"€ {total:,.0f}")
    c2.metric("Por dia", f"€ {total/dias:,.0f}")
    c3.metric("Horas de trabalho (€14,15/h)", f"{total/14.15:,.0f}h")

    detalhe = pd.DataFrame(
        [
            {"Item": "Voo (ida e volta)", "Valor (€)": round(voo, 2)},
            {"Item": f"Hospedagem ({noites} noites)", "Valor (€)": round(total_hosp, 2)},
            {"Item": f"Alimentação ({dias} dias)", "Valor (€)": round(total_alim, 2)},
            {"Item": "Transporte local", "Valor (€)": round(total_trans, 2)},
            {"Item": "Passeios e atrações", "Valor (€)": round(total_passeios, 2)},
            {"Item": "Reserva de imprevistos (15%)", "Valor (€)": round(reserva, 2)},
        ]
    )
    st.dataframe(detalhe, use_container_width=True, hide_index=True)

    st.info(
        f"💡 Essa viagem equivale a cerca de **{total/14.15:,.0f} horas** de trabalho no salário mínimo "
        f"(€14,15/h bruto) — ou aproximadamente **{total/283:,.1f} semanas** trabalhando 20h."
    )

# ============ TAB 2: Estimativas por destino ============
with tab2:
    st.subheader("Comparativo rápido de destinos")
    st.caption("Estimativa para uma viagem no estilo econômico, com a duração típica sugerida para cada destino.")

    linhas = []
    for nome, d in DESTINOS.items():
        noites_d = max(d["dias"] - 1, 1)
        sub = d["voo"] + d["hosp"] * noites_d + (d["alim"] + d["trans"] + d["passeios"]) * d["dias"]
        tot = sub * 1.15
        linhas.append(
            {
                "Destino": nome,
                "Dias": d["dias"],
                "Voo (€)": d["voo"],
                "Total estimado (€)": round(tot),
                "Por dia (€)": round(tot / d["dias"]),
                "Horas de trabalho": round(tot / 14.15),
            }
        )

    df_dest = pd.DataFrame(linhas).sort_values("Total estimado (€)")
    st.dataframe(df_dest, use_container_width=True, hide_index=True)

    st.markdown("### Custo total por destino")
    st.bar_chart(df_dest.set_index("Destino")["Total estimado (€)"])

    st.markdown(
        """
**Leitura rápida:**
- **Mais baratos**: bate-voltas na Irlanda, Belfast, Cracóvia, Budapeste e Praga (leste europeu tem custo de vida bem menor).
- **Custo médio**: Portugal, Espanha, Itália, Edimburgo.
- **Mais caros**: Londres, Paris e Amsterdã — principalmente pela hospedagem.
"""
    )
    st.warning(
        "⚠️ Estes são valores de referência para planejamento, não cotações reais. Preços de voo e "
        "hospedagem variam muito conforme antecedência, época do ano e eventos locais. Confirme sempre "
        "nos sites de busca antes de fechar o orçamento."
    )

# ============ TAB 3: Quando viajar ============
with tab3:
    st.subheader("Estratégia de calendário")
    st.markdown(
        """
Como as aulas são **à tarde**, suas manhãs ficam livres — o que muda bastante a estratégia:
o trabalho de meio período tende a caber de manhã, e as viagens ficam concentradas em
fins de semana longos e nos períodos de férias.
"""
    )

    step_card(
        1,
        "Out a Dez — chegada e estruturação",
        "Prioridade é resolver burocracia (PPS, IRP, conta), achar trabalho e se adaptar. "
        "Viagens curtas e baratas: bate-voltas na Irlanda (Howth, Galway, Cliffs of Moher) e Belfast. "
        "Guarde as viagens maiores para depois de ter renda estável.",
    )
    step_card(
        2,
        "15 Dez a 15 Jan — janela de 40h",
        "Período em que a lei permite 40h/semana. Duas opções: trabalhar forte para capitalizar, "
        "ou usar parte do período para uma viagem maior (é alta temporada de Natal, então voos e "
        "hospedagem ficam mais caros). Um meio-termo comum: trabalhar em dezembro e viajar no começo de janeiro.",
    )
    step_card(
        3,
        "Jan a Maio — melhor custo-benefício para viajar",
        "Baixa temporada na Europa: passagens e hospedagem nos menores preços do ano. "
        "Como você está limitada a 20h/semana nesse período mesmo, é a melhor janela para "
        "viagens de 3-5 dias. Londres, Paris, Espanha e Portugal saem bem mais barato aqui.",
    )
    step_card(
        4,
        "Jun a Set — janela de 40h (a mais importante)",
        "Quatro meses com direito a 40h/semana. É o período que mais gera caixa no ano inteiro. "
        "Estratégia recomendada: trabalhar a maior parte e reservar 1 ou 2 semanas para uma viagem "
        "maior (ex.: Itália, leste europeu ou um roteiro com 2 países).",
    )

    st.markdown("---")
    st.markdown(
        """
**Regra prática para fins de semana longos:** com aulas à tarde, dá para sair numa quinta à noite
ou sexta de manhã e voltar domingo à noite — o que permite viagens de 3 dias sem perder muita aula.
Confirme a política de frequência da escola, já que presença mínima costuma ser exigida para o visto.
"""
    )

# ============ TAB 4: Dicas de passagem ============
with tab4:
    st.markdown(
        """
**Por que sair de Dublin é vantajoso:**
Dublin é uma base da Ryanair e recebe voos da Aer Lingus e outras low cost, com conexões diretas
para praticamente toda a Europa ocidental.

**Como conseguir os melhores preços:**
- Use buscadores como Google Flights, Skyscanner e Kiwi com alertas de preço ativados.
- Voe em **terça, quarta ou sábado** — costumam ser os dias mais baratos.
- Compre com 4 a 8 semanas de antecedência para voos dentro da Europa.
- Viaje **só com bagagem de mão**: a bagagem despachada em low cost pode custar mais que a passagem.
- Confira o aeroporto de destino: algumas low cost pousam em aeroportos secundários, longe do centro
  (ex.: Paris Beauvais), e o transfer pode comer a economia.
- Cheque se o destino é Zona Euro — Reino Unido (libra), Hungria, Polônia e República Tcheca têm
  moeda própria, o que muda o câmbio.

**Documentação importante:**
- Com o IRP válido, você circula pela **Zona Schengen** — mas **Reino Unido e Irlanda não fazem parte do Schengen**.
- Para o **Reino Unido** (Londres, Edimburgo), brasileiros precisam verificar as exigências de entrada
  vigentes, incluindo autorização eletrônica de viagem, se aplicável.
- Leve **sempre passaporte + IRP** nas viagens, mesmo dentro da Europa.
- Confirme as regras de entrada atualizadas antes de cada viagem — elas mudam com frequência.
"""
    )
    st.warning(
        "⚠️ Regras de entrada e vistos mudam com frequência e variam conforme nacionalidade. "
        "Verifique sempre nos sites oficiais de imigração de cada país antes de comprar passagem."
    )
