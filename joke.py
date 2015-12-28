def cyberjoke():
    conn = http.client.HTTPConnection("www.allowe.com")
    conn.request("GET", "/humor/cj-main/cyberjoke-archive.html?option=com_jokes&view=search&search=ffunny&funny=1")

    r1 = conn.getresponse()
    data1 = r1.read().decode('utf-8')
    m = re.search('([0-9]+)', data1)

    conn.request("GET", "/humor/cj-main/cyberjoke-archive.html?option=com_jokes&view=joke&id=" + str(m.group(0)))
    r1 = conn.getresponse()
    data1 = r1.read().decode('utf-8')

    m = re.search('</b></p><p>(.*)</p><div class="ratingblock">', data1)

    return m.group(1)
