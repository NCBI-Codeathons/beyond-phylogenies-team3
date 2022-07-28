<?php
    $ds = DIRECTORY_SEPARATOR;

    $storeFolder = dirname( __DIR__ ).'/uploads/';

      if (!empty($_FILES)) {

          $tempFile = $_FILES['file']['tmp_name'];

          //$targetPath =  $storeFolder; // <-- we don't need this line anymore

          $targetFile =  $storeFolder . $_FILES['file']['name'];

          die($targetFile); // <-- just debug if your filename is correct and if you ever reach this point.

       }

?>
