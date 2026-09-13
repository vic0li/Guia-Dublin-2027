"""
Componentes e estilo compartilhados do Guia Dublin 🍀
Paleta inspirada na bandeira da Irlanda: verde, branco e laranja.
"""

import streamlit as st

# ---------- Paleta ----------
GREEN = "#169B62"
GREEN_DARK = "#0E7A4D"
GREEN_LIGHT = "#4FD897"
ORANGE = "#FF883E"
ORANGE_DARK = "#E8672A"
WHITE = "#FFFFFF"
CREAM = "#FBFBF8"
TEXT = "#1B1B1B"


def load_css():
    st.markdown(
        f"""
        <style>
        /* Fundo geral: não força cor — respeita o tema claro/escuro do Streamlit */

        /* Barra tricolor no topo de cada página */
        .tricolor-bar {{
            height: 8px;
            width: 100%;
            background: linear-gradient(to right, {GREEN} 0%, {GREEN} 33%, {WHITE} 33%, {WHITE} 66%, {ORANGE} 66%, {ORANGE} 100%);
            border-radius: 6px;
            margin-bottom: 1.2rem;
        }}

        /* Cabeçalho de página */
        .page-header {{
            padding: 1.1rem 1.4rem;
            border-radius: 14px;
            background: linear-gradient(120deg, {GREEN} 0%, {GREEN_DARK} 100%);
            color: white;
            margin-bottom: 1.4rem;
            box-shadow: 0 4px 14px rgba(22,155,98,0.25);
        }}
        .page-header h1 {{
            margin: 0;
            font-size: 1.7rem;
            color: {WHITE} !important;
        }}
        .page-header p {{
            margin: 0.3rem 0 0 0;
            opacity: 0.92;
            font-size: 0.95rem;
            color: {WHITE} !important;
        }}

        /* Sidebar */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {GREEN_DARK} 0%, {GREEN} 100%);
        }}
        section[data-testid="stSidebar"] * {{
            color: white !important;
        }}

        /* Cards de etapa — fundo branco fixo, texto escuro fixo, funciona em qualquer tema */
        .step-card {{
            border-left: 6px solid {ORANGE};
            background: {WHITE};
            border-radius: 10px;
            padding: 0.9rem 1.1rem;
            margin-bottom: 0.8rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            color: {TEXT};
        }}
        .step-card h4 {{
            margin: 0 0 0.35rem 0;
            color: {GREEN_DARK};
        }}
        .step-card p {{
            color: {TEXT} !important;
        }}

        /* Badges */
        .badge {{
            display: inline-block;
            background: {ORANGE};
            color: white;
            border-radius: 999px;
            padding: 0.15rem 0.7rem;
            font-size: 0.75rem;
            font-weight: 600;
            margin-right: 0.4rem;
        }}

        /* Botões */
        .stButton>button, .stDownloadButton>button {{
            background-color: {ORANGE};
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
        }}
        .stButton>button:hover, .stDownloadButton>button:hover {{
            background-color: {ORANGE_DARK};
            color: white;
        }}

        /* Progress bar custom color */
        div[role="progressbar"] > div > div {{
            background-color: {GREEN} !important;
        }}

        /* Expander header */
        .streamlit-expanderHeader {{
            font-weight: 600;
            color: {GREEN_DARK};
        }}

        h1, h2, h3 {{
            color: {GREEN_DARK};
        }}

        a {{
            color: {ORANGE_DARK} !important;
            font-weight: 600;
        }}

        /* No modo escuro, o verde escuro fica com pouco contraste — clareamos só os títulos */
        @media (prefers-color-scheme: dark) {{
            h1, h2, h3, .streamlit-expanderHeader {{
                color: {GREEN_LIGHT} !important;
            }}
            a {{
                color: {ORANGE} !important;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def tricolor_bar():
    st.markdown('<div class="tricolor-bar"></div>', unsafe_allow_html=True)


def page_header(title: str, subtitle: str = "", icon: str = "🍀"):
    tricolor_bar()
    st.markdown(
        f"""
        <div class="page-header">
            <h1>{icon} {title}</h1>
            {f'<p>{subtitle}</p>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def step_card(number, title, content_markdown):
    st.markdown(
        f"""
        <div class="step-card">
            <h4>Passo {number} — {title}</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(content_markdown)


def checklist(items: list, key_prefix: str):
    """Renderiza uma lista de checkboxes e retorna o progresso (0-1)."""
    done = 0
    for i, item in enumerate(items):
        checked = st.checkbox(item, key=f"{key_prefix}_{i}")
        if checked:
            done += 1
    total = len(items) if items else 1
    progress = done / total
    st.progress(progress, text=f"{done}/{len(items)} concluído")
    return progress


def badge(text: str):
    st.markdown(f'<span class="badge">{text}</span>', unsafe_allow_html=True)
