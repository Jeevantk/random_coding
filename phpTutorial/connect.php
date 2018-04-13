<?php

    define("DB_HOST", "localhost");
    define("DB_USER", "carpooling");
    define("DB_PASSWORD", "theeta");
    define("DB_DATABASE", "carpooling");

    $class_dir= "/home/jeevan/Documents/theeta/chinastreet/classes/";

    include_once($class_dir."functions.class.php");
    
    echo $class_dir;
    // $db = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);

    // echo "Connected Successfully\n";

?>