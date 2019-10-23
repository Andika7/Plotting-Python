# Pencarian Kata Top 10 Dalam 1 Bulan

## Crawling Laman web
berikut merupakan script yang digunakan untuk crawling halaman web

- script : python3 crawl-new.py url-output.txt banyak-hari dd-mm-yyyy
- script : python3 download.py file-url.txt pathOutput

## Preprocess
berikut script yang digunakan untuk membersihkan file dan menghitung frekuensi kata

- Cleaning
    - script : python3 extract-content.py pathCrawl pathOutput

- Count term frequency
    - script : python3 word-count.py pathClean pathOutput stopword.txt

## Plotting
berikut scrip yang digunakan untuk plotting top 10 kata teratas

- Histogram
    - script : python3 histogram.py frequency.txt

- Line-Pllot
    - script : python3 line-plot.py pathFrequency days

    days = berisi nilai interger untuk banyak hari yang ingin ditampilkan

- Pie Chart
    - script : python3 piechart.py frequency.txt

## Example running Plotting

- Histogram
    - script : python3 histogram.py term-freq/freq-all.txt

- Line-Pllot
    - script : python3 line-plot.py term-freq/ 14

- Pie Chart
    - script : python3 piechart.py term-freq/freq-all.txt