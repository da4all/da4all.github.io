---
layout: page
permalink: /defining-data/
title: Defining Data
description: 
nav: false
nav_rank: 
---

## Overview

"Defining data" is a crucial data literacy for students to become familiar with because, speaking more broadly, data literacy commonly refers to the ability to read, analyze, work, and communicate with data. Through defining data, this literacy argues that data literacy more broadly cannot be obtained without also learning how to define and interrogate data--to understand its complicated relations to power, privilege, oppression, and liberation. 

As such, this literacy introduces students to feminist, rhetorical, and equity data frameworks, all of which push students to ask critical questions about data such as: 
- What is “data”?
- How and why does data ethically matter?
- What rhetorical dimensions of data need to be carefully considered?
- How can we enact equitable data practices?

Such questions are especially important for doing data advocacy in ethical and just ways in our contemporary moment. This literacy thus specifically offers a theoretical understanding of data, an introduction to the data life cycle, and a brief dive into best practices of data advocacy in order to help students develop a strong rhetorical and ethical foundation from which to take up this important practice. 

<div style="height:1px;font-size:1px;">&nbsp;</div>

## Defining Data Toolkit

<div style="height:1px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Reading" and "Defining Data" -->

<details>
<summary> Readings </summary>

{% assign cards = site.cards | where: "group", "Reading" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Term" and "Defining Data" -->

<details>
<summary> Glossary </summary>

{% assign cards = site.cards | where: "group", "Term" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Assignment" and "Defining Data" -->

<details>
<summary> Assignments </summary>

{% assign cards = site.cards | where: "group", "Assignment" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Activity" and "Defining Data" -->

<details>
<summary> Activities </summary>

{% assign cards = site.cards | where: "group", "Activity" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Tutorial" and "Defining Data" -->

<details>
<summary> Tutorials </summary>

{% assign cards = site.cards | where: "group", "Tutorial" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Teaching Modules" and "Defining Data" -->

<details>
<summary> Teaching Modules </summary>

{% assign cards = site.cards | where: "group", "Teaching Module" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Dataset" and "Defining Data" -->

<details>
<summary> Datasets </summary>

{% assign cards = site.cards | where: "group", "Datasets" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>
