# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации
# вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" ' \
#       '"Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?


import re
need_str = re.compile(r'^((\d+\.){3}\d+) - - \[(.+)] "([A-Za-z]+) (.+) .+ (\d+) (\d+) .+$')
with open('../lesson7/nginx_logs.txt', 'r', encoding='utf-8') as f:
    n = 0
    while n < 10:
        line = f.readline().strip()
        result = need_str.search(line)
        if result:
            need_turple = (result.group(1), result.group(3), result.group(4), result.group(5), result.group(6),
                           result.group(7))
            print(need_turple)
        n += 1
