# Proyecto Yasuni

Este es un proyecto para gestionar la información de diferentes categorías y nacionalidades de una reserva ecológica, desarrollado con Flask, WTForms, y siguiendo el patrón DAO. Este sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una interfaz web.

### Funcionalidades Principales

- **Gestión de Nacionalidades:** Los usuarios pueden agregar nuevas nacionalidades, editar la información existente, y eliminar registros cuando sea necesario. La interfaz de usuario facilita la visualización y edición de las nacionalidades en un formato tabular.
  
- **Gestión de Categorías:** Además de gestionar las nacionalidades, la aplicación permite administrar las categorías a las que pertenecen dichas nacionalidades, garantizando una estructura organizada.

- **Interfaz Web Amigable:** La aplicación cuenta con una interfaz simple pero eficiente, donde las opciones de navegación son claras y accesibles. El diseño incluye estilos CSS personalizados para mejorar la experiencia del usuario.

- **Arquitectura Modular:** El proyecto sigue un patrón DAO (Data Access Object) para la gestión de la lógica de acceso a datos, asegurando una separación clara entre la lógica de negocios y la presentación.

### Tecnologías Utilizadas

- **Flask:** Framework de Python utilizado para desarrollar la aplicación web.
- **WTForms:** Biblioteca utilizada para gestionar y validar formularios web.
- **HTML/CSS/JavaScript:** Tecnologías usadas para crear la interfaz de usuario, mejorar la usabilidad y proporcionar una experiencia dinámica.
- **PostgreSQL:** Base de datos relacional utilizada para almacenar la información estructurada de las nacionalidades y categorías.

### Público Objetivo

Este sistema está pensado para administradores y gestores que deseen centralizar la información de la Reserva Ecológica Yasuni y proporcionar datos organizados sobre las nacionalidades que la habitan, ayudando a la preservación cultural y facilitando la gestión administrativa.

### Casos de Uso

- **Administración de la Reserva:** Los administradores pueden gestionar la información de la reserva, asegurando que la información cultural y turística esté siempre actualizada.
- **Investigación y Documentación:** Los datos almacenados pueden ser utilizados por investigadores y documentaristas para estudiar la diversidad cultural de la reserva.
- **Visitas Turísticas:** La plataforma podría extenderse para mostrar información relevante a los visitantes interesados en conocer más sobre las diferentes culturas presentes en la región.

## Estructura del Proyecto

```
yasuniPagina/
│
├── cruds/
│   ├── __init__.py
│   ├── categoria_nacionalidad.py
│   ├── categoria_nacionalidad_dao.py
│   ├── conexion.py
│   ├── nacionalidad.py
│   ├── nacionalidad_dao.py
│   └── NacionalidadForm.py
│
├── static/
│   ├── images/
│   │   └── Yasuni.png
│   ├── js/
│   │   ├── animacionInicio.js
│   │   ├── dynamicNacionalidades.js
│   │   ├── dynamicTurismo.js
│   │   ├── gestionarNacionalidad.js
│   │   ├── gestionarTurismo.js
│   │   └── login.js
│   ├── styles/
│   │   ├── actividades.css
│   │   ├── animaciones.css
│   │   ├── animacionesMasInformacion.css
│   │   ├── crud.css
│   │   ├── login.css
│   │   ├── paginaPrincipal.css
│   │   └── tarjetas.css
│   └── videos/
│       └── Yasuni.mp4
│
├── templates/
│   ├── gestionarNacionalidad.html
│   └── ...
│
├── app.py
└── crudNacionalidades.py
```

## Requisitos

Para poder ejecutar este proyecto, necesitas tener instalado lo siguiente:

- Python 3.x
- Flask
- Flask-WTF
- Una base de datos compatible (por ejemplo, PostgreSQL)

Puedes instalar las dependencias necesarias usando el archivo `requirements.txt` (si lo tienes) con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Configuración de la Base de Datos

Asegúrate de configurar tu base de datos con las tablas necesarias. A continuación se muestra un ejemplo de cómo crear la tabla `CATEGORIASNACIONALIDADES`:

