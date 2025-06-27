@echo off
:: Script para ejecutar la prueba funcional de Selenium en Windows
:: Adaptado específicamente para la estructura actual del proyecto

echo Activando entorno virtual...
call "c:\Users\Franc\Desktop\proyectos-awaken\selenium_test_funcional\venv\Scripts\activate.bat"

echo Ejecutando prueba de busqueda de inmuebles en DuckDuckGo...
"c:\Users\Franc\Desktop\proyectos-awaken\selenium_test_funcional\venv\Scripts\python.exe" "c:\Users\Franc\Desktop\proyectos-awaken\selenium_test_funcional\test_busqueda.py"

echo.
echo Prueba finalizada. Presiona cualquier tecla para salir.
pause
