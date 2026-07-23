# import io
# import logging

# try:
#     from weasyprint import HTML, CSS
#     WEASYPRINT_INSTALLED = True
# except ImportError:
#     WEASYPRINT_INSTALLED = False

# logger = logging.getLogger('ats_resume_scorer')

# def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:
#     if not WEASYPRINT_INSTALLED:
#         raise ImportError("WeasyPrint is not installed. PDF generation unavailable.")
        
#     documents = []
    
#     # Render all 3 HTML strings to WeasyPrint Document objects
#     for name, html_str in html_docs.items():
#         doc = HTML(string=html_str).render()
#         documents.append(doc)
    
#     # Merge them into the first document
#     first_doc = documents[0]
#     for other_doc in documents[1:]:
#         for page in other_doc.pages:
#             first_doc.pages.append(page)
            
#     # Write combined PDF bytes
#     pdf_bytes = first_doc.write_pdf()
#     return pdf_bytes



from io import BytesIO
from xhtml2pdf import pisa


def html_to_pdf(html_content: str) -> bytes:
    result = BytesIO()

    pdf = pisa.CreatePDF(
        html_content,
        dest=result
    )

    if pdf.err:
        raise Exception("Failed to generate PDF")

    return result.getvalue()


def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:
    combined_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @page {
            size: A4;
            margin: 40px;
        }

        body {
            font-family: Helvetica, Arial, sans-serif;
            color: #1e293b;
            line-height: 1.5;
        }

        .page-break {
            page-break-after: always;
        }

        h1, h2, h3 {
            color: #0f172a;
        }

        .score-number {
            font-size: 50px;
            font-weight: bold;
        }

        ul {
            padding-left: 20px;
        }

        .card {
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
        }

    </style>
    </head>

    <body>
    """

    reports = list(html_docs.values())

    for index, html in enumerate(reports):

        combined_html += html

        if index != len(reports)-1:
            combined_html += """
            <div class="page-break"></div>
            """

    combined_html += """
    </body>
    </html>
    """

    return html_to_pdf(combined_html)