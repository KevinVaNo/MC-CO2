# Nombre del Proyecto : MC-CO2

*****************************************************************************************************************
### Descripción del Proyecto

**MC-CO2** es un sistema de IoT basado en Azure dirigido a instituciones educativas y oficinas gubernamentales, que mediante un dispositivo situado en un espacio cerrado detecta los niveles de CO2 en el ambiente por medio de un sensor con el fin de alertar a una autoridad del lugar para que el área sea ventilada, despejada o desinfectada.

*****************************************************************************************************************
### Link al Tiktok

**https://vm.tiktok.com/ZMdcwvWXo/**

Cabe recalcar que debido a problemas con la conexión de la Raspberry fisica al bus service (la parte del enrutamiento, asi como realizar tareas de stream analytics con Python para leer los sensores y promediar valores (en el codigo ejemplo se usan dos valores analogicos) se hizo uso del simulador de Rasp visto en el curso; se cuenta con envio de Rasp fisica a Azure (se ve mediante la extension de Visual Studio).

![Envio de dato a azure visto desde visual studio](https://github.com/PapiroX/CO2-meter/blob/main/Enviodato.png)

*****************************************************************************************************************
### Diagrama de Azure

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



