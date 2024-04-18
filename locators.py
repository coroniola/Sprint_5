from selenium.webdriver.common.by import By

class Locators:

    LOGIN_MAINPAGE_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") # Кнопка "войти в аккаунт" на главной странице
    ACCOUNT_MAINPAGE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка "Личный кабинет" на главной странице
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href = '/account']") # Ссылка "Войти"
    RESET_PASSWORD_BUTTON = (By.XPATH, "//a[text() = 'Забыли пароль?']") # Кнопка "Забыли пароль"
    EMAIL_LOGINPAGE_INPUT = (By.XPATH, '//*[text()="Email"]/following-sibling::input') # Поле ввода Email
    PASSWORD_LOGINPAGE_INPUT = (By.XPATH, '//*[text()="Пароль"]/following-sibling::input') # Поле ввода Пароль
    GO_BUTTON = (By.XPATH, "//button[text() = 'Войти']") # Кнопка "Войти"
    SIGN_UP_LINK = (By.XPATH, "//*[contains(@class, 'Auth_link')]") # ссылка "Зарегистрироваться"
    REGISTRATION_BUTTON = (By.XPATH, "//*[contains(@class, 'button_size_medium') and text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    NAME_REG_PAGE_INPUT = (By.XPATH, "//*[text()='Имя']/following-sibling::input") # Поле ввода Имя
    INCORRECT_PASSWORD_MESSAGE = By.XPATH, "//*[contains(text(), 'Некорректный пароль')]" # Сообщение о некорректном пароле
    PROFILE_BUTTON = (By.XPATH, "//a[text() = 'Профиль']") # Кнопка "профиль"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//*[contains(@class, "AppHeader_header__linkText") and text()="Личный Кабинет"]') # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']/parent::a") # Текст "Конструктор"
    CREATE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']") # Текст в конструкторе "Соберите бургер"
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']") # Кнопка "выход"
    BUNS_SECTION = (By.XPATH, "//span[text() = 'Булки']") # Кнопка в конструкторе "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text() = 'Соусы']") # Кнопка в конструкторе "Соусы"
    TOPPINGS_SECTION = (By.XPATH, "//span[text() = 'Начинки']") # Кнопка в конструкторе  "Начинки"
    BUNS_SECTION_H2 = (By.XPATH, "//h2[text() = 'Булки']") #Заголовок в конструкторе "Булки"
    SAUCES_SECTION_H2 = (By.XPATH, "//h2[text() = 'Соусы']") #Заголовок в конструкторе "Соусы"
    TOPPINGS_SECTION_H2 = (By.XPATH, "//h2[text() = 'Начинки']") #Заголовок в конструкторе "Начинки"








