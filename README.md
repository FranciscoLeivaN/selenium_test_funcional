Ejercicio Guiado: Pruebas Funcionales con Selenium
Grupo 2 : Guillermo Torres / Francisco Leiva

1.- ¿Qué tipo de errores podrías detectar con esta prueba funcional?
Con la prueba funcional implementada, se pueden detectar varios tipos de errores importantes:
  * Errores de disponibilidad: Si el sitio web (DuckDuckGo en este caso) no está accesible o muestra errores de servidor.

Cambios en la interfaz de usuario:
  * Modificaciones en el campo de búsqueda (si cambiara el atributo name="q")
  * Cambios en la estructura HTML de los resultados que rompen los selectores CSS
    
Problemas de funcionalidad básica:
  * Si el motor de búsqueda no devuelve resultados cuando debería
  * Si la función de búsqueda no procesa correctamente la consulta

Errores de tiempo de respuesta:
  * Si la carga de resultados toma más tiempo del esperado (aunque el time.sleep(5) actual es una solución temporal)
  * Problemas de renderizado: Si los elementos están presentes en el DOM pero no se muestran visualmente.

2.- ¿Por qué es importante automatizar pruebas desde la perspectiva del usuario?
Automatizar pruebas desde la perspectiva del usuario es crucial por varios motivos:
  * Validación de la experiencia real: Estas pruebas simulan las acciones que realizaría un usuario final, verificando que los flujos completos funcionan correctamente.
  * Detección temprana de regresiones: Cambios en una parte del código pueden afectar inesperadamente la experiencia del usuario. Las pruebas automatizadas capturan estos problemas antes de llegar a producción.
  * Complementa pruebas unitarias: Mientras que las pruebas unitarias verifican componentes aislados, las pruebas funcionales validan la integración de todos los componentes desde la perspectiva del usuario.
  * Ahorro de tiempo y recursos: La ejecución manual repetitiva de pruebas es costosa y propensa a errores humanos. La automatización permite ejecutar pruebas complejas de forma consistente.
  * Facilita el desarrollo continuo: En un entorno de integración/entrega continua, estas pruebas proporcionan confianza para desplegar cambios con frecuencia.

3.-¿Qué limitaciones tiene Selenium y cómo las superarías?
Fragilidad ante cambios de UI:
* Problema: Los selectores pueden romperse cuando la estructura HTML cambia.
* Solución: Usar selectores más robustos, implementar estrategias de recuperación (como en tu código al intentar múltiples selectores) y considerar herramientas como Page Object Model para abstraer los selectores.

Tiempos de espera impredecibles:
* Problema: time.sleep() es ineficiente y puede hacer que las pruebas sean lentas o inestables.
* Solución: Usar esperas explícitas e implícitas.

Rendimiento y escalabilidad:
* Problema: Selenium es relativamente lento y consume muchos recursos.
* Solución: Implementar ejecución en paralelo, usar Selenium Grid para distribuir pruebas y considerar herramientas como Playwright o Cypress para pruebas más rápidas en algunos casos.

En esta prueba se valido -> La funcionalidad de búsqueda en DuckDuckGO, probando su disponibilidad y la presentación de resultados.

Que podría fallar si esta prueba no existiera -> Podrian surguir problemas sin ser detectados como cambios en el código que afecten al motor de búsqueda y fallas en la api que podrian degradar el tiempo de respuesta de la búsqueda.

Sugerencias para nuevos casos funcionales-> Pruebas de búsqueda avanzada - validación de filtros y pruebas de accesibilidad básica.