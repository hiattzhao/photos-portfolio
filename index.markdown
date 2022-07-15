---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
<div>
  <img src="/assets/photos/self.jpg" id="portrait" alt="Hiatt Zhao self portrait">

  <h2>I am 
    <em class="title">a fine art photographer</em>
    <em class="title">an application engineer</em>
    <em class="title">an avid traveler</em>
    <em class="title">an occasional writer</em>
    <em class="title">a curious learner</em>
  </h2>

  <p>I have a passion for the visual arts and I've been exhibiting my photographs in galleries for about twenty years. Along with a scientific mind, I currently work as an application engineer. And in my spare time, I love to travel.</p>

  <p>When I'm not doing the above, I like to read positive psychology, business, and finance books. I also like to write, hike, play the guitar, and visit the library.</p>

  <p>One of my goals in life is to see the world. My greatest adventure thus far has been a <a class="page-link" href="https://www.hiattzhao.com/search/label/2018%20Bicycle%20Across%20America" target="_blank">cross country bicycle trip <i class="fa fa-external-link"></i></a> in the spring and summer of 2018 where I biked from Philadelphia to San Francisco in 100 days.</p>
</div>

<div style="height: 25vh; display: flex; align-items: center; justify-content: center;">
  <div style="margin: 0;">
    <div class="post">
      <p>You can <a class="page-link" href="mailto:hiattzhao@gmail.com">email</a> me or find me on the following social media platforms.</p>
    </div>
    <div class="social_icons">
      <a href="https://www.facebook.com/hiattzhao" target="_blank"><i class="fab fa-facebook"></i></a>
      <a href="https://twitter.com/hiattzhao" target="_blank"><i class="fab fa-twitter"></i></a>
      <a href="https://www.instagram.com/hiattzhao/" target="_blank"><i class="fab fa-instagram"></i></a>
      <a href="https://www.linkedin.com/in/hiattzhao" target="_blank"><i class="fab fa-linkedin-in"></i></a>
      <a href="https://github.com/hiattzhao" target="_blank"><i class="fab fa-github"></i></a>
      <a href="https://vimeo.com/hiattzhao/" target="_blank"><i class="fab fa-vimeo-v"></i></a>
    </div>
  </div>
</div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  var titles = $(".title");
  var titleIndex = 0;
  function showNextTitle() {
    titles.eq(titleIndex % titles.length)
        .fadeIn(2000)
        .delay(1000)
        .fadeOut(2000, showNextTitle);
    titleIndex++;
  }
  showNextTitle();
});

</script>
