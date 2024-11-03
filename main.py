#inder.html
!DOCTYPE html>
<html>
<head>
    <title>Its something</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Gamers problem</h1>
    <p>Always in pc cant even go get water lol...</p>
    <h2>If you do the same then</h2>
             <ul>
                   <li>Go get a life </li>
                   <li>Get some friends (not in vidio game)</li>
             </ul>
    <img src="https://t3.ftcdn.net/jpg/02/85/90/44/360_F_285904422_IdADB85m2sNiBDvpEwIdRnOkbSNki9Kq.jpg">

    <iframe src="https://www.meteoblue.com/en/weather/widget/daily/ip_romania_675514?geoloc=fixed&days=4&tempunit=CELSIUS&windunit=KILOMETER_PER_HOUR&precipunit=MILLIMETER&coloured=coloured&pictoicon=1&maxtemperature=1&mintemperature=1&windspeed=1&windgust=0&winddirection=1&uv=0&humidity=0&precipitation=1&precipitationprobability=1&spot=1&pressure=0&layout=light"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 216px; height: 420px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/en/weather/week/ip_romania_675514?utm_source=daily_widget&utm_medium=linkus&utm_content=daily&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div>

</body>
</html>


#style.css
body {
    font-family: Arial,  sans-serif; /* Семейство шрифтов */
    font-size: 11px; /* Размер основного шрифта в <p></p>  */
    background-color: #f0f0f0; /* Цвет фона веб-страницы */
    color: #333333; /* Цвет основного текста */ 
}
h1 {
    color: #00a800; /* Цвет заголовка */
    font-size: 24px; /* Размер шрифта в пунктах */
    font-family: Georgia, serif; /* Семейство шрифтов */
    animation: color-change 3s infinite;
}
img{
    width: 100%;
    height: 100%;
}

h1:hover{
    animation: color-change 3s infinite;
}


@keyframes color-change {
    0% {
      color: blue;
    }
  
    50% {
      color: red;
    }
  
    100% {
      color: blue;
    }
}
