<!DOCTYPE html>
<meta charset="utf-8">
<html>
	<head>
		<link rel="stylesheet" href="style.css">
		<META NAME="keywords" CONTENT="empresas, manufactura, servicios, colombia"> 
		<META NAME="robots" CONTENT="all">
		<nav>Menu de opciones</nav>
	</head>
		
<body>

<main>

	<h1>QuienFabrica.co</h1>

<p>
<?php

if (isset($_POST["registro"]))	{
		$Registro = $_POST["registro"];
		
		echo("[Debug]Gracias por contactarnos.  Estos son los datos introducidos:<br>".$Registro."<br>"."Guardando registro...\n<br>");
		
		$archivoDatos = fopen ("c:web/cgi-bin/ansi.csv", "a") or die ("Error, no se pudo abrir archivo!!");
		fwrite($archivoDatos, $Registro);
		fclose($archivoDatos);
		
		
} else{
	echo("No recibido ningun registro");
}
	

?>

</main>
<footer><hr width=50%>Marco Antonio Achury 2022<br>
</footer>
</body>
</html>

</body></html>




