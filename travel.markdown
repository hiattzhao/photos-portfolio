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
  var bigLocation = imageLocation;
  var imagePrefix = 't';
  var totalImages = 26;
  
  var data = [];
  var titles = [
    '2005 Boston 041',
    '2006 Chicago 024',
    '2006 New Hope 006',
    '2006 New York City 114',
    '2006 Philadelphia 121',
    '2006 Philadelphia 151',
    '2009 New Year 151',
    '2010 New Jersey 045',
    '2013 Beijing 0226',
    '2013 Beijing 0507',
    '2013 Beijing 1454',
    '2013 Beijing 2143',
    '2013 Chichen Itza 280',
    '2013 Allentown 161',
    '2014 Burlington 21',
    '2014 Fort Myers 55',
    '2014 Pittsburgh 007',
    '2015 Las Vegas 027',
    '2015 New York City 035',
    '2015 New York City 0117',
    '2015 New York City 0139',
    '2015 New York City 0400',
    '2015 New York City 0683',
    '2015 New York City 1061',
    '2015 Rochester 059',
    '2015 Rochester 075'
  ];

  for (var i = totalImages; i >= 1; i--) {
    var j = i;
    if (i < 10) {
      j = '0' + i;
    }
    data.push({
      image : imageLocation + imagePrefix + j + '.jpg',
      thumb : thumbLocation + imagePrefix + j + '.jpg',
      big : imageLocation + imagePrefix + j + '.jpg',
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