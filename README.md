# Validador de números de tarjetas de crédito
Proyecto en python-django para verificar la validez de números de tarjetas de crédito, e identificar el emisor.

## Instalación
Se recomienda el uso de Docker, con Docker activo, ejecutar los siguientes comandos:
```
git clone https://github.com/Jcmantillam/credit_card_validator.git
cd card_validator
docker-compose build
docker-compose up
```

## Tests
Las pruebas realizadas se encuentran en `/cardverifier/tests`:
```
docker-compose run web python3 manage.py test
```

## Servicios
El servicio habilitado, permite que dado un número de tarjeta de crédito, se verifique su validez y su entidad emisora.
- /verify_card

### verify_card
 
 * **URL:** <api/v1/verify_card/>
 
 * **Métodos soportados:**
  `POST`

* **Parámetros de datos (POST)**
**Requeridos:**<br>
  `card_number=[String]`<br>

* **Respuesta:**

  * **Código:** 201 <br>
  * **Contenido:** <br><br>
  
  ```
  {
    "valid": true,
    "emisor": "Visa"
  }
  ```
### Ejemplos
* **Entradas válidas**
  <br><br>
  **Entrada:**<br>
  ```
  {
    "card_number": "4013021266290"
  }
  ```
  * **Respuesta:**<br>
  ```
  {
    "valid": true,
    "emisor": "Visa"
  }
  ```
  <br><br>
  **Entrada:**<br>
  ```
  {
    "card_number": "370485935825278"
  }
  ```
  * **Respuesta:**<br>
  ```
  {
    "valid": true,
    "emisor": "American Express"
  }
  ```
  <br><br>
  **Entrada:**<br>
  ```
  {
    "card_number": "6011 5947 8671 7005"
  }
  ```
  * **Respuesta:**<br>
  ```
  {
    "valid": true,
    "emisor": "Discover"
  }
  ```
  <br><br>
* **Entradas inválidas o erróneas**
  <br><br>
  **Entrada:**<br>
  ```
  {
    "card_number": "123456789"
  }
  ```
  * **Respuesta:**<br>
  ```
  {
    "valid": false
  }
  ```
  <br><br>
  **Entrada:**<br>
  ```
  {
    "card_number": "a370485935825278"
  }
  ```
  * **Respuesta:**<br>
  ```
  {
    "not_digit": [
        "'a' is not a digit."
    ]
  }
  ```
