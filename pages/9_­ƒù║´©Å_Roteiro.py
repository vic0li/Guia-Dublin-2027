import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from utils import load_css, page_header, step_card

st.set_page_config(page_title="Roteiro", page_icon="🗺️", layout="wide")
load_css()
page_header("Roteiro", "Sugestões de roteiro em Dublin, bate-voltas, rotina e mapas", icon="🗺️")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🏙️ Dublin", "🚗 Bate-voltas", "📆 Dia a Dia", "🗺️ Mapas", "📌 Lugares Salvos"]
)

# -------- Dublin --------
with tab1:
    st.subheader("Roteiro sugerido para conhecer Dublin")
    step_card(1, "Centro histórico", "Trinity College, Grafton Street, St. Stephen's Green — bom para o primeiro fim de semana, tudo próximo e a pé.")
    step_card(2, "The Liberties & Templebar", "Christ Church Cathedral, Dublin Castle, Temple Bar — próximo da escola (ILSC/Berlitz fica no bairro The Liberties).")
    step_card(3, "Guinness Storehouse & Kilmainham", "Guinness Storehouse e Kilmainham Gaol, no mesmo eixo oeste da cidade — dá para fazer no mesmo dia.")
    step_card(4, "Docklands & Phoenix Park", "Área moderna perto do rio Liffey e o Phoenix Park, um dos maiores parques urbanos da Europa.")
    st.caption("Ajuste a ordem conforme o clima do dia — dias de chuva, priorize museus e lugares cobertos.")

# -------- Bate-voltas --------
with tab2:
    st.subheader("Bate-voltas populares saindo de Dublin")
    bate_voltas = pd.DataFrame(
        [
            {"Destino": "Howth", "Tempo de viagem": "~30 min (DART)", "Destaque": "Vila de pescadores, trilha costeira e frutos do mar"},
            {"Destino": "Wicklow / Glendalough", "Tempo de viagem": "~1h (tour/carro)", "Destaque": "Montanhas, lago e ruínas monásticas"},
            {"Destino": "Belfast", "Tempo de viagem": "~2h (trem/ônibus)", "Destaque": "Titanic Museum e história da Irlanda do Norte"},
            {"Destino": "Cliffs of Moher", "Tempo de viagem": "~4-5h (tour de dia inteiro)", "Destaque": "Falésias famosas na costa oeste"},
            {"Destino": "Galway", "Tempo de viagem": "~2h30 (ônibus)", "Destaque": "Cidade costeira boêmia, boa vida noturna"},
            {"Destino": "Cork & Cobh", "Tempo de viagem": "~2h30 (trem)", "Destaque": "Segunda maior cidade + porto histórico"},
        ]
    )
    st.dataframe(bate_voltas, use_container_width=True, hide_index=True)
    st.caption("Tempos são aproximados — confirme sempre nos apps de transporte (TFI Live, Citylink, GoBus) antes de planejar.")

# -------- Dia a dia --------
with tab3:
    st.subheader("Rotina sugerida de dia a dia")
    st.markdown(
        """
- **Manhã**: aulas na ILSC/Berlitz.
- **Tarde**: estudo, procura de emprego/trabalho ou exploração da cidade em dias livres.
- **Fim de tarde/noite**: preparo de refeições, socialização (Meetup, colegas de curso), estudo de inglês.
- **Fins de semana**: reservar para bate-voltas, turismo mais completo e descanso.
"""
    )
    st.caption("Ajuste essa rotina conforme sua carga horária de aulas e eventual trabalho.")

# -------- Mapas --------
with tab4:
    st.subheader("Mapa da região da escola")
    st.caption("ILSC English Language School / Berlitz Language Centre Dublin — 4 Swift's Alley, The Liberties, Dublin, D08 WRK6")
    components.iframe(
        "https://www.google.com/maps?q=4+Swift%27s+Alley,+The+Liberties,+Dublin,+D08+WRK6,+Ireland&output=embed",
        height=420,
    )
    st.caption(
        "Dica: use este mapa como referência ao procurar acomodação — quanto mais perto ou melhor "
        "conectado por ônibus/Luas a este ponto, mais fácil o dia a dia."
    )

# -------- Lugares salvos --------
with tab5:
    st.subheader("Lugares que você quer visitar")
    st.caption("Adicione, edite ou marque como visitado — fica salvo durante esta sessão do navegador.")

    if "lugares_salvos" not in st.session_state:
        st.session_state.lugares_salvos = pd.DataFrame(
            [
                {"Lugar": "Trinity College", "Categoria": "Turístico", "Visitado": False, "Notas": ""},
                {"Lugar": "Howth", "Categoria": "Bate-volta", "Visitado": False, "Notas": ""},
            ]
        )
    st.session_state.lugares_salvos = st.data_editor(
        st.session_state.lugares_salvos,
        num_rows="dynamic",
        use_container_width=True,
        key="tabela_lugares_salvos",
        column_config={"Visitado": st.column_config.CheckboxColumn("Visitado")},
    )
