import streamlit as st
from utils import load_css, page_header, checklist, step_card

st.set_page_config(page_title="Antes de Ir", page_icon="📋", layout="wide")
load_css()
page_header("Antes de Ir", "Checklists de preparação e o que já dá para adiantar no Brasil", icon="📋")

tab1, tab2 = st.tabs(["✅ Checklists da Mala", "🚀 O que já dá para adiantar"])

# ---------------- TAB 1: Checklists ----------------
with tab1:
    st.subheader("Mala e roupas")
    st.caption("Dublin tem clima ameno mas chuvoso o ano todo — priorize camadas e itens à prova d'água.")
    checklist(
        [
            "Casaco corta-vento/impermeável (chuva é constante)",
            "Roupas em camadas (base térmica + moletom + casaco)",
            "Guarda-chuva compacto e/ou capa de chuva",
            "Tênis à prova d'água / bota curta",
            "Roupa social básica para entrevistas de emprego",
            "Adaptador de tomada (padrão G — 3 pinos)",
            "Conversor de voltagem se necessário (220-240V)",
        ],
        key_prefix="mala",
    )

    st.subheader("Remédios e pomadas")
    st.caption("Leve as receitas médicas (em inglês, se possível) para remédios controlados.")
    checklist(
        [
            "Remédios de uso contínuo (quantidade para todo o período)",
            "Receitas médicas traduzidas/em inglês",
            "Pomadas e cremes de uso recorrente",
            "Analgésicos e antialérgicos básicos",
            "Kit de primeiros socorros pequeno",
        ],
        key_prefix="remedios",
    )

    st.subheader("Produtos de cabelo")
    checklist(
        [
            "Chapinha/secador mini (bivolt)",
            "Tinta de cabelo (se usar cor específica difícil de achar lá)",
            "Hidratantes e produtos de finalização",
            "Escova/pente de viagem",
        ],
        key_prefix="cabelo",
    )

    st.subheader("O que pode e não pode na mala")
    st.markdown(
        """
- **Líquidos na bagagem de mão**: máximo 100ml por frasco, em saco transparente.
- **Medicamentos**: podem ir na bagagem de mão, de preferência com a receita.
- **Alimentos**: evite carnes, laticínios e produtos in natura — a alfândega irlandesa/UE restringe.
- **Valores em dinheiro**: declarar se levar acima de €10.000 (entrando na UE).
- Confirme sempre as regras atualizadas no site da companhia aérea antes de fazer as malas.
"""
    )

# ---------------- TAB 2: Passo a passo ----------------
with tab2:
    st.markdown("Processos que você pode começar a organizar **ainda no Brasil**, antes do embarque.")

    step_card(
        1,
        "Chip / eSIM irlandês (Three)",
        """
- A operadora **Three** vende planos pré-pagos a partir de ~€20 por 28 dias (confirme o valor atual no site da Three).
- Duas opções:
  - **Chip físico**: comprar em loja física assim que chegar (é o mais simples, não precisa de PPS).
  - **eSIM**: algumas operadoras já vendem eSIM online antes mesmo de embarcar — vale ativar um plano internacional de dados do seu chip brasileiro só para os primeiros dias, e comprar o chip irlandês local ao chegar.
- Leve seu número do Brasil ativo em roaming ou WhatsApp com Wi-Fi para os primeiros dias, até resolver o chip local.
""",
    )

    step_card(
        2,
        "Leap Card",
        """
- É o cartão de transporte público de Dublin (ônibus, DART, Luas).
- Pode comprar o cartão físico em lojas credenciadas (jornaleiros, algumas farmácias) assim que chegar.
- Para o **desconto estudantil**, é necessário validar sua matrícula com a carta da escola (Student Leap Card), processo geralmente feito online em leapcard.ie após ter a carta de matrícula da ILSC/Berlitz em mãos.
- Recarregas podem ser feitas no site, app ou em pontos físicos (TFI).
""",
    )

    step_card(
        3,
        "PPS Number (número fiscal)",
        """
- **Não pode ser solicitado antes de chegar à Irlanda** — é necessário estar fisicamente no país e já ter endereço de acomodação.
- Passo a passo geral:
  1. Criar uma conta básica no **MyGovID** (mygovid.ie).
  2. Acessar o **MyWelfare.ie** e solicitar o PPS Number online.
  3. Anexar comprovante de identidade (passaporte) e comprovante de endereço (carta da acomodação, contrato de aluguel ou carta da escola).
  4. Em alguns casos você é chamado para um atendimento presencial num Intreo Centre para confirmar os dados.
- Leve sempre a carta de matrícula/attendance letter da escola — ela costuma servir como comprovante de necessidade do PPS.
""",
    )

    step_card(
        4,
        "Revolut",
        """
- Pode iniciar a abertura da conta **ainda no Brasil**, direto pelo app, usando seu documento brasileiro.
- Após chegar na Irlanda, atualize o endereço residencial no app assim que tiver a acomodação definitiva.
- É uma alternativa mais rápida que os bancos tradicionais (AIB, Bank of Ireland) enquanto você não tem PPS/comprovante definitivo.
""",
    )

    step_card(
        5,
        "IRP (Irish Residence Permit)",
        """
- Só deve ser feito **depois de chegar** e **depois de começar as aulas** — é necessário apresentar a carta de frequência (attendance letter) da escola.
- Desde 2025, o primeiro registro (first-time registration) para todo o país passou a ser feito presencialmente no **Registration Office em Burgh Quay, Dublin**, mediante agendamento pelo portal do Immigration Service Delivery (ISD).
- Documentos a levar: passaporte, formulário de endereço preenchido, comprovantes exigidos impressos e taxa de registro (pagamento só por cartão de crédito/débito).
- Prazo: o registro deve ser feito dentro de 90 dias a partir da chegada — mas na prática, agende assim que tiver a attendance letter da escola.
- **Atenção**: os prazos e valores da taxa mudam com frequência — confirme sempre no site oficial (irishimmigration.ie) antes de agendar.
""",
    )

    st.warning(
        "As regras de imigração citadas aqui foram verificadas em 2026, mas historicamente mudam com "
        "frequência (já mudaram em 2020, 2022 e 2025). Revise o processo oficial mais perto da data da viagem."
    )
