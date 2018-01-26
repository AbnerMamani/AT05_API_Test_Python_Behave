Feature: Create a new email
    Scenario: create a new gmail account

    given I'm in the option to create an account
    when I introduce the following information
        | first      | last  | username | password   | year | month | day | gender  | phone   | email                       |
        | pinocho    | pino  | pinocho  | passworD12 | 2000 | 2     | 28  | I am    | 4239868 | laslomas.la@hotmail.com.ar  |
