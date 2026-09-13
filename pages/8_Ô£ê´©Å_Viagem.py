import streamlit as st
import pandas as pd
from utils import load_css, page_header, checklist, step_card

st.set_page_config(page_title="Viagem", page_icon="✈️", layout="wide")
load_css()
page_header("Viagem", "Voos, documentos, seguro, bagagem e preparação para o embarque", icon="✈️")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🛫 Voos", "📄 Documentos", "🩺 Seguro", "🧳 Bagagem", "🚀 Preparação"]
)

# -------- Voos --------
with tab1:
    st.subheader("Detalhes do voo")
    st.caption("Preencha conforme for comprando/confirmando as passagens. Fica salvo durante a sessão.")

    if "voos_info" not in st.session_state:
        st.session_state.voos_info = pd.DataFrame(
            [
                {"Trecho": "Ida (Brasil → Dublin)", "Companhia": "", "Data": "", "Nº do voo": "", "Conexão": ""},
                {"Trecho": "Volta (Dublin → Brasil)", "Companhia": "", "Data": "", "Nº do voo": "", "Conexão": ""},
            ]
        )
    st.session_state.voos_info = st.data_editor(
        st.session_state.voos_info, num_rows="dynamic", use_container_width=True, key="tabela_voos"
    )

    st.markdown("---")
    st.markdown(
        """
**Dicas ao comprar:**
- Prefira conexões com no mínimo 2h de intervalo (imigração e retirada de bagagem podem demorar).
- Faça o check-in online assim que abrir (geralmente 24-48h antes) para garantir assento.
- Guarde o localizador (PNR) e o número do voo em um lugar de fácil acesso offline (print/foto).
"""
    )

# -------- Documentos de viagem --------
with tab2:
    st.subheader("Documentos para embarcar")
    checklist(
        [
            "Passaporte com validade mínima de 6 meses após a volta",
            "Carta de aceite/matrícula da ILSC/Berlitz impressa",
            "Comprovante de reserva de acomodação temporária",
            "Comprovante de seguro viagem",
            "Comprovante de reserva do voo de volta (ou passagem aberta, se aplicável)",
            "Comprovante de saldo/reserva financeira para a estadia",
            "Cópias digitais (nuvem/e-mail) de todos os documentos acima",
        ],
        key_prefix="doc_viagem",
    )
    st.info(
        "⚠️ Ao entrar na Irlanda como estudante, o oficial de imigração pode pedir para ver estes "
        "documentos na chegada — tenha tudo impresso e também salvo no celular/nuvem."
    )

# -------- Seguro --------
with tab3:
    st.subheader("Seguro viagem")
    checklist(
        [
            "Seguro viagem contratado com cobertura médica adequada",
            "Cobertura mínima confirmada (verificar exigência da escola/imigração)",
            "Número da apólice e telefone de emergência anotados",
            "Cópia da apólice salva no celular e impressa",
        ],
        key_prefix="seguro",
    )
    st.markdown(
        """
- Muitas escolas de idiomas exigem um seguro saúde válido durante todo o período do curso — confirme
  o valor mínimo de cobertura exigido pela ILSC/Berlitz antes de contratar.
- Guarde o contato de emergência da seguradora em local de fácil acesso (ex.: anotação no celular
  fora do app, caso fique sem internet).
"""
    )

# -------- Bagagem --------
with tab4:
    st.subheader("Bagagem")
    st.markdown(
        """
- Confirme com a companhia aérea o **peso e tamanho permitidos** para bagagem despachada e de mão
  (varia bastante entre companhias e tipos de tarifa).
- Para estadias longas, considere levar uma mala extra vazia dobrável — útil para compras e para a volta.
- Pese a mala em casa antes de ir ao aeroporto para evitar taxas de excesso de bagagem.
"""
    )
    checklist(
        [
            "Peso e tamanho da bagagem confirmados com a companhia aérea",
            "Mala pesada em casa antes do embarque",
            "Itens de valor e documentos na bagagem de mão",
            "Etiqueta de identificação na mala despachada",
        ],
        key_prefix="bagagem_viagem",
    )

# -------- Preparação --------
with tab5:
    st.subheader("Últimos passos antes de embarcar")
    step_card(1, "Check-in online", "Feito com 24-48h de antecedência, assento escolhido.")
    step_card(2, "Avisar o banco/cartão", "Informar ao banco/cartão de crédito sobre a viagem internacional, para evitar bloqueio por uso no exterior.")
    step_card(3, "Chip/eSIM internacional temporário", "Ativar um pacote de dados internacional do chip brasileiro para os primeiros dias, até comprar o chip irlandês (ver página Antes de Ir).")
    step_card(4, "Compartilhar itinerário", "Enviar para família/amigos os dados do voo e o endereço da acomodação temporária.")
    step_card(5, "Conferir documentos impressos", "Passaporte, carta da escola, comprovante de seguro e de acomodação — todos impressos e também salvos no celular.")
