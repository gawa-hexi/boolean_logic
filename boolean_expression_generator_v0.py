
# Calculate the SOP functions for each product of a table



def U(txt):
    """
    prints with overline:
    #    print(u'IV\u0305V\u0305')
    """
    str = ""
    for t in txt:
        str += t + "\u0305"
    return str
