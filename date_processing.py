import pyperclip
import re
import datetime as dt

def date_regex(text):
    dateRegex = re.compile(r'''((
       (
       (\d{1,2}|sunday|monday|tuesday|wednesday|thursday|friday|saturday|sun|mon|tue|wed|thu|fri|sat)[-./,\s]
       (\d{1,2}|january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)
       [-./,\s](\d{2,4}))|
       ((sunday|monday|tuesday|wednesday|thursday|friday|saturday|sun|mon|tue|wed|thu|fri|sat)[-./,\s]
       ((january|february|march|april|may|june|july|august|september|october|november|december)|((jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[\s]))
       )|
       (
     (january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[-./,\s]
       (\d{2,4}))
       |((sunday|monday|tuesday|wednesday|thursday|friday|saturday|sun|mon|tue|wed|thu|fri|sat)
       [-./,\s](\d{2,4}))
       |((\d{1,2})
       [-./,\s](\d{2,4}))
       |(\s(\d{4})\s) |((in|on)\s(\d{2})\s)
       |((in|on)\s(sunday|monday|tuesday|wednesday|thursday|friday|saturday|sun|mon|tue|wed|thu|fri|sat))
       |((in|on)\s(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec))

         |((\d{2,4})[-./,\s]
       (\d{1,2}|sunday|monday|tuesday|wednesday|thursday|friday|saturday|sun|mon|tue|wed|thu|fri|sat)[-./,\s]
       (\d{1,2}|january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)
       )|
       ((\d{2,4})[-./,\s]
     (january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)
       )
       |((\d{2,4})[-./,\s]
       (sunday|monday|tuesday|wednesday|thursday|friday|saturday|sun|mon|tue|wed|thu|fri|sat))
       |((\d{2,4})
       [-./,\s](\d{1,2}))

        ))''', re.VERBOSE)

    fmts = (
        ' %Y ', 'in %y ', 'on %y ', '%m-%Y', '%m-%y', '%A-%B', '%a-%B', '%A-%b ', '%a-%b ', '%a-%B', '%b-%Y', '%b-%y',
        '%B-%y',
        '%B-%Y', '%a-%Y', '%A-%Y', '%a-%y', '%A-%y',
        '%A-%B-%Y', '%a-%B-%Y', '%a-%b-%Y', '%A-%b-%Y', '%d-%m-%Y', '%a-%m-%Y', '%A-%B-%y', '%a-%B-%y', '%a-%b-%y',
        '%A-%b-%y',
        '%d-%m-%y', '%a-%m-%y',
        '%Y-%m', '%y-%m', '%Y-%b', '%y-%b', '%y-%B', '%Y-%B', '%Y-%a', '%Y-%A', '%y-%a', '%y-%A',
        '%Y-%A-%B', '%Y-%a-%B', '%Y-%a-%b', '%Y-%A-%b', '%Y-%d-%m', '%Y-%a-%m', '%y-%A-%B', '%y-%a-%B', '%y-%a-%b',
        '%y-%A-%b',
        '%y-%d-%m', '%y-%a-%m',

        '%m/%Y', '%A/%B', '%a/%B', '%A/%b ', '%a/%b ', '%a/%B', '%b/%Y', '%b/%y', '%B/%y', '%B/%Y', '%a/%Y', '%A/%Y',
        '%a/%y',
        '%A/%y',
        '%A/%B/%Y', '%a/%B/%Y', '%a/%b/%Y', '%A/%b/%Y', '%d/%m/%Y', '%a/%m/%Y', '%A/%B/%y', '%a/%B/%y', '%a/%b/%y',
        '%A/%b/%y',
        '%d/%m/%y', '%a/%m/%y',
        '%Y/%m', '%Y/%b', '%y/%b', '%y/%B', '%Y/%B', '%Y/%a', '%Y/%A', '%y/%a', '%y/%A',
        '%Y/%A/%B', '%Y/%a/%B', '%Y/%a/%b', '%Y/%A/%b', '%Y/%d/%m', '%Y/%a/%m', '%y/%A/%B', '%y/%a/%B', '%y/%a/%b',
        '%y/%A/%b',
        '%y/%d/%m', '%y/%a/%m',

        '%A,%B', '%a,%B', '%A,%b ', '%a,%b ', '%a,%B', '%b,%Y', '%b,%y', '%B,%y', '%B,%Y', '%a,%Y', '%A,%Y', '%a,%y',
        '%A,%y',
        '%A,%B,%Y', '%a,%B,%Y', '%a,%b,%Y', '%A,%b,%Y', '%d,%m,%Y', '%a,%m,%Y', '%A,%B,%y', '%a,%B,%y', '%a,%b,%y',
        '%A,%b,%y',
        '%d,%m,%y', '%a,%m,%y',
        '%Y,%b', '%y,%b', '%y,%B', '%Y,%B', '%Y,%a', '%Y,%A', '%y,%a', '%y,%A',
        '%Y,%A,%B', '%Y,%a,%B', '%Y,%a,%b', '%Y,%A,%b', '%Y,%d,%m', '%Y,%a,%m', '%y,%A,%B', '%y,%a,%B', '%y,%a,%b',
        '%y,%A,%b',
        '%y,%d,%m', '%y,%a,%m',

        '%A.%B', '%a.%B', '%A.%b ', '%a.%b ', '%a.%B', '%b.%Y', '%b.%y', '%B.%y', '%B.%Y', '%a.%Y', '%A.%Y', '%a.%y',
        '%A.%y',
        '%A.%B.%Y', '%a.%B.%Y', '%a.%b.%Y', '%A.%b.%Y', '%d.%m.%Y', '%a.%m.%Y', '%A.%B.%y', '%a.%B.%y', '%a.%b.%y',
        '%A.%b.%y',
        '%d.%m.%y', '%a.%m.%y',
        '%Y.%b', '%y.%b', '%y.%B', '%Y.%B', '%Y.%a', '%Y.%A', '%y.%a', '%y.%A',
        '%Y.%A.%B', '%Y.%a.%B', '%Y.%a.%b', '%Y.%A.%b', '%Y.%d.%m', '%Y.%a.%m', '%y.%A.%B', '%y.%a.%B', '%y.%a.%b',
        '%y.%A.%b',
        '%y.%d.%m', '%y.%a.%m',

        '%A %B', '%a %B', '%A %b ', '%a %b ', '%a %B', '%b %Y', '%b %y', '%B %y', '%B %Y', '%a %Y', '%A %Y', '%a %y',
        '%A %y',
        '%A %B %Y', '%a %B %Y', '%a %b %Y', '%A %b %Y', '%d %m %Y', '%a %m %Y', '%A %B %y', '%a %B %y', '%a %b %y',
        '%A %b %y',
        '%d %m %y', '%a %m %y',
        '%Y %b', '%y %b', '%y %B', '%Y %B', '%Y %a', '%Y %A', '%y %a', '%y %A',
        '%Y %A %B', '%Y %a %B', '%Y %a %b', '%Y %A %b', '%Y %d %m', '%Y %a %m', '%y %A %B', '%y %a %B', '%y %a %b',
        '%y %A %b',
        '%y %d %m', '%y %a %m',

        'in %a', 'on %a', 'in %A', 'on %A', 'in %b', 'on %b', 'in %B', 'on %B')

    for groups in dateRegex.findall(text):
        for fmt in fmts:
            try:

                t = dt.datetime.strptime(groups[0], fmt)
                if (fmt == ' %Y ' or fmt == ' %y '):
                    t = t.strftime(' %m/%d/%Y ')
                elif (fmt.__contains__(" ")):
                    t = t.strftime('%m/%d/%Y ')
                elif (fmt.__contains__("d")):
                    t = t.strftime('%m/%d/%Y ')
                else:
                    t = t.strftime('%m/%W/%Y')
                # print(t)
                # print(groups[0])
                text = text.replace(groups[0], t)
                break
            except ValueError as err:
                pass
    # print(text)
    return text