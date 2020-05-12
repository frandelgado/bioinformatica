# bioinformatica TP1

## Instalación de programas

### BLAST+
Blast+ nos permitira buscar los alineamientos locales de nuestra secuencia fasta contra una base de datos de proteinas para obtener los alineamientos de mayor coincidencia

#### Instalación
Para instalar BLAST+ en linux podemos hacerlo directamente desde el repositorio apt mediante el siguiente comando
```
sudo apt-get install ncbi-blast+
```

### Clustal Omega
Para el alineamiento de sequencias multiples utilizaremos Clustal Omega, una herramienta de linea de comandos diseñada especificamente para esta tarea.

#### Instalación
Clustal Omega se puede instalar en linux directamente del repositorio apt corriendo el siguiente comando

```
sudo apt-get install -y clustalw
```

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

## Ejercicio 3
Despues de obtener las secuencias con un alto grado de alineamiento realizando alineamiento de a pares resulta interesante poder realizar un alineamiento multiple entre varios de estos resultados.

El ejercicio 3 realiza un alineamiento multiple utilizando la heramienta de comandos clustalw.

### Configuración
Para configurar el script se deben configurar las siguientes variables dentro del mismo:
- FASTA_FILE: El archivo multifasta que contiene todas las secuencias que seran alineadas con alineamiento multiple.
- OUT_FILE: Archivo en el donde se escribe el resultado de la consulta.

### Resultados
De la alineación podemos saber en que aminoacidos coincide la secuencia ya que estos estaran marcados con un asterisco. Esto nos permite ver en que partes de la secuencias tenemos los mismos lo cual indica que probablemente los que no se repitan en todas las secuencias no son de tanta importancia como los que si.