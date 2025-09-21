---
layout: page
title: travel
permalink: /travel
---

<div id="galleria"></div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
    crossorigin="anonymous"></script>
<script src="/assets/js/galleria-1.4.2.min.js"></script>

<script>
  var imageLocation = '/assets/photos/travel/';
  var thumbLocation = imageLocation + 'thumb-t/';
  var imagePrefix = 't';
  
  var data = [];
  var titles = ['2002 StElizabeth 12', '2003 BlackHills 070', '2003 BlackHills 255', '2003 Butte 004', '2003 Butte 007', '2003 Chicago 267', '2003 Chicago 277', '2003 Chicago 312', '2003 Dallas 051', '2003 Houston 097', '2003 LosAngeles 002', '2003 LosAngeles 005', '2003 LosAngeles 008', '2003 Minneapolis 378', '2003 NewOrleans 181', '2003 NewOrleans 281', '2003 Philadelphia 039', '2003 Philadelphia 055', '2003 Portland 117', '2003 SaltLakeCity 060', '2003 SaltLakeCity 083', '2003 SanAntonio 106', '2003 SanFrancisco 089', '2003 SantaFe 034', '2003 Savannah 026', '2003 Seattle 050', '2003 StAugustine 023', '2004 BrooklynHeights 25', '2004 NewYorkCity 179', '2004 NewYorkCity 793', '2004 NewYorkCity 941', '2004 NewYorkCity 954', '2004 NewYorkCity 961', '2004 NewYorkCity 1070', '2004 NewYorkCity 1124', '2004 NewYorkCity 1290', '2005 Boston 041', '2005 Rochester 038', '2006 Chicago 024', '2006 JimThorpe 04', '2006 LehighValley 20', '2006 NewHope 006', '2006 NewYorkCity 114', '2006 Philadelphia 005', '2006 Philadelphia 121', '2006 Philadelphia 151', '2006 Quakertown 007', '2009 NewYear 151', '2010 Bethlehem 41', '2010 Madison 045', '2011 Bethlehem 33', '2011 Naples 49', '2011 Wescosville 003', '2013 Beijing 0226', '2013 Beijing 0507', '2013 Beijing 1454', '2013 Beijing 2143', '2013 ChichenItza 280', '2013 Seattle 389', '2013 TowersEast 161', '2014 Burlington 21', '2014 FortMyers 55', '2014 Pittsburgh 007', '2015 LasVegas 027', '2015 NewYorkCity 035', '2015 NewYorkCity 0117', '2015 NewYorkCity 0139', '2015 NewYorkCity 0400', '2015 NewYorkCity 0683', '2015 NewYorkCity 1061', '2015 Rochester 059', '2015 Rochester 075', '2016 Cambridge 124', '2016 Lisbon 089', '2016 Lisbon 197', '2016 Lisbon 289', '2016 Lisbon 493', '2016 London 333', '2016 Madrid 074', '2016 Madrid 296', '2016 Marseille 247', '2016 NewYorkCity 040', '2016 NewYorkCity 096', '2016 NewYorkCity 161', '2016 NewYorkCity 187', '2016 NewYorkCity 199', '2016 Nice 079', '2016 Paris 0067', '2016 Paris 0695', '2016 Sintra 216', '2016 Sintra 283', '2016 Toledo 286', '2017 AtlanticCity 27', '2017 Philadelphia 296', '2017 Pittsburgh 055', '2017 Pittsburgh 093', '2017 Pittsburgh 100', '2017 Pittsburgh 140', '2017 WestOakLane 091', '2017 WestOakLane 134', '2018 Denver 250', '2023 Bohol 41', '2023 Bohol 111', '2023 Haiphong 11', '2023 HalongBay 35', '2023 HalongBay 95', '2023 Hanoi 32', '2023 Hanoi 70', '2023 Hanoi 91', '2023 Hilo 153', '2023 Himeji 25', '2023 Himeji 62', '2023 Hiroshima 24', '2023 Hiroshima 38', '2023 Hiroshima 123', '2023 HoChiMinhCity 3', '2023 Kaohsiung 15', '2023 Kaohsiung 155', '2023 Kaohsiung 182', '2023 Kobe 124', '2023 Kyoto 189', '2023 Kyoto 223', '2023 Kyoto 372', '2023 Kyoto 467', '2023 Manila 55', '2023 Manila 79', '2023 Nara 39', '2023 Nara 43', '2023 Nara 104', '2023 Nara 145', '2023 Nara 151', '2023 Okayama 18', '2023 Okayama 26', '2023 Osaka 2', '2023 Osaka 84', '2023 Osaka 134', '2023 Seattle 97', '2023 Seattle 149', '2023 Seattle 168', '2023 Seattle 235', '2023 Seoul 144', '2023 Taipei 38', '2023 Taipei 132', '2023 Taipei 201', '2023 Taipei 246', '2023 Taipei 418', '2023 Takamatsu 38', '2023 Tokyo 134', '2023 Tokyo 237', '2023 Tokyo 257', '2024 Ayutthaya 51', '2024 Ayutthaya 67', '2024 ElNido 23', '2024 ElNido 45', '2024 ElNido 49', '2024 GeorgeTown 115', '2024 KualaLumpur 185', '2024 Manila 68', '2024 PhnomPenh 60', '2024 Phuket 232', '2024 SiemReap 54', '2024 SiemReap 161', '2024 Singapore 12', '2024 Singapore 407', '2024 Taipei 43'];

  var totalImages = titles.length;
  var ext = '.webp';

  for (var i = 1; i <= totalImages; i++) {
    data.push({
      image : imageLocation + imagePrefix + i + ext,
      thumb : thumbLocation + imagePrefix + i + ext,
      title: titles[i - 1]
    });
  }

  data.reverse(); // Reverse the order of the photos

  // Load the custom theme
  Galleria.loadTheme('/assets/js/galleria/galleria.portfolio.js');
  // Configure Galleria
  Galleria.configure({
    showInfo: true
  });
  // Initialize Galleria
  Galleria.run('#galleria', {
    dataSource: data
  });
</script>
