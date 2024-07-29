---
layout: page
permalink: /understanding-data/
title: Understanding Data
description:
nav: false
nav_order: 
display_categories:
horizontal: false
toc:
  sidebar: left
---

## Overview

“Understanding data” is a crucial literacy domain for helping students develop the critical, ethical, and rhetorical impulses needed to define data; understand its complicated relations to power, privilege, oppression, and liberation; and imagine ethical and responsible ways of working with data toward more just futures.

The resources offered under this literacy domain push students to ask critical questions about data such as:

- What is “data”?
- How and why does data ethically matter?
- What critical habits toward data are important to develop?
- What rhetorical dimensions of data need to be considered?
- What is data advocacy? And how can we do data advocacy ethically and responsibly?
  <br>

<div class ="projects">
  <h1 class="category">Defining Data</h1>
</div>

Resources for this literacy domain offers students opportunities to explore what data is from a variety of disciplinary and professional perspectives. Students are especially encouraged to explore the important links between data, contexts, people, organizations, and power.

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Defining Data" | sort: "title" %}

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Critiquing Data</h1>
</div>

Resources for this literacy domain introduce students to critical data studies, data feminism, and other critical frameworks for interrogating how data yields power in various contexts and who benefits and does not benefit from such data use. In addition to these frameworks, resources in this literacy domain offer readings, activities, and assignments to help students hone their critical abilities to evaluate existing data sets, examples of data advocacy, and real-world scenarios concerning data ethics.

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Critiquing Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Acting Ethically with Data</h1>
</div>

Resources for this literacy domain introduce students to data ethics in order to help students better understand the significance of transparency, accountability, agency, and privacy, among other matters, when working with data. 

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Acting Ethically with Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Advocating with Data</h1>
</div>

Resources for this literacy domain introduce students to the practice of data advocacy and explore how a rhetorical data studies framework can help students advocate with data in ethical, persuasive, and just ways.

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Advocating with Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>
