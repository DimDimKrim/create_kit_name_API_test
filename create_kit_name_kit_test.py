import sender_stand_request

authToken = sender_stand_request.get_auth_token()

#Создаём набор с 1 буквой
def test_moy_nabor_kit_1symb():
    sender_stand_request.create_kit_positive_check(authToken, 201, 'a')

#Создаем набор с 511 буквами
def test_tvoy_nabor_kit511symb():
    sender_stand_request.create_kit_positive_check(authToken, 201, 'a'*511)

#Создаём набор без букв
def test_tvoy_nabor_0_symb():
    sender_stand_request.create_kit_negative_check(authToken, 400, '')

#Создаем набор с 512 буквами
def test_tvoy_nabor_512_symb():
    sender_stand_request.create_kit_negative_check(authToken, 400, 'a'*512)

#Создаем набор с английскими символами
def test_tvoy_nabor_english_symb():
    sender_stand_request.create_kit_positive_check(authToken, 201, 'QWErty')

#Создаем набор с русскими символами
def test_tvoy_nabor_russian_symb():
    sender_stand_request.create_kit_positive_check(authToken, 201, 'Мария')

#Создаем набор со спецсимволами
def test_tvoy_nabor_special_symb():
    sender_stand_request.create_kit_positive_check(authToken, 201, '"№%@",')

#Создаём набор с пробелами
def test_tvoy_nabor_with_gap():
    sender_stand_request.create_kit_positive_check(authToken, 201, 'Человек и КО')

#Создаём набор с цифрами
def test_tvoy_nabor_with_number():
    sender_stand_request.create_kit_positive_check(authToken, 201, '123')

#Создаём набор без передачи параметра
def test_empty_kit():
    sender_stand_request.create_kit_negative_check(authToken, 400)

#Создаём набор с другим типом данных(числом)
def test_tvoy_nabor_with_number_in_params():
    sender_stand_request.create_kit_negative_check(authToken, 400, 123)







