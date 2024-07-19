---
layout: page
permalink: /testing2/
title: Testing 2
description:
nav: false
nav_order: 
---

# IFRAMES

## GIF
<iframe width="100%" src="../assets/documents/Fitz.gif" allowfullscreen>iFrame HERE</iframe>

## DOCX - impossible with GitHub
<iframe width="100%" src="../assets/documents/Lore Whittemore_Archival Methods Micropaper_Longer Draft.docx" allowfullscreen>iFrame HERE</iframe>

## PPTX - not likely
<iframe width="100%" src="../assets/documents/SCMSPresentation2024.pptx" allowfullscreen>iFrame HERE</iframe>

## XLSX
<iframe width="100%" src="../assets/documents/Sample_Data_Exploration.xlsx" allowfullscreen>iFrame HERE</iframe>

## TXT
<iframe width="100%" src="../assets/documents/Week1_Johnson - from Media Franchising-annotations.txt" allowfullscreen>iFrame HERE</iframe>

## CSV
<div id="CSVTable"></div>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script src="//jquerycsvtotable.googlecode.com/files/jquery.csvToTable.js"></script>

<script>
$(function() {
  $('#CSVTable').CSVToTable('../assets/documents/metadata.csv');
});
</script>
