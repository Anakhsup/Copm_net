import csv
import subprocess

# Список доменов для пингования
domains = ['google.com', 'facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com', 'youtube.com', 'amazon.com', 'microsoft.com', 'apple.com', 'yahoo.com']

# Открываем файл для записи результатов
with open('ping_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Записываем заголовки столбцов
    writer.writerow(['Domain', 'Time', 'TTL', 'IP', 'Bytes'])

    # Пингуем каждый домен и записываем результаты в таблицу
    for domain in domains:
        # Выполняем пинг команду
        ping_result = subprocess.run(['ping', '-c', '4', domain], capture_output=True, text=True)
        print(ping_result)

        # Получаем результаты пинга
        time = ping_result.stdout.splitlines()[-1].split('=')[-1].split()[0]
        ttl = ping_result.stdout.splitlines()[-2].split('=')[-1].split()[0]
        ip = ping_result.stdout.splitlines()[1].split()[2][1:-1]
        bytes = ping_result.stdout.splitlines()[-3].split('=')[-1].split()[0]

        # Записываем результаты в таблицу
        writer.writerow([domain, time, ttl, ip, bytes])

print("Результаты пингования успешно записаны в файл ping_results.csv")
