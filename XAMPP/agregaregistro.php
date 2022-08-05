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

<?php

if (isset($_POST)){
	echo("Recibidos datos via post");
}else
{
	echo("<article>No se recibieron datos de formulario.  Por favor vuelva a intentar.</article>");
	
};


