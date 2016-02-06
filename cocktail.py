import re
import http.client
import html

def cocktail(args):
    conn = http.client.HTTPConnection("www.cocktaildb.com")

    conn.request("GET", "/?_action_randomRecipe=1")
    resp = conn.getresponse()
    data = html.unescape(resp.read().decode('utf-8'))

    rid = re.search('<a href="recipe_detail\?id=([0-9]+)">', data)

    conn.request("GET", "/recipe_detail?id=" + rid.group(1))
    resp = conn.getresponse()
    data = html.unescape(resp.read().decode('utf-8'))

    out = ''

    name = re.search('<h2>(.*)</h2>', data).group(1)
    out += name + '\n\n'

    directions = re.findall('<div class="recipeDirection">(.*)</div>', data)
    direction = re.sub('<a .*?>', '', directions[0])
    direction = direction.replace('</a>', '')
    out += direction + '\n\n'

    measures = re.findall(
        '<div class="recipeMeasure">(.*?)'
        '<a href="ingr_detail\?id=[0-9]+">(.*?)</a>', data)
    for measure in measures:
        out += measure[0] + measure[1] + '\n'

    for direction in directions[1:]:
        direction = re.sub('<a .*?>', '', direction)
        direction = direction.replace('</a>', '')
        out += '\n' + direction

    return out
