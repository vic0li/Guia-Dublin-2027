import streamlit as st
from utils import load_css, page_header

st.set_page_config(page_title="Transporte", page_icon="🚍", layout="wide")
load_css()
page_header("Transporte", "Como se locomover em Dublin: bus, Luas, DART, Leap Card e aeroporto", icon="🚍")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🚌 Bus", "🚊 Luas", "🚆 DART", "💳 Leap Card", "✈️ Aeroporto"])

with tab1:
    st.markdown(
        """
- Rede de ônibus urbanos da **Dublin Bus**, cobre praticamente toda a cidade e subúrbios.
- Consulte horários e rotas em tempo real pelo app **TFI Live** ou pelo site da Dublin Bus.
- Pagamento com Leap Card é mais barato que pagar em dinheiro direto ao motorista.
- Linhas noturnas (Nitelink) funcionam em horários e frequência reduzidos — confirme antes de contar com elas de madrugada.
"""
    )

with tab2:
    st.markdown(
        """
- **Luas** é o sistema de bondes/VLT de Dublin, com duas linhas principais:
  - **Linha Verde**: liga o centro à zona sul (ex.: Sandyford, Bride's Glen).
  - **Linha Vermelha**: liga o centro à zona oeste/leste (ex.: Tallaght, The Point).
- Boa opção para deslocamentos rápidos dentro da área central e conexões com trens/ônibus.
- Compra de bilhete/validação também é feita com Leap Card ou pelo app oficial.
"""
    )

with tab3:
    st.markdown(
        """
- **DART** (Dublin Area Rapid Transit) é o trem urbano que percorre a costa de Dublin.
- Ótimo para bate-voltas costeiros como **Howth** (norte) e **Dún Laoghaire/Bray** (sul).
- Funciona com Leap Card, tap-in/tap-out nas catracas das estações.
"""
    )

with tab4:
    st.markdown(
        """
- Cartão de transporte público usado em bus, Luas e DART — evita comprar bilhete avulso toda vez.
- **Student Leap Card**: desconto para estudantes, validado com a carta de matrícula da ILSC/Berlitz
  em leapcard.ie.
- Recarregas: app **TFI**, site oficial, ou em pontos físicos credenciados (jornaleiros, algumas lojas).
- Sempre faça o "tap" tanto na entrada quanto na saída do DART/Luas — esquecer pode gerar cobrança extra.
"""
    )

with tab5:
    st.markdown(
        """
Opções para ir do **Dublin Airport (DUB)** até o centro:

- **Aircoach**: ônibus executivo direto para vários pontos da cidade, com bagageiro.
- **Dublin Bus 16/41/757 e Airlink 747/757**: opções mais econômicas, param em pontos centrais.
- **Táxi/Uber**: mais caro, mas direto até a porta da acomodação — bom para chegadas tarde da noite ou com muita bagagem.
- Confirme sempre os valores e horários atualizados no site do aeroporto (dublinairport.com) antes de decidir.
"""
    )
