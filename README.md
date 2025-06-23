# 📉 Depreciación_INE - Comparación de Métodos de Depreciación

Este proyecto es una aplicación interactiva desarrollada con **Python** y **Streamlit** que permite comparar dos métodos de depreciación contable (Línea Recta y Saldo Decreciente), calculando la depreciación anual, el valor en libros y el valor presente neto (VPN) de cada alternativa.

## 🧠 Características

- Comparación lado a lado de dos activos con diferentes métodos de depreciación.
- Cálculo del VPN de las depreciaciones con una tasa de descuento configurable.
- Visualización de datos en tablas y gráficos.
- Descarga en Excel de la comparación realizada.

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/depreciacion_ine.git
cd depreciacion_ine
```

### 2. Crear entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # En Linux/macOS
.venv\Scripts\activate    # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
streamlit run app.py
```

Una vez ejecutado, se abrirá automáticamente en tu navegador predeterminado:  
📍 `http://localhost:8501`

---

## 🛠 Estructura del Proyecto

```
depreciacion_ine/
├── app.py                  # Código principal de la aplicación
├── requirements.txt        # Lista de dependencias
└── README.md               # Este archivo
```

---

## 📦 Dependencias

- Python 3.8 o superior
- Streamlit
- Pandas
- Matplotlib
- XlsxWriter

> Todas las dependencias se instalan automáticamente desde `requirements.txt`.

---

## 📥 Exportación a Excel

La aplicación genera un archivo `.xlsx` descargable que incluye:

- Hoja `Comparacion`: Depreciaciones y valores en libros año a año.
- Hoja `Resumen`: Total depreciado y VPN de cada alternativa.

Esto facilita el análisis financiero y la toma de decisiones contables.

---

## 📸 Capturas del proyecto

Capturas del proyecto y su visualización del interfaz:

```markdown
![image](https://github.com/user-attachments/assets/f0fcd8c2-a496-4994-b14d-e2e0006c9117)

![image](https://github.com/user-attachments/assets/30043a41-eac0-4f40-a29f-c452352bd3c9)

![image](https://github.com/user-attachments/assets/a2ab2460-a5f7-4c19-8eaa-261a3068e9b9)

![image](https://github.com/user-attachments/assets/57be554b-6327-4f8b-b4de-74177b675b61)


```

---

## 💡 Autor

**Leonel Antonio Hernández Pérez**   | HP12002


---

