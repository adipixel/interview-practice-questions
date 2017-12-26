def createHTMLList(listOfStrings):
  html = "<ul>"
  for x in listOfStrings:
    html += "<li>" + x + "</li>"
  html += "</ul>"
  return html

def main():
  listOfStrings = ["Bread", "Milk", "Cereals", "Honey", "Coffee"]
  print createHTMLList(listOfStrings)

main()
