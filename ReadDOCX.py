import xml.etree.ElementTree as ET
import docx

"""
The first function saveXMLfile takes two arguments, a filename and a string containing XML text, 
and writes the XML string to a file with the specified name using UTF-8 encoding.
"""


def saveXMLfile(filename, xmlText):
    # Write the XML string to a file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(xmlText)
        return True

"""
The second function textFromOutputTableConversion takes a string as input and returns a list of dictionaries 
representing pairs of text and dates extracted from the input string. It does this by splitting the input string 
using a regular expression to find dates of the form dd/mm/yy, and then using the resulting date matches to split 
the input string into pairs of text and dates. It then extracts the first three characters of the text and assigns 
them to the 'Type' key of the dictionary, and assigns the remainder of the text to the 'Description' key of the dictionary.
"""
def textFromOutputTableConversion(text):
    text = text.strip()

    dates = []
    x = 1
    tem = ""
    for i in text:
        if x == 0 and ('”' == i or '“' == i):
            tem += i
            dates.append(tem)
            tem = ""
            x = 1
        elif ('”' == i or '“' == i):
            tem += i
            x = 0
        elif x == 0:
            tem += i

    split_text = [text]

    for delimiter in dates:
        new_words = []
        for word in split_text:
            new_words.extend(word.split(delimiter))
        split_text = new_words

    result = []
    # Append the text and date pairs to the result list
    for i, match in enumerate(dates):
        result.append({'Date': match[1:-1], 'Type': split_text[i + 1][:3].strip(), 'Description': split_text[i + 1][3:].strip()})
    else:
        result.append({'Date': "", 'Type': "", 'Description': ""})

    return result

"""
The third function textFromBudgetTableConversion takes a string as input and returns a list of dictionaries 
representing pairs of descriptions and amounts extracted from the input string. It does this by splitting the 
input string using a regular expression to find dates of the form yyyy/mm, and then using the resulting date 
matches to split the input string into pairs of descriptions and amounts. It then extracts the first word of 
the second element in the split text list and assigns it to the 'Description' key of the dictionary, and 
assigns the second word to the 'Amount' key of the dictionary.
"""

def textFromBudgetTableConversion(text):
    text = text.strip()

    try:
        dates = []
        x = 1
        tem = ""
        for i in text:
            if x == 0 and ('”' == i or '“' == i):
                tem += i
                dates.append(tem)
                tem = ""
                x = 1
            elif ('”' == i or '“' == i):
                tem += i
                x = 0
            elif x == 0:
                tem += i

        split_text = [text]

        for delimiter in dates:
            new_words = []
            for word in split_text:
                new_words.extend(word.split(delimiter))
            split_text = new_words

        split_text.insert(1, "".join(split_text[1].split(maxsplit=2)[0:2]))
        split_text.insert(3, "".join(split_text[3].split(maxsplit=2)[0:2]))


        split_text[2] = split_text[2].split(maxsplit=2)[2]
        split_text[4] = split_text[4].split(maxsplit=2)[2]

        result = []
        # Append the text and date pairs to the result list
        j = 0
        k = 1
        for i, match in enumerate(dates):
            result.append({'Date': match[1:-1].strip(), 'Description': split_text[j].strip(), 'Amount': split_text[k].strip()})
            j += 2
            k += 2
        else:
            result.append({'Date': "", 'Description': "", 'Amount': ""})
    except:
        result = [{'Date': "", 'Description': "", 'Amount': ""}]

    return result

"""
The fourth function ReadingXMLFileToText takes a filename as input, parses the XML file using ElementTree 
and extracts all text content within <w:t> tags in the document. It returns a list of strings, 
each representing the text content of a <w:t> tag.
"""
def ReadingXMLFileToText(filename):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Find all <w:t> tags in the document
    w_t_tags = root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')

    # Extract the text content of each <w:t> tag
    text = [w_t.text for w_t in w_t_tags]

    return text

"""
The fifth function RemoveTextTill takes two arguments, a list of strings text and a string x, and 
removes all elements of the text list up to (but not including) the first occurrence of x.
"""
def RemoveTextTill(text,x):
    new = []
    for i in range(text.index(x)):
        new.append(text[i])

    for i in new:
        text.remove(i)

    return text


