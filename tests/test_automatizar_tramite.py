import os
from src.automatizar_tramite import generar_texto_solicitud, generar_pdf


def test_generar_texto_solicitud_contiene_datos():
    texto = generar_texto_solicitud(
        nombre="Juan Pérez",
        cedula="0955555555",
        correo="juan@email.com",
        tipo_tramite="Solicitud de certificado",
        motivo="Necesito el certificado para un proceso académico.",
        fecha="05/07/2026"
    )

    assert "Juan Pérez" in texto
    assert "0955555555" in texto
    assert "juan@email.com" in texto
    assert "Solicitud de certificado" in texto
    assert "Necesito el certificado" in texto
    assert "05/07/2026" in texto


def test_generar_texto_solicitud_no_esta_vacio():
    texto = generar_texto_solicitud(
        nombre="María López",
        cedula="0911111111",
        correo="maria@email.com",
        tipo_tramite="Actualización de datos",
        motivo="Cambio de correo electrónico..",
        fecha="05/07/2026"
    )

    assert texto.strip() != ""


def test_generar_pdf_crea_archivo(tmp_path):
    archivo_pdf = tmp_path / "solicitud_test.pdf"

    resultado = generar_pdf(
        nombre="Carlos Vera",
        cedula="0922222222",
        correo="carlos@email.com",
        tipo_tramite="Solicitud de permiso",
        motivo="Permiso por motivos personales.",
        nombre_archivo=str(archivo_pdf)
    )

    assert os.path.exists(resultado)
    assert resultado.endswith(".pdf")