---
layout: page
title: abstract
permalink: /abstract
---

<div id="galleria"></div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
    crossorigin="anonymous"></script>
<script src="/assets/js/galleria-1.4.2.min.js"></script>

<script>
  var imageLocation = '/assets/photos/architecture-reflections/';
  var thumbLocation = imageLocation + 'thumb-ar/';
  var imagePrefix = 'ar';
  
  var data = [];
  var titles = ['2006 Atlanta 174', '2006 Boston 015', '2007 NewYorkCity 029', '2007 NewYorkCity 279', '2007 NewYorkCity 290', '2007 Philadelphia 089', '2007 Philadelphia 184', '2008 Dallas 27', '2011 Bethlehem 54', '2012 Beijing 0156', '2012 Beijing 1304', '2012 Beijing 2532', '2012 Beijing 2562', '2012 Beijing 2581', '2012 Beijing 2602', '2012 HongKong 093', '2012 HongKong 108', '2012 HongKong 267', '2012 HongKong 273', '2012 HongKong 290', '2012 HongKong 299', '2012 Shanghai 0200', '2012 Shanghai 0415', '2012 Shanghai 0433', '2012 Shanghai 0541', '2012 Shanghai 0797', '2012 Shanghai 0933', '2012 Shanghai 1181', '2012 Shanghai 1427', '2012 Shanghai 1581', '2012 Shanghai 1598', '2012 Shanghai 1624', '2012 Shanghai 2136', '2012 Shanghai 2389', '2012 Shanghai 2414', '2012 Shanghai 2427', '2012 Shanghai 2454', '2012 Shanghai 3043', '2012 Shanghai 3063', '2012 Shanghai 3202', '2012 Shanghai 3236', '2012 Shanghai 3277', '2012 Shenzhen 329', '2012 Shenzhen 418', '2012 Shenzhen 453', '2012 XiAn 1151', '2012 XiAn 1164', '2012 XiAn 1176', '2012 XiAn 1270', '2013 Anchorage 118', '2013 Anchorage 202', '2013 Beijing 0218', '2013 Portland 085', '2013 Portland 150', '2013 SanDiego 047', '2013 SanDiego 058', '2013 Seattle 785', '2013 Vancouver 169', '2013 Vancouver 176', '2013 Vancouver 339', '2013 Vancouver 347', '2013 Vancouver 393', '2013 Vancouver 627', '2014 Orlando 144', '2014 Richmond 75', '2015 LasVegas 170', '2015 NewYorkCity 0659', '2016 Barcelona 156', '2016 Barcelona 184', '2016 Barcelona 301', '2016 Barcelona 313', '2016 Cambridge 097', '2016 Lisbon 467', '2016 London 082', '2016 London 127', '2016 Marseille 137', '2016 Valencia 216', '2018 Chicago 442', '2019 Atlanta 42', '2019 WinstonSalem 27', '2019 WinstonSalem 36', '2023 Busan 103', '2023 Fukuoka 104', '2023 Seattle 136', '2023 Seattle 228', '2023 Seoul 22', '2023 Tokyo 73', '2024 KualaLumpur 57', '2024 Manila 96', '2024 Manila 188', '2024 Manila 208', '2024 Manila 216', '2024 Singapore 322', '2024 Singapore 325', '2024 Singapore 360', '2024 Taipei 142', '2024 Taipei 235', '2024 Taipei 408', '2024 Taipei 462', '2024 Taipei 467', '2024 Taipei 472', '2024 Taipei 522'];

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
