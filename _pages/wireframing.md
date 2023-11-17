---
layout: page
permalink: /wireframing/
title: Wireframing Sample
description:
nav: false
nav_rank: 8
---

<head>
  <script>
    var frame = document.querySelector("iframe");
    header = frame.contentDocument.querySelector("header");
    header.remove();
    footer = frame.contentDocument.querySelector("footer");
    footer.remove();
  </script>
</head>

# Singular

<iframe src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007/#content" width="90%" height=400px title="Collection Builder Integration"></iframe>

<br><br>

# Columns

<html>
 <head>
    <style>
    {
        box-sizing: border-box;
    }
    /* Set additional styling options for the columns*/
    .column {
    float: left;
    width: 50%;
    }

    .row:after {
    content: "";
    display: table;
    clear: both;
    }
    </style>
 </head>
 <body>
    <div class="row">
        <div class="column" style="background-color:#FFB695;">
            <h2>Column 1</h2>
            <p>Data..</p>
        </div>
        <div class="column" style="background-color:#96D1CD;">
            <h2>Column 2</h2>
            <p>Data..</p>
        </div>
    </div>
 </body>
</html>
