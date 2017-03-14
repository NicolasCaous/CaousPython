<?php
	$conf = parse_ini_file("php.ini");

	$servername = $conf["servername"];
	$username = $conf["username"];
	$password = $conf["password"];
	$dbname = $conf["dbname"];

	// Cria conexão
	$conn = mysqli_connect($servername, $username, $password, $dbname);

	// Checa conexão
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 

	$agora = (new \DateTime())->format('Y-m-d H:i:s');
	$codigo = htmlspecialchars($_POST['codigo']);
	if($codigo == "") { $codigo = "NULL";} else { $codigo = "'$codigo'";}
	$tipo = htmlspecialchars($_POST['tipo']);
	if($tipo == "") { $tipo = "NULL";} else { $tipo = "'$tipo'";}
	$nome = htmlspecialchars($_POST['nome']);
	if($nome == "") { $nome = "NULL";} else { $nome = "'$nome'";}
	$quantidade = htmlspecialchars($_POST['quantidade']);
	if($quantidade == "") { $quantidade = "NULL";} else { $quantidade = "'$quantidade'";}
	$preco = str_replace(",",".",htmlspecialchars($_POST['preco']));
	if($preco == "") { $preco = "NULL";} else { $preco = "'$preco'";}
	$negocio = htmlspecialchars($_POST['negocio']);
	$sql = "INSERT INTO mercadoria VALUES ($codigo,$tipo,$nome,$quantidade,$preco,'$negocio', '$agora')";

	if ($conn->query($sql) === TRUE) {
		redirect("sucesso.html");
		exit();
	} else {
		redirect("falha.html");
		exit();
	}
	
	// Redirecionar para url
	function redirect($url) {
		if (headers_sent()) {
			die('<script type="text/javascript">window.location.href="' . $url . '";</script>');
		} else {
			header('Location: ' . $url);
			die();
		}    
	}
?>	