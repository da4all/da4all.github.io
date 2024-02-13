---
layout: page
permalink: /understanding-data/
title: Understanding Data
description: 
nav: false
nav_rank: 8
---

## A Ref

### domain: 
- <a href="../understanding-data/">Understanding Data</a>
- <a href="../processing-data/">Processing Data</a>
- <a href="../persuading-with-data/">Persuading with Data</a>

### topic: 
- <a href="../defining-data/">Defining Data</a>
- <a href="../critiquing-data/">Critiquing Data</a>
- <a href="../acting-ethically-with-data/">Acting Ethically with Data</a>
- <a href="../linking-data-and-justice/">Linking Data and Justice</a>
- <a href="../collecting-data/">Collecting Data</a>
- <a href="../organizing-and-cleaning-data/">Organizing and Cleaning Data</a>
- <a href="../analyzing-and-drawing-insights-from-data/">Analyzing and Drawing Insights from Data</a>
- <a href="../storing-and-preserving-data/">Storing and Preserving Data</a>
- <a href="../appealing-with-data/">Appealing with Data</a>
- <a href="../visualizing-data/">Visualizing Data</a>
- <a href="../mapping-data/">Mapping Data</a>
- <a href="../telling-multi-modal-stories-with-data/">Telling Multi-Modal Stories with Data</a>

## Overview

“Understanding data” is a crucial literacy domain for helping students develop the critical, ethical, and rhetorical impulses needed to define data; understand its complicated relations to power, privilege, oppression, and liberation; and imagine ethical and responsible ways of working with data toward more just futures.

The resources offered under this literacy domain push students to ask critical questions about data such as:
- What is “data”?
- How and why does data ethically matter?
- What critical habits toward data are important to develop?
- What rhetorical dimensions of data need to be considered?
- What is data advocacy? And how can we do data advocacy ethically and responsibly?

<details>
<summary>Defining Data</summary>
	
<details>
<summary> Readings</summary>

{% assign cards = site.cards | where: "group", "Reading" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    <p class="card-text">
			<div style="height:1px;font-size:1px;">&nbsp;</div>
			{% if card.profile.author %}<small class="test-muted"><i class="fas fa-user-pen"></i>  Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}
			{% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			<small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.literacy | replace: '<br />', ', ' }} </small> <br>
			<small class="test-muted"><i class="fas fa-table-columns"></i>  Type of Resource: {{ card.profile.group | replace: '<br />', ', ' }} </small>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br>

</details>

<details>
<summary> Glossary</summary>

{% assign cards = site.cards | where: "group", "Term" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    <p class="card-text">
			<div style="height:1px;font-size:1px;">&nbsp;</div>
			{% if card.profile.author %}<small class="test-muted"><i class="fas fa-user-pen"></i>  Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}
			{% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			<small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.literacy | replace: '<br />', ', ' }} </small> <br>
			<small class="test-muted"><i class="fas fa-table-columns"></i>  Type of Resource: {{ card.profile.group | replace: '<br />', ', ' }} </small>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br>

</details>

<details>
<summary> Assignments</summary>

{% assign cards = site.cards | where: "group", "Assignment" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    <p class="card-text">
			<div style="height:1px;font-size:1px;">&nbsp;</div>
			{% if card.profile.author %}<small class="test-muted"><i class="fas fa-user-pen"></i>  Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}
			{% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			<small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.literacy | replace: '<br />', ', ' }} </small> <br>
			<small class="test-muted"><i class="fas fa-table-columns"></i>  Type of Resource: {{ card.profile.group | replace: '<br />', ', ' }} </small>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br>


</details>

<details>
<summary> Activities</summary>

Word

</details>

<details>
<summary> Tutorials</summary>
<br>
Internal text here
</details>

<details>
<summary> Teaching Modules</summary>
<br>
Internal text here
</details>


<details>
<summary> Data Sets</summary>
<br>

Internal text here

</details>

<details>
<summary> All Defining Data Resources</summary>

{% assign cards = site.cards | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    <p class="card-text">
			<div style="height:1px;font-size:1px;">&nbsp;</div>
			{% if card.profile.author %}<small class="test-muted"><i class="fas fa-user-pen"></i>  Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}
			{% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			<small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.literacy | replace: '<br />', ', ' }} </small> <br>
			<small class="test-muted"><i class="fas fa-table-columns"></i>  Type of Resource: {{ card.profile.group | replace: '<br />', ', ' }} </small>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br>

</details>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<details>
<summary>Critiquing Data</summary>
Organized cards will go here.</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<details>
<summary>Acting Ethically with Data</summary>
Organized cards will go here.</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<details>
<summary>Linking Data and Justice</summary>
Organized cards will go here.</details>
