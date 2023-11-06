# write-up

- Question 1) What is the SHA1 hash value of the sample? (Format: SHA1Hash)

<details>
  <summary>Flag</summary>

  ```
  06727ffda60359236a8029e0b3e8a0fd11c23313
  ```
</details>
metodo:
analizando el archivo word adjunto en virustotal, obtenemos el hash automaticamente.
Tambien es posible desde la terminal

```
sha1sum {file}
sha1sum sample.doc
``` 
---

- Question 2) According to VirusTotal, what is the full filetype of the provided sample? (Format: X X X X) 

<details>
  <summary>Flag</summary>

  ```
  Office Open XML Document
  ```
</details>
 virustotal da la respuesta en la pestaña "details" opcion "file type

 ---
 Question 3) Extract the URL that is used within the sample and submit it (Format: https://x.domain.tld/path/to/something)

 <details>
  <summary>Flag</summary>

  ```
  https://www.xmlformats.com/office/word/2022/wordprocessingDrawing/RDF842l.html!"
  ```
</details>
dentro del archivo sample.doc habia 10 archivos (en su mayoria xml), se extrajeron y al revizarlos un archivo "document.xml.rels" era el unico que tenia un link no relacionado a word o archivo de texto
el link tiene 13 alertas en virus total

---
Question 4) What is the name of the XML file that is storing the extracted URL? (Format: file.name.ext) 
 <details>
  <summary>Flag</summary>

  ```
  document.xml.rels
  ```
</details>
