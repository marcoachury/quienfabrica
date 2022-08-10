#!./eui
-- CSV2HTML
-- Version 1.1
-- Present data from a CSV file on a web page
--
-- Presenta los datos de un archivo CSV en forma de una 
-- pagina web donde cada registro se presenta en forma de una "tarjeta"
--
-- La primera version era lento para archivos grandes, porque primero procesa 
-- todo el archivo y genera la pagina.  Hasta no tenerlo procesado no 
-- manda al servidor los datos a imprimir.
--
-- La idea es que la proxima version mande al servidor los datos de cada 
-- registro una vez se procesa

--with trace

with batch
without warning

include std/search.e
include std/get.e
include std/wildcard.e
include std/io.e
include std/math.e
include std/text.e
include euphoria/info.e
include std/net/url.e

--trace(1)
-- USER MODIFICABLE CONSTANTS.  FEEL FREE TO CUSTOMIZE YOUR PAGE
-- Constantes modificables.  Se pueden usar para personalizar la pagina

constant FORM_URL = "/ModeloFormImagen/formnuevaempresa.html"
constant TITLE_FIELD = 3   -- Number of field (column) at CSV that will be used as article title
constant CSV_FILE_NAME = "ansi.csv"
constant PAGE_BEGIN= "Content-type: text/html\n\n" & --Keep this part
		"<!DOCTYPE html>\n<meta charset=\"utf-8\">\n" & 
		"<html>\n<head><link rel=\"stylesheet\" href=\"/style.css\">\n" & --Is important to check CSS File
		"<META NAME=\"keywords\" CONTENT=\"empresas, manufactura, servicios, colombia\">" & 
		"<META NAME=\"robots\" CONTENT=\"all\"></head> "
constant PAGE_BODY ="<body><h1>QuienFabrica.co</h1>\n<h2>Directorio</h2><p>Empresas de manufactura y servicios en Colombia</p><a href='" & FORM_URL & "'>Agregar mi empresa (en construccion)</a></div>"
constant SEARCH_FORM = "<center><form align='center' method='post' action='/cgi-bin/pruebadb.cgi'>\n <input type='text' name='cadena'> <input type='submit' value='Buscar'></form></center>"
constant formAgregar = "<form method='post' action= '/cgi-bin/pruebadb.cgi'> \n <input type = 'text' name='cadena'> <input type = 'submit' value ='Buscar'></form><br><br>"
constant PAGE_FOOT = "</main><hr width=50%><footer>Marco Antonio Achury 2022<br>Running on Euphoria " & 
		version_string() &  "aáeé</footer>"          
constant PAGE_END= "</body>\n</html>\n\n"

--END OF USER MODIFICABLE CONSTANTS. Fin de las constantes modificables

procedure UserError(sequence msg)
-- Report fatal error
    puts(1, "<p>Error: " & msg & "\n<br>" & PAGE_FOOT & PAGE_END)
	--Write to error log??
    abort(0)
end procedure

function getPost()
	sequence key, content, pairs
    object nbytes
	object env
	object query
    --integer filled_in, dollar
	env = upper(getenv("REQUEST_METHOD"))
    if equal(env, "POST") then
		nbytes = getenv("CONTENT_LENGTH")
		if atom(nbytes) then
			UserError("read_input - no CONTENT_LENGTH")
		end if
		nbytes = value(nbytes)
		if nbytes[1] = GET_SUCCESS then
			nbytes = nbytes[2]
		else
			UserError("read_input - bad CONTENT_LENGTH")
		end if
		query = get_bytes(0, nbytes)
		return query
	else
		return ""
	end if
end function

procedure registro_arreglado(sequence registro) 
	sequence salida =""
		for i=3 to length (registro) do
			if length(registro[i])>0 then
				if i = 12 then
					puts(1, "<a target=\"_blank\" href=\"http://" & registro[i] & "\">Ver Web</a><br>\n")
				else
					puts(1, registro[i] & "<br>\n")
				end if
			end if
		end for
end procedure

procedure imprime_registro(sequence registro)                   
		puts(1, "<article><h4>" & registro[TITLE_FIELD] & "</h4>")
		registro_arreglado(registro)
		puts(1, "</article>\n")
		flush(1)
end procedure

