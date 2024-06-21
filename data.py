class ElementsPage:
    field_name = 'Имя пользователя'
    field_email = 'Электронная почта'
    field_password = 'Пароль'
    field_referral = 'Реферальный код'

    error_message_empty = ' Поле не заполнено '
    error_message_name = ' Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы '
    error_message_email = ' Формат e-mail: username@test.ru '
    error_message_password = ' Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры '
    error_message_password_min = ' Пароль должен содержать минимум 8 символов '
    error_message_referral = ' Неверный формат ссылки '

    button_checkbox = 'checkbox'


class InputData:
    big_name = 'apdaidapidajdgmgnuasfdsifj6464fsgpofjsfjs'
    big_email = 'Sposfjpsjfpsjfpsjpfsjpfsfpsjfs61687434668168@mail.ru'
    big_password ='dfasfafdapihfaofhsouhgsdoguhsouhgohsoghsoughsoghsoghoshgoshoguhsohgoshoghsoghsohgosrho'

    min_name = 'a'
    min_email = 'a'
    min_password = 'b'

    incorrect_name = '@1354John'
    incorrect_email = 'John2323'
    incorrect_password = 'aaaaaaaaa'
    incorrect_referral = 'aaaaaaaaaaaaaaa'

    correct_name = 'John323232'
    correct_email = 'John22@mail.ru'
    correct_password = 'John_realme_2225'