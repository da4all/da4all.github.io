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

Placeholder text defining the sub-domain.

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

Placeholder text defining the sub-domain.

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

Placeholder text defining the sub-domain.

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
  <h1 class="category">Linking Data and Justice</h1>
</div>

Placeholder text defining the sub-domain.

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Linking Data and Justice" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>
