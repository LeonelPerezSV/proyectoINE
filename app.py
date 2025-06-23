import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

def linea_recta(costo, residual, vida):
    d = (costo - residual) / vida
    depreciaciones = [d] * vida
    valor_en_libros = [costo - d * (i + 1) for i in range(vida)]
    return depreciaciones, valor_en_libros

def saldo_decreciente(costo, vida, tasa=0.2):
    depreciaciones = []
    valor_en_libros = []
    actual = costo
    for _ in range(vida):
        d = actual * tasa
        depreciaciones.append(d)
        actual -= d
        valor_en_libros.append(actual)
    return depreciaciones, valor_en_libros

def valor_presente(depreciaciones, tasa):
    return sum(d / ((1 + tasa) ** (i + 1)) for i, d in enumerate(depreciaciones))

st.set_page_config(
    page_title="Depreciación_INE", # Título que aparecerá en la pestaña del navegador
    page_icon="📉", # Puedes usar un emoji como icono...
    # page_icon="https://www.streamlit.io/images/brand/streamlit-logo-light.svg", # ...o la URL de una imagen
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Comparación de Alternativas de Depreciación")
                                                                                                                                                                                                                                                    
st.subheader("Datos para Alternativas")
col1, col2 = st.columns(2)

with col1:
    costo1 = st.number_input("Costo Inicial A1", value=10000.0)
    residual1 = st.number_input("Valor Residual A1", value=1000.0)
    vida1 = st.number_input("Vida Útil A1 (años)", value=5, step=1)
    metodo1 = st.selectbox("Método A1", ["Línea Recta", "Saldo Decreciente"])

with col2:
    costo2 = st.number_input("Costo Inicial A2", value=10000.0)
    residual2 = st.number_input("Valor Residual A2", value=1000.0)
    vida2 = st.number_input("Vida Útil A2 (años)", value=5, step=1)
    metodo2 = st.selectbox("Método A2", ["Línea Recta", "Saldo Decreciente"])

tasa = st.slider("Tasa de Descuento (%)", min_value=0.0, max_value=30.0, value=10.0) / 100

if st.button("Comparar Alternativas"):
    # Cálculo A1
    if metodo1 == "Línea Recta":
        dep1, libros1 = linea_recta(costo1, residual1, int(vida1))
    else:
        dep1, libros1 = saldo_decreciente(costo1, int(vida1))

    # Cálculo A2
    if metodo2 == "Línea Recta":
        dep2, libros2 = linea_recta(costo2, residual2, int(vida2))
    else:
        dep2, libros2 = saldo_decreciente(costo2, int(vida2))

    # VPN
    vpn1 = valor_presente(dep1, tasa)
    vpn2 = valor_presente(dep2, tasa)

    # Tabla comparativa
    max_vida = max(len(dep1), len(dep2))
    df_comp = pd.DataFrame({
        "Año": list(range(1, max_vida + 1)),
        "Depreciación A1": dep1 + [None] * (max_vida - len(dep1)),
        "Valor en libros A1": libros1 + [None] * (max_vida - len(libros1)),
        "Depreciación A2": dep2 + [None] * (max_vida - len(dep2)),
        "Valor en libros A2": libros2 + [None] * (max_vida - len(libros2)),
    })

    st.dataframe(df_comp)

    # Gráfica
    fig, ax = plt.subplots()
    ax.plot(df_comp["Año"], df_comp["Valor en libros A1"], label="A1", marker='o')
    ax.plot(df_comp["Año"], df_comp["Valor en libros A2"], label="A2", marker='x')
    ax.set_title("Valor en Libros Comparativo")
    ax.set_xlabel("Año")
    ax.set_ylabel("Valor en libros ($)")
    ax.legend()
    st.pyplot(fig)

    # Resumen
    resumen = pd.DataFrame({
        "Método": [metodo1, metodo2],
        "Total Depreciado": [sum(dep1), sum(dep2)],
        "Valor Presente Neto": [vpn1, vpn2],
    })

    st.write("**Resumen Financiero**")
    st.dataframe(resumen)

    # Exportar
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_comp.to_excel(writer, index=False, sheet_name='Comparacion')
        resumen.to_excel(writer, index=False, sheet_name='Resumen')
    st.download_button(
        label="Descargar comparación en Excel",
        data=output.getvalue(),
        file_name="comparacion_depreciacion.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
