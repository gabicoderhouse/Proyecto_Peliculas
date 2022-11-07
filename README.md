# Nombre            : Proyecto_Peliculas

## Descripción       : Es un Blog de Películas, donde poder buscar dentro de un listado de Películas ingresadas, y actualizar las existentes.

## Instalación       : Se debe tener Git Instalado y el link del repositorio en GitHub

  1 . Crear carpeta local.
 
  2 . Iniciar Visual Code.
 
  3 . Abrir terminal.
 
  4 . Acceder al link del GitHub que te hemos pasado.
 
  5 . Mediante el botón "Code" de HitGub copiar las sentencias necesarias para Clonar.
 
  7 . En la terminal poner git clone <url copiada en paso 5>
 
  8 . Instalar el entorno virtual y activarlo
 
  9 . Instalar lo definido en el archivo requirements.txt
 
  10 . Ejecutar las migraciones para la base db.sqlite3
 
  11 . Levantar el servidor de Django
 
  12 . Listo ya podes navegar por el blog

## ¿Cómo Usar?
- Inicio          : Es el acceso inicial al blog, acceso al menú principal
- Ver Películas   : Muestra un listado de Películas ya cargadas mostrando una imagen de la película, el Nombre de la misma y el género al que pertenece. 
                    En la parte superior de la ventana se ve "Agregar Películas" y clickeando sobre el mismo se accede a creación de una nueva película en el blog.
                    También hay un buscador de Películas por el nombre o parte del mismo.
                    El nombre de la película es un link que habilita solo la visualización de los datos de la misma, sin permitir su modificación, y está permitido para 
                    usuario logeado o no.
                    Al lado de cada película hay dos botones uno para Editar los datos de la Películas y otro para eliminarla. (Solo podrán modificar o eliminar las 
                    Películas ingresadas por el user que se logeo a la página o el administrador del sistema.)
- Iniciar sesión  : Habilita para ingresar el usuario y password. Y luego de logeado, muestra el nombre del User
- Registrarse     : Es necesario obtener un usuario / Password para operar en el blog, el mismo se ingresa en esta sección. Una vez logeado el usuario esta opción se 
                    convierte en cerrar sesión, para dar finalizada la navegación por el blog.

- El módulo de administración no tiene acceso por menú, solo por url completa "http://127.0.0.1:8000/admin/"
 
 ## Licencia         : Uso privado curso CoderHouse

Se incluye un video del funcionamiento del blog, nombre del archivo: "peliculasApp.mp4"