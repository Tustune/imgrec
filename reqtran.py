# https://translate.google.cn/translate_a/single?client=gtx&sl=en&tl=zh&dt=t&q=
from urllib import request




def makereq(text='rabbit'):
    gurl = 'https://translate.google.cn/translate_a/single?client=gtx&sl=en&tl=zh&dt=t&q=' + text
    req = request.Request(gurl)
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        cn = f.read().decode('utf-8').split(r'"')[1]
    return cn