function tokenizar (sequence datos) 
--Recibe un registro (sequencia de texto en formato CSV) y lo separa formando una sequencia de sequencias
-- La version antigua tokenizaba el archivo completo. Recibía y devolvía una sequencia de sequencias. 
--Esta nueva version tokeniza una linea a la vez, por lo tanto solo solo recibe una linea de texto, decuelve una secuencia de secuencias.
	sequence tokenizado = {}
	sequence registro ={{}} --El registro actualmente en construcción
	integer campoactual = 1
	integer cadena =0 --No se está examinando una cadena
	if equal(datos, "") then
		UserError("La funcion tokenizar no puede recibir cadenas vacias")
	end if

	for j=1 to length(datos) do  --Para cada caracter de esa línea
		if cadena=0 then -- Si no hay cadena en proceso
			if equal(datos[j], ',') then --Campo vacío
				registro = append(registro, {})
				campoactual=campoactual+1
			elsif equal(datos[j], '"') then --Empieza campo nuevo
				cadena=1
			end if
		else  -- Si hay una cadena en proceso
			if datos[j]='"' then -- Fin de la cadena
				cadena=0 --Terminó la cadena
			else
				registro[campoactual] = append(registro[campoactual] , datos[j] ) --Añadir a la cadena el siguiente caracter                                
			end if
		end if
	end for
		--tokenizado = append(tokenizado, registro)
		campoactual=1
		cadena=0
	return registro
end function

function upper_SP(sequence texto)
	sequence salida
	if equal(texto, "") then
		return ""
	end if
--      texto =  upper(texto)  
	sequence MINUSCULAS = "ñáÁéÉíÍóÓúÚüÜ"
	sequence MAYUSCULAS = "ÑAAEEIIOOUUUU"
	for j=1 to 13 do
		for k=1 to length(texto) do
			if equal(texto[k],MINUSCULAS[j]) then
				texto[k]=MAYUSCULAS[j]
			else 
				texto[k] = upper(texto[k])  
				--Terriblemente lento! Hay que hacerlo mas eficiente
			end if
		end for 
	end for
	return texto
end function

function textos (sequence patron)
-- Obtener datos de la base de datos
-- Ojo segun patron filtrar los datos
-- Devuelve el numero de coincidencias
	object database
	sequence salida
	integer cuantos = 0
	integer ArchivoAbierto
	--Carga la base de datos a la memoria
	database=read_lines(CSV_FILE_NAME)
	--Aca se filtra?? Antes de tokenizar
	if atom(database) then  --read_lines devuelve -1 si no encontró el arhivo 
		UserError("Archivo de datos no encontrado!!!!!<br>")
	else --Todo bien?
		if not equal(patron, "") then
			sequence PatronMayuscula = upper_SP((patron))
			puts(1, "PatronMayuscula = " & PatronMayuscula & "<br>")
			for i=2 to length (database) do
				if match(PatronMayuscula, upper_SP(database[i])) then
					cuantos=cuantos+1
				salida=tokenizar(database[i])
				imprime_registro(salida)
				end if
			end for
		else -- patron == "" => Imprimir todo
			for i=2 to length(database) do
				cuantos=cuantos+1
				salida=tokenizar(database[i])
				imprime_registro(salida)
			end for
		end if 	
	end if	
	return cuantos
end function

procedure ImprimeSeccionMain()
	object busqueda
	sequence datos, patron
	integer coincidencias = 0
	busqueda=getPost() --Buscar casilla de busqueda
	patron=""
	if length(busqueda) > 7 then  --Se supone que los 7 primeros caracteres son "cadena="
		patron = busqueda[8..$]
		patron = url:decode(patron)
	end if  
	-- datos= textos(patron) -- Antes pasaba todo el arreglo
	  --Ahora solo pasa la linea con el registro a evaluar
	puts(1, "<main>")
	coincidencias = textos(patron)  --Busca e imprime los registros, devuelve coincidencias
	puts(1, "</main>")
	if coincidencias > 1 then
		printf(1,"<p>Encontradas %d coincidencias" ,{coincidencias})
	else
		puts(1, "<p>No se encontraron coincidencias para " & patron & "</p>") 
	end if
end procedure

procedure principal()
	puts(1, PAGE_BEGIN)
	puts(1, PAGE_BODY)
	puts(1, SEARCH_FORM)
	ImprimeSeccionMain()  --Print database records: Aca es donde todo ocurre
	puts(1, PAGE_FOOT)
	puts(1, PAGE_END)      
end procedure

-- main()
principal()
abort(0)
