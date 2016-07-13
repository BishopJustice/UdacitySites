import timeit
import cgi

def valid_month(month):
    months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
    if month:
        cap_month = month.capitalize()
        if cap_month in months:
            return cap_month
def valid_day(day):
    if day.isdigit():
        day = int(day)
        if day > 0 and day < 32:
            return day
def valid_year(year):
    if year.isdigit():
        year = int(year)
        if year > 1900 and year < 2020:
            return year



def esc(y):
    return cgi.escape(y, quote=True)


# def esc2():
#     s = ">"
#     for(i,o) in (("&","&amp;"),
#                  (">","&gt;"),
#                  ("<","&lt;"),
#                  ('"',"&quot;")):
#         s.replace(i, o)
#     return s

# def esc(char):
#     char=">"
#     if char == "&":
#         char = "&amp;"
#     elif char == ">":
#         char = "&gt;"
#     elif char == "<":
#         char = "&lt;"
#     elif char == '"':
#         char = "&quot;"
#     else:
#         pass
#     return char

