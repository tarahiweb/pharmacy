from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import Image
from .models import Refill, Drug
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date


pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))






def Create_report(pk):
    refill= Refill.objects.get(pk = pk )
    drug = Drug.objects.filter(med=refill)
    full_name= refill.info.user.first_name + ' ' + refill.info.user.last_name
    pdf_file_name = 'Refill order'
    c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
    #brand
    brand= 'refill/picture/4f3bce418e3c434ca407cec8b348d9da.png'
    c.drawImage(brand, 50, 500, width=50, height=50)
    #header
    c.setFont('Vera', 20, leading=None)
    c.drawCentredString(415, 500, "Refill order")
    c.drawString(50, 450, full_name + '  costumer email: ' + refill.info.user.email)
    #c.drawString(50, 400, date(refill.created))
    c.drawString(50, 350, "Ordered Drugs")
    t = 300
    for i in drug:
        t -= 20
        c.drawString(50, t, i.drug_name+ i.drug_dose)
    c.drawCentredString(415, 250, "patients Info")
    c.drawString(50, 220, refill.Dr_name +  ' ' +str(refill.Dr_Phone_number) + ' ' + refill.Dr_adrress)
    c.drawString(50, 200, refill.last_pharmacy + refill.last_pharmacy_adrress)
    c.drawString(50, 150, "patients Address" + ' ' + refill.info.address + ' ' + refill.info.zip + ' ' + refill.info.city)
    #c.drawImage(refill.prescription, 400, 200, width=100, height=100)

    c.showPage()
    c.save()
