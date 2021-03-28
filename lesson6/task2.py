# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
# превышает объем ОЗУ компьютера.


with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    need_list = []
    remote_addr_spam = []
    for line in f:
        remote_addr = line.split(' - - ')[0]
        request_type = line.split('/downloads')[0].split('"')[1]
        requested_resource = '/' + line.split(' HTTP')[0].split(' /')[1]
        need_tuple = (remote_addr, request_type, requested_resource)
        need_list.append(need_tuple)
        remote_addr_spam.append(remote_addr)
    max_spam = remote_addr_spam.count(remote_addr_spam[0])
    for element in remote_addr_spam:
        if remote_addr_spam.count(element) > max_spam:
            max_spam = remote_addr_spam.count(element)
            spam = element
    print(max_spam, spam)
