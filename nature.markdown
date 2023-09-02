---
layout: page
title: nature
permalink: /nature
---

<div id="galleria"></div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
    crossorigin="anonymous"></script>
<script src="/assets/js/galleria-1.4.2.min.js"></script>

<script>
  var imageLocation = '/assets/photos/nature/';
  var thumbLocation = imageLocation + 'thumb-n/';
  var bigLocation = imageLocation;
  var imagePrefix = 'n';
  
  var data = [];
  var titles = [
    '2005 Rochester 100 ',
    '2006 Chicago 147',
    '2011 Birds 11',
    '2011 Flowers 209',
    '2011 Flowers 344',
    '2011 Hope Ln 003',
    '2011 Trexler Park 22',
    '2012 Hope Ln 169',
    '2013 Beijing 1136',
    '2013 Carmel 390',
    '2013 Juneau 564',
    '2013 Los Angeles 289',
    '2013 Monterey 233',
    '2013 Pacific Grove 089',
    '2014 Lake George 87',
    '2014 Lake Placid 099',
    '2014 Lake Placid 155',
    '2014 Orlando 094',
    '2014 Orlando 116',
    '2014 St Petersburg 249',
    '2015 Antelope Canyon 137',
    '2015 Grand Canyon 032',
    '2015 New York City 0542',
    '2015 New York City 0995',
    '2015 Rochester 196',
    '2015 Salt Lake City 014',
    '2017 Moon 39',
    '2017 New Years Day 22'
  ];

  var totalImages = titles.length;

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