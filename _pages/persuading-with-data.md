---
layout: page
permalink: /persuading-with-data/
title: Persuading with Data
description:
nav: false
nav_order: 
display_categories:
horizontal: false
toc:
  sidebar: left
---

## Overview

“Persuading with Data” is a crucial literacy domain for helping students learn how to generate persuasive data-driven content to assist advocacy aims for diverse contexts, purposes, and audiences.

Persuading with Data is a multi-modal affair, meaning that when it comes to data advocacy, not only does data often come in various forms (numerical, imagistic, geolocational) but data is also commonly woven together with various resources for communication (words, sounds, images, etc.) to achieve various aims. To help students learn the various multi-modal ways one can persuade with data for advocacy purposes, we offer resources that specifically focus on: appealing with data; visualizing data; mapping data; and telling multi-modal stories with data.

The resources offered under this literacy domain focus on these and other important questions:

- How can rhetoric—the art of persuasion—inform and enhance our data advocacy efforts?
- How can we use data to make emotional, ethical, and logical appeals to help achieve our advocacy aims?
- How can data visualizations and maps be responsibly used to assist our advocacy efforts?
- How can we tell ethical, effective, and affective data-driven stories to achieve our various rhetorical aims?
<br>

<div class ="projects">
  <h1 class="category">Making Claims with Data</h1>
</div>

Resources for this literacy domain introduce students to the art of rhetoric and teach students how to identify a rhetorical situation, make ethical and persuasive claims with data, and move a targeted audience through logical, emotional, and ethical appeals. 

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Making Claims with Data" | sort: "title" %}

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Visualizing Data</h1>
</div>

Resources for this literacy domain teach students how to analyze and generate data visualizations with potential for moving an audience in service of one’s advocacy aims. 

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Visualizing Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Mapping Data</h1>
</div>

Resources for this literacy domain teach students how to analyze and generate data driven maps with potential for moving an audience in service of one’s advocacy aims. 

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Mapping Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Telling Stories with Data</h1>
</div>

Resources for this literacy domain teach students how to integrate claims, visualizations, and maps with narrative to generate powerful multi-modal stories in various genres for data advocacy purposes.

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Telling Stories with Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>


