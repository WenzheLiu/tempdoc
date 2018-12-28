from docx import Document

doc = Document('temp.docx')
for p in doc.paragraphs:
    txt = p.text
    if 'WK' in txt and 'DAY' in txt:
        p.text = txt.replace('WK', '2').replace('DAY', '3').replace('YYYY', '2018').replace('MM', '4').replace('DD', '5')
doc.save('week1.docx')
