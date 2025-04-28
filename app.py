# app.py
import streamlit as st
from fpdf import FPDF
import io

# Configuración de la página
st.set_page_config(
    page_title="Inscripción Curso Excel",
    page_icon="📊",
    layout="centered"
)

# Tema oscuro con CSS personalizado
st.markdown(
    """
    <style>
    .css-18e3th9 { background-color: #1e1e1e; color: #fafafa; }
    .css-1d391kg { background-color: #1e1e1e; }
    .stTextInput input, .stNumberInput input {
        background-color: #333; color: #fafafa;
    }
    .stButton>button, .stDownloadButton>button {
        background-color: #0e639c; color: #fafafa; border: none;
    }
    .stCheckbox>div>input { accent-color: #0e639c; }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la app
st.title("📊 Inscripción - Curso Intensivo de Excel")

# Captura de datos del usuario
name = st.text_input("Nombre completo")
age = st.number_input("Edad", min_value=1, max_value=100, step=1)
accepted = st.checkbox("Acepto compartir mis datos con Santander Academy")

# Mostrar detalles del curso
st.subheader("Datos del curso")
st.markdown("""
- **Fechas:** 5 al 8 de mayo  
- **Horario:** 1:00 p.m. a 2:00 p.m.  
- **Modalidad:** Online (Excel Online)  
- **Duración:** Curso intensivo (4 días)  
- **Certificado:** con número de serie oficial  
- **Costo:** $500 MXN  
""")

# Mostrar datos de pago
st.subheader("Datos de pago")
st.markdown("""
**ALEXANDER EDUARDO ROJAS**  
CLABE: `138580000011747469`  
Banco: **Ualá**  
Teléfono: `7225597963`
""")

# Generar y descargar el PDF
if st.button("Generar comprobante PDF"):
    if not name:
        st.error("Por favor ingresa tu nombre.")
    elif not accepted:
        st.error("Debes aceptar compartir tus datos para continuar.")
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Comprobante de Inscripción", ln=True, align="C")
        pdf.ln(5)

        pdf.set_font("Arial", size=12)
        pdf.cell(0, 8, f"Nombre: {name}", ln=True)
        pdf.cell(0, 8, f"Edad: {int(age)}", ln=True)
        pdf.cell(0, 8, "Acepta compartir datos con Santander Academy: Sí", ln=True)
        pdf.ln(5)

        pdf.cell(0, 8, "Datos del curso:", ln=True)
        for line in [
            " - Fechas: 5 al 8 de mayo",
            " - Horario: 1:00 p.m. a 2:00 p.m.",
            " - Modalidad: Online (Excel Online)",
            " - Certificado: número de serie oficial",
            " - Costo: $500 MXN"
        ]:
            pdf.cell(0, 8, line, ln=True)
        pdf.ln(5)

        pdf.cell(0, 8, "Datos de pago:", ln=True)
        pdf.multi_cell(0, 8,
            "ALEXANDER EDUARDO ROJAS\n"
            "CLABE: 138580000011747469\n"
            "Banco: Ualá\n"
            "Teléfono: 7225597963"
        )

        # Preparar buffer para descarga
        pdf_buffer = io.BytesIO()
        pdf.output(pdf_buffer)
        pdf_buffer.seek(0)

        st.download_button(
            label="📥 Descargar comprobante (PDF)",
            data=pdf_buffer,
            file_name="comprobante_inscripcion.pdf",
            mime="application/pdf"
        )
