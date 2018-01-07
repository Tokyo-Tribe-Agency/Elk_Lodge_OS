from django.contrib import admin
from lodge.models.models import *
import reportlab
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, Spacer
from django.core.files.storage import FileSystemStorage

admin.site.register(Photos)
admin.site.register(Elks)
admin.site.register(Events)
admin.site.register(Newsletter)
admin.site.register(Inquiry)


class Test(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.width, self.height = letter
        self.styles = getSampleStyleSheet()
 
    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y
 
    #----------------------------------------------------------------------
    def run(self, queryset):
        """
        Run the report
        """

        self.doc = SimpleDocTemplate("/tmp/test.pdf")
        self.story = [Spacer(1, 2.5*inch)]
        self.createLineItems(queryset)
 
        self.doc.build(self.story, onFirstPage=self.createDocument)
        print("finished!")
 
    #----------------------------------------------------------------------
    def createDocument(self, canvas, response):
        """
        Create the document
        """
        self.c = canvas

        normal = self.styles["Normal"]
 
        header_text = "<b>Elk Lodge Donation</b>"
        p = Paragraph(header_text, normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(100, 12, mm))
 
        ptext = """This is the output of the Donations made to the Elk Lodge"""
 
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width-50, self.height)
        p.drawOn(self.c, 30, 700)
 
        
 
    #----------------------------------------------------------------------
    def createLineItems(self, queryset):

        """
        Create the line items
        """
        text_data = ["Line","Transaction Id", "Payment Type", "Donation Amount",
                     "Donation Date", "Cardholder Name"]
        d = []
        font_size = 8
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in text_data:
            ptext = "<font size=%s><b>%s</b></font>" % (font_size, text)
            p = Paragraph(ptext, centered)
            d.append(p)
 
        data = [d]
 
        line_num = 1
 
        formatted_line_data = []
 		
        for x in queryset:
            line_data = [str(line_num), str(x.donation_id), str(x.donation_type), 
                         str(x.donation_amount), str(x.donation_date), str(x.donation_cardholder_name)]
 
            for item in line_data:
                ptext = "<font size=%s>%s</font>" % (font_size-1, item)
                p = Paragraph(ptext, centered)
                formatted_line_data.append(p)
            data.append(formatted_line_data)
            formatted_line_data = []
            line_num += 1
 
        table = Table(data, colWidths=[60, 80, 80, 80, 100, 100, 90])
 
        self.story.append(table)



def export_pdf(modeladmin, response, queryset):
	
	queryset = queryset
	
	doc = Test()
	doc.run(queryset)
	
	fs = FileSystemStorage("/tmp")
	with fs.open("test.pdf") as pdf:
	    response = HttpResponse(pdf, content_type='application/pdf')
	    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
	    return response

	return response

	

class  donationsAdmin(admin.ModelAdmin):
	actions = [export_pdf]


admin.site.register(Donations, donationsAdmin)
