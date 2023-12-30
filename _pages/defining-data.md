---
layout: page
permalink: /defining-data/
title: Defining Data
description: 
nav: false
nav_rank: 8
---

# Overview
***Description of what it means to define data here. For simplicity's sake, I've taken this one from the previous Module 1 overview:*** Data Literacy commonly refers to the ability to read, analyze, work, and communicate with data. This module argues that data literacy cannot be obtained without also learning how to define and interrogate data--to understand its complicated relations to power, privilege, oppression, and liberation. As such, this module introduces students to feminist, rhetorical, and equity data frameworks, all of which push students to ask critical questions about data such as: What is “data”? How and why does data ethically matter? What rhetorical dimensions of data need to be carefully considered? How can we enact equitable data practices? Such questions are especially important for doing data advocacy in ethical and just ways in our contemporary moment. This module thus specifically offers a theoretical understanding of data, an introduction to the data life cycle, and a brief dive into best practices of data advocacy in order to help students develop a strong rhetorical and ethical foundation from which to take up this important practice. 

# Sample

<br>

<details open>
<summary>Header Text</summary>
<br>
Internal text here
</details>

<br><br>

# Defining Data Toolkit

<details>
<summary>Readings</summary>
<br>

{% assign cards = site.cards | where: "group", "Reading" | where: "topic", "Defining" | sort: "last_name" %}

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
                        <br><small class="test-muted"><i class="fas fa-list"></i> {{ card.profile.group | replace: '<br />', ', ' }}</small>
			<br><small class="test-muted"><i class="fas fa-gears"></i> {{ card.profile.literacy | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br></details>

<br><br>
