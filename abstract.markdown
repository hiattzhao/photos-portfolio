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
  var bigLocation = imageLocation;
  var imagePrefix = 'ar';
  var totalImages = 60;
  
  var data = [];
  var titles = [
    '2006 Atlanta 174',
    '2006 Boston 015',
    '2007 NYC 029',
    '2007 NYC 279',
    '2007 NYC 290',
    '2007 Philadelphia 089',
    '2007 Philadelphia 184',
    '2008 Dallas 27',
    '2011 Bethlehem 54',
    '2012 Beijing 0156',
    '2012 Beijing 1304',
    '2012 Beijing 2532',
    '2012 Beijing 2562',
    '2012 Beijing 2581',
    '2012 Beijing 2602',
    '2012 Hong Kong 093',
    '2012 Hong Kong 108',
    '2012 Hong Kong 267',
    '2012 Hong Kong 273',
    '2012 Hong Kong 290',
    '2012 Hong Kong 299',
    '2012 Shanghai 0200',
    '2012 Shanghai 0415',
    '2012 Shanghai 0433',
    '2012 Shanghai 0541',
    '2012 Shanghai 0797',
    '2012 Shanghai 0933',
    '2012 Shanghai 1181',
    '2012 Shanghai 1427',
    '2012 Shanghai 1581',
    '2012 Shanghai 1598',
    '2012 Shanghai 1624',
    '2012 Shanghai 2136',
    '2012 Shanghai 2389',
    '2012 Shanghai 2414',
    '2012 Shanghai 2427',
    '2012 Shanghai 2454',
    '2012 Shanghai 3043',
    '2012 Shanghai 3063',
    '2012 Shanghai 3202',
    '2012 Shanghai 3236',
    '2012 Shanghai 3277',
    '2012 Shenzhen 329',
    '2012 Shenzhen 418',
    '2012 Shenzhen 453',
    '2012 XiAn 1151',
    '2012 XiAn 1164',
    '2012 XiAn 1176',
    '2012 XiAn 1270',
    '2013 Anchorage 118',
    '2013 Anchorage 202',
    '2013 Beijing 0218',
    '2013 Portland 085',
    '2013 Portland 150',
    '2013 San Diego 047',
    '2013 San Diego 058',
    '2013 Seattle 785',
    '2013 Vancouver 169',
    '2013 Vancouver 176',
    '2013 Vancouver 339'
  ];

  for (var i = totalImages; i >= 1; i--) {
    data.push({
      image : imageLocation + imagePrefix + i + '.jpg',
      thumb : thumbLocation + imagePrefix + i + '.jpg',
      big : imageLocation + imagePrefix + i + '.jpg',
      title: titles[i - 1],
      description: 'none'
    });
  }

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