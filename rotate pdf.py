import pikepdf

old_pdf=pikepdf.Pdf.open('portfolio.pdf')

#to check how many pages are in this pdf
print(old_pdf.pages)


#loop - to rotate each page one by one -by given degree no.
for i in old_pdf.pages:
    i.rotate(180,relative=True)
    old_pdf.save('Rotate_pdf.pdf')


#Rotate is a func not property - can only rotate-90,180,270
