---
layout: page
permalink: /processing-data/
title: Processing Data
description:
nav: false
nav_order: 
display_categories:
horizontal: false
toc:
  sidebar: left
---

## Overview

“Processing Data” is a crucial literacy domain for helping students learn how to perform various operations on data so that they can extract valuable insights from data in critical and ethical ways.

Processing Data is often understood to be an iterative cycle involving several phrases. For the purposes of this project, we identify 4 key phases: collecting data; organizing and cleaning data; analyzing data; and storing and preserving data.

The resources offered under this literacy domain push students to ask critical questions about data processing such as:

- What ethical issues do we need to consider when collecting data?
- What are useful strategies for organizing and cleaning data?
- What are different ways we can analyze data to glean useful information?
- How can we store and preserve data to make it sustainable and accessible?
<br>

<div class ="projects">
  <h1 class="category">Collecting Data</h1>
</div>

Resources for this literacy domain introduce students to various methods for gathering data for decision-making, planning, research and other purposes as well as challenge students to consider the ethical obligations of doing such data work.

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Collecting Data" | sort: "title" %}

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Organizing and Cleaning Data</h1>
</div>

Resources for this literacy domain help students learn how to assemble, categorize, classify, structure, and edit data so that it can be easily and ethically accessed, processed, and analyzed.

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Organizing and Cleaning Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Analyzing Data</h1>
</div>

Resources for this literacy domain teach students how to enact various methods to glean useful information and insights from data, which can then be used for various rhetorical purposes such as decision-making, advocacy, and education.

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Analyzing Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>

<div class ="projects">
  <h1 class="category">Storing and Preserving Data</h1>
</div>

Resources for this literacy domain introduce students to various practices and open-access tools for providing long-term storage of and access to data as well as conserving and maintaining its safety and integrity.

{% assign cards = site.cards | where: "sample_resource", true | where: "subdomain", "Storing and Preserving Data" | sort: "title" %}

<div class ="projects">
  <h2 class="category">Sample Toolkit Resources</h2>
</div>

<div class="grid-container">
    {%- for card in cards -%}
        {% include sample-cards.html %}
    {%- endfor %}
</div>


