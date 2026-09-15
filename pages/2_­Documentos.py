import streamlit as st
from utils import load_css, page_header, step_card, checklist

st.set_page_config(page_title="Documentos", page_icon="📄", layout="wide")
load_css()
page_header("Documentos", "Passo a passo de tudo que precisa ser regularizado na Irlanda", icon="📄")

st.markdown("### ✅ Checklist geral de documentos")
checklist(
    [
        "PPS Number solicitado",
        "IRP agendado/feito",
        "Conta bancária aberta (Revolut/AIB/Bank of Ireland)",
        "Registrado com um GP (médico de família)",
        "Leap Card (estudante) ativado",
    ],
    key_prefix="doc_geral",
)

st.markdown("---")

with st.expander("🪪 IRP — Irish Residence Permit", expanded=True):
    step_card(
        1,
        "Quando fazer",
        "Somente depois de já ter começado as aulas na ILSC/Berlitz — a escola fornece uma "
        "attendance letter que é exigida no agendamento.",
    )
    step_card(
        2,
        "Onde",
        "Registration Office, Burgh Quay, Dublin 2, D02 XK70 (primeiro registro é sempre presencial).",
    )
    step_card(
        3,
        "Como agendar",
        "Pelo portal online do Immigration Service Delivery (ISD) / Digital Contact Centre. "
        "Crie uma conta, escolha o tipo de permissão (ex.: Stamp 2 para estudante) e selecione data/horário.",
    )
    step_card(
        4,
        "O que levar",
        "- Passaporte\n"
        "- Formulário de endereço preenchido e impresso\n"
        "- Attendance letter da escola\n"
        "- Comprovante de endereço da acomodação\n"
        "- Cartão de crédito/débito para pagar a taxa de registro",
    )

with st.expander("🔢 PPS Number"):
    step_card(1, "Criar conta no MyGovID", "Acesse mygovid.ie e crie uma conta básica.")
    step_card(
        2,
        "Solicitar no MyWelfare.ie",
        "Preencha o formulário informando o motivo (estudos/trabalho) e anexe os documentos.",
    )
    step_card(
        3,
        "Documentos necessários",
        "- Comprovante de identidade (passaporte)\n"
        "- Comprovante de endereço na Irlanda (carta da acomodação/contrato)\n"
        "- Comprovante do motivo (carta da escola confirmando necessidade do PPS)",
    )
    step_card(
        4,
        "Depois de enviar",
        "Aguarde contato — pode ser necessário comparecer a um Intreo Centre para confirmar os dados. "
        "O número costuma ser enviado por carta para o endereço informado.",
    )

with st.expander("🏦 Conta bancária"):
    st.markdown(
        """
- **Revolut**: pode abrir ainda no Brasil, sem precisar de PPS. Ideal para os primeiros meses.
- **AIB / Bank of Ireland**: bancos tradicionais irlandeses, geralmente pedem comprovante de endereço e PPS Number para conta completa.
- Ter uma conta local facilita recebimento de salário e evita tarifas de conversão constantes.
"""
    )

with st.expander("🩺 Registro com um GP (médico de família)"):
    st.markdown(
        """
- Ter um GP cadastrado facilita muito o acesso ao sistema de saúde (consultas, encaminhamentos, atestados).
- Procure clínicas de GP próximas à sua acomodação e pergunte se aceitam novos pacientes (registration).
- Costuma ser necessário apresentar PPS Number e comprovante de endereço.
- Tenha seguro de saúde de estudante válido (geralmente exigido pela escola/visto).
"""
    )

with st.expander("🚌 Leap Card"):
    st.markdown(
        """
- Cartão físico pode ser comprado em pontos credenciados assim que chegar.
- Para o desconto de estudante, valide sua matrícula em leapcard.ie usando a carta da ILSC/Berlitz.
- Recarregas: app TFI, site oficial ou pontos físicos.
"""
    )

st.info(
    "⚠️ Processos de imigração e taxas mudam com frequência (já mudaram em 2020, 2022 e 2025). "
    "Confirme sempre no site oficial antes de agendar qualquer coisa."
)
