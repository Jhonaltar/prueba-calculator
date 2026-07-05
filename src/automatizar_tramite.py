from fpdf import FPDF
from datetime import date


def generar_texto_solicitud(nombre, cedula, correo, tipo_tramite, motivo, fecha=None):
    if fecha is None:
        fecha = date.today().strftime("%d/%m/%Y")

    texto = f"""
Fecha: {fecha}

Señores:
Departamento Administrativo

De mi consideración:

Yo, {nombre}, con cédula de identidad No. {cedula}, solicito cordialmente la atención del siguiente trámite:

Tipo de trámite: {tipo_tramite}

Motivo de la solicitud:
{motivo}

Para cualquier comunicación adicional, dejo registrado mi correo electrónico:
{correo}

Agradezco de antemano la atención brindada a la presente solicitud.

Atentamente,

{nombre}
C.I. {cedula}
"""
    return texto


def generar_pdf(nombre, cedula, correo, tipo_tramite, motivo, nombre_archivo=None):
    if nombre_archivo is None:
        nombre_archivo = f"solicitud_{cedula}.pdf"

    texto = generar_texto_solicitud(
        nombre,
        cedula,
        correo,
        tipo_tramite,
        motivo
    )

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "SOLICITUD DE TRÁMITE", ln=True, align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, texto)
    pdf.output(nombre_archivo)

    return nombre_archivo


if __name__ == "__main__":
    nombre = input("Ingrese el nombre del solicitante: ")
    cedula = input("Ingrese la cédula: ")
    correo = input("Ingrese el correo: ")
    tipo_tramite = input("Ingrese el tipo de trámite: ")
    motivo = input("Ingrese el motivo de la solicitud: ")

    archivo = generar_pdf(nombre, cedula, correo, tipo_tramite, motivo)

    print(f"Trámite generado correctamente: {archivo}")