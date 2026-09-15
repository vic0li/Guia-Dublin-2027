import streamlit as st
from utils import load_css, page_header, step_card, checklist

st.set_page_config(page_title="Trabalho", page_icon="💼", layout="wide")
load_css()
page_header("Trabalho", "Currículo, vagas, homecare e o processo completo até o primeiro emprego", icon="💼")

tab1, tab2, tab3, tab4 = st.tabs(
    ["📝 Currículo", "🏢 Empresas & Sites", "🏥 Processo de Homecare", "🎓 Cursos HSE"]
)

# -------- Currículo --------
with tab1:
    st.subheader("Preparando o currículo padrão IE")
    checklist(
        [
            "Currículo simples e direto, adaptado para cada vaga",
            "Palavras-chave da vaga incluídas",
            "Sem foto, sem enrolação",
            "Salvo em Word (.docx) para aplicações online",
            "Situação de emprego com permissão legal explicada com segurança",
        ],
        key_prefix="curriculo",
    )
    st.markdown(
        """
**Estratégia de aplicação:**
- Não aplique só online — vá pessoalmente, porta a porta, principalmente para vagas de **hospitality** e **cleaning**.
- Explique sua situação de visto com clareza e segurança — isso transmite confiança ao empregador.

**Roteiro sugerido de aplicação diária:**
- 9h–12h: entrega de currículos presenciais
- Tarde: follow-up das aplicações feitas
- Noite: ajustes de currículo e novas aplicações
"""
    )

# -------- Empresas & Sites --------
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Empresas que contratam quem fala português")
        st.markdown("**Outsourcing:**")
        st.markdown("- Accenture\n- Teleperformance\n- Cognizant\n- CPL")
        st.markdown("**Porta de entrada:**")
        st.markdown("- Workhuman\n- Atlas Language School\n- Yuno")

        st.subheader("🏠 Empresas de Homecare")
        st.markdown(
            """
- Home Instead
- Comfort Keepers
- Bluebird Care
- Caremark
- MyHomecare
- Connected Health
- Virtue Integrated Care
- Heritage Homecare
- Be Independent Home Care
- Irish Homecare

Acompanhe vagas no Indeed, LinkedIn e nos sites oficiais dessas empresas.
"""
        )

    with col2:
        st.subheader("Sites de vagas")
        st.markdown(
            """
- www.irishjobs.ie
- www.jobs.ie
- www.studentjob.ie
- www.indeed.ie
- LinkedIn
"""
        )
        st.subheader("Outras fontes")
        st.markdown(
            """
- Grupos de Facebook communities
- Indicação (word of mouth)
- Plataformas de babysitting e pet care
- Conexões de vizinhança
"""
        )

# -------- Processo Homecare --------
with tab3:
    st.markdown(
        "Relato real do processo do início ao primeiro dia de trabalho como assistente de homecare "
        "(**36 dias no total**, do envio do currículo até começar a trabalhar):"
    )

    step_card(
        1,
        "Aplicação",
        "Aplicar no Indeed e nos sites das empresas de homecare, além de tentar indicação. "
        "Entrevista por telefone e depois presencial, com avaliação do nível de inglês.",
    )
    step_card(
        2,
        "Garda Vetting",
        "Encaminhamento para o Garda (polícia irlandesa) para verificação de antecedentes — "
        "essa costuma ser a etapa mais demorada do processo (levou cerca de 30 dias no relato).",
    )
    step_card(
        3,
        "Formulários e documentos",
        "Formulário extenso da empresa (cerca de 22 páginas) sobre disponibilidade, experiência no "
        "Brasil e empregos anteriores. Também é solicitado um atestado médico de aptidão ao trabalho "
        "(pode ser feito via consulta online, ~€45) e no mínimo duas cartas de recomendação de "
        "empregos anteriores na Irlanda.",
    )
    step_card(
        4,
        "Antecedentes criminais do Brasil",
        "Certificado de antecedentes criminais obtido diretamente no site da Polícia Federal/Rodoviária do Brasil.",
    )
    step_card(
        5,
        "Cursos obrigatórios HSE",
        "Enquanto aguarda o resultado do Garda Vetting, é possível ir fazendo os 12 cursos obrigatórios "
        "do HSE (veja a aba 'Cursos HSE'). É necessário concluir todos para avançar de fase.",
    )
    step_card(
        6,
        "Treinamento presencial",
        "Cerca de 3 semanas após enviar a documentação, treinamento presencial de 2 dias "
        "(segunda e terça, das 9h às 17h).",
    )

    st.success("⏱️ **Tempo total do processo relatado: 36 dias**, do envio do currículo até o início do trabalho.")

# -------- Cursos HSE --------
with tab4:
    st.markdown("Cursos do HSE necessários para estar apto ao trabalho de homecare (12 no total):")
    checklist(
        [
            "AMRIC — Putting On e Taking Off PPE",
            "Children First",
            "Safeguarding Adults at Risk of Abuse",
            "AMRIC — Hand Hygiene",
            "PPE in Community Healthcare Settings",
            "GDPR",
            "Open Disclosure",
            "Manual & People Handling",
            "Standard & Transmission Based Precautions",
            "Infection Prevention & Control",
            "HSE Cyber Security",
            "Dementia Enhanced",
            "Dignity at Work",
        ],
        key_prefix="hse",
    )
