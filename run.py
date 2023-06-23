import subprocess

# Ruta a los scripts que deseas ejecutar
script1 = 'tiktok.py'
script2 = 'voz.py'

# Ejecutar el primer script en un proceso independiente
p1 = subprocess.Popen(['python', script1])

# Ejecutar el segundo script en un proceso independiente
p2 = subprocess.Popen(['python', script2])

# Esperar a que ambos procesos terminen
p1.wait()
p2.wait()

# Verificar si los scripts se ejecutaron correctamente
if p1.returncode == 0 and p2.returncode == 0:
    print("Ambos scripts se ejecutaron correctamente.")
else:
    print("Al menos uno de los scripts tuvo un error.")
