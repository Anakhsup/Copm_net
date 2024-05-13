from git import Repo

# Клонирование удаленного репозитория
repo = Repo.clone_from('https://github.com/username/repository.git', '/path/to/local/repository')

# Добавление изменений
repo.index.add(['file1.txt', 'file2.txt'])

# Создание коммита
repo.index.commit('Commit message')

# Отправка изменений на удаленный репозиторий
repo.remotes.origin.push()

# Получение изменений с удаленного репозитория
repo.remotes.origin.pull()
