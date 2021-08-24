import webbrowser    # Module that allows us to open pages in the browser
import xlrd    # Module that allows us to work with XLSX files (version 1.2.0)

urls = []    # Array where urls are stored
excel = False    # Indicates if we are working with a TXT or XLSX file

if excel == True:
    # ===== EXCEL =====                                      
    filePath = "C:\\wamp64\\www\\urls\\urls.xlsx"    # Get the urls from the corresponding XLSX file
    sheet = xlrd.open_workbook(filePath)
    hoja = sheet.sheet_by_name("Hoja1")
    for i in range(0, hoja.nrows):
        urls.append(hoja.cell_value(i,0))
else:
    # ===== TXT =====                                               
    with open("urls.txt") as fichero:    # Get the urls from the corresponding TXT file
                    for linea in fichero:
                        linea = linea.strip("\n")
                        urls.append(linea)

for url in urls:
    webbrowser.open_new(url)    # Open a new page for each url contained in the defined array
