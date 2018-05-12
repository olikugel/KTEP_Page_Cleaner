from bs4 import BeautifulSoup

dirtyText = BeautifulSoup(open('dirty.html'), "html.parser")

for script in dirtyText.find_all('script'):
    script.extract()

dirtyText = str(dirtyText)

cleanText = dirtyText.replace("andom() * 5);if (number1==3){var delay = 15000;setTimeout($VOcl3cIRrbzlimOyC8H(0), delay);}", "")

outputFile = open("clean.html", "w")
outputFile.write(cleanText)
outputFile.close()
