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
    <iframe 
        src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#item-title" 
        width="90%" 
        height="400px"
        title="Collection Builder Integration"
        scrolling="no"></iframe>
</a>

# Clickable 2

<div style="position:relative;">
<iframe src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#item-title" width="90%" height="400px" title="Collection Builder Integration" scrolling="no"></iframe>
<a  href="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#item-title" target="_blank" style="position:absolute; bottom:0; left:0; display:inline-block;"></a>
</div>

# Clickable 3

<div style="position:relative;">
<a  href="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#item-title" target="_blank" style="position:absolute; bottom:0; left:0; display:inline-block;"><iframe src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#item-title" width="90%" height="400px" title="Collection Builder Integration" scrolling="no"></iframe>
</a>
</div>

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
    padding-left: 20px;
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
