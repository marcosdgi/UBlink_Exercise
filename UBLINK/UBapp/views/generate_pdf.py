import json
from django.shortcuts import render
from UBapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONOpenAPIRenderer
from reportlab.pdfgen import canvas







from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

""" class GenerarPDFAPIView(APIView):
    def get(self, request):
        # Obtener los datos de las vistas
        response1 = requests.get('http://127.0.0.1:8000/subtotal')
        response2 = requests.get('http://url_de_la_segunda_vista')

        data1 = response1.json()
        data2 = response2.json()

        # Generar el PDF
        pdf_data = self.generar_pdf(data1, data2)

        # Devolver el PDF como respuesta
        response = Response(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="tabla.pdf"'
        return response """

"""     def generar_pdf(self, data1, data2):
        # Crear el documento PDF
        doc = SimpleDocTemplate("tabla.pdf", pagesize=letter)

        # Crear la tabla con los datos
        tabla_data = [list(data1[0].keys())] + [list(item.values()) for item in data1] + [list(data2[0].keys())] + [list(item.values()) for item in data2]
        tabla = Table(tabla_data)

        # Estilo de la tabla
        estilo_tabla = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        tabla.setStyle(estilo_tabla)

        # Crear el contenido del PDF y agregar la tabla
        contenido = []
        contenido.append(tabla)

        # Construir el PDF
        buffer = BytesIO()
        doc.build(contenido, onFirstPage=self.header_footer, onLaterPages=self.header_footer, canvasmaker=NumberedCanvas)
        pdf_data = buffer.getvalue()
        buffer.close()

        return pdf_data

    def header_footer(self, canvas, doc):
        # Agregar encabezado y pie de página al PDF
        # Puedes personalizar el encabezado y pie de página según tus necesidades
        pass

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, num_pages):
        self.setFont("Helvetica", 9)
        self.drawRightString(200 * mm, 20 * mm,
                             "Page %d of %d" % (self._pageNumber, num_pages))
 """