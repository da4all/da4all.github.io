---
layout: page
permalink: /defining-data/
title: Defining Data
description: 
nav: false
nav_rank: 8
---

# Overview

"Defining data" is a crucial data literacy for students to become familiar with because, speaking more broadly, data literacy commonly refers to the ability to read, analyze, work, and communicate with data. Through defining data, this literacy argues that data literacy more broadly cannot be obtained without also learning how to define and interrogate data--to understand its complicated relations to power, privilege, oppression, and liberation. 

As such, this literacy introduces students to feminist, rhetorical, and equity data frameworks, all of which push students to ask critical questions about data such as: 
- What is “data”?
- How and why does data ethically matter?
- What rhetorical dimensions of data need to be carefully considered?
- How can we enact equitable data practices?

Such questions are especially important for doing data advocacy in ethical and just ways in our contemporary moment. This literacy thus specifically offers a theoretical understanding of data, an introduction to the data life cycle, and a brief dive into best practices of data advocacy in order to help students develop a strong rhetorical and ethical foundation from which to take up this important practice. 

# Defining Data Toolkit

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
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-list"></i> Type: {{ card.profile.group | replace: '<br />', ', ' }} ; Literacy: {{ card.profile.literacy | replace: '<br />', ', ' }}</small>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br></details>
<br>
<details>
<summary>Assignments</summary>
<br>
Internal text here
</details>
<br>
<details>
<summary>Activities</summary>
<br>
Internal text here
</details>
<br>
<details>
<summary>Tutorials</summary>
<br>
Internal text here
</details>
<br>
<details>
<summary>Teaching Modules</summary>
<br>
Internal text here
</details>
<br>
<details>
<summary>Data Sets</summary>
<br>
Internal text here
</details>