"""
The sixth function CleanText takes a list of strings text as input and performs a series of 
cleaning operations on it. It removes all occurrences of a single space character, then strips 
leading and trailing whitespace from each element of the list and joins them into a single string. 
It replaces several headers and question prompts in the text with a string '$-' to help later parsing. 
Finally, it replaces some additional text strings with a format that begins with the string ']:', 
followed by the original string, followed by ']:'. This format will be used later in the ExtractData 
function to extract data.
"""
def removeFromList(lst,to_remove):
    for item in lst:
        if item == to_remove:
            lst.remove(item)

def getText(text):
    dictionary = {}

    toRemoves = []
    x = 1
    tem = ""
    for i in text:
        if x == 0 and "~" == i:
            toRemoves.append(tem)
            tem = ""
            x = 1
        elif "~" == i:
            x = 0
        elif x == 0:
            tem += i

    for i in toRemoves:
        text = text.replace("~"+i+"~","")

    headers = []
    x = 1
    tem = ""
    for i in text:
        if x == 0 and "^" == i:
            headers.append(tem)
            tem = ""
            x = 1
        elif "^" == i:
            x = 0
        elif x == 0:
            tem+=i

    headers = [i.strip() for i in headers]
    text = text.split("^")
    text = [i.strip() for i in text]
    removeFromList(text,"")

    k = 0
    for i in range(len(text)):
        if text[i] == headers[k]:
            dictionary[headers[k]] = ""

            try:
                if text[i+1] != headers[k+1]:
                    dictionary[headers[k]] = text[i+1]
            except:
                try:
                    dictionary[headers[k]] = text[i + 1]
                except:
                    pass

            k = (k+1)%len(headers)

    return dictionary

def CleanText(text):
    removeFromList(text," ")

    text = [x.strip() for x in text]
    text = " ".join(text)
    text = text.split("|")
    removeFromList(text,"")

    headers = []
    dictionary = {}
    for i,x in enumerate(text):
        if i%2==0:
            try:
                headers.append(x)
                dictionary[x] = text[i+1]
            except:
                dictionary[x] = ""

    dictionary["INTERNATIONAL COLLABORATION"] = dictionary.pop(headers[1])
    dictionary["ADDITIONAL INFORMATION"] = dictionary.pop(headers[-1])

    headers[1]  = "INTERNATIONAL COLLABORATION"
    headers[-1] = "ADDITIONAL INFORMATION"

    dict = {}
    for i,x in enumerate(headers):
        if i != len(headers)-1:
            dict[headers[i]] = getText(dictionary[headers[i]])

    dict[headers[-1]] = dictionary[headers[-1]]

    dict[headers[-3]][list(dict[headers[-3]].keys())[0]] = textFromOutputTableConversion(dict[headers[-3]][list(dict[headers[-3]].keys())[0]])
    dict[headers[-2]][list(dict[headers[-2]].keys())[0]] = textFromBudgetTableConversion(dict[headers[-2]][list(dict[headers[-2]].keys())[0]])


    return dict

"""
The seventh function ExtractData takes a filename as input and returns a dictionary containing data extracted 
from the input Word document. It first opens the document using the docx library and converts it to an XML 
string using the _element attribute. It then saves the XML string to a file with the same name as the input 
file but with a .xml extension. It extracts the text content of the XML file using ReadingXMLFileToText, 
removes all text before the header "LEAD ACADEMIC" using RemoveTextTill, and cleans the remaining text using 
CleanText. It then splits the cleaned text into sections using the string "$-" as a delimiter, and creates a 
dictionary with keys corresponding to the section headers and values corresponding to dictionaries of key-value 
pairs extracted from the section content. For the 'OUTPUTS' section, it passes the 'Planned Date 3* / VA /RF / O 
Description' value through textFromOutputTableConversion before adding it to the dictionary. For the 'BUDGET' 
section, it passes the 'Funds requested and how to be spent Spending profile' value through 
textFromBudgetTableConversion
"""
def ExtractData(filename,type):
    filename = str(filename)
    doc = docx.Document(filename)
    xml_str = doc._element.xml
    saveXMLfile(filename.replace(".docx",".xml"),xml_str)
    text = ReadingXMLFileToText(filename.replace(".docx",".xml"))
    print(text)
    text = [i.strip() for i in text]
    text = RemoveTextTill(text,"|")

    text = CleanText(text)
    print(text)
    return text

