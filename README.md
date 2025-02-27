# API Flask - Consumo de Datos CPG

## Descripción

Este microservicio en Flask permite consumir información de productos CPG (Consumer Packaged Goods) desde una API pública. Ofrece endpoints para obtener información de un producto por su ID y una lista de productos disponibles en la API.

El proyecto utiliza Flask como framework principal y se gestiona con `pip` para la instalación de dependencias. La configuración se maneja a través de un archivo `.env`, lo que permite flexibilidad en la configuración de la API.

---

## Requisitos previos

Antes de instalar el proyecto, asegúrate de tener instalados los siguientes componentes:

- [Python 3.11](https://www.python.org/downloads/)
- Git (para clonar el repositorio)

---

## Instalación y configuración

### 1. Clonar el repositorio

Ejecuta el siguiente comando en la terminal:

```bash
git clone https://github.com/avaradius/api-flask.git
cd api-flask
```
### 2. Instalar dependencias

Ejecuta el siguiente comando en la terminal:

```bash
pip install python-dotenv
pip install flask flask-dotenv requests
```
### 3. Ejecutar servicio

Ejecuta el siguiente comando en la terminal:

```bash
python run.py
```
Servidor: http://127.0.0.1:5000

## Endpoints

GET /api/products
```bash
curl -X GET http://127.0.0.1:5000/api/products
```

GET /api/product/<product_id>
```bash
curl -X GET http://127.0.0.1:5000/api/product/737628064502
```


## Notas Extras

Para eliminar todas las carpetas __pycache__ y liberar el cache ejecutar en PowerShell
```bash
Get-ChildItem -Path . -Filter __pycache__ -Recurse | Remove-Item -Recurse -Force
```
