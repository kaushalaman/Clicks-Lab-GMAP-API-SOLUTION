# Name: Aman Kaushal
# Contact No: +918989673137
# email: kaushalaman02@gmail.com
# IIIT, Gwalior, India

import csv
   
 # Open the CSV file for reading
reader = csv.reader(open('response.csv'))
  
# Create the HTML file for output
htmlfile = open('result.html',"w")
htmlfile.write('<h1>')
htmlfile.write('<center>')
htmlfile.write('Name: AMAN KAUSHAL')
htmlfile.write("</br>")
htmlfile.write('IIIT Gwalior')
htmlfile.write('</center>')
htmlfile.write('</h1>')
htmlfile.write("</br>")
htmlfile.write("</br>")
htmlfile.write('<center>')
htmlfile.write('<h2>')
htmlfile.write("Mechanism for Engangement faulty")
htmlfile.write('</h2>')
htmlfile.write('</center>')
htmlfile.write("</br>")
htmlfile.write("<h3>")
htmlfile.write(" Note: If difference of Actual Data and Google Data for distance is greater then 2 km and if difference of Actual Data and Google Data for time is greater then 10 min then Faulty will set to 'YES' otherwise 'NO'" )
htmlfile.write("</h3>")
htmlfile.write('</br>')
htmlfile.write('</br>')
 
# initialize rownum variable
rownum = 0
  
 # write <table> tag
htmlfile.write('<center>')
htmlfile.write('<table>')
   
# generate table contents
for row in reader: # Read a single row from the CSV file
  
    # write header row. assumes first row in csv contains header
    if rownum == 0:
        htmlfile.write('<tr>') # write <tr> tag
        for column in row:
            htmlfile.write('<th>' + column + '</th>')
        htmlfile.write('</tr>')
   
      #write all other rows  
    else:
        htmlfile.write('<tr>')   
        for column in row:
            htmlfile.write('<td>' + column + '</td>')
        htmlfile.write('</tr>')
       
     #increment row count   
    rownum += 1
   
  # write </table> tag
htmlfile.write('</table>')
htmlfile.write('</center>')
   
  # print results to shell
print "Created " + str(rownum) + " row table."
exit(0)