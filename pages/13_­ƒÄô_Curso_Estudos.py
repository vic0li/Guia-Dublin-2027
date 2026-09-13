import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from utils import load_css, page_header, checklist

st.set_page_config(page_title="Curso / Estudos", page_icon="🎓", layout="wide")
load_css()
page_header("Curso / Estudos", "Informações da escola, horários, materiais e rotina de estudo", icon="🎓")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏫 Curso", "📍 Local", "🕒 Horários", "📚 Materiais", "🔁 Rotina"])

with tab1:
    st.subheader("ILSC English Language School / Berlitz Language Centre Dublin")
    st.markdown(
        """
- Escola de inglês em Dublin, com aulas de idioma para estudantes internacionais.
- Confirme com a escola: carga horária semanal, nível de inglês inicial (teste de nivelamento),
  e se há certificado ao final do curso.
- Guarde sempre a **attendance letter** (carta de frequência) — ela é exigida no processo do IRP
  (ver página Documentos) e pode ser pedida em outras burocracias.
"""
    )

with tab2:
    st.subheader("Endereço da escola")
    st.markdown("**4 Swift's Alley, The Liberties, Dublin, D08 WRK6, Irlanda**")
    components.iframe(
        "https://www.google.com/maps?q=4+Swift%27s+Alley,+The_Liberties,+Dublin,+D08+WRK6,+Ireland&output=embed",
        height=400,
    )
    st.caption("Bairro: The Liberties — próximo a Christ Church e Temple Bar, boa conexão de ônibus e Luas.")

with tab3:
    st.subheader("Horários de aula")
    st.caption("Preencha conforme a escola confirmar sua grade — fica salvo durante esta sessão.")

    if "horarios_curso" not in st.session_state:
        st.session_state.horarios_curso = pd.DataFrame(
            [
                {"Dia": "Segunda", "Horário": "", "Sala/Professor": ""},
                {"Dia": "Terça", "Horário": "", "Sala/Professor": ""},
                {"Dia": "Quarta", "Horário": "", "Sala/Professor": ""},
                {"Dia": "Quinta", "Horário": "", "Sala/Professor": ""},
                {"Dia": "Sexta", "Horário": "", "Sala/Professor": ""},
            ]
        )
    st.session_state.horarios_curso = st.data_editor(
        st.session_state.horarios_curso, use_container_width=True, key="tabela_horarios"
    )

with tab4:
    st.subheader("Materiais necessários")
    checklist(
        [
            "Material didático da escola (livro/apostila indicado)",
            "Caderno e material de anotação",
            "Notebook/tablet para atividades online",
            "Fones de ouvido para exercícios de listening",
            "Aplicativo de dicionário/tradução instalado",
        ],
        key_prefix="materiais_curso",
    )

with tab5:
    st.subheader("Rotina de estudo sugerida")
    st.markdown(
        """
- **Antes da aula**: revisar vocabulário do dia anterior (15 min).
- **Depois da aula**: revisar anotações e fazer exercícios indicados (30-45 min).
- **Prática extra**: assistir séries/podcasts em inglês, conversar com colegas de turma fora da sala.
- **Fins de semana**: revisão geral da semana + planejamento da semana seguinte.
"""
    )
