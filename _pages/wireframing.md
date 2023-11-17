---
layout: page
permalink: /wireframing/
title: Wireframing Sample
description:
nav: false
nav_rank: 8
---

# iFrame
<iframe 
        src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#item-title" 
        width="90%" 
        height="400px"
        title="Collection Builder Integration"
        scrolling="no"></iframe>

# Clickable

<a href="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#item-title" target="_blank" class="linkwrap">
    <div class="blocker"></div>
    <iframe 
        src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#item-title" 
        width="90%" 
        height="400px"
        title="Collection Builder Integration"
        scrolling="no"></iframe>
</a>

<br><br>

# Columns
<br>
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
    padding: 20px;
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
        <div class="column" style="background-color:;">
            <h2>Example</h2>
            <iframe src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a005#item-title" width="90%" height=400px title="Collection Builder Integration"></iframe>
        </div>
        <div class="column" style="background-color:;">
            <h2>Example 2</h2>
            <iframe src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a001#item-title" width="90%" height=400px title="Collection Builder Integration"></iframe>
        </div>
    </div>
 </body>
</html>
