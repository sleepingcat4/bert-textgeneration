import xml.etree.ElementTree as ET

# Open the TMX file
tree = ET.parse('output_polskapomoc-gov-pl_eng-pol_eng-pol.tmx')
root = tree.getroot()

# Extract the Polish and English text from the TMX file
polish_text = []
english_text = []
for tu in root.iter('tu'):
    for tuv in tu.iter('tuv'):
        lang = tuv.attrib.get('{http://www.w3.org/XML/1998/namespace}lang')
        if lang == 'pl':
            for seg in tuv.iter('seg'):
                polish_text.append(seg.text.strip())
        elif lang == 'en':
            for seg in tuv.iter('seg'):
                english_text.append(seg.text.strip())

# Write the Polish and English text to a plain text file in a dataset format
with open('dataset.txt', 'w', encoding='utf-8') as file:
    for i in range(len(polish_text)):
        file.write(english_text[i] + '\t' + '\n')
        file.write(polish_text[i] + '\t' + '\n')
        
"""    for i in range(len(polish_text)):
        file.write(polish_text[i] + '\t' + 'polish\n')
        file.write(english_text[i] + '\t' + 'english\n')
"""