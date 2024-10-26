# Project1
My first project

Dashboard de Análisis de Vehículos
Descripción
Este proyecto consiste en una aplicación web interactiva que permite visualizar y analizar datos de vehículos usados. La aplicación está construida con Streamlit y permite a los usuarios explorar diferentes aspectos de los datos a través de visualizaciones interactivas.
Funcionalidades

Visualización de la distribución del kilometraje de los vehículos mediante un histograma interactivo
Análisis de la relación entre precio y kilometraje a través de un gráfico de dispersión
Interfaz intuitiva con botones para generar las visualizaciones
Gráficos interactivos que permiten zoom y hover para ver detalles

Tecnologías Utilizadas

Python 3.11
Streamlit para la interfaz web
Pandas para el manejo de datos
Plotly Express para las visualizaciones
Render para el despliegue

Instalación Local

Clona este repositorio:

bashCopygit clone <https://github.com/SoyBadman/Project1.git>

Navega al directorio del proyecto:

bashCopycd <nombre-del-directorio>

Instala las dependencias:

pip install -r requirement.txt

Ejecuta la aplicación:

bashCopystreamlit run app.py
Estructura del Proyecto
Copy.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirement.txt
├── notebooks
│   └── EDA.ipynb
├── .gitignore(python)
└── .streamlit
    └── config.toml

Demo en Vivo
Puedes acceder a la aplicación desplegada en: [https://project1-jbtv.onrender.com]
Autor
Yury Ccotaccallapa
Licencia
Este proyecto está bajo la Licencia MIT.