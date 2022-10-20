<!-- Nama   : Riska Octavia Arianto -->
<!-- NIM    : 21091397059 -->
<!-- Kelas  : D4 Manajemen Informatika 2021A -->
<!-- Praktikum 5 -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Praktikum 5</title>
</head>
<body>
    <div class="container">
        <h2>Soal 2</h2>

        <!-- Program PHP -->
        <?php
class Pegawai
{
	public  $nama;
	public $gaji;
	public	function __construct($nama, $gaji)
	{
		$this->nama = $nama;
		$this->gaji = $gaji;
	}
	public	function infoGaji()
	{
		return $this->gaji;
	}
}
class Manajer extends Pegawai
{
	private $tunjangan;
	public	function __construct($nama, $gaji, $tunjangan)
	{
		parent::__construct($nama, $gaji);
		$this->tunjangan = $tunjangan;
	}
	public	function infoGaji()
	{
		return $this->gaji;
	}
	public	function infoTunjangan()
	{
		return $this->tunjangan;
	}
}
class Programmer extends Pegawai
{
	private $bonus;
	public	function __construct($nama, $gaji, $bonus)
	{
		parent::__construct($nama, $gaji);
		$this->bonus = $bonus;
	}
	public	function infoGaji()
	{
		return $this->gaji;
	}
	public	function infoBonus()
	{
		return $this->bonus;
	}
}
class Bayaran
{
	public function hitungBayaran($peg)
	{
		$uang = $peg->infoGaji();
		
		return $uang;
	}
	public static function main($args)
	{
		$man = new Manajer("Agus", 10000000, 5000000);
		$prog = new Programmer("Bambang", 4600000, 3000000);
		$hr = new Bayaran();
		echo "<br> <br> Nama Manajer : ". $man->nama, "\n";
        echo "<br> Gaji : Rp. ".strval($hr->hitungBayaran($man)), "\n";
		echo "<br> <br> Nama Programmer : ".$prog->nama, "\n";
        echo "<br> Gaji : Rp. ".strval($hr->hitungBayaran($prog)), "\n";
        echo "<br> <br> <br> <br> <center> by : Riska Octavia Arianto (21091397059) </center> ";
        // echo $man->nama;
	}
}
Bayaran::main(array());
        ?>
        <!-- END PHP  -->
    </div>
</body>
</html>