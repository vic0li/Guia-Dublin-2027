import streamlit as st
from utils import load_css, page_header, checklist

st.set_page_config(page_title="Checklist", page_icon="✅", layout="wide")
load_css()
page_header("Checklist", "Checklist consolidado do começo ao fim do intercâmbio", icon="✅")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🚀 Antes da Viagem", "🧳 Mala", "📄 Documentos", "✈️ Durante a Viagem", "🏡 Volta"]
)

with tab1:
    st.subheader("Antes da viagem")
    checklist(
        [
            "Passagem aérea comprada",
            "Escola confirmada e matrícula paga (ILSC/Berlitz)",
            "Acomodação temporária reservada",
            "Seguro viagem contratado",
            "Orçamento inicial planejado (ver página Orçamento)",
            "Câmbio/reserva inicial em euros ou Revolut carregado",
            "Avisar banco/cartão sobre a viagem internacional",
            "Aplicativos essenciais instalados (TFI Live, Revolut, Google Maps offline)",
        ],
        key_prefix="check_antes",
    )

with tab2:
    st.subheader("Mala")
    checklist(
        [
            "Roupas em camadas para clima ameno e chuvoso",
            "Casaco corta-vento/impermeável",
            "Calçado à prova d'água",
            "Remédios de uso contínuo + receitas",
            "Produtos de cabelo essenciais (chapinha/secador bivolt)",
            "Adaptador de tomada padrão G",
            "Roupa social básica para entrevistas de emprego",
        ],
        key_prefix="check_mala",
    )

with tab3:
    st.subheader("Documentos")
    checklist(
        [
            "Passaporte com validade suficiente",
            "Carta de aceite/matrícula da escola impressa",
            "Comprovante de acomodação temporária",
            "Comprovante de seguro viagem",
            "Cópias digitais de todos os documentos (nuvem/e-mail)",
        ],
        key_prefix="check_documentos_geral",
    )
    st.caption("Para os documentos burocráticos feitos já na Irlanda (PPS, IRP, banco), veja a página Documentos.")

with tab4:
    st.subheader("Durante a viagem")
    checklist(
        [
            "Check-in online feito",
            "Documentos e itens de valor na bagagem de mão",
            "Chip/eSIM internacional ativado para os primeiros dias",
            "Itinerário compartilhado com família/amigos",
            "Endereço da acomodação temporária salvo offline",
        ],
        key_prefix="check_durante",
    )

with tab5:
    st.subheader("Volta")
    checklist(
        [
            "Passagem de volta confirmada/reemitida se necessário",
            "Documentos de saída da Irlanda organizados",
            "Contas e serviços locais encerrados/avisados (banco, aluguel, etc.)",
            "Bagagem organizada dentro do limite de peso",
            "Souvenirs e lembranças separados com antecedência",
        ],
        key_prefix="check_volta",
    )
