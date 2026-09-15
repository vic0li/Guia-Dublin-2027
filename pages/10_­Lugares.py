import streamlit as st
from utils import load_css, page_header

st.set_page_config(page_title="Lugares", page_icon="🏛️", layout="wide")
load_css()
page_header("Lugares", "Ideias de pontos turísticos, museus, gastronomia e natureza em Dublin", icon="🏛️")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["🏛️ Pontos Turísticos", "🖼️ Museus", "🍽️ Restaurantes", "☕ Cafés", "🍺 Pubs", "🌳 Natureza"]
)

with tab1:
    st.markdown(
        """
- **Trinity College** — universidade histórica, biblioteca com o *Book of Kells*.
- **Dublin Castle** — antigo centro de poder britânico na Irlanda.
- **Christ Church Cathedral** e **St Patrick's Cathedral** — as duas grandes catedrais medievais da cidade.
- **Temple Bar** — bairro histórico e boêmio, famoso pelos pubs e vida noturna.
- **St. Stephen's Green** — parque central, ótimo para uma pausa entre um ponto turístico e outro.
- **Ha'penny Bridge** — ponte pedestre icônica sobre o rio Liffey.
"""
    )

with tab2:
    st.markdown(
        """
- **Guinness Storehouse** — história da cervejaria mais famosa da Irlanda, com vista panorâmica no topo.
- **EPIC The Irish Emigration Museum** — história da diáspora irlandesa, bem interativo.
- **Kilmainham Gaol** — antiga prisão, ligada à história da independência irlandesa.
- **National Museum of Ireland** (Archaeology / Natural History) — entrada gratuita.
- **National Gallery of Ireland** — acervo de arte, também com entrada gratuita.
"""
    )

with tab3:
    st.markdown(
        """
- Explore a região de **Camden Street** e **George's Street**, com boa variedade de preços.
- **Food markets** (ex.: mercados de fim de semana) costumam ter opções mais baratas e variadas.
- Restaurantes asiáticos e indianos em geral têm ótimo custo-benefício em Dublin.
- Para ocasiões especiais, o bairro de **Temple Bar** tem opções mais turísticas (e mais caras).
"""
    )
    st.caption("Adicione aqui seus próprios favoritos conforme for testando — esta lista é só um ponto de partida.")

with tab4:
    st.markdown(
        """
- Dublin tem uma cena de café bem forte — vale explorar cafeterias independentes no bairro de
  **The Liberties** (perto da escola) e em **Rathmines**/**Portobello**.
- Cafés com boa opção para estudar (wi-fi, tomadas) costumam ficar cheios em horário de almoço —
  bom ir de manhã cedo ou no meio da tarde.
"""
    )

with tab5:
    st.markdown(
        """
Sugestões de pubs para conhecer a cultura irlandesa:

- The Brazen Head — um dos pubs mais antigos de Dublin.
- Grogan's — clássico, boa opção para socializar.
- The Stags Head — pub tradicional vitoriano.
- Bad Bobs / The Church — mais movimentado, próximo a Temple Bar.
- 4 Dame Lane — vida noturna mais jovem (18+/21+, conferir regras de idade).

Para baladas: Coppers Face Jacks, The Academy e Dicey's Garden são pontos conhecidos entre estudantes internacionais.
"""
    )
    st.caption("Confira sempre a idade mínima de entrada (muitos lugares exigem 21+ à noite) e horários de funcionamento.")

with tab6:
    st.markdown(
        """
- **Phoenix Park** — um dos maiores parques urbanos murados da Europa, com veados selvagens.
- **Howth Cliff Walk** — trilha costeira curta e acessível de DART.
- **Dublin Bay / Sandymount Strand** — praia urbana para caminhadas.
- **Wicklow Mountains National Park** — natureza a poucas horas da cidade, ótimo para um bate-volta.
- **Bull Island** — reserva natural próxima ao centro, boa para pássaros e praia tranquila.
"""
    )
