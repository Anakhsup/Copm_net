import paramiko

# Создание объекта SSH клиента
client = paramiko.SSHClient()

# Установка политики автоматического подключения к неизвестным хостам
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Подключение к серверу
client.connect('hostname', username='username', password='password')

# Выполнение команды на удаленном сервере
stdin, stdout, stderr = client.exec_command('ls')

# Вывод результатов выполнения команды
print(stdout.read().decode())

# Закрытие соединения
client.close()
