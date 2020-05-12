# bioinformatica TP1

## Ejercicio 2
### Configuración
Para configurar el script se requieren ajustar los siguientes parametros dentro del archivo ej2.py

- ONLINE: True si se quiere procesar online, False si se quiere porcesar con blast local
- BLAST_EXECUTABLE: string representando el path al ejecutable de blast (Solo aplica a blast local)
- E_VALUE_THRESH: el threshold de e para utilizar en la consulta de blast
- PROT_DB: Path a la DB a utilizar
- FASTA_FILE: string representando el path al archivo fasta que se desa usar para la query
- RESULTS_XML: string representando el archivo en donde se guardaran los resultados de la consulta de blast

### Ejecutar el script
Luego, simplemente correr el script con 
```
python ej2.py
```

### Interpretación de los resultados
El script busca los alineamientos locales posibles dentro de la base de datos de proteinas especificada, este retorna las secuencias con las cuales se hizo el alineamiento ordenandolas por su valor de identity que representa la similitud entre las secuencias. 