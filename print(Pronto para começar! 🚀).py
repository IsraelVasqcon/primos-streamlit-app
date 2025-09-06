import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeiros_primos(quantidade):
    primos = []
    num = 2
    while len(primos) < quantidade:
        if eh_primo(num):
            primos.append(num)
        num += 1
    return primos

# Sidebar controls
st.sidebar.title("Configurações")
n = st.sidebar.slider("Quantidade de primos:", 2, 100, 10)
tipo = st.sidebar.selectbox("Tipo de gráfico", ['Barras', 'Pizza'])

# Main title
st.title("Visualizador de Números Primos")

primos = primeiros_primos(n)
df = pd.DataFrame({'Índice': range(1, n+1), 'Primo': primos})

# Show stats
st.subheader("Estatísticas")
st.write(f"**Soma dos primos:** {sum(primos)}")
st.write(f"**Média dos primos:** {sum(primos)/len(primos):.2f}")
st.write(f"**Maior primo:** {max(primos)}")

# Show table
with st.expander("Mostrar tabela de primos"):
    st.dataframe(df)

# Download CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Baixar CSV dos primos",
    data=csv,
    file_name='primos.csv',
    mime='text/csv'
)

# Plot
fig, ax = plt.subplots()
if tipo == 'Barras':
    colors = ['skyblue'] * (n-1) + ['orange']  # Highlight last bar
    ax.bar(range(1, n+1), primos, color=colors)
    ax.set_title("Gráfico de Barras")
    ax.set_xlabel("Índice")
    ax.set_ylabel("Valor Primo")
    ax.bar_label(ax.containers[0])
else:
    labels = [f"P{i+1}" for i in range(n)]
    explode = [0.05] * n
    ax.pie(primos, labels=labels, explode=explode, autopct='%1.1f%%', startangle=140)
    ax.set_title("Gráfico de Pizza")
st.pyplot(fig)

# About section
with st.expander("Sobre este app"):
    st.markdown("""
    - Desenvolvido com [Streamlit](https://streamlit.io/)
    - Visualize, baixe e explore os primeiros números primos.
    - Autor: Israel Siqueira
    - [GitHub](IsraelSiqueira) | [LinkedIn](https://www.linkedin.com/in/israelsiqueira/)
    """)
    
    import csv

    filename = "primos.csv"
    data = []

    with open(filename, 'primos.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        # Optionally, skip the header row if present
        # header = next(csvreader) 
        for row in csvreader:
            data.append(row)

    print(data)