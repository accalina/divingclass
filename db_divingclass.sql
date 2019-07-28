-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2019 at 06:23 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_divingclass`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `userid` int(3) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` text NOT NULL,
  `fullname` text NOT NULL,
  `level` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`userid`, `username`, `password`, `fullname`, `level`) VALUES
(1, 'accalina', '$2b$12$oOL/jDP75o6CGhXh/8py8e8Frg2vZ5UBv7JIaSHqSi9sNWaxqy.02', 'Accalina Shirosachi', 1),
(2, 'didit', '$2b$12$vY88mU.SVmfLtWJHh/.XIOpotdNAfitGAKvuceRxJiCgBt3Tnxn5G', 'Didit Nugroho', 1),
(3, 'admin', '$2b$12$S.1MOFjtLnB66Ayhvp6b1OaXUEs.Z2SC3aE1wqFeO/EZeb79HZD8C', 'Administrator', 9);

-- --------------------------------------------------------

--
-- Table structure for table `module_access`
--

CREATE TABLE `module_access` (
  `no` int(3) NOT NULL,
  `userid` int(3) NOT NULL,
  `module` varchar(6) NOT NULL,
  `active` int(1) NOT NULL,
  `payment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `module_access`
--

INSERT INTO `module_access` (`no`, `userid`, `module`, `active`, `payment`) VALUES
(1, 1, 'bab1', 1, '1_bab1_bukti-pembayaran_03-36-41.png'),
(2, 1, 'bab2', 1, '1_bab2_bukti-pembayaran_03-40-08.jpg'),
(3, 1, 'bab3', 1, '1_bab3_bukti-pembayaran_04-06-07.png'),
(4, 1, 'bab4', 1, '1_bab4_bukti-pembayaran_11-09-08.jpg'),
(5, 1, 'bab5', 1, '1_bab5_bukti-pembayaran_11-09-43.jpg'),
(6, 1, 'bab6', 1, '1_bab6_bukti-pembayaran_11-09-49.jpg'),
(7, 1, 'final', 1, '1_final_bukti-pembayaran_11-09-54.gif'),
(8, 2, 'bab1', 1, '2_bab1_bukti-pembayaran_09-41-15.jpg'),
(9, 2, 'bab2', 1, '2_bab2_bukti-pembayaran_09-42-11.jpg'),
(10, 2, 'bab3', 0, '...'),
(11, 2, 'bab4', 0, '...'),
(12, 2, 'bab5', 0, '...'),
(13, 2, 'bab6', 0, '...'),
(14, 2, 'final', 0, '...');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `no` int(11) NOT NULL,
  `question` text NOT NULL,
  `opt1` text NOT NULL,
  `opt2` text NOT NULL,
  `opt3` text NOT NULL,
  `opt4` text NOT NULL,
  `ans` text NOT NULL,
  `module` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`no`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `ans`, `module`) VALUES
(1, '_________ yang terpasang pada masker digunakan untuk menyetarakan tekanan dalam telinga dan sinus.', 'Lensa Masker', 'Strap', 'Nose Pockets', 'Positive Locking Device', 'Nose Pockets', 'bab1'),
(2, 'Air menyerap panas tubuh _____ kali lebih cepat daripada udara.', '25', '15', '40', '20', '25', 'bab1'),
(3, 'Sebuah _______ adalah salah satu pertimbangan yang paling penting dalam memilih pakaian selam basah.', 'ketebalan', 'fitur-fitur pakaian', 'ukuran yang pas', 'bahan', 'ukuran yang pas', 'bab1'),
(4, 'Kebanyakan penyelaman rekreasi dilakukan pada suhu antara 50? F - 80? F. Pencakupan dan ketebalan pakaian selam dapat dipilih sesuai dengan suhu ekstrim panas atau dingin di antara angka tersebut, tetapi umumnya disepakati bahwa pakaian selam basah lengkap harus dipakai pada suhu _______.', '75F - 90F', '55F - 70F', '40F - 50F', '65F - 80F', '65F - 80F', 'bab1'),
(5, 'Tidak ada alasan kehabisan udara Para penyelam diperlengkapi dengan ________ untuk memantau persediaan udara mereka.', 'Tabung', 'Submersible Pressure Gauge', 'Buoyancy Compensator Device', 'Regulator', 'Submersible Pressure Gauge', 'bab1'),
(6, 'Singkatan dari S.C.U.B.A adalah __________', 'Self Contained Underwater Buoyancy Apparatus', 'Self Condition Underwater Best Apparatus', 'System Contained Underwater Breathing Apparatus', 'Self Contained Underwater Breathing Apparatus', 'Self Contained Underwater Breathing Apparatus', 'bab1'),
(7, 'Menggunakan sebuah _______ memberikan banyak manfaat untuk seorang penyelam daripada alat ukur analog biasa dan tabel selam.', 'Dive Computer', 'Submersible Pressure Gauge', 'Fin', 'Masker', 'Dive Computer', 'bab1'),
(8, 'Pada waktu menggunakan tombol pengendali manual, tarik _______ sampai titik terpanjang untuk mendapatkan efisiensi terbesar dalam pengempisan.', 'Low Pressure Inflator', 'Tali penyetel', 'Katup pembuang', 'Selang Pemompa', 'Katup pembuang', 'bab1'),
(9, 'Anda mungkin mempertimbangkan untuk menggunakan ________ di perairan yang bersuhu di bawah 65? F (16? C).', 'Pakaian Selam Kering', 'Boot', 'Pakaian Selam Basah', 'Bagasi Penyelam', 'Pakaian Selam Kering', 'bab1'),
(10, 'Katup Deutsches Industrie Normen (DIN) digunakan pada tabung yang berkapasitas lebih dari _______ psi.', '4000', '3000', '2500', '2000', '3000', 'bab1'),
(11, 'Permukaan planet ini sesungguhnya hanya terdiri dari sedikit daratan. Kenyataannya planet ini terdiri dari _____ air.', '0.85', '0.5', '0.72', '0.65', '0.72', 'bab2'),
(12, 'Diperkirakan bahwa produksi tumbuh-tumbuhan di lautan mungkin _____ kali lebih banyak daripada di daratan. Lebih dari ______ oksigen dihasilkan oleh tumbuhan laut.', '20, 85%', '10, 85%', '5, 50%', '20, 40%', '10, 85%', 'bab2'),
(13, 'Bintang laut, brittle stars, bulu babi, sand dollars dan timun laut/teripang, semuanya termasuk dalam anggota kelompok hewan yang dikenal sebagai _______.', 'Moluska', 'Crustaceans', 'Coral', 'Echinodermata', 'Echinodermata', 'bab2'),
(14, 'Kapanpun gelombang mencapai garis tepi pantai, air harus kembali ke laut. Air yang kembali menciptakan sebuah ______ .', 'Longshore Current', 'Back Current', 'Surf', 'Surge', 'Back Current', 'bab2'),
(15, 'Penyelam bawah air mengalami _____, gerakan air yang maju dan mundur yang disebabkan oleh ernergi gelombang', 'Surge', 'Surf', 'Longshore Current', 'Back Current', 'Surge', 'bab2'),
(16, 'Apa yang dimaksud dengan Termoklin?', 'Gelombang pasang yang bergerak melewati permukaan bumi', 'Batas antara lapisan-lapisan dari berbagai suhu pada air', 'Gelombang pasang surut', 'Gelombang Seismik', 'Batas antara lapisan-lapisan dari berbagai suhu pada air', 'bab2'),
(17, 'Manakah yang termasuk dalam Cephalopoda?', 'Sea Fan', 'Lobster', 'Glasseye', 'Cumi-cumi', 'Cumi-cumi', 'bab2'),
(18, 'Manakah yang termasuk ke dalam jenis Hiu tidak agresif?', 'Hammerhead', 'Sand Shark', 'Great White', 'Tiger Shark', 'Sand Shark', 'bab2'),
(19, 'Manakah yang tidak termasuk dalam Pari penyengat?', 'Pari kupu-kupu', 'Pari manta', 'Pari kelelawar', 'Pari bulat', 'Pari manta', 'bab2'),
(20, 'Berikut merupakan jenis-jenis Hard Coral, kecuali_____', 'Fire Coral', 'Elkhorn Coral', 'Staghorn Coral', 'Sea Fan', 'Sea Fan', 'bab2'),
(21, 'Jumlah waktu yang digunakan dari awal anda turun (descent) hingga waktu anda mulai naik (ascent) langsung ke permukaan disebut?', 'Residual Time', 'Total Time', 'Bottom Time', 'Surface Interval', 'Bottom Time', 'bab3'),
(22, 'Jika anda melakukan penyelaman hingga 15 meter selama 30 menit. Apa kode huruf untuk penentuan kelompok (Group Designation Letter) anda?', 'B', 'E', 'D', 'C', 'E', 'bab3'),
(23, 'Bagaimana cara menghitung Total Time?', 'Bottom Time - Residual Time', 'Bottom Time + Residual Time', 'Bottom Time / Residual Time', 'Bottom Time x Residual Time', 'Bottom Time + Residual Time', 'bab3'),
(24, 'Setelah melakukan penyelaman, anda tidak diperkenankan untuk berada di ketinggian di atas ________ selama ______.', '2400 meter, 24 jam', '3000 meter, 2 jam', '1500 meter, 10 jam', '2000 meter, 5 jam', '2400 meter, 24 jam', 'bab3'),
(25, 'Selain mencatat jumlah penyelaman, ________ anda merupakan sumber informasi penting untuk penyelaman selanjutnya, untuk menyimpan catatan pelatihan anda.', 'Submersible Pressure Gauge', 'Buoyancy compensator', 'Dive Computer', 'Dive Table', 'Dive Computer', 'bab3'),
(26, 'Jumlah waktu yang diperlukan seorang penyelam di luar air atau di permukaan air diantara beberapa penyelaman disebut?', 'Bottom Time', 'Decompression Stop', 'Total Time', 'Surface Interval', 'Surface Interval', 'bab3'),
(27, 'Jika pada penyelaman pertama anda termasuk dalam kelompok E, maka berapa batas waktu non dekompresi jika pada penyelaman berikutnya anda ingin menyelam di kedalaman 12 meter?', '81 menit', '30 menit', '50 menit', '120 menit', '81 menit', 'bab3'),
(28, 'Titik terdalam yang anda capai dalam sebuah penyelaman, tanpa memperdulikan seberapa singkatnya anda berada di kedalaman tersebut di sebut?', 'Bottom Time', 'non decompression dive', 'Depth', 'Pressure', 'Depth', 'bab3'),
(29, 'Penyelaman apapun yang dimulai lebih dari _______ menit dan kurang dari _______ jam setelah penyelaman scuba yang sebelumnya disebut sebagai penyelaman berulang.', '5, 24', '10, 12', '30, 12', '20, 10', '10, 12', 'bab3'),
(30, 'Residual Time didefinisikan sebagai tekanan ________ berlebih yang masih tersisa di dalam tubuh penyelam pada awal penyelaman berulang.', 'Oksigen', 'Karbon Dioksida', 'Emboli', 'Nitrogen', 'Nitrogen', 'bab3'),
(31, 'Permukaan planet ini sesungguhnya hanya terdiri dari sedikit daratan. Kenyataannya planet ini terdiri dari _____ air.', '85%', '50%', '72%', '65%', '72%', 'bab4'),
(32, 'Diperkirakan bahwa produksi tumbuh-tumbuhan di lautan mungkin _____ kali lebih banyak daripada di daratan. Lebih dari ______ oksigen dihasilkan oleh tumbuhan laut.', '20, 85%', '10, 85%', '5, 50%', '20, 40%', '10, 85%', 'bab4'),
(33, 'Bintang laut, brittle stars, bulu babi, sand dollars dan timun laut/teripang, semuanya termasuk dalam anggota kelompok hewan yang dikenal sebagai _______.', 'Moluska', 'Crustaceans', 'Coral', 'Echinodermata', 'Echinodermata', 'bab4'),
(34, 'Kapanpun gelombang mencapai garis tepi pantai, air harus kembali ke laut. Air yang kembali menciptakan sebuah ______ .', 'Longshore Current', 'Back Current', 'Surf', 'Surge', 'Back Current', 'bab4'),
(35, 'Penyelam bawah air mengalami _____, gerakan air yang maju dan mundur yang disebabkan oleh ernergi gelombang', 'Surge', 'Surf', 'Longshore Current', 'Back Current', 'Surge', 'bab4'),
(36, 'Apa yang dimaksud dengan Termoklin?', 'Gelombang pasang yang bergerak melewati permukaan bumi', 'Batas antara lapisan-lapisan dari berbagai suhu pada air', 'Gelombang pasang surut', 'Gelombang Seismik', 'Batas antara lapisan-lapisan dari berbagai suhu pada air', 'bab4'),
(37, 'Manakah yang termasuk dalam Cephalopoda?', 'Sea Fan', 'Lobster', 'Glasseye', 'Cumi-cumi', 'Cumi-cumi', 'bab4'),
(38, 'Manakah yang termasuk ke dalam jenis Hiu tidak agresif?', 'Hammerhead', 'Sand Shark', 'Great White', 'Tiger Shark', 'Sand Shark', 'bab4'),
(39, 'Manakah yang tidak termasuk dalam Pari penyengat?', 'Pari kupu-kupu', 'Pari manta', 'Pari kelelawar', 'Pari bulat', 'Pari manta', 'bab4'),
(40, 'Berikut merupakan jenis-jenis Hard Coral, kecuali_____', 'Fire Coral', 'Elkhorn Coral', 'Staghorn Coral', 'Sea Fan', 'Sea Fan', 'bab4'),
(41, 'Berapakah syarat usia untuk mendapatkan Junior Certification?', '10-11 tahun', '12-15 tahun', '5-10 tahun', '10-12 tahun', '12-15 tahun', 'bab5'),
(42, 'Berikut merupakan tiga jenis SSI Continuing Education Ratings, kecuali___', 'Speciality Diver', 'Advanced Open Water Diver', 'Advanced Adventurer', 'Master Diver', 'Advanced Adventurer', 'bab5'),
(43, 'Berapakah kali penyelaman yang dibutuhkan untuk mengikuti jenjang Speciality Diver?', '50 kali', '12 kali', '100 kali', '24 kali', '12 kali', 'bab5'),
(44, 'Berapakah batas kedalaman bagi seorang Open water Diver saat melakukan penyelaman?', '30 meter', '20 meter', '10 meter', '18 meter', '18 meter', 'bab5'),
(45, 'Manakah yang tidak termasuk dalam komponen dari program pengalaman SSI?', 'SSI Total DiveLog', 'SSI Level of Experience Decals', 'SSI Levels of Recognition', 'Cap timbul SSI', 'SSI Levels of Recognition', 'bab5'),
(46, 'Berapa kali penyelaman yang dibutuhkan untuk mendapatkan Platinum Pro Divers?', '100 kali', '500 kali', '50 kali', '5000 kali', '5000 kali', 'bab5'),
(47, 'Ada berapa tingkatan instruktur dalam SSI ?', '3', '5', '4', '2', '5', 'bab5'),
(48, 'Manakah yang tidak termasuk dalam SSI Diamond Diver ?', 'Knowledge', 'Experience', 'Equipment', 'Safety', 'Safety', 'bab5'),
(49, 'Berapakah rentang usia untuk bisa mendapatkan Special Junior Certification ?', '10-11 tahun', '10-15 tahun', '5-10 tahun', '15-17 tahun', '10-11 tahun', 'bab5'),
(50, 'Manakah yang merupakan kegiatan yang dilakukan sebelum penyelamannya ?', 'Safety Stop', 'Decompression Stop', 'Pre Dive Safety Check', 'Giant Stride', 'Pre Dive Safety Check', 'bab5'),
(51, '_________ yang terpasang pada masker digunakan untuk menyetarakan tekanan dalam telinga dan sinus.', 'Lensa Masker', 'Strap', 'Nose Pockets', 'Positive Locking Device', 'Nose Pockets', 'bab6'),
(52, 'Air menyerap panas tubuh _____ kali lebih cepat daripada udara.', '25', '15', '40', '20', '25', 'bab6'),
(53, 'Sebuah _______ adalah salah satu pertimbangan yang paling penting dalam memilih pakaian selam basah.', 'ketebalan', 'fitur-fitur pakaian', 'ukuran yang pas', 'bahan', 'ukuran yang pas', 'bab6'),
(54, 'Kebanyakan penyelaman rekreasi dilakukan pada suhu antara 50? F - 80? F. Pencakupan dan ketebalan pakaian selam dapat dipilih sesuai dengan suhu ekstrim panas atau dingin di antara angka tersebut, tetapi umumnya disepakati bahwa pakaian selam basah lengkap harus dipakai pada suhu _______.', '75F - 90F', '55F - 70F', '40F - 50F', '65F - 80F', '65F - 80F', 'bab6'),
(55, 'Tidak ada alasan kehabisan udara Para penyelam diperlengkapi dengan ________ untuk memantau persediaan udara mereka.', 'Tabung', 'Submersible Pressure Gauge', 'Buoyancy Compensator Device', 'Regulator', 'Submersible Pressure Gauge', 'bab6'),
(56, 'Singkatan dari S.C.U.B.A adalah __________', 'Self Contained Underwater Buoyancy Apparatus', 'Self Condition Underwater Best Apparatus', 'System Contained Underwater Breathing Apparatus', 'Self Contained Underwater Breathing Apparatus', 'Self Contained Underwater Breathing Apparatus', 'bab6'),
(57, 'Menggunakan sebuah _______ memberikan banyak manfaat untuk seorang penyelam daripada alat ukur analog biasa dan tabel selam.', 'Dive Computer', 'Submersible Pressure Gauge', 'Fin', 'Masker', 'Dive Computer', 'bab6'),
(58, 'Pada waktu menggunakan tombol pengendali manual, tarik _______ sampai titik terpanjang untuk mendapatkan efisiensi terbesar dalam pengempisan.', 'Low Pressure Inflator', 'Tali penyetel', 'Katup pembuang', 'Selang Pemompa', 'Katup pembuang', 'bab6'),
(59, 'Anda mungkin mempertimbangkan untuk menggunakan ________ di perairan yang bersuhu di bawah 65? F (16? C).', 'Pakaian Selam Kering', 'Boot', 'Pakaian Selam Basah', 'Bagasi Penyelam', 'Pakaian Selam Kering', 'bab6'),
(60, 'Katup Deutsches Industrie Normen (DIN) digunakan pada tabung yang berkapasitas lebih dari _______ psi.', '4000', '3000', '2500', '2000', '3000', 'bab6'),
(61, 'Berapakah syarat usia untuk mendapatkan Junior Certification?', '10-11 tahun', '12-15 tahun', '5-10 tahun', '10-12 tahun', '12-15 tahun', 'final'),
(62, 'Berikut merupakan tiga jenis SSI Continuing Education Ratings, kecuali___', 'Speciality Diver', 'Advanced Open Water Diver', 'Advanced Adventurer', 'Master Diver', 'Advanced Adventurer', 'final'),
(63, 'Berapakah kali penyelaman yang dibutuhkan untuk mengikuti jenjang Speciality Diver?', '50 kali', '12 kali', '100 kali', '24 kali', '12 kali', 'final'),
(64, 'Berapakah batas kedalaman bagi seorang Open water Diver saat melakukan penyelaman?', '30 meter', '20 meter', '10 meter', '18 meter', '18 meter', 'final'),
(65, 'Manakah yang tidak termasuk dalam komponen dari program pengalaman SSI?', 'SSI Total DiveLog', 'SSI Level of Experience Decals', 'SSI Levels of Recognition', 'Cap timbul SSI', 'SSI Levels of Recognition', 'final'),
(66, 'Berapa kali penyelaman yang dibutuhkan untuk mendapatkan Platinum Pro Divers?', '100 kali', '500 kali', '50 kali', '5000 kali', '5000 kali', 'final'),
(67, 'Ada berapa tingkatan instruktur dalam SSI ?', '3', '5', '4', '2', '5', 'final'),
(68, 'Manakah yang tidak termasuk dalam SSI Diamond Diver ?', 'Knowledge', 'Experience', 'Equipment', 'Safety', 'Safety', 'final'),
(69, 'Berapakah rentang usia untuk bisa mendapatkan Special Junior Certification ?', '10-11 tahun', '10-15 tahun', '5-10 tahun', '15-17 tahun', '10-11 tahun', 'final'),
(70, 'Manakah yang merupakan kegiatan yang dilakukan sebelum penyelamannya ?', 'Safety Stop', 'Decompression Stop', 'Pre Dive Safety Check', 'Giant Stride', 'Pre Dive Safety Check', 'final');

-- --------------------------------------------------------

--
-- Table structure for table `resource`
--

CREATE TABLE `resource` (
  `module` varchar(10) NOT NULL,
  `name` varchar(25) NOT NULL,
  `url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `resource`
--

INSERT INTO `resource` (`module`, `name`, `url`) VALUES
('bab1', 'Modul Bab 1', '/static/books/bab1.pdf'),
('bab2', 'Modul Bab 2', '/static/books/bab2.pdf'),
('bab3', 'Modul Bab 3', '/static/books/bab3.pdf'),
('bab4', 'Modul Bab 4', '/static/books/bab4.pdf'),
('bab5', 'Modul Bab 5', '/static/books/bab5.pdf'),
('bab6', 'Modul Bab 6', '/static/books/bab6.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `no` int(3) NOT NULL,
  `userid` int(3) NOT NULL,
  `reviewdata` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `scores`
--

CREATE TABLE `scores` (
  `no` int(3) NOT NULL,
  `userid` int(3) NOT NULL,
  `module` varchar(12) NOT NULL,
  `testscore` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scores`
--

INSERT INTO `scores` (`no`, `userid`, `module`, `testscore`) VALUES
(1, 1, 'bab1', 10),
(2, 1, 'bab2', 10),
(3, 1, 'bab3', 10),
(4, 1, 'bab4', 10),
(5, 1, 'bab5', 10),
(6, 1, 'bab6', 10),
(7, 1, 'final', 0),
(8, 2, 'bab1', 9),
(9, 2, 'bab2', 4),
(10, 2, 'bab3', 0),
(11, 2, 'bab4', 0),
(12, 2, 'bab5', 0),
(13, 2, 'bab6', 0),
(14, 2, 'final', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `module_access`
--
ALTER TABLE `module_access`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `resource`
--
ALTER TABLE `resource`
  ADD PRIMARY KEY (`module`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `scores`
--
ALTER TABLE `scores`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `userid` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `module_access`
--
ALTER TABLE `module_access`
  MODIFY `no` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `no` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `scores`
--
ALTER TABLE `scores`
  MODIFY `no` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
