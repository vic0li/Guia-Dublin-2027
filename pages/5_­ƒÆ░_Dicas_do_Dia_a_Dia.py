import streamlit as st
from utils import load_css, page_header

st.set_page_config(page_title="Dicas do Dia a Dia", page_icon="💰", layout="wide")
load_css()
page_header("Dicas do Dia a Dia", "Como viver mais barato e se organizar em Dublin", icon="💰")

st.subheader("🌐 Sites essenciais")

sites = [
    ("Daft.ie", "Procurar casa/quarto para alugar."),
    ("Citizens Information", "Entender seus direitos como residente/estudante."),
    ("Revenue.ie", "Informações sobre impostos."),
    ("MyGovID", "Acesso a serviços públicos digitais (PPS, etc)."),
    ("Boards.ie", "Fórum com experiências de quem já morou/mora na Irlanda."),
    ("Meetup", "Conhecer pessoas e grupos de interesse."),
    ("Too Good To Go", "Comprar sobras de restaurantes/mercados por preço baixo."),
    ("TFI Live", "Consultar horários de ônibus, trens e Luas em tempo real."),
    ("Adverts.ie", "Comprar e vender produtos novos e usados."),
]

cols = st.columns(3)
for i, (nome, desc) in enumerate(sites):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="step-card">
                <h4>🔗 {nome}</h4>
                <p style="margin:0;color:#333;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")
st.subheader("💡 Dicas gerais para economizar")
st.markdown(
    """
- Use o **Too Good To Go** diariamente para refeições/mercado com desconto grande no fim do dia.
- Compare preços entre **Aldi, Lidl, Tesco e Dunnes Stores** — Aldi e Lidl costumam ser os mais baratos para o básico.
- Ative o **Student Leap Card** assim que possível — a economia no transporte é significativa no longo prazo.
- Cozinhar em casa a maior parte da semana, reservando refeições fora para ocasiões específicas.
- Fique de olho em grupos de Facebook/Meetup da comunidade brasileira e de estudantes internacionais em Dublin — costuma ter dicas de promoções, caronas e produtos em segunda mão.
- Compras de roupas e itens de casa em segunda mão: Adverts.ie, grupos de Facebook Marketplace e charity shops (Oxfam, Enable Ireland, etc.) costumam ser bem mais baratos.
"""
)
