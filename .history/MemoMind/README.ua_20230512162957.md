Бот "MemoMind 1.1.0".
Цей бот використовується для зберігання важливої інформації, такої як телефонна книга, а також список нотаток/завдань з хештегами і ще даяких інших корисних функцій. Основні команди (всі команди сase-insensitive):

- HELLO: вітається з користувачем
- LANG: Виьирає мову виводу на екран для додатка. Зміни вступають в силу після рестарту. Frmat: lang  
- SOUND OFF: вимикає озвучку голосових повідомлень. Запроваджено тільки в англійській версії. Формат: sound off
- SOUND ON: вмикає озвучку голосових повідомлень. Запроваджено тільки в англійській версії. Формат: sound on
- ADD CONTACT: додає контакт та його дані в телефонну книгу. Формат: add contact ім'я (обов'язковий параметр) телефон e-mail адреса (необов'язкові праметри). Імена користувачів не можуть складатись лише з цифр і бути коротше 2-х символів. Якщо контакт вже існує, додаються нові дані
- ADD NOTE: додає нотатку(з поточною датою та статусом "не виконано") до списку нотаток. Формат: add note текст нотатки через пробіли
- ADD TAG: додає тег до нотатки. Формат: add tag перші_літери_нотатки... #тег
- ADD ADDRESS: Додає адресу контакта. Формат: add address ім'я адреса
- ADD EMAIL: додає e-mail контакта. Формат: add email ім'я e-mail
- ADD BDAY: додає дату народження контакта. Формат: add bday ім'я дата

- CHANGE PHONE: змінює телефон(и) контакту. Формат: change phone ім'я телефон (необов'язковий праметр). Якщо в контакту не було телефона, можна одразу його додати. Якщо 1 номер - він замінюється на новий. Якщо у контакта у книзі більше одного номера телефону можна вибрати який з них змінити
- CHANGE EMAIL: змінює e-mail контакта. Формат: change email ім'я (обов'язковий параметр) e-mail
- CHANGE BDAY: змінює дату народження. Формат: change bday ім'я дата
- CHANGE ADDRESS: змінює адресу. Формат: change address ім'я адерса
- CHANGE NOTE: змінює зміст нотатки. Формат: change note (перші_літери_нотатки... або #тег) новий_зміст
- CHANGE STATUS: змінює статус нотатки на "виконано" зі збереженням дати. Формат: change status (перші_літери_нотатки... або #тег)

- PHONE: виводить телефон(и) контакту на екран. Формат: phone ім'я
- DEL PHONE: видаляє телефон контакту. Формат: del phone ім'я телефон (необов'язковий праметр). Якщо номер введено то видаляється саме він, якщо ні, то вибираєте який номер видалити
- DEL CONTACT: видаляє контакт з телефонної книги. Формат: del contact ім'я
- DEL ADDRESS: видаляє адресу контакта. Формат: del address ім'я
- DEL NOTE: видаляє нотатку. Формат: del note (перші_літери_нотатки... або #тег)
- DEL EMAIL: видаляє e-mail контакта. Формат: del email ім'я
- DEL BDAY: видаляє дату народження контакта. Формат: del bday ім'я

- CONGRAT: виводить список контактів, у яких буде день народження в зазначений період. Формат: congrat число_днів
- SHOW CONTACTS: виводить на екран телефонну книгу. Формат: show contacts
- SHOW NOTES: виводить всі нотатки, дату створення, статус виконання та дату виконання. Формат: show notes
- SEARCH: виконує пошук по книзі контактів. Знаходить всі співпадіння в номерах, іменах або імейлах. Рядок пошуку не меньше 3-х символів. Формат: search рядок
- SEARCH NOTE: знаходить співпадіння в нотатках від 1 символу або за тегом. Формат: search note (перші_літери_нотатки... або #тег)
- SORT FOLDER: розсортовує файли за типами в теці по вказаному шляху. Розпаковує архіви, видаляє порожні теки. Перекладає імена файлів і тек транслітом з кирилиці. Формат: sort folder шлях_до_теки. Типи файлів можна задавати в конігураційному файлі config.JSON. Назва теки "archives" незмінна!
- CLOSE, GOOD BYE, EXIT: виходить в операційну систему
- HELP: виводить цей мануал на екран. Імена файлів з телефонною книгою і з книгою нотаток також прописані в файлі config.JSON