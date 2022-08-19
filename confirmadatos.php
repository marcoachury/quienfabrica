<!DOCTYPE html>
<meta charset="utf-8">
<html>
	<head>
		<link rel="stylesheet" href="/style.css">
		<META NAME="keywords" CONTENT="empresas, manufactura, servicios, colombia"> 
		<META NAME="robots" CONTENT="all">
		<nav>Menu de opciones</nav>
	</head>
		
<body>
<h1>QuienFabrica.co</h1>

Gracias por contactarnos.  Estos son los datos introducidos, por favor verifique todo antes de guardar.
<?php

$Registro = '","","';  #cATEGORIA Y SUBCATEGORIA POR DEFINIR

if (isset($_POST["nombre"]))	{echo ("\n<br>Nombre del negocio: ".$_POST["nombre"]); $Registro = '"'.$Registro.$_POST["nombre"].'","';}
if (isset($_POST["contacto1"]))	{echo ("\n<br>Persona contacto 1: ".$_POST["contacto1"]); $Registro = $Registro.$_POST["contacto1"].'","';}
if (isset($_POST["contacto2"]))	{echo ("\n<br>Persona contacto 2: ".$_POST["contacto2"]); $Registro = $Registro.$_POST["contacto2"].'","';}
if (isset($_POST["departamento"])){echo	("\n<br>Departamento: "	.$_POST["departamento"]); $Registro = $Registro.$_POST["departamento"].'","';}
if (isset($_POST["ciudad"]))	{echo ("\n<br>Ciudad: "	.$_POST["ciudad"]); $Registro = $Registro.$_POST["ciudad"].'","';}
if (isset($_POST["barrio"]))	{echo ("\n<br>Barrio: "	.$_POST["barrio"]); $Registro = $Registro.$_POST["barrio"].'","';}
if (isset($_POST["direccion"]))	{echo ("\n<br>Direccion: ".$_POST["direccion"]); $Registro = $Registro.$_POST["direccion"].'","';}
if (isset($_POST["puntoReferencia"])){echo	("\n<br>Punto de referencia: ".$_POST["puntoReferencia"]); $Registro = $Registro.$_POST["puntoReferencia"].'","';}
if (isset($_POST["web"]))		{echo ("\n<br>Pagina web: ".$_POST["web"]); $Registro = $Registro.$_POST["web"].'","';}
if (isset($_POST["email1"]))	{echo ("\n<br>email principal: ".$_POST["email1"]); $Registro = $Registro.$_POST["email1"].'","';}
if (isset($_POST["email2"]))	{echo ("\n<br>email secundario: ".$_POST["email2"]); $Registro = $Registro.$_POST["email2"].'","';}
if (isset($_POST["facebook"]))	{echo ("\n<br>Facebook: ".$_POST["facebook"]); $Registro = $Registro.$_POST["facebook"].'","';}
if (isset($_POST["instagram"]))	{echo ("\n<br>Instagram: ".$_POST["instagram"]); $Registro = $Registro.$_POST["instagram"].'","';}
if (isset($_POST["twitter"]))	{echo ("\n<br>Twitter: ".$_POST["twitter"]); $Registro = $Registro.$_POST["twitter"].'","';}
if (isset($_POST["tiktok"]))	{echo ("\n<br>TikTok: ".$_POST["tiktok"]); $Registro = $Registro.$_POST["tiktok"].'","';}
if (isset($_POST["telefono1"]))	{echo ("\n<br>Telefono principal: ".$_POST["telefono1"]); $Registro = $Registro.$_POST["telefono1"].'","';}
if (isset($_POST["telefono2"]))	{echo ("\n<br>Telefono secundario: ".$_POST["telefono2"]); $Registro = $Registro.$_POST["telefono2"].'","';}
if (isset($_POST["whatsapp"]))	{echo ("\n<br>numero WhatsApp: ".$_POST["whatsapp"]); $Registro = $Registro.$_POST["whatsapp"].'"';}

/* El $Registro puede contener dobles comillas ¿Eliminarlas? */

echo("\n<br><br>[DEBUG]El registro es: ".$Registro."\n<br>");  
# Solo para debug, esto no debería presentarse al usuario
?>
<form action="agregaregistro.php" method="POST" enc="application/x-www-form-urlencoded">
	<input type="hidden" name="registro" value = '<?php echo($Registro);?>'>
	<input type="hidden" name="nombre" value = '<?php echo($_POST["nombre"]);?>'>
	
	
	Confirmado, quiero guardar los datos <input type ="submit" >
</form>
<br><br>
<form action="formnuevaempresa.html" method="POST">
	Regresar al formulario 
<input type = "submit">
</form>
<br><br>
</main>
<footer><hr width=50%>Marco Antonio Achury 2022<br>
</footer>
</body>
</html>

</body></html>


