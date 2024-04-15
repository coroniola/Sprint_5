import random as rand
class User:
    test_name = 'Ольга'
    test_email = 'olga_ilnitskaya_7_777@gmail.com'
    test_password = 123456
    wrong_password = 1234
    test_rand_email = f'olga_ilnitskaya_7_{rand.randint(100, 900)}@yandex.ru'
    test_rand_password = rand.randint(123456, 654321)
