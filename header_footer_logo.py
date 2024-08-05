from fpdf import FPDF
 
# inheriting form the class
class PDF(FPDF):
    
    def header(self):              #we are custormising the header and footer methods of the FPDP class hence, we are inherting the same
        
        self.image("logo.png", 10, 8, 33)
      
        self.set_font("helvetica", "B", 15)
        
        self.cell(80)                        #empty cell betwee nthe header and the logo so,there could be the horizontal space between the haeder and the logo
       
        self.cell(30, 10, "Welcome", border=1, align="C")
       
        self.ln(40)               #line break means after how much space the lins will start to print
 
    def footer(self):
        
        self.set_y(-15)   #-15 because 15 from bottom
      
        self.set_font("helvetica", "I", 8)
       
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
 
 
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
 
 
for i in range(1, 41):
    pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
pdf.output("new-tuto2.pdf")
