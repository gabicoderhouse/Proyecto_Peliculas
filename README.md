Nombre            : Proyecto_Peliculas

Descripci�n       : Es un Blog de pel�culas, donde poder buscar dentro de un listado de pel�culas ingresadas, y actualizar las existentes.

Instalaci�n       : Se debe tener Git Instalado y el link del repositorio en GitHub

  1 . Crear carpeta local.
 
  2 . Iniciar Visual Code.
 
  3 . Abrir terminal.
 
  4 . Acceder al link del GitHub que te hemos pasado.
 
  5 . Mediante el bot�n "Code" de HitGub copiar las sentencias necesarias para Clonar.
 
  7 . En la terminal poner git clone <url copiada en paso 5>
 
  8 . Instalar el entorno virtual y activarlo
 
  9 . Instalar lo definido en el archivo requirements.txt
 
  10 . Ejecutar las migraciones para la base db.sqlite3
 
  11 . Levantar el servidor de Django
 
  12 . Listo ya podes navegar por el blog

�C�mo Usar?
- Inicio          : Es el acceso inicial al blog, acceso al men� principal
- Ver Pel�culas   : Muestra un listado de Pel�culas ya cargadas mostrando una imagen de la pel�cula, el Nombre de la misma y el g�nero al que pertenece. 
                    En la parte superior de la ventana se ve "Agregar Pel�culas" y clickeando sobre el mismo se accede a creaci�n de una nueva pel�cula en el blog.
                    Tambi�n hay un buscador de pel�culas por el nombre o parte del mismo.
                    El nombre de la pel�cula es un link que habilita solo la visualizaci�n de los datos de la misma, sin permitir su modificaci�n, y est� permitido para 
                    usuario logeado o no.
                    Al lado de cada pel�cula hay dos botones uno para Editar los datos de la pel�culas y otro para eliminarla. (Solo podr�n modificar o eliminar las 
                    pel�culas ingresadas por el user que se logeo a la p�gina o el administrador del sistema.)
- Iniciar sesi�n  : Habilita para ingresar el usuario y password. Y luego de logeado, muestra el nombre del User
- Registrarse     : Es necesario obtener un usuario / Password para operar en el blog, el mismo se ingresa en esta secci�n. Una vez logeado el usuario esta opci�n se 
                    convierte en cerrar sesi�n, para dar finalizada la navegaci�n por el blog.

- El m�dulo de administraci�n no tiene acceso por men�, solo por url completa "http://127.0.0.1:8000/admin/"
 
 Licencia         : Uso privado curso CoderHouse

Se incluye un video del funcionamiento del blog, nombre del archivo: peliculasApp.mp4