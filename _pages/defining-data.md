---
layout: page
permalink: /defining-data/
title: Defining Data
description: 
nav: false
nav_rank: 8
---

## Overview

"Defining data" is a crucial data literacy for students to become familiar with because, speaking more broadly, data literacy commonly refers to the ability to read, analyze, work, and communicate with data. Through defining data, this literacy argues that data literacy more broadly cannot be obtained without also learning how to define and interrogate data--to understand its complicated relations to power, privilege, oppression, and liberation. 

As such, this literacy introduces students to feminist, rhetorical, and equity data frameworks, all of which push students to ask critical questions about data such as: 
- What is “data”?
- How and why does data ethically matter?
- What rhetorical dimensions of data need to be carefully considered?
- How can we enact equitable data practices?

Such questions are especially important for doing data advocacy in ethical and just ways in our contemporary moment. This literacy thus specifically offers a theoretical understanding of data, an introduction to the data life cycle, and a brief dive into best practices of data advocacy in order to help students develop a strong rhetorical and ethical foundation from which to take up this important practice. 

## Defining Data Toolkit

<details>
<summary>Readings</summary>

{% assign cards = site.cards | where: "group", "Reading" | where: "topic", "Defining Data" | sort: "last_name" %}

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
		    <br>{% if card.profile.source %}<br><small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
		    {% if card.profile.author %}<small class="test-muted"><i class="fas fa-user-pen"></i>  Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}
		    <small class="test-muted"><i class="fas fa-table-columns"></i>   Literacy: {{ card.profile.literacy | replace: '<br />', ', ' }} ; Type: {{ card.profile.group | replace: '<br />', ', ' }}</small>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br></details>

<div style="height:5px;font-size:1px;">&nbsp;</div>



<details>
<summary>Assignments</summary>

{% assign cards = site.cards | where: "group", "Assignment" | where: "topic", "DataJustice" | sort: "last_name" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
		    {% if card.profile.group %}<h6 class="card-subtitle mb-2 text-muted">Type: {{ card.profile.group }}</h6>{% endif %}
                    {% if card.profile.literacy %}<h6 class="card-subtitle mb-2 text-muted">Literacy: {{ card.profile.literacy }}</h6>{% endif %}
                    {% if card.profile.position %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.position }}</h6>{% endif %}
                    {% if card.profile.department %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.department }}</h6>{% endif %}
                    {% if card.profile.organization %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.organization }}</h6>{% endif %}
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    {% if card.profile.website %}
                        <br><a href="{{ card.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                    {% endif %}
                    {% if card.profile.email %}
                        <a href="mailto:{{ card.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                    {% endif %}
                    {% if card.profile.phone %}
                        <a href="tel:{{ card.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                    {% endif %}
                    {% if card.profile.orcid %}
                        <a href="https://orcid.org/{{ card.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                    {% endif %}
                    {% if card.profile.twitter %}
                        <a href="https://twitter.com/{{ card.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                    {% endif %}
                    {% if card.profile.github %}
                        <a href="https://github.com/{{ card.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                    {% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-table-columns"></i> Literacy: {{ card.profile.literacy | replace: '<br />', ', ' }} ; Type: {{ card.profile.group | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>



<details>
<summary>Activities</summary>

Word

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<details>
<summary>Tutorials</summary>
<br>
Internal text here
</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<details>
<summary>Teaching Modules</summary>
<br>
Internal text here
</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<details>
<summary>Data Sets</summary>
<br>

Internal text here

</details>
