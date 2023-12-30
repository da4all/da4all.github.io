---
layout: page
permalink: /toolkit/
title: Toolkit
description: 
nav: false
nav_rank: 8
---

## Overview

With the Data Advocacy for All toolkit, you have two ways to explore:

## Exploring by Resource Type

<details>
<summary> Readings</summary>

{% assign cards = site.cards | where: "group", "Reading" | sort: "last_name" %}

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

<div style="height:5px;font-size:1px;">&nbsp;</div>



<details>
<summary> Glossary</summary>

{% assign cards = site.cards | where: "group", "Term" | sort: "last_name" %}

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

<div style="height:5px;font-size:1px;">&nbsp;</div>



<details>
<summary> Assignments</summary>

{% assign cards = site.cards | where: "group", "Assignment" | sort: "last_name" %}

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

<div style="height:5px;font-size:1px;">&nbsp;</div>



<details>
<summary> Activities</summary>

{% assign cards = site.cards | where: "group", "Activity" | sort: "last_name" %}

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

<div style="height:5px;font-size:1px;">&nbsp;</div>



<details>
<summary> Tutorials</summary>

{% assign cards = site.cards | where: "group", "Tutorial" | sort: "last_name" %}

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

<div style="height:5px;font-size:1px;">&nbsp;</div>



<details>
<summary> Teaching Modules</summary>

{% assign cards = site.cards | where: "group", "Teaching Module" | sort: "last_name" %}

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

<div style="height:5px;font-size:1px;">&nbsp;</div>



<details>
<summary> Data Sets</summary>

{% assign cards = site.cards | where: "group", "Data Set" | sort: "last_name" %}

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

<div style="height:5px;font-size:1px;">&nbsp;</div>


## Exploring by Data Literacy


