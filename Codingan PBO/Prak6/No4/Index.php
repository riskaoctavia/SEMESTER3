<!-- Nama   : Riska Octavia Arianto -->
<!-- NIM    : 21091397059 -->
<!-- Kelas  : D4 Manajemen Informatika 2021A -->
<!-- Praktikum 6 -->

<?php 
    require_once 'no4.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>        
    <title>Praktikum 6</title>
</head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" 
    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<body>
        <h2 class="text-center">Praktikum 6</h2>
        <div class="container">
  <div class="row">
  <h4 class="text-center">Soal 4</h4>
    <div >
                <h4>-----------------------------------</h4>
                <?= $riverBarge2->getMaxLoad(); ?> <br>
                <?= $riverBarge2->addBox(12000); ?> <br>
                <?= $riverBarge2->addBox(15000); ?> <br>
                <?= $riverBarge2->addBox(1000); ?> <br>
                <?= $riverBarge2->addBox(3000); ?> <br>
                <?= $riverBarge2->dock(); ?> <br>
                <?= $riverBarge2->cruise(); ?> <br>
                <?= $riverBarge2->calcFuelNeeds(); ?> <br>
    </div>
    <div>
                <h4>-----------------------------------</h4>
                <?= $seaPlane->getMaxLoad(); ?> <br>
                <?= $seaPlane->addBox(12000); ?> <br>
                <?= $seaPlane->addBox(8000); ?> <br>
                <?= $seaPlane->addBox(3000); ?> <br>
                <?= $seaPlane->dock(); ?> <br>
                <?= $seaPlane->cruise(); ?> <br>
                <?= $seaPlane->takeOff(); ?> <br>
                <?= $seaPlane->fly(); ?> <br>
                <?= $seaPlane->land(); ?> <br>
                <?= $seaPlane->calcFuelNeeds(); ?> <br>
    </div>
    <div>
                <h4>-----------------------------------</h4>
                <?= $helicopter->getMaxLoad(); ?> <br>
                <?= $helicopter->addBox(8000); ?> <br>
                <?= $helicopter->addBox(2000); ?> <br>
                <?= $helicopter->addBox(3000); ?> <br>
                <?= $helicopter->takeOff(); ?> <br>
                <?= $helicopter->fly(); ?> <br>
                <?= $helicopter->land(); ?> <br>
                <?= $helicopter->calcFuelNeeds(); ?> <br>
                <h4>-----------------------------------</h4>
    </div>
  </div>
</div>
</body>

</html>