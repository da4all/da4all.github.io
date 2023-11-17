---
layout: page
permalink: /wireframing/
title: Wireframing Sample
description:
nav: false
nav_rank: 8
---

(function(){
      if (window!=window.top) {
        var noiframe = document.getElementsByClassName("noiframeyall"), 
            body = document.getElementsByTagName('body')[0],
            html = document.getElementsByTagName('html')[0];

        for (i=0, len = noiframe.length; i < len; i++){
          noiframe[i].style.display = 'none';
        }
      body.className = body.className.replace( /(?:^|\s)noiframe(?!\S)/ , '' );
      html.style.overflow = 'hidden';
      }
    })();

# Singular iFrame

<iframe 
  src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#content?isdtp=mn" 
  width="90%" 
  height="400px"
  title="Collection Builder Integration"
  margin-top="-2000px"
  ></iframe>

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
            <iframe src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#content" width="90%" height=400px title="Collection Builder Integration"></iframe>
        </div>
        <div class="column" style="background-color:;">
            <h2>Example 2</h2>
            <iframe src="https://lore3581.github.io/da4a-collectionbuilder/item.html?id=da4a007#content" width="90%" height=400px title="Collection Builder Integration"></iframe>
        </div>
    </div>
 </body>
</html>
