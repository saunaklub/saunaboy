import re
import http.client
import html

def rezeptChefkoch(args):
    conn = http.client.HTTPConnection("www.chefkoch.de")
    conn.request("GET", "/napping/js/script.js")

    r1 = conn.getresponse()
    data = html.unescape(r1.read().decode('utf-8'))

    out = ''

    rezept = re.search('<div id="ck-rezeptname">(.*)</div>', data)
    out += 'Rezept-Tipp des Tages: *' + rezept.group(1) + '*\n\n'

    zutaten = re.search('<div id="ck-zutaten">(.*)</div>', data).group(1)
    zutaten = zutaten.replace('<br>', '\n')
    out += zutaten + '\n'

    zubereitung = re.search('<div id="ck-zubereitung">(.*)</div>', data).group(1)
    zubereitung = zubereitung.replace('<br>', '\n')
    zubereitung = zubereitung.replace('<strong>Zubereitung:</strong>\n', '')
    zubereitung = zubereitung.replace('\\\'', '\'')
    out += zubereitung

    return out
