#!c:/euphoria/bin/eui.exe
include std/io.e
include std/math.e
without warning

constant iniciar_pagina = 
		"Content-type: text/html\n\n " &
		"<!DOCTYPE html>\n" &
		"<meta charset=\"utf-8\">\n" &
		"<html>\n" &
		"<head>\n" &
		"<title>Directorio</title>\n" &
		"<meta charset=\"utf-8\">\n" &
		"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n" &
		"<link rel=\"stylesheet\" href=\"/w3.css\">\n" &
		"</head>\n\n" &
		"<body>\n\n"

constant encabezado_pagina = 
		"<div class=\"w3-container w3-green\">\n " &
		"<a href=\"/\">Volver al inicio</a>" &
		"<h1>Ibague.info</h1>\n" &
		"<h2>Directorio</h2>Empresas del turismo, confección y otras en Ibagué\n" &
		"</div>\n\n" &
		"<div class=\"w3-row-padding w3-margin-top\">\n" 

function registro_arreglado(sequence registro)
	sequence salida =""
		for i=6 to length (registro) do
			if length(registro[i])>0 then
			salida = salida & registro[i] & "\n<br>"
			end if
		end for	
	return salida
end function

procedure imprime_registro(sequence registro)
		puts(1, "     <div class=\"w3-third\">\n" &
			"        <div class=\"w3-card-4\">\n" &
			"              <div class=\"w3-container\"\n>" )
			
		puts(1, "                  <h4>"& registro[3] &"</h4>\n")
		puts(1, registro_arreglado(registro))
		
		puts(1,"           </div>\n" &
		"        </div>\n" &
		"    </div>\n")
end procedure

procedure cierra_pagina()
		puts(1, "</div>\n" &
		"</body>" &
		"</html>\n")
end procedure



function tokenizar (sequence datos)
	sequence tokenizado = {}
	sequence registro ={{}} --El registro actualmente en construcción
	integer registroactual = 1
	integer campoactual = 1
	
	integer cadena =0 --No se está examinando una cadena

	for i=1 to length(datos) do --Para cada linea del archivo
		--registro = append(registro, {})
		for j=1 to length(datos[i]) do  --Para cada caracter de esa línea
			if cadena=0 then -- Si no hay cadena en proceso
				if datos[i][j]=',' then --Campo nuevo
					registro = append(registro, {})
					campoactual=campoactual+1
				elsif datos[i][j]='\"' then 
					cadena=1
					
				else
					puts(1,"Error: datos sin comillas")
					--abort(1)
				end if
			
			else  -- Si hay una cadena en proceso
				
				if datos[i][j]='\"' then -- Fin de la cadena
					cadena=0
				else
					registro[campoactual] = append(registro[campoactual] , datos[i][j] )
					--Añadir a la cadena el siguiente caracter
				end if
			end if
		end for
		tokenizado = append(tokenizado, registro)
		registro={{}}
		campoactual=1
		cadena=0
	end for

	return tokenizado
end function



function textos ()
-- Obtener datos de la base de datos
-- Ojo segun querystring filtrar los datos
	sequence database
	database = read_lines(".\\ansi.csv")
	database = tokenizar(database)
	return database
	--return {"primero", "segundo", "tercero"}
end function

procedure principal()
	sequence datos = ""
	
		datos= textos()
		puts(1, iniciar_pagina & encabezado_pagina)
		

		for i=2 to length(datos) do
			
			imprime_registro(datos[i])
			if mod(i-1, 3) = 0 then
				puts(1,"   </div>")
				puts(1,"   <div class=\"w3-row-padding w3-margin-top w3\">")
			end if
		end for

		cierra_pagina()
end procedure

principal()
abort(0)


--
--puts(1,"This is the environmental variable QUERY_STRING printed as Euphoria sequence.<br><br>")
--
--object a
--a=getenv("QUERY_STRING")         
--
--if atom(a) then 
--    a = ""
--end if
--
--puts(1,"<br><br>This is the environmental variable QUERY_STRING as text using puts()<br><br>")
--
--puts(1,a)
--