```sql
CREATE TABLE CATEGORIASNACIONALIDADES (
   CATXNACCODIGO SERIAL NOT NULL,
   CATXNACNOMBRE VARCHAR(255) NOT NULL,
   CONSTRAINT PK_CATEGORIASNACIONALIDADES PRIMARY KEY (CATXNACCODIGO)
);


### Otras tablas necesarias:

SQL
create table CATEGORIASNACIONALIDADES (
   CATXNACCODIGO SERIAL not null,
   CATXNACNOMBRE VARCHAR(255) not null,
   constraint PK_CATEGORIASNACIONALIDADES primary key (CATXNACCODIGO)
);

create unique index CATEGORIASNACIONALIDADES_PK on CATEGORIASNACIONALIDADES (CATXNACCODIGO);

create table CATEGORIASTURISTICAS (
   CATXTURCODIGO SERIAL not null,
   CATXTURNOMBRE VARCHAR(255) not null,
   constraint PK_CATEGORIASTURISTICAS primary key (CATXTURCODIGO)
);


create unique index CATEGORIASTURISTICAS_PK on CATEGORIASTURISTICAS (CATXTURCODIGO);

create table NACIONALIDADES (
   NACCODIGO SERIAL not null,
   CATXNACCODIGO INT4 not null,
   NACTITULO VARCHAR(255) not null,
   NACDESCRIPCION VARCHAR(2000) not null,
   NACURLIMAGEN VARCHAR(1000) not null,
   NACFECHACREACION DATE not null,
   constraint PK_NACIONALIDADES primary key (NACCODIGO)
);

create unique index NACIONALIDADES_PK on NACIONALIDADES (NACCODIGO);

create  index CATENACIXNACI_FK on NACIONALIDADES (CATXNACCODIGO);

create table TURISTICAS (
   TURCODIGO SERIAL not null,
   CATXTURCODIGO INT4 not null,
   TURTITULO VARCHAR(255) not null,
   TURDESCRIPCION VARCHAR(2000) not null,
   TURURLIMAGEN VARCHAR(1000) not null,
   TURFECHACREACION DATE not null,
   constraint PK_TURISTICAS primary key (TURCODIGO)
);

create unique index TURISTICAS_PK on TURISTICAS (TURCODIGO);

create  index CATETURIXTURI_FK on TURISTICAS (CATXTURCODIGO);

alter table NACIONALIDADES
   add constraint FK_NACIONAL_CATENACIX_CATEGORI foreign key (CATXNACCODIGO)
      references CATEGORIASNACIONALIDADES (CATXNACCODIGO)
      on delete restrict on update restrict;

alter table TURISTICAS
   add constraint FK_TURISTIC_CATETURIX_CATEGORI foreign key (CATXTURCODIGO)
      references CATEGORIASTURISTICAS (CATXTURCODIGO)
      on delete restrict on update restrict;
```

```

## Cómo Ejecutar el Proyecto

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/yasuni-pagina.git
```

2. Navega al directorio del proyecto:

```bash
cd yasuni-pagina
```

3. Configura un entorno virtual (opcional, pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecuta la aplicación:

```bash
python app.py
```

6. Abre tu navegador en `http://127.0.0.1:5000` para ver la aplicación.

## Funcionalidades

- **Gestión de Nacionalidades:** CRUD completo para las nacionalidades de la reserva.
- **Gestión de Categorías:** Operaciones CRUD para las categorías de nacionalidades.
- **Interfaz amigable:** Plantillas HTML con CSS personalizadas para una mejor experiencia de usuario.

## Estructura del Código

- **cruds/:** Contiene los DAOs y formularios necesarios para las operaciones CRUD.
- **static/:** Archivos estáticos como imágenes, estilos, y scripts JavaScript.
- **templates/:** Plantillas HTML que se renderizan en las distintas vistas.
- **app.py:** Punto de entrada principal de la aplicación Flask.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna mejora o encuentras algún bug, no dudes en decirnos
