from fpdf import FPDF, HTMLMixin
from flask import Flask,request
import urllib
import psycopg2
import random
import json

def generatepdf(request):
            
    class HTML2PDF(FPDF, HTMLMixin):
        pass

        
    pdf = HTML2PDF()
    '''
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Hello_priya", border=0)
    pdf.output('test_priya1.pdf', 'F')
    '''
    name="Aravindh"
    hotel_name = "Hilton Hotel"
    address = "No:5, First cross street,Chennai-600 001."
    mobile_no = "9677577914"
    email = "abcd96@gmail.com"
    arrival = "2019-05-10"
    departure ="2019-05-15"
    room_type = "Standard Room"
    conf_no = "8974561234"

    pdf.add_page()
    pdf.set_font("Arial",'B', size=16)
    pdf.cell(200, 10, txt="Booking Confirmation", ln=1, align="C")
    pdf.ln(10)
    pdf.set_font('Arial','B',size=14)
    pdf.cell(10)
    pdf.cell(0, 5,"%s," %hotel_name, ln=1, align="L")

    pdf.set_font('Arial',size=12)
    pdf.cell(10)
    pdf.cell(0, 5, '%s'%address, ln=1, align="L")
    pdf.cell(10)
    pdf.cell(0, 5, '%s'%mobile_no, ln=1, align="L")
    pdf.cell(10)
    pdf.cell(0, 5, '%s'%email, ln=1, align="L")
    pdf.cell(10)
    pdf.cell(200, 10, txt="Dear %s, " %name, ln=1, align="J")
    pdf.cell(10)
    pdf.output('8220772736.pdf','D')

    return json.dumps({"Return":"sucess"})


