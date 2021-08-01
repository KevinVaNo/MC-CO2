# Nombre del Proyecto : MC-CO2

*****************************************************************************************************************
### Descripción del Proyecto

**MC-CO2** es un sistema de IoT basado en Azure dirigido a instituciones educativas y oficinas gubernamentales, que mediante un dispositivo situado en un espacio cerrado detecta los niveles de CO2 en el ambiente por medio de un sensor con el fin de alertar a una autoridad del lugar para que el área sea ventilada, despejada o desinfectada y asì prevenir el contagio con el virus COVID-19.

*****************************************************************************************************************
### Link al Tiktok

**https://vm.tiktok.com/ZMdcwvWXo/**

Cabe recalcar que debido a problemas con la conexión de la Raspberry fisica al bus service (la parte del enrutamiento, asi como realizar tareas de stream analytics con Python para leer los sensores y promediar valores (en el codigo ejemplo se usan dos valores analogicos)) se hizo uso del simulador de Rasp visto en el curso; se cuenta con envio de Rasp fisica a Azure (se ve mediante la extension de Visual Studio).

![Envio de dato a azure visto desde visual studio](https://github.com/PapiroX/CO2-meter/blob/main/Enviodato.png)

*****************************************************************************************************************
### Diagrama de Azure
![Diagrama Azure](https://user-images.githubusercontent.com/86867751/127775093-c44169a1-8b43-4d11-b8da-0345a3d00a0a.png)

*****************************************************************************************************************
### SLA Compuesto

|          **Recurso**        |     **SLA**   |
|          :----:             |     :----:    |
|Azure IoT Hub                |     99.9 %    |
|Service Bus                  |     99.9 %    |
|Notification Hubs            |     99.9 %    |
|Azure Logic Apps             |     99.9 %    |
|SLA COMPUESTO                |    99.60 %    |

SLA compuesto = 99.9 % x 99.9 % x 99.9 % x 99.9% = 99.60 %

*****************************************************************************************************************
### TCO 3 años y Precio Total por mes

![TCO](https://user-images.githubusercontent.com/87109811/127764517-8bce13a2-31e4-4654-acc7-441fa747f498.jpg)
![tco2](https://user-images.githubusercontent.com/87109811/127764555-57756c82-d633-40fb-a55f-d365da002429.jpg)
![tco3](https://user-images.githubusercontent.com/87109811/127764599-42ce59a8-6e05-4158-9358-374d94c149c8.jpg)


*****************************************************************************************************************
### Tiempo sin disponibilidad a un año

FORMULA: Tiempo de NO DISPONIBILIDAD = tiempo * (1 - SLA)

525600 * (1 - 0.9960) = 2102.4 minutos al año.
*****************************************************************************************************************
### Qué te pareció el evento

**Mejía Trujillo Mario Alberto** :D

Me llevo una muy grata sorpresa por parte de innovaccion pues, rompiendo esa barrera donde el conocimiento se 
queda en las lineas "científicas", llega a tik tok como un regalo del cielo a aventarme muchisima informacion 
con la cual me dotan de conocimientos para aprobar una certificacion muy enfocada en mi carrera. me fascinó la
clase y guia del sherpa José, la convivencia del teams y sobre todo las practicas, que dificiles, divertidas.

**Vasquez Nogueda Kevin**🍄

Este fue mi primer Hackathon, por lo que tenía mis dudas sobre participar y temía salir de mi área de comfort 
pero definitivamente me considero afortunado de ser parte de esta gran oportunidad, donde aprendí nuevas cosas 
junto a mi equipo y, aún con ciertas complicaciones técnicas, logramos sacar a flote una gran idea.

**Noè Alexaner Espinoza Gonzàlez**

Es el primer evento de este tipo en dònde participo, se pudo complementar los conocimientos tenidos con los 
obtenidos, la mejor parte fue el compañerismo y equipo, es agradable conocer a personas dedicadas y enfocadas,
trabajar en equipo, que las ideas fluyeron y todos estuvimos de acuerdo, tambièn de esta manera se conocieron
màs a fondo como utilizar los servicios de Azure en un entorno real.

**Oscar Donis Hernández**

este summer hack, al ser el primero, iba un poco temeroso por no saber que encontrar en el, pero todo cambio 
al entrar y pertenecer a un equipo entregado al proyecto que, dicho sea de paso, cumplió mis expectativas y 
puso mis conocimientos a prueba. ora parte muy interesante fueron los eventos nocturnos que se estuvieron 
celebrando los días activos del hackaton, participé sin pena y como siempre la experiencia por delante. 
viva innovaccion.

**Raúl Suárez Viveros**

Summer hack me permitió conocer mas allá de los límites que implica un concepto educativo a darme cuenta
que realmente hay una visión de aplicación con la nube de azure que va más allá de un solo enfoque, y que 
un proyecto abarca distintas disciplinas por lo que considero que es una experiencia que suma demasiado 
a desarrollar otras habilidades.



