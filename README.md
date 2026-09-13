# 🍀 Guia Dublin — Intercâmbio 2027

App em Streamlit com o guia de preparação para o intercâmbio em Dublin (ILSC/Berlitz),
organizado em seções, com checklists interativos, passo a passo dos processos
burocráticos e visual inspirado na bandeira da Irlanda (verde, branco e laranja).

## Estrutura do projeto

```
dublin_guide/
├── app.py                          # Página inicial
├── utils.py                        # Estilo e componentes reutilizáveis
├── requirements.txt
├── .streamlit/
│   └── config.toml                 # Tema (cores) do Streamlit
└── pages/
    ├── 1_📋_Antes_de_Ir.py
    ├── 2_📄_Documentos.py
    ├── 3_🏠_Acomodação.py
    ├── 4_💼_Trabalho.py
    ├── 5_💰_Dicas_do_Dia_a_Dia.py
    └── 6_🍽️_Comida.py
```

O Streamlit reconhece automaticamente a pasta `pages/` e cria a navegação lateral
com múltiplas páginas — não precisa configurar nada além disso.

## Rodando localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publicando no GitHub + Streamlit Community Cloud

1. Crie um repositório novo no GitHub (ex.: `guia-dublin`).
2. Suba todos os arquivos **mantendo a estrutura de pastas exatamente como está**
   (o `pages/` precisa ficar na raiz do repositório, no mesmo nível do `app.py`).
3. Acesse [share.streamlit.io](https://share.streamlit.io), conecte sua conta do GitHub
   e clique em **"New app"**.
4. Selecione o repositório, a branch (`main`) e o arquivo principal `app.py`.
5. Clique em **Deploy** — em alguns minutos o app estará no ar com uma URL pública.

## Observações

- Os checkboxes e a tabela de preços de mercado usam `st.session_state`, ou seja,
  o progresso só fica salvo enquanto a aba do navegador estiver aberta (não há
  banco de dados). Se quiser persistência entre sessões, dá para evoluir depois
  usando `st.connection` com Google Sheets ou um banco simples (SQLite/Supabase).
- Os nomes de arquivo em `pages/` usam emojis e números para controlar a ordem
  e o ícone exibido no menu — pode renomear, mas mantenha o prefixo numérico
  (`1_`, `2_`, ...) para preservar a ordem.
- Informações de imigração (PPS, IRP) mudam com frequência — sempre revise nos
  sites oficiais antes de cada etapa.
